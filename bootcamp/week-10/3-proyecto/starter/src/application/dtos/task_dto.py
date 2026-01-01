"""
DTOs para Task.

Los DTOs son objetos simples para transferir datos
entre capas. Son independientes del dominio.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class TaskDTO:
    """DTO de respuesta para Task."""
    id: UUID
    title: str
    description: str
    status: str
    priority: str
    project_id: UUID | None
    assignee_id: UUID | None
    due_date: datetime | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class TaskListDTO:
    """DTO para lista paginada de tareas."""
    items: list[TaskDTO]
    total: int
    skip: int
    limit: int
