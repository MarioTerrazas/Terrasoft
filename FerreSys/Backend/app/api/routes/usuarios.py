from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.deps import exigir_roles
from app.core.security import crear_hash_password
from app.db.session import get_db
from app.models.rol import Rol
from app.models.usuario import Usuario
from app.schemas.usuario import (
    RolRespuesta,
    UsuarioActualizar,
    UsuarioCambiarPassword,
    UsuarioCrear,
    UsuarioRespuesta,
)


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    dependencies=[
        Depends(exigir_roles("ADMINISTRADOR")),
    ],
)


def construir_respuesta(
    usuario: Usuario,
    rol: Rol,
) -> UsuarioRespuesta:
    return UsuarioRespuesta(
        id_usuario=usuario.id_usuario,
        id_rol=usuario.id_rol,
        rol=rol.nombre,
        nombre=usuario.nombre,
        usuario=usuario.usuario,
        correo=usuario.correo,
        telefono=usuario.telefono,
        estado=usuario.estado,
        fecha_creacion=usuario.fecha_creacion,
        fecha_actualizacion=usuario.fecha_actualizacion,
    )


@router.get(
    "/roles",
    response_model=list[RolRespuesta],
)
def listar_roles(
    db: Session = Depends(get_db),
) -> list[Rol]:
    consulta = (
        select(Rol)
        .where(Rol.estado.is_(True))
        .order_by(Rol.id_rol)
    )

    return list(db.scalars(consulta).all())


@router.post(
    "",
    response_model=UsuarioRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_usuario(
    datos: UsuarioCrear,
    db: Session = Depends(get_db),
) -> UsuarioRespuesta:
    rol = db.get(Rol, datos.id_rol)

    if rol is None or not rol.estado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rol no encontrado o inactivo",
        )

    usuario = Usuario(
        id_rol=datos.id_rol,
        nombre=datos.nombre.strip(),
        usuario=datos.usuario.strip().lower(),
        password_hash=crear_hash_password(datos.password),
        correo=datos.correo,
        telefono=datos.telefono,
        estado=True,
    )

    db.add(usuario)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El nombre de usuario o correo ya está registrado",
        )

    db.refresh(usuario)

    return construir_respuesta(usuario, rol)


@router.get(
    "",
    response_model=list[UsuarioRespuesta],
)
def listar_usuarios(
    db: Session = Depends(get_db),
    buscar: str | None = Query(default=None, max_length=100),
    id_rol: int | None = Query(default=None, gt=0),
    solo_activos: bool = True,
    limite: int = Query(default=50, ge=1, le=200),
    desplazamiento: int = Query(default=0, ge=0),
) -> list[UsuarioRespuesta]:
    consulta = (
        select(Usuario, Rol)
        .join(Rol, Rol.id_rol == Usuario.id_rol)
    )

    if solo_activos:
        consulta = consulta.where(Usuario.estado.is_(True))

    if id_rol is not None:
        consulta = consulta.where(Usuario.id_rol == id_rol)

    if buscar:
        patron = f"%{buscar}%"
        consulta = consulta.where(
            or_(
                Usuario.nombre.ilike(patron),
                Usuario.usuario.ilike(patron),
                Usuario.correo.ilike(patron),
                Usuario.telefono.ilike(patron),
            )
        )

    consulta = (
        consulta
        .order_by(Usuario.id_usuario.desc())
        .offset(desplazamiento)
        .limit(limite)
    )

    resultados = db.execute(consulta).all()

    return [
        construir_respuesta(usuario, rol)
        for usuario, rol in resultados
    ]


@router.get(
    "/{id_usuario}",
    response_model=UsuarioRespuesta,
)
def obtener_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
) -> UsuarioRespuesta:
    resultado = db.execute(
        select(Usuario, Rol)
        .join(Rol, Rol.id_rol == Usuario.id_rol)
        .where(Usuario.id_usuario == id_usuario)
    ).first()

    if resultado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    usuario, rol = resultado

    return construir_respuesta(usuario, rol)


@router.put(
    "/{id_usuario}",
    response_model=UsuarioRespuesta,
)
def actualizar_usuario(
    id_usuario: int,
    datos: UsuarioActualizar,
    db: Session = Depends(get_db),
) -> UsuarioRespuesta:
    usuario = db.get(Usuario, id_usuario)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    cambios = datos.model_dump(exclude_unset=True)

    if "id_rol" in cambios:
        rol_nuevo = db.get(Rol, cambios["id_rol"])

        if rol_nuevo is None or not rol_nuevo.estado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Rol no encontrado o inactivo",
            )

    if "usuario" in cambios and cambios["usuario"] is not None:
        cambios["usuario"] = cambios["usuario"].strip().lower()

    if "nombre" in cambios and cambios["nombre"] is not None:
        cambios["nombre"] = cambios["nombre"].strip()

    for campo, valor in cambios.items():
        setattr(usuario, campo, valor)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El nombre de usuario o correo ya está registrado",
        )

    db.refresh(usuario)
    rol = db.get(Rol, usuario.id_rol)

    return construir_respuesta(usuario, rol)


@router.put(
    "/{id_usuario}/password",
    status_code=status.HTTP_204_NO_CONTENT,
)
def cambiar_password(
    id_usuario: int,
    datos: UsuarioCambiarPassword,
    db: Session = Depends(get_db),
) -> None:
    usuario = db.get(Usuario, id_usuario)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    usuario.password_hash = crear_hash_password(
        datos.nueva_password
    )

    db.commit()


@router.delete(
    "/{id_usuario}",
    response_model=UsuarioRespuesta,
)
def desactivar_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
) -> UsuarioRespuesta:
    usuario = db.get(Usuario, id_usuario)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )

    if usuario.usuario == "admin":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="No se puede desactivar el administrador principal",
        )

    usuario.estado = False
    db.commit()
    db.refresh(usuario)

    rol = db.get(Rol, usuario.id_rol)

    return construir_respuesta(usuario, rol)
