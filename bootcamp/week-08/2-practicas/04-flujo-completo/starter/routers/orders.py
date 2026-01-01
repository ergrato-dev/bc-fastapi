# ============================================
# ROUTER ORDERS - ENDPOINT PRINCIPAL
# ============================================
print("--- Router: Orders Endpoint ---")

# El endpoint principal de esta práctica.
# Observa cómo el router es simple - toda la lógica está en el service.

# Descomenta las siguientes líneas:

# from fastapi import APIRouter, Depends, status
# from sqlalchemy.orm import Session

# from database import get_db
# from schemas.order import OrderCreate, OrderResponse
# from services.order import OrderService
# from repositories.user import UserRepository
# from repositories.product import ProductRepository
# from repositories.order import OrderRepository

# router = APIRouter(prefix="/orders", tags=["orders"])


# def get_order_service(db: Session = Depends(get_db)) -> OrderService:
#     """Factory de OrderService con todos sus repositories."""
#     return OrderService(
#         user_repo=UserRepository(db),
#         product_repo=ProductRepository(db),
#         order_repo=OrderRepository(db)
#     )


# @router.post(
#     "/",
#     response_model=OrderResponse,
#     status_code=status.HTTP_201_CREATED
# )
# def create_order(
#     data: OrderCreate,
#     service: OrderService = Depends(get_order_service)
# ):
#     """
#     Crea un nuevo pedido.
#     
#     Este endpoint:
#     1. Recibe OrderCreate (user_id, items, shipping_address)
#     2. Delega al service toda la lógica
#     3. Retorna OrderResponse con todos los cálculos
#     
#     Posibles errores (manejados por handlers globales):
#     - 404: Usuario o producto no encontrado
#     - 400: Stock insuficiente
#     """
#     return service.create_order(data)


# @router.get("/{order_id}", response_model=OrderResponse)
# def get_order(
#     order_id: int,
#     service: OrderService = Depends(get_order_service)
# ):
#     """Obtiene un pedido por ID."""
#     return service.get_order(order_id)
