# ============================================
# SQLAlchemy Models
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para definir el modelo Task.
# ============================================

from datetime import datetime

# TODO: Importar SQLAlchemy
# from sqlalchemy import String, Boolean, DateTime, func
# from sqlalchemy.orm import Mapped, mapped_column

# from src.database import Base


# ============================================
# TODO 1: Definir el modelo Task
# ============================================
# class Task(Base):
#     """Task model for the database"""
#
#     __tablename__ = "tasks"
#
#     id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     title: Mapped[str] = mapped_column(String(200), nullable=False)
#     description: Mapped[str | None] = mapped_column(String(1000), nullable=True)
#     completed: Mapped[bool] = mapped_column(Boolean, default=False)
#     priority: Mapped[str] = mapped_column(String(20), default="medium")
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now()
#     )
#
#     def __repr__(self) -> str:
#         return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"


# ============================================
# Placeholder mientras se implementa
# ============================================
class Task:
    """Placeholder - implement real SQLAlchemy model above"""

    id: int
    title: str
    description: str | None
    completed: bool = False
    priority: str = "medium"
    created_at: datetime
    updated_at: datetime
