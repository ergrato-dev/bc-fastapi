"""
Schemas para Task - Request/Response de la API.
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


# ============================================
# REQUEST SCHEMAS
# ============================================

class TaskCreateRequest(BaseModel):
    """Request: Crear tarea."""
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(default="")
    priority: str = Field(default="medium", pattern="^(low|medium|high|urgent)$")
    project_id: UUID | None = None
    due_date: datetime | None = None


class TaskAssignRequest(BaseModel):
    """Request: Asignar tarea."""
    user_id: UUID


# ============================================
# RESPONSE SCHEMAS
# ============================================

class TaskResponse(BaseModel):
    """Response: Tarea."""
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


class TaskListResponse(BaseModel):
    """Response: Lista de tareas."""
    items: list[TaskResponse]
    total: int
    skip: int
    limit: int
