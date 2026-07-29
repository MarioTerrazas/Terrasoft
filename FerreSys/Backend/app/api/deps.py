from collections.abc import Callable

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.rol import Rol
from app.models.usuario import Usuario


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


def obtener_usuario_actual(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Usuario:
    excepcion_credenciales = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )

        subject = payload.get("sub")

        if subject is None:
            raise excepcion_credenciales

        id_usuario = int(subject)

    except (InvalidTokenError, TypeError, ValueError):
        raise excepcion_credenciales

    usuario = db.get(Usuario, id_usuario)

    if usuario is None:
        raise excepcion_credenciales

    if not usuario.estado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario está inactivo",
        )

    return usuario


def exigir_roles(
    *roles_permitidos: str,
) -> Callable:
    def verificar_rol(
        usuario_actual: Usuario = Depends(obtener_usuario_actual),
        db: Session = Depends(get_db),
    ) -> Usuario:
        rol = db.get(Rol, usuario_actual.id_rol)

        if rol is None or not rol.estado:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El rol del usuario no existe o está inactivo",
            )

        if rol.nombre not in roles_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    "No tienes permiso para realizar esta operación"
                ),
            )

        return usuario_actual

    return verificar_rol
