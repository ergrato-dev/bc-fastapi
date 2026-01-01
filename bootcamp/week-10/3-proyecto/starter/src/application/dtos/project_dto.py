"""
DTOs para Project.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class ProjectDTO:
    """DTO de respuesta para Project."""
    id: UUID
    name: str
    description: str
    owner_id: UUID
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class ProjectListDTO:
    """DTO para lista de proyectos."""
    items: list[ProjectDTO]
    total: int
