# models.py
"""Modelo SQLAlchemy para usuarios."""

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    """
    Modelo de usuario para autenticación.
    
    Attributes:
        id: ID único del usuario
        email: Email único (usado como username)
        full_name: Nombre completo
        hashed_password: Password hasheado con bcrypt
        role: Rol del usuario (user, admin)
        is_active: Si el usuario está activo
    """
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), default="user")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    def __repr__(self) -> str:
        return f"<User {self.email}>"
