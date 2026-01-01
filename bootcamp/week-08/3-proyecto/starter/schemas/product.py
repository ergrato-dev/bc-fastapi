# ============================================
# SCHEMAS PRODUCT
# ============================================

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ProductCreate(BaseModel):
    """
    DTO para crear producto.
    
    TODO: Definir los campos con validaciones
    """
    # TODO: name con validaciones
    name: str = Field(..., min_length=1, max_length=200)
    
    # TODO: sku con pattern para formato (ej: ABC-1234)
    sku: str = Field(..., pattern=r"^[A-Z]{2,4}-\d{3,6}$")
    
    # TODO: description opcional
    description: str | None = Field(None, max_length=2000)
    
    # TODO: price mayor a 0
    price: float = Field(..., gt=0)
    
    # TODO: stock >= 0
    stock: int = Field(default=0, ge=0)
    
    # TODO: category_id
    category_id: int


class ProductUpdate(BaseModel):
    """
    DTO para actualizar producto (PATCH).
    
    TODO: Todos los campos opcionales excepto SKU
    """
    name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    price: float | None = Field(None, gt=0)
    stock: int | None = Field(None, ge=0)
    category_id: int | None = None
    is_active: bool | None = None
    # SKU no se puede cambiar


class ProductResponse(BaseModel):
    """
    DTO de respuesta para producto.
    """
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    sku: str
    description: str | None
    price: float
    stock: int
    category_id: int
    is_active: bool
    created_at: datetime
