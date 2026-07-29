from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.producto import Producto
from app.schemas.producto import (
    ProductoActualizar,
    ProductoCrear,
    ProductoRespuesta,
)

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)


@router.post(
    "",
    response_model=ProductoRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_producto(
    datos: ProductoCrear,
    db: Session = Depends(get_db),
) -> Producto:
    producto = Producto(**datos.model_dump())
    db.add(producto)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un producto con ese código",
        )

    db.refresh(producto)
    return producto


@router.get(
    "",
    response_model=list[ProductoRespuesta],
)
def listar_productos(
    db: Session = Depends(get_db),
    buscar: str | None = Query(default=None, max_length=100),
    solo_activos: bool = True,
    limite: int = Query(default=50, ge=1, le=200),
    desplazamiento: int = Query(default=0, ge=0),
) -> list[Producto]:
    consulta = select(Producto)

    if solo_activos:
        consulta = consulta.where(Producto.estado.is_(True))

    if buscar:
        patron = f"%{buscar}%"
        consulta = consulta.where(
            or_(
                Producto.codigo.ilike(patron),
                Producto.nombre.ilike(patron),
            )
        )

    consulta = (
        consulta
        .order_by(Producto.id_producto.desc())
        .offset(desplazamiento)
        .limit(limite)
    )

    return list(db.scalars(consulta).all())


@router.get(
    "/{id_producto}",
    response_model=ProductoRespuesta,
)
def obtener_producto(
    id_producto: int,
    db: Session = Depends(get_db),
) -> Producto:
    producto = db.get(Producto, id_producto)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return producto


@router.put(
    "/{id_producto}",
    response_model=ProductoRespuesta,
)
def actualizar_producto(
    id_producto: int,
    datos: ProductoActualizar,
    db: Session = Depends(get_db),
) -> Producto:
    producto = db.get(Producto, id_producto)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    cambios = datos.model_dump(exclude_unset=True)

    nuevo_precio_compra = cambios.get(
        "precio_compra",
        producto.precio_compra,
    )
    nuevo_precio_venta = cambios.get(
        "precio_venta",
        producto.precio_venta,
    )

    if nuevo_precio_venta < nuevo_precio_compra:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="El precio de venta no puede ser menor que el precio de compra",
        )

    for campo, valor in cambios.items():
        setattr(producto, campo, valor)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un producto con ese código",
        )

    db.refresh(producto)
    return producto


@router.delete(
    "/{id_producto}",
    response_model=ProductoRespuesta,
)
def eliminar_producto(
    id_producto: int,
    db: Session = Depends(get_db),
) -> Producto:
    producto = db.get(Producto, id_producto)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    producto.estado = False
    db.commit()
    db.refresh(producto)

    return producto
