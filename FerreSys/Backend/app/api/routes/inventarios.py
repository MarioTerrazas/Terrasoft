from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.almacen import Almacen
from app.models.inventario import Inventario
from app.models.producto import Producto
from app.schemas.inventario import (
    InventarioActualizar,
    InventarioCrear,
    InventarioRespuesta,
)


router = APIRouter(
    prefix="/inventarios",
    tags=["Inventario"],
)


def construir_respuesta(
    inventario: Inventario,
    producto: Producto,
    almacen: Almacen,
) -> InventarioRespuesta:
    stock_disponible = (
        inventario.stock_actual
        - inventario.stock_reservado
    )

    return InventarioRespuesta(
        id_inventario=inventario.id_inventario,
        id_producto=inventario.id_producto,
        id_almacen=inventario.id_almacen,
        stock_actual=inventario.stock_actual,
        stock_reservado=inventario.stock_reservado,
        stock_minimo=inventario.stock_minimo,
        stock_disponible=stock_disponible,
        bajo_stock=stock_disponible <= inventario.stock_minimo,
        producto_codigo=producto.codigo,
        producto_nombre=producto.nombre,
        almacen_nombre=almacen.nombre,
        fecha_creacion=inventario.fecha_creacion,
        fecha_actualizacion=inventario.fecha_actualizacion,
    )


@router.post(
    "",
    response_model=InventarioRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_inventario(
    datos: InventarioCrear,
    db: Session = Depends(get_db),
) -> InventarioRespuesta:
    producto = db.get(Producto, datos.id_producto)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    if not producto.estado:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El producto está inactivo",
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

    inventario = Inventario(**datos.model_dump())
    db.add(inventario)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Ya existe un inventario para este producto "
                "en este almacén"
            ),
        )

    db.refresh(inventario)

    return construir_respuesta(
        inventario,
        producto,
        almacen,
    )


@router.get(
    "",
    response_model=list[InventarioRespuesta],
)
def listar_inventarios(
    db: Session = Depends(get_db),
    id_producto: int | None = Query(default=None, gt=0),
    id_almacen: int | None = Query(default=None, gt=0),
    solo_bajo_stock: bool = False,
    limite: int = Query(default=50, ge=1, le=200),
    desplazamiento: int = Query(default=0, ge=0),
) -> list[InventarioRespuesta]:
    consulta = (
        select(Inventario, Producto, Almacen)
        .join(
            Producto,
            Producto.id_producto == Inventario.id_producto,
        )
        .join(
            Almacen,
            Almacen.id_almacen == Inventario.id_almacen,
        )
    )

    if id_producto is not None:
        consulta = consulta.where(
            Inventario.id_producto == id_producto
        )

    if id_almacen is not None:
        consulta = consulta.where(
            Inventario.id_almacen == id_almacen
        )

    if solo_bajo_stock:
        consulta = consulta.where(
            (
                Inventario.stock_actual
                - Inventario.stock_reservado
            )
            <= Inventario.stock_minimo
        )

    consulta = (
        consulta
        .order_by(Inventario.id_inventario.desc())
        .offset(desplazamiento)
        .limit(limite)
    )

    resultados = db.execute(consulta).all()

    return [
        construir_respuesta(
            inventario,
            producto,
            almacen,
        )
        for inventario, producto, almacen in resultados
    ]


@router.get(
    "/{id_inventario}",
    response_model=InventarioRespuesta,
)
def obtener_inventario(
    id_inventario: int,
    db: Session = Depends(get_db),
) -> InventarioRespuesta:
    consulta = (
        select(Inventario, Producto, Almacen)
        .join(
            Producto,
            Producto.id_producto == Inventario.id_producto,
        )
        .join(
            Almacen,
            Almacen.id_almacen == Inventario.id_almacen,
        )
        .where(Inventario.id_inventario == id_inventario)
    )

    resultado = db.execute(consulta).first()

    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro de inventario no encontrado",
        )

    inventario, producto, almacen = resultado

    return construir_respuesta(
        inventario,
        producto,
        almacen,
    )


@router.put(
    "/{id_inventario}",
    response_model=InventarioRespuesta,
)
def actualizar_inventario(
    id_inventario: int,
    datos: InventarioActualizar,
    db: Session = Depends(get_db),
) -> InventarioRespuesta:
    inventario = db.get(Inventario, id_inventario)

    if inventario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro de inventario no encontrado",
        )

    cambios = datos.model_dump(exclude_unset=True)

    nuevo_stock_reservado = cambios.get(
        "stock_reservado",
        inventario.stock_reservado,
    )

    if nuevo_stock_reservado > inventario.stock_actual:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=(
                "El stock reservado no puede superar "
                "el stock actual"
            ),
        )

    for campo, valor in cambios.items():
        setattr(inventario, campo, valor)

    db.commit()
    db.refresh(inventario)

    producto = db.get(Producto, inventario.id_producto)
    almacen = db.get(Almacen, inventario.id_almacen)

    return construir_respuesta(
        inventario,
        producto,
        almacen,
    )
