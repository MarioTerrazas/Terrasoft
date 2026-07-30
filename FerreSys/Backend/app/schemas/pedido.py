from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field, model_validator


class DetallePedidoCrear(BaseModel):
    id_producto: int = Field(gt=0)

    cantidad: Decimal = Field(
        gt=0,
        max_digits=14,
        decimal_places=3,
    )

    descuento: Decimal = Field(
        default=0,
        ge=0,
        max_digits=14,
        decimal_places=2,
    )


class PedidoCrear(BaseModel):
    id_cliente: int = Field(gt=0)
    id_almacen: int = Field(gt=0)

    descuento: Decimal = Field(
        default=0,
        ge=0,
        max_digits=14,
        decimal_places=2,
    )

    detalles: list[DetallePedidoCrear] = Field(
        min_length=1,
        max_length=100,
    )

    @model_validator(mode="after")
    def validar_productos_repetidos(self):
        productos = [
            detalle.id_producto
            for detalle in self.detalles
        ]

        if len(productos) != len(set(productos)):
            raise ValueError(
                "No se puede repetir un producto dentro del pedido"
            )

        return self


class PedidoCambiarEstado(BaseModel):
    estado: Literal[
        "PENDIENTE",
        "CONFIRMADO",
        "PREPARANDO",
        "ENTREGADO",
        "CANCELADO",
    ]


class DetallePedidoRespuesta(BaseModel):
    id_detalle_pedido: int
    id_producto: int
    producto_codigo: str
    producto_nombre: str
    cantidad: Decimal
    precio_unitario: Decimal
    descuento: Decimal
    subtotal: Decimal


class PedidoRespuesta(BaseModel):
    id_pedido: int
    numero_pedido: str

    id_cliente: int
    cliente_nombre: str

    id_almacen: int
    almacen_nombre: str

    fecha: datetime
    estado: str

    subtotal: Decimal
    descuento: Decimal
    total: Decimal

    detalles: list[DetallePedidoRespuesta]

    fecha_creacion: datetime
    fecha_actualizacion: datetime
