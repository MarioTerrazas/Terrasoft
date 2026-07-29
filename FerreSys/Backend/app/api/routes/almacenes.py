from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session
from app.api.deps import obtener_usuario_actual
from app.db.session import get_db
from app.models.almacen import Almacen
from app.schemas.almacen import (
    AlmacenActualizar,
    AlmacenCrear,
    AlmacenRespuesta,
)


router = APIRouter(
    prefix="/almacenes",
    tags=["Almacenes"],
    dependencies=[Depends(obtener_usuario_actual)],
)


@router.post(
    "",
    response_model=AlmacenRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_almacen(
    datos: AlmacenCrear,
    db: Session = Depends(get_db),
) -> Almacen:
    almacen = Almacen(**datos.model_dump())

    db.add(almacen)
    db.commit()
    db.refresh(almacen)

    return almacen


@router.get(
    "",
    response_model=list[AlmacenRespuesta],
)
def listar_almacenes(
    db: Session = Depends(get_db),
    buscar: str | None = Query(
        default=None,
        max_length=100,
    ),
    solo_activos: bool = True,
    limite: int = Query(
        default=50,
        ge=1,
        le=200,
    ),
    desplazamiento: int = Query(
        default=0,
        ge=0,
    ),
) -> list[Almacen]:
    consulta = select(Almacen)

    if solo_activos:
        consulta = consulta.where(
            Almacen.estado.is_(True)
        )

    if buscar:
        patron = f"%{buscar}%"

        consulta = consulta.where(
            or_(
                Almacen.nombre.ilike(patron),
                Almacen.direccion.ilike(patron),
                Almacen.responsable.ilike(patron),
                Almacen.telefono.ilike(patron),
            )
        )

    consulta = (
        consulta
        .order_by(Almacen.id_almacen.desc())
        .offset(desplazamiento)
        .limit(limite)
    )

    return list(db.scalars(consulta).all())


@router.get(
    "/{id_almacen}",
    response_model=AlmacenRespuesta,
)
def obtener_almacen(
    id_almacen: int,
    db: Session = Depends(get_db),
) -> Almacen:
    almacen = db.get(Almacen, id_almacen)

    if almacen is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Almacén no encontrado",
        )

    return almacen


@router.put(
    "/{id_almacen}",
    response_model=AlmacenRespuesta,
)
def actualizar_almacen(
    id_almacen: int,
    datos: AlmacenActualizar,
    db: Session = Depends(get_db),
) -> Almacen:
    almacen = db.get(Almacen, id_almacen)

    if almacen is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Almacén no encontrado",
        )

    cambios = datos.model_dump(exclude_unset=True)

    for campo, valor in cambios.items():
        setattr(almacen, campo, valor)

    db.commit()
    db.refresh(almacen)

    return almacen


@router.delete(
    "/{id_almacen}",
    response_model=AlmacenRespuesta,
)
def eliminar_almacen(
    id_almacen: int,
    db: Session = Depends(get_db),
) -> Almacen:
    almacen = db.get(Almacen, id_almacen)

    if almacen is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Almacén no encontrado",
        )

    almacen.estado = False

    db.commit()
    db.refresh(almacen)

    return almacen
