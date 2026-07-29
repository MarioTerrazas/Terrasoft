from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ClienteBase(BaseModel):
    nombre: str = Field(min_length=2, max_length=180)
    documento: str | None = Field(default=None, max_length=30)
    nit: str | None = Field(default=None, max_length=30)
    telefono: str | None = Field(default=None, max_length=30)
    correo: EmailStr | None = None
    direccion: str | None = Field(default=None, max_length=255)


class ClienteCrear(ClienteBase):
    pass


class ClienteActualizar(BaseModel):
    nombre: str | None = Field(default=None, min_length=2, max_length=180)
    documento: str | None = Field(default=None, max_length=30)
    nit: str | None = Field(default=None, max_length=30)
    telefono: str | None = Field(default=None, max_length=30)
    correo: EmailStr | None = None
    direccion: str | None = Field(default=None, max_length=255)
    estado: bool | None = None


class ClienteRespuesta(ClienteBase):
    id_cliente: int
    estado: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    model_config = ConfigDict(from_attributes=True)
