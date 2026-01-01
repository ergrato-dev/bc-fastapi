"""
Schemas para User - Request/Response de la API.
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


class UserCreateRequest(BaseModel):
    """Request: Crear usuario."""
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)


class UserResponse(BaseModel):
    """Response: Usuario."""
    id: UUID
    email: str
    name: str
    is_active: bool
    created_at: datetime


class UserListResponse(BaseModel):
    """Response: Lista de usuarios."""
    items: list[UserResponse]
    total: int
