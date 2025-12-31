"""
Schemas Pydantic
================

Define los modelos de datos para validación.

TODO: Completa los schemas siguiendo las instrucciones.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


# ============================================
# ENUMS
# ============================================

class SortOrder(str, Enum):
    """Orden de clasificación"""
    asc = "asc"
    desc = "desc"


class ProductSortField(str, Enum):
    """Campos para ordenar productos"""
    name = "name"
    price = "price"
    created_at = "created_at"
    stock = "stock"


# ============================================
# CATEGORY SCHEMAS
# ============================================

class CategoryBase(BaseModel):
    """Schema base para categorías"""
    name: str = Field(..., min_length=2, max_length=50)
    description: str | None = Field(default=None, max_length=200)


class CategoryCreate(CategoryBase):
    """Schema para crear categoría"""
    # TODO: Hereda de CategoryBase, no necesita campos adicionales
    pass


class CategoryUpdate(BaseModel):
    """Schema para actualizar categoría"""
    # TODO: Todos los campos opcionales
    # name: str | None = None
    # description: str | None = None
    pass


class CategoryResponse(CategoryBase):
    """Schema de respuesta para categoría"""
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


# ============================================
# PRODUCT SCHEMAS
# ============================================

class ProductBase(BaseModel):
    """Schema base para productos"""
    # TODO: Define los campos base
    # name: str (2-100 chars)
    # description: str | None (max 500 chars)
    # price: float (> 0)
    # stock: int (>= 0, default 0)
    # tags: list[str] (default [])
    pass


class ProductCreate(ProductBase):
    """Schema para crear producto"""
    # TODO: Añade category_id requerido (> 0)
    pass


class ProductUpdate(BaseModel):
    """Schema para actualización parcial"""
    # TODO: Todos los campos opcionales
    # name: str | None
    # description: str | None
    # price: float | None
    # category_id: int | None
    # stock: int | None
    # tags: list[str] | None
    pass


class ProductResponse(ProductBase):
    """Schema de respuesta para producto"""
    # TODO: Añade id, category_id, created_at
    # También incluye category (CategoryResponse | None)
    pass


# ============================================
# PAGINATION SCHEMAS
# ============================================

class PaginatedResponse(BaseModel):
    """Schema para respuestas paginadas"""
    # TODO: Define los campos de paginación
    # items: list
    # total: int
    # page: int
    # per_page: int
    # pages: int
    # has_next: bool
    # has_prev: bool
    pass
