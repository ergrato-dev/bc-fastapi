# ============================================
# MODELO USER
# ============================================

from datetime import datetime
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    """
    Entidad User.
    
    TODO: Completar los campos del modelo
    """
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # TODO: Agregar campo email (String 200, unique, index)
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    
    # TODO: Agregar campo name (String 100)
    name: Mapped[str] = mapped_column(String(100))
    
    # TODO: Agregar campo password_hash (String 200)
    # Este campo NO debe exponerse en las respuestas
    password_hash: Mapped[str] = mapped_column(String(200))
    
    # TODO: Agregar campo is_active (Boolean, default True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # TODO: Agregar campo created_at (DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Relación con orders
    orders: Mapped[list["Order"]] = relationship(back_populates="user")
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}')>"
