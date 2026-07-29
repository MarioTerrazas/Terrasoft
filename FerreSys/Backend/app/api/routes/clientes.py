from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import (
    ClienteActualizar,
    ClienteCrear,
    ClienteRespuesta,
)

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"],
)


@router.post(
    "",
    response_model=ClienteRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_cliente(
    datos: ClienteCrear,
    db: Session = Depends(get_db),
) -> Cliente:
    cliente = Cliente(**datos.model_dump())

    db.add(cliente)
    db.commit()
    db.refresh(cliente)

    return cliente


@router.get(
    "",
    response_model=list[ClienteRespuesta],
)
def listar_clientes(
    db: Session = Depends(get_db),
    buscar: str | None = Query(default=None, max_length=100),
    solo_activos: bool = True,
    limite: int = Query(default=50, ge=1, le=200),
    desplazamiento: int = Query(default=0, ge=0),
) -> list[Cliente]:
    consulta = select(Cliente)

    if solo_activos:
        consulta = consulta.where(Cliente.estado.is_(True))

    if buscar:
        patron = f"%{buscar}%"
        consulta = consulta.where(
            Cliente.nombre.ilike(patron)
            | Cliente.documento.ilike(patron)
            | Cliente.nit.ilike(patron)
            | Cliente.telefono.ilike(patron)
        )

    consulta = (
        consulta
        .order_by(Cliente.id_cliente.desc())
        .offset(desplazamiento)
        .limit(limite)
    )

    return list(db.scalars(consulta).all())


@router.get(
    "/{id_cliente}",
    response_model=ClienteRespuesta,
)
def obtener_cliente(
    id_cliente: int,
    db: Session = Depends(get_db),
) -> Cliente:
    cliente = db.get(Cliente, id_cliente)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado",
        )

    return cliente


@router.put(
    "/{id_cliente}",
    response_model=ClienteRespuesta,
)
def actualizar_cliente(
    id_cliente: int,
    datos: ClienteActualizar,
    db: Session = Depends(get_db),
) -> Cliente:
    cliente = db.get(Cliente, id_cliente)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado",
        )

    cambios = datos.model_dump(exclude_unset=True)

    for campo, valor in cambios.items():
        setattr(cliente, campo, valor)

    db.commit()
    db.refresh(cliente)

    return cliente


@router.delete(
    "/{id_cliente}",
    response_model=ClienteRespuesta,
)
def eliminar_cliente(
    id_cliente: int,
    db: Session = Depends(get_db),
) -> Cliente:
    cliente = db.get(Cliente, id_cliente)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado",
        )

    cliente.estado = False

    db.commit()
    db.refresh(cliente)

    return cliente
