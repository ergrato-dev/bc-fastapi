# ============================================
# Pydantic Schemas
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para definir los schemas.
# ============================================

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


# ============================================
# Enums
# ============================================
class Priority(str, Enum):
    """Task priority levels"""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# ============================================
# TODO 1: Schema base para Task
# ============================================
class TaskBase(BaseModel):
    """Base schema for Task"""

    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(None, max_length=1000)
    priority: Priority = Priority.MEDIUM


# ============================================
# TODO 2: Schema para crear Task
# ============================================
class TaskCreate(TaskBase):
    """Schema for creating a task"""

    pass


# ============================================
# TODO 3: Schema para actualizar Task
# ============================================
class TaskUpdate(BaseModel):
    """Schema for updating a task (all fields optional)"""

    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=1000)
    completed: bool | None = None
    priority: Priority | None = None


# ============================================
# TODO 4: Schema de respuesta Task
# ============================================
class TaskResponse(TaskBase):
    """Schema for task response"""

    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ============================================
# TODO 5: Schema de lista paginada
# ============================================
class TaskListResponse(BaseModel):
    """Paginated list of tasks"""

    items: list[TaskResponse]
    total: int
    page: int
    size: int
    pages: int


# ============================================
# Health Schemas
# ============================================
class HealthResponse(BaseModel):
    """Health check response"""

    status: str
    version: str
    environment: str


class ReadinessResponse(BaseModel):
    """Readiness check response"""

    status: str
    database: str
    redis: str
