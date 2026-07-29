from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UsuarioCrear(BaseModel):
    id_rol: int = Field(gt=0)
    nombre: str = Field(min_length=2, max_length=120)
    usuario: str = Field(min_length=3, max_length=60)
    password: str = Field(min_length=8, max_length=128)
    correo: EmailStr | None = None
    telefono: str | None = Field(default=None, max_length=30)


class UsuarioActualizar(BaseModel):
    id_rol: int | None = Field(default=None, gt=0)
    nombre: str | None = Field(default=None, min_length=2, max_length=120)
    usuario: str | None = Field(default=None, min_length=3, max_length=60)
    correo: EmailStr | None = None
    telefono: str | None = Field(default=None, max_length=30)
    estado: bool | None = None


class UsuarioCambiarPassword(BaseModel):
    nueva_password: str = Field(min_length=8, max_length=128)


class UsuarioRespuesta(BaseModel):
    id_usuario: int
    id_rol: int
    rol: str
    nombre: str
    usuario: str
    correo: str | None
    telefono: str | None
    estado: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    model_config = ConfigDict(from_attributes=True)


class RolRespuesta(BaseModel):
    id_rol: int
    nombre: str
    descripcion: str | None
    estado: bool

    model_config = ConfigDict(from_attributes=True)
