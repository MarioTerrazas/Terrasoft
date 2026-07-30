from datetime import datetime, timezone
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.deps import exigir_roles, obtener_usuario_actual
from app.db.session import get_db
from app.models.almacen import Almacen
from app.models.cliente import Cliente
from app.models.detalle_pedido import DetallePedido
from app.models.inventario import Inventario
from app.models.movimiento_inventario import MovimientoInventario
from app.models.pedido import Pedido
from app.models.producto import Producto
from app.models.tipo_movimiento import TipoMovimiento
from app.models.usuario import Usuario
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

ROLES_CAMBIO_ESTADO = (
    "ADMINISTRADOR",
    "VENDEDOR",
    "ALMACENERO",
)

TRANSICIONES_PERMITIDAS = {
    "PENDIENTE": {"CONFIRMADO", "CANCELADO"},
    "CONFIRMADO": {"PREPARANDO", "ENTREGADO", "CANCELADO"},
    "PREPARANDO": {"ENTREGADO", "CANCELADO"},
    "ENTREGADO": set(),
    "CANCELADO": set(),
}


def generar_numero_pedido() -> str:
    ahora = datetime.now(timezone.utc)
    return ahora.strftime("PED-%Y%m%d-%H%M%S-%f")


def construir_respuesta(
    pedido: Pedido,
    cliente: Cliente,
    almacen: Almacen,
    detalles: list[tuple[DetallePedido, Producto]],
) -> PedidoRespuesta:
    return PedidoRespuesta(
        id_pedido=pedido.id_pedido,
        numero_pedido=pedido.numero_pedido,
        id_cliente=cliente.id_cliente,
        cliente_nombre=cliente.nombre,
        id_almacen=almacen.id_almacen,
        almacen_nombre=almacen.nombre,
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
        select(Pedido, Cliente, Almacen)
        .join(
            Cliente,
            Cliente.id_cliente == Pedido.id_cliente,
        )
        .join(
            Almacen,
            Almacen.id_almacen == Pedido.id_almacen,
        )
        .where(Pedido.id_pedido == id_pedido)
    ).first()

    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido no encontrado",
        )

    pedido, cliente, almacen = resultado

    detalles = db.execute(
        select(DetallePedido, Producto)
        .join(
            Producto,
            Producto.id_producto == DetallePedido.id_producto,
        )
        .where(DetallePedido.id_pedido == pedido.id_pedido)
        .order_by(DetallePedido.id_detalle_pedido)
    ).all()

    return construir_respuesta(
        pedido,
        cliente,
        almacen,
        list(detalles),
    )


def obtener_inventarios_bloqueados(
    db: Session,
    pedido: Pedido,
    detalles: list[DetallePedido],
) -> dict[int, Inventario]:
    inventarios: dict[int, Inventario] = {}

    ids_productos = sorted(
        detalle.id_producto
        for detalle in detalles
    )

    for id_producto in ids_productos:
        inventario = db.scalar(
            select(Inventario)
            .where(
                Inventario.id_producto == id_producto,
                Inventario.id_almacen == pedido.id_almacen,
            )
            .with_for_update()
        )

        if inventario is None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"El producto {id_producto} no tiene inventario "
                    "en el almacén seleccionado"
                ),
            )

        inventarios[id_producto] = inventario

    return inventarios


def reservar_stock(
    detalles: list[DetallePedido],
    inventarios: dict[int, Inventario],
) -> None:
    for detalle in detalles:
        inventario = inventarios[detalle.id_producto]

        stock_disponible = (
            inventario.stock_actual
            - inventario.stock_reservado
        )

        if detalle.cantidad > stock_disponible:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"Stock insuficiente para el producto "
                    f"{detalle.id_producto}. "
                    f"Disponible: {stock_disponible}"
                ),
            )

    for detalle in detalles:
        inventario = inventarios[detalle.id_producto]
        inventario.stock_reservado += detalle.cantidad


def liberar_reserva(
    detalles: list[DetallePedido],
    inventarios: dict[int, Inventario],
) -> None:
    for detalle in detalles:
        inventario = inventarios[detalle.id_producto]

        if detalle.cantidad > inventario.stock_reservado:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "La reserva de inventario es inconsistente "
                    f"para el producto {detalle.id_producto}"
                ),
            )

        inventario.stock_reservado -= detalle.cantidad


def entregar_pedido(
    db: Session,
    pedido: Pedido,
    detalles: list[DetallePedido],
    inventarios: dict[int, Inventario],
    usuario_actual: Usuario,
) -> None:
    tipo_salida = db.scalar(
        select(TipoMovimiento).where(
            TipoMovimiento.nombre == "SALIDA_VENTA",
            TipoMovimiento.estado.is_(True),
        )
    )

    if tipo_salida is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No existe el tipo de movimiento SALIDA_VENTA",
        )

    for detalle in detalles:
        inventario = inventarios[detalle.id_producto]

        if detalle.cantidad > inventario.stock_reservado:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "La reserva es insuficiente para entregar "
                    f"el producto {detalle.id_producto}"
                ),
            )

        if detalle.cantidad > inventario.stock_actual:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "El stock actual es insuficiente para entregar "
                    f"el producto {detalle.id_producto}"
                ),
            )

    for detalle in detalles:
        inventario = inventarios[detalle.id_producto]

        inventario.stock_reservado -= detalle.cantidad
        inventario.stock_actual -= detalle.cantidad

        movimiento = MovimientoInventario(
            id_inventario=inventario.id_inventario,
            id_tipo_movimiento=tipo_salida.id_tipo_movimiento,
            cantidad=detalle.cantidad,
            motivo=f"Entrega del pedido {pedido.numero_pedido}",
            observaciones=(
                f"Salida automática por entrega "
                f"del pedido {pedido.id_pedido}"
            ),
            id_usuario=usuario_actual.id_usuario,
        )

        db.add(movimiento)


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

    almacen = db.get(Almacen, datos.id_almacen)

    if almacen is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Almacén no encontrado",
        )

    if not almacen.estado:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El almacén está inactivo",
        )

    productos: dict[int, Producto] = {}

    for detalle in datos.detalles:
        producto = db.get(Producto, detalle.id_producto)

        if producto is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto {detalle.id_producto} no encontrado",
            )

        if not producto.estado:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"El producto {producto.nombre} está inactivo",
            )

        productos[producto.id_producto] = producto

    pedido = Pedido(
        id_cliente=datos.id_cliente,
        id_almacen=datos.id_almacen,
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
                    f"El descuento del producto {producto.nombre} "
                    "supera su importe"
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
            detail="El descuento general supera el subtotal del pedido",
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

    return obtener_pedido_completo(db, pedido.id_pedido)


@router.get(
    "",
    response_model=list[PedidoRespuesta],
)
def listar_pedidos(
    db: Session = Depends(get_db),
    id_cliente: int | None = Query(default=None, gt=0),
    id_almacen: int | None = Query(default=None, gt=0),
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

    if id_almacen is not None:
        consulta = consulta.where(
            Pedido.id_almacen == id_almacen
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
    return obtener_pedido_completo(db, id_pedido)


@router.put(
    "/{id_pedido}/estado",
    response_model=PedidoRespuesta,
)
def cambiar_estado_pedido(
    id_pedido: int,
    datos: PedidoCambiarEstado,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(
        exigir_roles(*ROLES_CAMBIO_ESTADO)
    ),
) -> PedidoRespuesta:
    pedido = db.scalar(
        select(Pedido)
        .where(Pedido.id_pedido == id_pedido)
        .with_for_update()
    )

    if pedido is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido no encontrado",
        )

    estado_anterior = pedido.estado
    estado_nuevo = datos.estado

    if estado_nuevo == estado_anterior:
        return obtener_pedido_completo(db, pedido.id_pedido)

    permitidos = TRANSICIONES_PERMITIDAS.get(
        estado_anterior,
        set(),
    )

    if estado_nuevo not in permitidos:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                f"No se permite cambiar de {estado_anterior} "
                f"a {estado_nuevo}"
            ),
        )

    detalles = list(
        db.scalars(
            select(DetallePedido)
            .where(DetallePedido.id_pedido == pedido.id_pedido)
            .order_by(DetallePedido.id_producto)
        ).all()
    )

    if not detalles:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El pedido no tiene productos",
        )

    inventarios: dict[int, Inventario] = {}

    requiere_inventario = (
        estado_nuevo == "CONFIRMADO"
        or estado_nuevo == "ENTREGADO"
        or (
            estado_nuevo == "CANCELADO"
            and estado_anterior in {"CONFIRMADO", "PREPARANDO"}
        )
    )

    if requiere_inventario:
        inventarios = obtener_inventarios_bloqueados(
            db,
            pedido,
            detalles,
        )

    if estado_anterior == "PENDIENTE" and estado_nuevo == "CONFIRMADO":
        reservar_stock(detalles, inventarios)

    elif (
        estado_nuevo == "CANCELADO"
        and estado_anterior in {"CONFIRMADO", "PREPARANDO"}
    ):
        liberar_reserva(detalles, inventarios)

    elif (
        estado_nuevo == "ENTREGADO"
        and estado_anterior in {"CONFIRMADO", "PREPARANDO"}
    ):
        entregar_pedido(
            db,
            pedido,
            detalles,
            inventarios,
            usuario_actual,
        )

    pedido.estado = estado_nuevo

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    return obtener_pedido_completo(db, pedido.id_pedido)
