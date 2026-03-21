"""
Task Entity - Entidad del dominio.
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from enum import Enum
from datetime import datetime, UTC


class TaskStatus(Enum):
    """Value Object: Estado de la tarea."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass
class Task:
    """Entidad: Tarea del dominio."""
    
    id: UUID
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    
    @classmethod
    def create(cls, title: str, description: str) -> "Task":
        """Factory method para crear tarea."""
        return cls(
            id=uuid4(),
            title=title,
            description=description,
        )
    
    def start(self) -> None:
        """Iniciar la tarea."""
        self.status = TaskStatus.IN_PROGRESS
    
    def complete(self) -> None:
        """Completar la tarea."""
        self.status = TaskStatus.COMPLETED
