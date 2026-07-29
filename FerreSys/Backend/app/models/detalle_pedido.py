from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class DetallePedido(Base):
    __tablename__ = "detalle_pedido"

    id_detalle_pedido: Mapped[int] = mapped_column(primary_key=True)

    id_pedido: Mapped[int] = mapped_column(
        ForeignKey(
            "pedido.id_pedido",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    id_producto: Mapped[int] = mapped_column(
        ForeignKey("producto.id_producto"),
        nullable=False,
    )

    cantidad: Mapped[Decimal] = mapped_column(
        Numeric(14, 3),
        nullable=False,
    )

    precio_unitario: Mapped[Decimal] = mapped_column(
        Numeric(14, 2),
        nullable=False,
    )

    descuento: Mapped[Decimal] = mapped_column(
        Numeric(14, 2),
        nullable=False,
        default=0,
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(14, 2),
        nullable=False,
    )

    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    fecha_actualizacion: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
