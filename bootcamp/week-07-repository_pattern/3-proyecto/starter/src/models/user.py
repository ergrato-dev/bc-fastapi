# ============================================
# Modelo User
# ============================================
from datetime import datetime
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    """
    Modelo de Usuario
    
    TODO: Implementar los campos:
    - id: int (primary key)
    - username: str (unique, max 50 chars)
    - email: str (unique, max 100 chars)
    - is_active: bool (default True)
    - created_at: datetime (default now)
    - tasks: relación con Task (one-to-many)
    """
    __tablename__ = "users"
    
    # TODO: Implementar campos
    id: Mapped[int] = mapped_column(primary_key=True)
    # username: ...
    # email: ...
    # is_active: ...
    # created_at: ...
    
    # TODO: Implementar relación con tasks
    # tasks: Mapped[list["Task"]] = relationship(...)
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{getattr(self, 'username', 'N/A')}')>"
