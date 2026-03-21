"""
Pydantic Schemas
================
Schemas de validación para la Library API.

Schemas a implementar:
- AuthorCreate, AuthorUpdate, AuthorResponse
- BookCreate, BookUpdate, BookResponse
"""

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


# ============================================
# AUTHOR SCHEMAS
# ============================================

class AuthorBase(BaseModel):
    """Campos comunes de Author"""
    name: str = Field(..., min_length=1, max_length=100)
    country: str | None = Field(None, max_length=50)


class AuthorCreate(AuthorBase):
    """Schema para crear autor"""
    # Hereda name y country de AuthorBase
    pass


class AuthorUpdate(BaseModel):
    """Schema para actualizar autor (campos opcionales)"""
    # TODO: Agregar campo 'name' opcional (str | None)
    # TODO: Agregar campo 'country' opcional (str | None)
    pass


class AuthorResponse(AuthorBase):
    """Schema de respuesta de autor"""
    id: int
    created_at: datetime
    
    # Permite crear desde objeto SQLAlchemy
    model_config = ConfigDict(from_attributes=True)


# ============================================
# BOOK SCHEMAS
# ============================================

class BookBase(BaseModel):
    """Campos comunes de Book"""
    title: str = Field(..., min_length=1, max_length=200)
    isbn: str = Field(..., min_length=10, max_length=13)
    year: int | None = Field(None, ge=1000, le=2100)
    author_id: int


class BookCreate(BookBase):
    """Schema para crear libro"""
    # Hereda todos los campos de BookBase
    pass


class BookUpdate(BaseModel):
    """Schema para actualizar libro (campos opcionales)"""
    # TODO: Agregar campos opcionales para actualización
    # - title: str | None
    # - isbn: str | None  
    # - year: int | None
    # - author_id: int | None
    pass


class BookResponse(BookBase):
    """Schema de respuesta de libro"""
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================
# PAGINATION SCHEMAS
# ============================================

class PaginatedAuthors(BaseModel):
    """Respuesta paginada de autores"""
    authors: list[AuthorResponse]
    total: int
    skip: int
    limit: int


class PaginatedBooks(BaseModel):
    """Respuesta paginada de libros"""
    books: list[BookResponse]
    total: int
    skip: int
    limit: int
