# ============================================
# Modelo Task
# ============================================
from datetime import datetime
from enum import Enum
from sqlalchemy import String, Boolean, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Priority(str, Enum):
    """Prioridad de la tarea"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Task(Base):
    """
    Modelo de Tarea
    
    TODO: Implementar los campos:
    - id: int (primary key)
    - title: str (max 200 chars)
    - description: str | None (text)
    - is_completed: bool (default False)
    - priority: Priority (default MEDIUM)
    - user_id: int (foreign key -> users.id)
    - created_at: datetime (default now)
    - completed_at: datetime | None
    - user: relación con User (many-to-one)
    """
    __tablename__ = "tasks"
    
    # TODO: Implementar campos
    id: Mapped[int] = mapped_column(primary_key=True)
    # title: ...
    # description: ...
    # is_completed: ...
    # priority: ...
    # user_id: ...
    # created_at: ...
    # completed_at: ...
    
    # TODO: Implementar relación con user
    # user: Mapped["User"] = relationship(...)
    
    def __repr__(self) -> str:
        return f"<Task(id={self.id}, title='{getattr(self, 'title', 'N/A')}')>"
