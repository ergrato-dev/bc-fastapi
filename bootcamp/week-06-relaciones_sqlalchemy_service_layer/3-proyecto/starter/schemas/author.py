# ============================================
# Schemas de Author
# ============================================
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class AuthorBase(BaseModel):
    """Base schema para Author"""
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    bio: str | None = None


class AuthorCreate(AuthorBase):
    """Schema para crear Author"""
    pass


class AuthorUpdate(BaseModel):
    """Schema para actualizar Author (todos opcionales)"""
    name: str | None = Field(None, min_length=2, max_length=100)
    email: EmailStr | None = None
    bio: str | None = None


class AuthorResponse(AuthorBase):
    """Schema de respuesta para Author"""
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class AuthorWithPosts(AuthorResponse):
    """Schema de Author con sus posts"""
    posts: list["PostSummary"] = []


# Import circular fix
from schemas.post import PostSummary
AuthorWithPosts.model_rebuild()
