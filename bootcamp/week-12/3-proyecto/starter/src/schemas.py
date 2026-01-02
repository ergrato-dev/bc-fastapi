"""
Pydantic schemas.
"""

from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


# ============================================
# USER SCHEMAS
# ============================================

class UserCreate(BaseModel):
    """Schema for creating a user."""
    email: EmailStr
    password: str = Field(min_length=6)
    full_name: str | None = None


class UserResponse(BaseModel):
    """Schema for user response."""
    id: int
    email: EmailStr
    full_name: str | None
    is_active: bool
    
    model_config = {"from_attributes": True}


# ============================================
# TASK SCHEMAS
# ============================================

class TaskCreate(BaseModel):
    """Schema for creating a task."""
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    priority: str = Field(default="medium", pattern="^(low|medium|high)$")
    due_date: datetime | None = None


class TaskUpdate(BaseModel):
    """Schema for updating a task."""
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    priority: str | None = Field(default=None, pattern="^(low|medium|high)$")
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    """Schema for task response."""
    id: int
    title: str
    description: str | None
    completed: bool
    priority: str
    due_date: datetime | None
    created_at: datetime
    completed_at: datetime | None
    owner_id: int
    
    model_config = {"from_attributes": True}


# ============================================
# AUTH SCHEMAS
# ============================================

class Token(BaseModel):
    """Schema for authentication token."""
    access_token: str
    token_type: str
