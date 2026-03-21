"""
Commands para Task.

Los commands representan intenciones de cambio.
Son inmutables y contienen solo los datos necesarios.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class CreateTaskCommand:
    """Comando: Crear nueva tarea."""
    title: str
    description: str
    priority: str = "medium"
    project_id: UUID | None = None
    due_date: datetime | None = None


@dataclass(frozen=True)
class StartTaskCommand:
    """Comando: Iniciar tarea."""
    task_id: UUID


@dataclass(frozen=True)
class CompleteTaskCommand:
    """Comando: Completar tarea."""
    task_id: UUID


@dataclass(frozen=True)
class AssignTaskCommand:
    """Comando: Asignar tarea a usuario."""
    task_id: UUID
    user_id: UUID


@dataclass(frozen=True)
class DeleteTaskCommand:
    """Comando: Eliminar tarea."""
    task_id: UUID
