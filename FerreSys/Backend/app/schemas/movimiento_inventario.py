from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class MovimientoInventarioCrear(BaseModel):
    id_inventario: int = Field(gt=0)
    id_tipo_movimiento: int = Field(gt=0)
    cantidad: Decimal = Field(
        gt=0,
        max_digits=14,
        decimal_places=3,
    )
    motivo: str | None = Field(default=None, max_length=255)
    observaciones: str | None = None


class MovimientoInventarioRespuesta(BaseModel):
    id_movimiento: int
    id_inventario: int
    id_tipo_movimiento: int
    tipo_movimiento: str
    naturaleza: str

    cantidad: Decimal
    stock_anterior: Decimal
    stock_actual: Decimal
    stock_disponible: Decimal

    motivo: str | None
    observaciones: str | None
    id_usuario: int
    usuario_nombre: str

    producto_codigo: str
    producto_nombre: str
    almacen_nombre: str

    fecha_movimiento: datetime
