# ============================================
# ORDERS ROUTER
# ============================================

from fastapi import APIRouter, Depends, status

from schemas.order import OrderCreate, OrderResponse, OrderStatusUpdate
from services.order import OrderService
from dependencies import get_order_service

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    service: OrderService = Depends(get_order_service)
):
    """Obtiene pedido por ID."""
    return service.get_by_id(order_id)


@router.get("/user/{user_id}", response_model=list[OrderResponse])
def get_orders_by_user(
    user_id: int,
    service: OrderService = Depends(get_order_service)
):
    """Obtiene pedidos de un usuario."""
    return service.get_by_user(user_id)


@router.post(
    "/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
def create_order(
    data: OrderCreate,
    service: OrderService = Depends(get_order_service)
):
    """
    Crea nuevo pedido.
    
    Valida usuario, productos y stock.
    Calcula totales automáticamente.
    Reduce stock de productos.
    """
    return service.create(data)


@router.patch("/{order_id}/status", response_model=OrderResponse)
def update_order_status(
    order_id: int,
    data: OrderStatusUpdate,
    service: OrderService = Depends(get_order_service)
):
    """Actualiza estado del pedido."""
    return service.update_status(order_id, data.status)


@router.patch("/{order_id}/cancel", response_model=OrderResponse)
def cancel_order(
    order_id: int,
    service: OrderService = Depends(get_order_service)
):
    """
    Cancela pedido.
    
    Solo pedidos pending o confirmed pueden cancelarse.
    Restaura stock de productos.
    """
    return service.cancel(order_id)
