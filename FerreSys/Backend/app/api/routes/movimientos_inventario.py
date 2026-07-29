from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.almacen import Almacen
from app.models.inventario import Inventario
from app.models.movimiento_inventario import MovimientoInventario
from app.models.producto import Producto
from app.models.tipo_movimiento import TipoMovimiento
from app.models.usuario import Usuario
from app.schemas.movimiento_inventario import (
    MovimientoInventarioCrear,
    MovimientoInventarioRespuesta,
)


router = APIRouter(
    prefix="/movimientos-inventario",
    tags=["Movimientos de inventario"],
)


TIPOS_ENTRADA = {
    "ENTRADA_COMPRA",
    "ENTRADA_DEVOLUCION",
    "AJUSTE_ENTRADA",
    "TRASLADO_ENTRADA",
    "INVENTARIO_INICIAL",
}

TIPOS_SALIDA = {
    "SALIDA_VENTA",
    "SALIDA_DEVOLUCION_PROVEEDOR",
    "AJUSTE_SALIDA",
    "TRASLADO_SALIDA",
    "MERMA",
}


def determinar_naturaleza(nombre: str) -> str:
    if nombre in TIPOS_ENTRADA:
        return "ENTRADA"

    if nombre in TIPOS_SALIDA:
        return "SALIDA"

    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="El tipo de movimiento no tiene una naturaleza válida",
    )


def construir_respuesta(
    movimiento: MovimientoInventario,
    inventario: Inventario,
    tipo: TipoMovimiento,
    usuario: Usuario,
    producto: Producto,
    almacen: Almacen,
    stock_anterior: Decimal,
) -> MovimientoInventarioRespuesta:
    naturaleza = determinar_naturaleza(tipo.nombre)

    return MovimientoInventarioRespuesta(
        id_movimiento=movimiento.id_movimiento,
        id_inventario=movimiento.id_inventario,
        id_tipo_movimiento=movimiento.id_tipo_movimiento,
        tipo_movimiento=tipo.nombre,
        naturaleza=naturaleza,
        cantidad=movimiento.cantidad,
        stock_anterior=stock_anterior,
        stock_actual=inventario.stock_actual,
        stock_disponible=(
            inventario.stock_actual
            - inventario.stock_reservado
        ),
        motivo=movimiento.motivo,
        observaciones=movimiento.observaciones,
        id_usuario=movimiento.id_usuario,
        usuario_nombre=usuario.nombre,
        producto_codigo=producto.codigo,
        producto_nombre=producto.nombre,
        almacen_nombre=almacen.nombre,
        fecha_movimiento=movimiento.fecha_movimiento,
    )


@router.get(
    "/tipos",
    response_model=list[dict[str, object]],
)
def listar_tipos_movimiento(
    db: Session = Depends(get_db),
) -> list[dict[str, object]]:
    tipos = db.scalars(
        select(TipoMovimiento)
        .where(TipoMovimiento.estado.is_(True))
        .order_by(TipoMovimiento.id_tipo_movimiento)
    ).all()

    return [
        {
            "id_tipo_movimiento": tipo.id_tipo_movimiento,
            "nombre": tipo.nombre,
            "descripcion": tipo.descripcion,
            "naturaleza": determinar_naturaleza(tipo.nombre),
        }
        for tipo in tipos
    ]


@router.post(
    "",
    response_model=MovimientoInventarioRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def registrar_movimiento(
    datos: MovimientoInventarioCrear,
    db: Session = Depends(get_db),
) -> MovimientoInventarioRespuesta:
    consulta_inventario = (
        select(Inventario)
        .where(
            Inventario.id_inventario == datos.id_inventario
        )
        .with_for_update()
    )

    inventario = db.scalar(consulta_inventario)

    if inventario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro de inventario no encontrado",
        )

    tipo = db.get(
        TipoMovimiento,
        datos.id_tipo_movimiento,
    )

    if tipo is None or not tipo.estado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo de movimiento no encontrado o inactivo",
        )

    usuario = db.get(Usuario, datos.id_usuario)

    if usuario is None or not usuario.estado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado o inactivo",
        )

    producto = db.get(Producto, inventario.id_producto)
    almacen = db.get(Almacen, inventario.id_almacen)

    naturaleza = determinar_naturaleza(tipo.nombre)
    stock_anterior = inventario.stock_actual

    if naturaleza == "ENTRADA":
        inventario.stock_actual += datos.cantidad

    else:
        stock_disponible = (
            inventario.stock_actual
            - inventario.stock_reservado
        )

        if datos.cantidad > stock_disponible:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Stock disponible insuficiente. "
                    f"Disponible: {stock_disponible}"
                ),
            )

        inventario.stock_actual -= datos.cantidad

    movimiento = MovimientoInventario(
        **datos.model_dump()
    )

    db.add(movimiento)
    db.commit()

    db.refresh(inventario)
    db.refresh(movimiento)

    return construir_respuesta(
        movimiento=movimiento,
        inventario=inventario,
        tipo=tipo,
        usuario=usuario,
        producto=producto,
        almacen=almacen,
        stock_anterior=stock_anterior,
    )


@router.get(
    "",
    response_model=list[dict[str, object]],
)
def listar_movimientos(
    db: Session = Depends(get_db),
    id_inventario: int | None = Query(default=None, gt=0),
    limite: int = Query(default=50, ge=1, le=200),
    desplazamiento: int = Query(default=0, ge=0),
) -> list[dict[str, object]]:
    consulta = (
        select(
            MovimientoInventario,
            TipoMovimiento,
            Usuario,
        )
        .join(
            TipoMovimiento,
            TipoMovimiento.id_tipo_movimiento
            == MovimientoInventario.id_tipo_movimiento,
        )
        .join(
            Usuario,
            Usuario.id_usuario
            == MovimientoInventario.id_usuario,
        )
    )

    if id_inventario is not None:
        consulta = consulta.where(
            MovimientoInventario.id_inventario
            == id_inventario
        )

    consulta = (
        consulta
        .order_by(
            MovimientoInventario.fecha_movimiento.desc()
        )
        .offset(desplazamiento)
        .limit(limite)
    )

    resultados = db.execute(consulta).all()

    return [
        {
            "id_movimiento": movimiento.id_movimiento,
            "id_inventario": movimiento.id_inventario,
            "tipo_movimiento": tipo.nombre,
            "naturaleza": determinar_naturaleza(tipo.nombre),
            "cantidad": movimiento.cantidad,
            "motivo": movimiento.motivo,
            "observaciones": movimiento.observaciones,
            "id_usuario": usuario.id_usuario,
            "usuario_nombre": usuario.nombre,
            "fecha_movimiento": movimiento.fecha_movimiento,
        }
        for movimiento, tipo, usuario in resultados
    ]
