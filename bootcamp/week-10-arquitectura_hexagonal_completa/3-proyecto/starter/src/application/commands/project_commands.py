"""
Commands para Project.
"""

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateProjectCommand:
    """Comando: Crear nuevo proyecto."""
    name: str
    description: str
    owner_id: UUID


@dataclass(frozen=True)
class AddTaskToProjectCommand:
    """Comando: Agregar tarea a proyecto."""
    project_id: UUID
    task_id: UUID
