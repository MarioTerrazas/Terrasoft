from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class InventarioCrear(BaseModel):
    id_producto: int = Field(gt=0)
    id_almacen: int = Field(gt=0)

    stock_actual: Decimal = Field(
        default=0,
        ge=0,
        max_digits=14,
        decimal_places=3,
    )

    stock_reservado: Decimal = Field(
        default=0,
        ge=0,
        max_digits=14,
        decimal_places=3,
    )

    stock_minimo: Decimal = Field(
        default=0,
        ge=0,
        max_digits=14,
        decimal_places=3,
    )

    @model_validator(mode="after")
    def validar_stock(self):
        if self.stock_reservado > self.stock_actual:
            raise ValueError(
                "El stock reservado no puede superar el stock actual"
            )

        return self


class InventarioActualizar(BaseModel):
    stock_reservado: Decimal | None = Field(
        default=None,
        ge=0,
        max_digits=14,
        decimal_places=3,
    )

    stock_minimo: Decimal | None = Field(
        default=None,
        ge=0,
        max_digits=14,
        decimal_places=3,
    )


class InventarioRespuesta(BaseModel):
    id_inventario: int
    id_producto: int
    id_almacen: int

    stock_actual: Decimal
    stock_reservado: Decimal
    stock_minimo: Decimal

    stock_disponible: Decimal
    bajo_stock: bool

    producto_codigo: str
    producto_nombre: str
    almacen_nombre: str

    fecha_creacion: datetime
    fecha_actualizacion: datetime

    model_config = ConfigDict(from_attributes=True)
