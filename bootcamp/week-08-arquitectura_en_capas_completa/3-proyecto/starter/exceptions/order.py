# ============================================
# EXCEPCIONES ORDER
# ============================================

from .base import NotFoundError, ValidationError


class OrderNotFoundError(NotFoundError):
    """Pedido no encontrado."""
    
    def __init__(self, order_id: int):
        super().__init__(
            message=f"Order with id {order_id} not found",
            code="ORDER_NOT_FOUND"
        )


class OrderCannotBeCancelledError(ValidationError):
    """No se puede cancelar el pedido."""
    
    def __init__(self, order_id: int, current_status: str):
        super().__init__(
            message=f"Order {order_id} with status '{current_status}' cannot be cancelled",
            code="ORDER_CANNOT_CANCEL"
        )
