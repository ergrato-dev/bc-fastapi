"""
Queries para Task.

Las queries representan peticiones de lectura.
No modifican el estado del sistema.
"""

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetTaskQuery:
    """Query: Obtener tarea por ID."""
    task_id: UUID


@dataclass(frozen=True)
class ListTasksQuery:
    """Query: Listar tareas con filtros."""
    status: str | None = None
    priority: str | None = None
    project_id: UUID | None = None
    assignee_id: UUID | None = None
    skip: int = 0
    limit: int = 100
