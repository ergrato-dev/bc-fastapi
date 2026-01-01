# ============================================
# ORDER MAPPER
# ============================================

from models.order import Order, OrderItem
from schemas.order import OrderResponse, OrderItemResponse


class OrderMapper:
    """Mapper para conversiones de Order."""
    
    @staticmethod
    def to_item_response(entity: OrderItem) -> OrderItemResponse:
        """Convierte OrderItem → OrderItemResponse."""
        return OrderItemResponse.model_validate(entity)
    
    @staticmethod
    def to_response(entity: Order) -> OrderResponse:
        """
        Convierte Order entity → OrderResponse.
        
        TODO: Implementar conversión incluyendo items
        """
        return OrderResponse(
            id=entity.id,
            user_id=entity.user_id,
            status=entity.status,
            items=[OrderMapper.to_item_response(item) for item in entity.items],
            subtotal=entity.subtotal,
            tax=entity.tax,
            shipping_cost=entity.shipping_cost,
            total=entity.total,
            shipping_address=entity.shipping_address,
            created_at=entity.created_at
        )
    
    @staticmethod
    def to_response_list(entities: list[Order]) -> list[OrderResponse]:
        """Convierte lista de entities."""
        return [OrderMapper.to_response(e) for e in entities]
