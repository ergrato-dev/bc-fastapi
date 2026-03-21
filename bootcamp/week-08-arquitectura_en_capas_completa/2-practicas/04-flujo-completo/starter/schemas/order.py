# ============================================
# SCHEMAS ORDER
# ============================================
print("--- Schemas: Order DTOs ---")

# DTOs para el flujo de pedidos.
# Observa cómo Input (Create) es diferente de Output (Response).

# Descomenta las siguientes líneas:

# from datetime import datetime
# from pydantic import BaseModel, Field, ConfigDict


# # ============================================
# # INPUT DTOs
# # ============================================

# class OrderItemCreate(BaseModel):
#     """
#     Item de pedido - INPUT.
#     
#     Solo necesita product_id y quantity.
#     El precio se obtiene del producto.
#     """
#     product_id: int
#     quantity: int = Field(..., gt=0)


# class OrderCreate(BaseModel):
#     """
#     Crear pedido - INPUT.
#     
#     El cliente envía user_id, items y dirección.
#     Todo lo demás se calcula en el backend.
#     """
#     user_id: int
#     items: list[OrderItemCreate] = Field(..., min_length=1)
#     shipping_address: str = Field(..., min_length=10)


# # ============================================
# # OUTPUT DTOs
# # ============================================

# class OrderItemResponse(BaseModel):
#     """
#     Item de pedido - OUTPUT.
#     
#     Incluye toda la información calculada.
#     """
#     model_config = ConfigDict(from_attributes=True)
#     
#     id: int
#     product_id: int
#     product_name: str
#     quantity: int
#     unit_price: float
#     subtotal: float


# class OrderResponse(BaseModel):
#     """
#     Pedido - OUTPUT.
#     
#     Incluye todos los montos calculados y los items.
#     """
#     model_config = ConfigDict(from_attributes=True)
#     
#     id: int
#     user_id: int
#     status: str
#     items: list[OrderItemResponse]
#     subtotal: float
#     tax: float
#     shipping_cost: float
#     total: float
#     shipping_address: str
#     created_at: datetime
