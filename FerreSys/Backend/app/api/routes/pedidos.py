from datetime import datetime, timezone
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.deps import exigir_roles, obtener_usuario_actual
from app.db.session import get_db
from app.models.cliente import Cliente
from app.models.detalle_pedido import DetallePedido
from app.models.pedido import Pedido
from app.models.producto import Producto
from app.schemas.pedido import (
    DetallePedidoRespuesta,
    PedidoCambiarEstado,
    PedidoCrear,
    PedidoRespuesta,
)


router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"],
    dependencies=[Depends(obtener_usuario_actual)],
)


ROLES_LECTURA = (
    "ADMINISTRADOR",
    "VENDEDOR",
    "ALMACENERO",
    "CHOFER",
)

ROLES_ESCRITURA = (
    "ADMINISTRADOR",
    "VENDEDOR",
)


def generar_numero_pedido() -> str:
    ahora = datetime.now(timezone.utc)

    return ahora.strftime("PED-%Y%m%d-%H%M%S-%f")


def construir_respuesta(
    pedido: Pedido,
    cliente: Cliente,
    detalles: list[tuple[DetallePedido, Producto]],
) -> PedidoRespuesta:
    return PedidoRespuesta(
        id_pedido=pedido.id_pedido,
        numero_pedido=pedido.numero_pedido,
        id_cliente=cliente.id_cliente,
        cliente_nombre=cliente.nombre,
        fecha=pedido.fecha,
        estado=pedido.estado,
        subtotal=pedido.subtotal,
        descuento=pedido.descuento,
        total=pedido.total,
        detalles=[
            DetallePedidoRespuesta(
                id_detalle_pedido=detalle.id_detalle_pedido,
                id_producto=producto.id_producto,
                producto_codigo=producto.codigo,
                producto_nombre=producto.nombre,
                cantidad=detalle.cantidad,
                precio_unitario=detalle.precio_unitario,
                descuento=detalle.descuento,
                subtotal=detalle.subtotal,
            )
            for detalle, producto in detalles
        ],
        fecha_creacion=pedido.fecha_creacion,
        fecha_actualizacion=pedido.fecha_actualizacion,
    )


def obtener_pedido_completo(
    db: Session,
    id_pedido: int,
) -> PedidoRespuesta:
    resultado = db.execute(
        select(Pedido, Cliente)
        .join(
            Cliente,
            Cliente.id_cliente == Pedido.id_cliente,
        )
        .where(Pedido.id_pedido == id_pedido)
    ).first()

    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido no encontrado",
        )

    pedido, cliente = resultado

    detalles = db.execute(
        select(DetallePedido, Producto)
        .join(
            Producto,
            Producto.id_producto
            == DetallePedido.id_producto,
        )
        .where(DetallePedido.id_pedido == pedido.id_pedido)
        .order_by(DetallePedido.id_detalle_pedido)
    ).all()

    return construir_respuesta(
        pedido,
        cliente,
        list(detalles),
    )


@router.post(
    "",
    response_model=PedidoRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_pedido(
    datos: PedidoCrear,
    db: Session = Depends(get_db),
    _usuario_actual=Depends(
        exigir_roles(*ROLES_ESCRITURA)
    ),
) -> PedidoRespuesta:
    cliente = db.get(Cliente, datos.id_cliente)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado",
        )

    if not cliente.estado:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El cliente está inactivo",
        )

    productos: dict[int, Producto] = {}

    for detalle in datos.detalles:
        producto = db.get(Producto, detalle.id_producto)

        if producto is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=(
                    f"Producto {detalle.id_producto} "
                    "no encontrado"
                ),
            )

        if not producto.estado:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"El producto {producto.nombre} "
                    "está inactivo"
                ),
            )

        productos[producto.id_producto] = producto

    pedido = Pedido(
        id_cliente=datos.id_cliente,
        numero_pedido=generar_numero_pedido(),
        estado="PENDIENTE",
        subtotal=Decimal("0"),
        descuento=datos.descuento,
        total=Decimal("0"),
    )

    db.add(pedido)
    db.flush()

    subtotal_pedido = Decimal("0")

    for datos_detalle in datos.detalles:
        producto = productos[datos_detalle.id_producto]

        importe_bruto = (
            datos_detalle.cantidad
            * producto.precio_venta
        )

        if datos_detalle.descuento > importe_bruto:
            db.rollback()

            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=(
                    f"El descuento del producto "
                    f"{producto.nombre} supera su importe"
                ),
            )

        subtotal_linea = (
            importe_bruto
            - datos_detalle.descuento
        )

        detalle = DetallePedido(
            id_pedido=pedido.id_pedido,
            id_producto=producto.id_producto,
            cantidad=datos_detalle.cantidad,
            precio_unitario=producto.precio_venta,
            descuento=datos_detalle.descuento,
            subtotal=subtotal_linea,
        )

        db.add(detalle)
        subtotal_pedido += subtotal_linea

    if datos.descuento > subtotal_pedido:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=(
                "El descuento general supera "
                "el subtotal del pedido"
            ),
        )

    pedido.subtotal = subtotal_pedido
    pedido.total = subtotal_pedido - datos.descuento

    try:
        db.commit()
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se pudo generar el pedido",
        )

    return obtener_pedido_completo(
        db,
        pedido.id_pedido,
    )


@router.get(
    "",
    response_model=list[PedidoRespuesta],
)
def listar_pedidos(
    db: Session = Depends(get_db),
    id_cliente: int | None = Query(default=None, gt=0),
    estado_pedido: str | None = Query(
        default=None,
        alias="estado",
        max_length=30,
    ),
    limite: int = Query(default=50, ge=1, le=200),
    desplazamiento: int = Query(default=0, ge=0),
    _usuario_actual=Depends(
        exigir_roles(*ROLES_LECTURA)
    ),
) -> list[PedidoRespuesta]:
    consulta = select(Pedido.id_pedido)

    if id_cliente is not None:
        consulta = consulta.where(
            Pedido.id_cliente == id_cliente
        )

    if estado_pedido:
        consulta = consulta.where(
            Pedido.estado == estado_pedido.upper()
        )

    consulta = (
        consulta
        .order_by(Pedido.id_pedido.desc())
        .offset(desplazamiento)
        .limit(limite)
    )

    ids = list(db.scalars(consulta).all())

    return [
        obtener_pedido_completo(db, id_pedido)
        for id_pedido in ids
    ]


@router.get(
    "/{id_pedido}",
    response_model=PedidoRespuesta,
)
def obtener_pedido(
    id_pedido: int,
    db: Session = Depends(get_db),
    _usuario_actual=Depends(
        exigir_roles(*ROLES_LECTURA)
    ),
) -> PedidoRespuesta:
    return obtener_pedido_completo(
        db,
        id_pedido,
    )


@router.put(
    "/{id_pedido}/estado",
    response_model=PedidoRespuesta,
)
def cambiar_estado_pedido(
    id_pedido: int,
    datos: PedidoCambiarEstado,
    db: Session = Depends(get_db),
    _usuario_actual=Depends(
        exigir_roles(*ROLES_ESCRITURA)
    ),
) -> PedidoRespuesta:
    pedido = db.get(Pedido, id_pedido)

    if pedido is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido no encontrado",
        )

    if pedido.estado in {"ENTREGADO", "CANCELADO"}:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "No se puede modificar un pedido "
                "que ya está finalizado"
            ),
        )

    pedido.estado = datos.estado
    db.commit()
    db.refresh(pedido)

    return obtener_pedido_completo(
        db,
        pedido.id_pedido,
    )
