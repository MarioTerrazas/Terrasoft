from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class ProductoBase(BaseModel):
    codigo: str = Field(min_length=1, max_length=50)
    nombre: str = Field(min_length=2, max_length=180)
    descripcion: str | None = None
    observaciones: str | None = None

    precio_compra: Decimal = Field(default=0, ge=0, max_digits=14, decimal_places=2)
    precio_venta: Decimal = Field(default=0, ge=0, max_digits=14, decimal_places=2)
    stock_minimo: Decimal = Field(default=0, ge=0, max_digits=14, decimal_places=3)

    @model_validator(mode="after")
    def validar_precios(self):
        if self.precio_venta < self.precio_compra:
            raise ValueError(
                "El precio de venta no puede ser menor que el precio de compra"
            )
        return self


class ProductoCrear(ProductoBase):
    pass


class ProductoActualizar(BaseModel):
    codigo: str | None = Field(default=None, min_length=1, max_length=50)
    nombre: str | None = Field(default=None, min_length=2, max_length=180)
    descripcion: str | None = None
    observaciones: str | None = None

    precio_compra: Decimal | None = Field(
        default=None,
        ge=0,
        max_digits=14,
        decimal_places=2,
    )
    precio_venta: Decimal | None = Field(
        default=None,
        ge=0,
        max_digits=14,
        decimal_places=2,
    )
    stock_minimo: Decimal | None = Field(
        default=None,
        ge=0,
        max_digits=14,
        decimal_places=3,
    )
    estado: bool | None = None


class ProductoRespuesta(ProductoBase):
    id_producto: int
    estado: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    model_config = ConfigDict(from_attributes=True)
