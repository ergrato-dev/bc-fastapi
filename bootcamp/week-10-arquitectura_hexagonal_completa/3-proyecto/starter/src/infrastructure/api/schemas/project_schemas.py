"""
Schemas para Project - Request/Response de la API.
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class ProjectCreateRequest(BaseModel):
    """Request: Crear proyecto."""
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="")
    owner_id: UUID


class ProjectResponse(BaseModel):
    """Response: Proyecto."""
    id: UUID
    name: str
    description: str
    owner_id: UUID
    created_at: datetime
    updated_at: datetime


class ProjectListResponse(BaseModel):
    """Response: Lista de proyectos."""
    items: list[ProjectResponse]
    total: int
