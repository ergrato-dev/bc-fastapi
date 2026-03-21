"""
Schemas Pydantic para validación y serialización.
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ============================================
# Enums
# ============================================

class TaskStatus(str, Enum):
    """Estados posibles de una tarea."""
    
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskPriority(str, Enum):
    """Prioridades de tarea."""
    
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# ============================================
# User Schemas
# ============================================

class UserBase(BaseModel):
    """Schema base de usuario."""
    
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    """Schema para crear usuario."""
    
    password: str = Field(..., min_length=8)


class UserResponse(UserBase):
    """Schema de respuesta de usuario."""
    
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    is_active: bool
    created_at: datetime


# ============================================
# Task Schemas
# ============================================

class TaskBase(BaseModel):
    """Schema base de tarea."""
    
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    priority: TaskPriority = TaskPriority.MEDIUM


class TaskCreate(TaskBase):
    """Schema para crear tarea."""
    pass


class TaskUpdate(BaseModel):
    """Schema para actualizar tarea."""
    
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    status: TaskStatus | None = None
    priority: TaskPriority | None = None


class TaskResponse(TaskBase):
    """Schema de respuesta de tarea."""
    
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    status: TaskStatus
    owner_id: int
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None = None


class TaskList(BaseModel):
    """Schema para lista paginada de tareas."""
    
    items: list[TaskResponse]
    total: int
    page: int
    size: int
    pages: int


# ============================================
# Auth Schemas
# ============================================

class Token(BaseModel):
    """Schema de token JWT."""
    
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Datos extraídos del token."""
    
    username: str | None = None


class LoginRequest(BaseModel):
    """Schema para login."""
    
    username: str
    password: str
