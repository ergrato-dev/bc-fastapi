# ============================================
# PASO 2: Implementar OrderService
# ============================================
"""
El Service recibe repositorios por inyección.
Contiene TODA la lógica de negocio.
"""

from pydantic import BaseModel, Field, EmailStr

from models import User, Product, Order, OrderStatus
from repositories import UserRepository, ProductRepository, OrderRepository


# ============================================
# Schemas
# ============================================
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int = Field(..., gt=0)


# ============================================
# Excepciones
# ============================================
class NotFoundError(Exception):
    pass


class BusinessError(Exception):
    pass


# ============================================
# Descomenta OrderService:
# ============================================

# class OrderService:
#     """
#     Service para gestión de órdenes.
#     Recibe repositorios por inyección de dependencias.
#     """
#     
#     def __init__(
#         self,
#         user_repo: UserRepository,
#         product_repo: ProductRepository,
#         order_repo: OrderRepository
#     ):
#         # ✅ Recibe repositorios, NO Session
#         self.user_repo = user_repo
#         self.product_repo = product_repo
#         self.order_repo = order_repo
#     
#     def create_order(self, data: OrderCreate) -> Order:
#         """
#         Crea una nueva orden.
#         
#         Lógica de negocio:
#         1. Verificar que usuario existe
#         2. Verificar que producto existe
#         3. Verificar stock disponible
#         4. Calcular total
#         5. Descontar stock
#         6. Crear orden
#         """
#         # Validar usuario
#         user = self.user_repo.get_by_id(data.user_id)
#         if not user:
#             raise NotFoundError(f"User {data.user_id} not found")
#         
#         # Validar producto
#         product = self.product_repo.get_by_id(data.product_id)
#         if not product:
#             raise NotFoundError(f"Product {data.product_id} not found")
#         
#         # Validar stock
#         if product.stock < data.quantity:
#             raise BusinessError(
#                 f"Insufficient stock. Available: {product.stock}, Requested: {data.quantity}"
#             )
#         
#         # Calcular total
#         total = product.price * data.quantity
#         
#         # Descontar stock
#         product.stock -= data.quantity
#         self.product_repo.update(product)
#         
#         # Crear orden
#         order = Order(
#             user_id=data.user_id,
#             product_id=data.product_id,
#             quantity=data.quantity,
#             total=total,
#             status=OrderStatus.PENDING
#         )
#         return self.order_repo.add(order)
#     
#     def get_order(self, order_id: int) -> Order:
#         """Obtiene orden con detalles"""
#         order = self.order_repo.get_with_details(order_id)
#         if not order:
#             raise NotFoundError(f"Order {order_id} not found")
#         return order
#     
#     def get_user_orders(self, user_id: int) -> list[Order]:
#         """Obtiene órdenes de un usuario"""
#         user = self.user_repo.get_by_id(user_id)
#         if not user:
#             raise NotFoundError(f"User {user_id} not found")
#         return self.order_repo.get_by_user(user_id)
#     
#     def confirm_order(self, order_id: int) -> Order:
#         """Confirma una orden pendiente"""
#         order = self.get_order(order_id)
#         
#         if order.status != OrderStatus.PENDING:
#             raise BusinessError(f"Order is {order.status.value}, cannot confirm")
#         
#         order.status = OrderStatus.CONFIRMED
#         return self.order_repo.update(order)
#     
#     def cancel_order(self, order_id: int) -> Order:
#         """
#         Cancela una orden y restaura el stock.
#         Solo órdenes PENDING o CONFIRMED pueden cancelarse.
#         """
#         order = self.get_order(order_id)
#         
#         if order.status not in (OrderStatus.PENDING, OrderStatus.CONFIRMED):
#             raise BusinessError(f"Order is {order.status.value}, cannot cancel")
#         
#         # Restaurar stock
#         product = self.product_repo.get_by_id(order.product_id)
#         if product:
#             product.stock += order.quantity
#             self.product_repo.update(product)
#         
#         order.status = OrderStatus.CANCELLED
#         return self.order_repo.update(order)
