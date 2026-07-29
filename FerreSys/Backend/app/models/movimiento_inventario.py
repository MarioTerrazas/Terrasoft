from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class MovimientoInventario(Base):
    __tablename__ = "movimiento_inventario"

    id_movimiento: Mapped[int] = mapped_column(primary_key=True)

    id_inventario: Mapped[int] = mapped_column(
        ForeignKey("inventario.id_inventario"),
        nullable=False,
    )
    id_tipo_movimiento: Mapped[int] = mapped_column(
        ForeignKey("tipo_movimiento.id_tipo_movimiento"),
        nullable=False,
    )
    cantidad: Mapped[Decimal] = mapped_column(
        Numeric(14, 3),
        nullable=False,
    )
    motivo: Mapped[str | None] = mapped_column(String(255))
    observaciones: Mapped[str | None] = mapped_column(Text)
    fecha_movimiento: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario.id_usuario"),
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
