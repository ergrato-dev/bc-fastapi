# ============================================
# Schemas Pydantic (DTOs)
# ============================================
from pydantic import BaseModel, EmailStr, ConfigDict


# ============================================
# Author Schemas
# ============================================
class AuthorBase(BaseModel):
    name: str
    email: EmailStr


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class AuthorResponse(AuthorBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)


# ============================================
# Tag Schemas
# ============================================
class TagBase(BaseModel):
    name: str


class TagResponse(TagBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)


# ============================================
# Post Schemas
# ============================================
class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    author_id: int
    tag_names: list[str] | None = None


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    tag_names: list[str] | None = None


class PostResponse(PostBase):
    id: int
    author_id: int
    author: AuthorResponse
    tags: list[TagResponse]
    
    model_config = ConfigDict(from_attributes=True)
