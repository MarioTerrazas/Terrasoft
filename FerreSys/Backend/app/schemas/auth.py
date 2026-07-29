from pydantic import BaseModel


class TokenRespuesta(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UsuarioAutenticado(BaseModel):
    id_usuario: int
    nombre: str
    usuario: str
    id_rol: int
    rol: str
