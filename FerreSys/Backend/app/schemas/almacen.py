from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class AlmacenBase(BaseModel):
    nombre: str = Field(
        min_length=2,
        max_length=120,
    )

    descripcion: str | None = Field(
        default=None,
        max_length=255,
    )

    direccion: str | None = Field(
        default=None,
        max_length=255,
    )

    telefono: str | None = Field(
        default=None,
        max_length=30,
    )

    responsable: str | None = Field(
        default=None,
        max_length=150,
    )


class AlmacenCrear(AlmacenBase):
    pass


class AlmacenActualizar(BaseModel):
    nombre: str | None = Field(
        default=None,
        min_length=2,
        max_length=120,
    )

    descripcion: str | None = Field(
        default=None,
        max_length=255,
    )

    direccion: str | None = Field(
        default=None,
        max_length=255,
    )

    telefono: str | None = Field(
        default=None,
        max_length=30,
    )

    responsable: str | None = Field(
        default=None,
        max_length=150,
    )

    estado: bool | None = None


class AlmacenRespuesta(AlmacenBase):
    id_almacen: int
    estado: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    model_config = ConfigDict(from_attributes=True)
