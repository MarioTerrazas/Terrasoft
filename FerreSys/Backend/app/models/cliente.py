from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(180), nullable=False)
    documento: Mapped[str | None] = mapped_column(String(30))
    nit: Mapped[str | None] = mapped_column(String(30))
    telefono: Mapped[str | None] = mapped_column(String(30))
    correo: Mapped[str | None] = mapped_column(String(150))
    direccion: Mapped[str | None] = mapped_column(String(255))
    estado: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
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
