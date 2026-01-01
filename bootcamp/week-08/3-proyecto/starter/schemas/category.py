# ============================================
# SCHEMAS CATEGORY
# ============================================

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class CategoryCreate(BaseModel):
    """
    DTO para crear categoría.
    
    TODO: Definir los campos con validaciones
    """
    # TODO: name con min_length y max_length
    name: str = Field(..., min_length=2, max_length=100)
    
    # TODO: description opcional
    description: str | None = Field(None, max_length=500)


class CategoryUpdate(BaseModel):
    """
    DTO para actualizar categoría (PATCH).
    
    TODO: Todos los campos opcionales
    """
    name: str | None = Field(None, min_length=2, max_length=100)
    description: str | None = Field(None, max_length=500)
    is_active: bool | None = None


class CategoryResponse(BaseModel):
    """
    DTO de respuesta para categoría.
    """
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    description: str | None
    is_active: bool
    created_at: datetime
