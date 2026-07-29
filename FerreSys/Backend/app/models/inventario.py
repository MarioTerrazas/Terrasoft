from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Inventario(Base):
    __tablename__ = "inventario"
    __table_args__ = (
        UniqueConstraint(
            "id_producto",
            "id_almacen",
            name="uq_inventario_producto_almacen",
        ),
    )

    id_inventario: Mapped[int] = mapped_column(primary_key=True)

    id_producto: Mapped[int] = mapped_column(
        ForeignKey("producto.id_producto"),
        nullable=False,
    )

    id_almacen: Mapped[int] = mapped_column(
        ForeignKey("almacen.id_almacen"),
        nullable=False,
    )

    stock_actual: Mapped[Decimal] = mapped_column(
        Numeric(14, 3),
        nullable=False,
        default=0,
    )

    stock_reservado: Mapped[Decimal] = mapped_column(
        Numeric(14, 3),
        nullable=False,
        default=0,
    )

    stock_minimo: Mapped[Decimal] = mapped_column(
        Numeric(14, 3),
        nullable=False,
        default=0,
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
