from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import obtener_usuario_actual
from app.core.security import (
    crear_access_token,
    verificar_password,
)
from app.db.session import get_db
from app.models.rol import Rol
from app.models.usuario import Usuario
from app.schemas.auth import (
    TokenRespuesta,
    UsuarioAutenticado,
)


router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"],
)


@router.post(
    "/login",
    response_model=TokenRespuesta,
)
def iniciar_sesion(
    formulario: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> TokenRespuesta:
    usuario = db.scalar(
        select(Usuario).where(
            Usuario.usuario == formulario.username
        )
    )

    credenciales_invalidas = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuario o contraseña incorrectos",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if usuario is None:
        raise credenciales_invalidas

    if not usuario.estado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario está inactivo",
        )

    try:
        password_correcto = verificar_password(
            formulario.password,
            usuario.password_hash,
        )
    except Exception:
        password_correcto = False

    if not password_correcto:
        raise credenciales_invalidas

    rol = db.get(Rol, usuario.id_rol)

    if rol is None or not rol.estado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El rol del usuario no existe o está inactivo",
        )

    access_token = crear_access_token(
        subject=str(usuario.id_usuario),
        datos_adicionales={
            "usuario": usuario.usuario,
            "rol": rol.nombre,
        },
    )

    return TokenRespuesta(
        access_token=access_token,
        token_type="bearer",
    )


@router.get(
    "/me",
    response_model=UsuarioAutenticado,
)
def obtener_mi_usuario(
    usuario_actual: Usuario = Depends(
        obtener_usuario_actual
    ),
    db: Session = Depends(get_db),
) -> UsuarioAutenticado:
    rol = db.get(Rol, usuario_actual.id_rol)

    if rol is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rol del usuario no encontrado",
        )

    return UsuarioAutenticado(
        id_usuario=usuario_actual.id_usuario,
        nombre=usuario_actual.nombre,
        usuario=usuario_actual.usuario,
        id_rol=usuario_actual.id_rol,
        rol=rol.nombre,
    )
