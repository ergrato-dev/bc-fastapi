# ============================================
# SCHEMAS ORDER
# ============================================

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class OrderItemCreate(BaseModel):
    """DTO para item de pedido - INPUT."""
    product_id: int
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    """
    DTO para crear pedido.
    
    TODO: Definir los campos
    """
    # TODO: user_id
    user_id: int
    
    # TODO: items con al menos 1 elemento
    items: list[OrderItemCreate] = Field(..., min_length=1)
    
    # TODO: shipping_address con min_length
    shipping_address: str = Field(..., min_length=10)


class OrderItemResponse(BaseModel):
    """DTO de respuesta para item de pedido."""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    product_id: int
    product_name: str
    quantity: int
    unit_price: float
    subtotal: float


class OrderResponse(BaseModel):
    """DTO de respuesta para pedido."""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    user_id: int
    status: str
    items: list[OrderItemResponse]
    subtotal: float
    tax: float
    shipping_cost: float
    total: float
    shipping_address: str
    created_at: datetime


class OrderStatusUpdate(BaseModel):
    """DTO para cambiar estado de pedido."""
    status: str = Field(..., description="Nuevo estado del pedido")
