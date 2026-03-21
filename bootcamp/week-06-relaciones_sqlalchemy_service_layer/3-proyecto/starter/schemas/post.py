# ============================================
# Schemas de Post
# ============================================
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class PostBase(BaseModel):
    """Base schema para Post"""
    title: str = Field(..., min_length=5, max_length=200)
    content: str = Field(..., min_length=10)


class PostCreate(PostBase):
    """Schema para crear Post"""
    author_id: int
    tag_names: list[str] | None = None  # Tags por nombre


class PostUpdate(BaseModel):
    """Schema para actualizar Post"""
    title: str | None = Field(None, min_length=5, max_length=200)
    content: str | None = Field(None, min_length=10)
    tag_names: list[str] | None = None


class TagSummary(BaseModel):
    """Schema resumido de Tag (para anidado)"""
    id: int
    name: str
    slug: str
    
    model_config = ConfigDict(from_attributes=True)


class AuthorSummary(BaseModel):
    """Schema resumido de Author (para anidado)"""
    id: int
    name: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)


class PostSummary(BaseModel):
    """Schema resumido de Post (para listados)"""
    id: int
    title: str
    published: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class PostResponse(PostBase):
    """Schema completo de Post con relaciones"""
    id: int
    published: bool
    created_at: datetime
    updated_at: datetime | None
    author: AuthorSummary
    tags: list[TagSummary]
    
    model_config = ConfigDict(from_attributes=True)


class PostList(BaseModel):
    """Schema para listado paginado de Posts"""
    items: list[PostResponse]
    total: int
    page: int
    size: int
