# ============================================
# ORDER SERVICE
# ============================================

from datetime import datetime

from config import get_settings
from models.order import Order, OrderItem, OrderStatus
from schemas.order import OrderCreate, OrderResponse
from repositories.order import OrderRepository
from repositories.user import UserRepository
from repositories.product import ProductRepository
from mappers.order import OrderMapper
from exceptions.user import UserNotFoundError
from exceptions.product import ProductNotFoundError, InsufficientStockError
from exceptions.order import OrderNotFoundError, OrderCannotBeCancelledError

settings = get_settings()


class OrderService:
    """
    Service para lógica de negocio de Order.
    
    Este es el service más complejo - orquesta múltiples repositories.
    """
    
    def __init__(
        self,
        order_repo: OrderRepository,
        user_repo: UserRepository,
        product_repo: ProductRepository
    ):
        self.order_repo = order_repo
        self.user_repo = user_repo
        self.product_repo = product_repo
    
    def get_by_id(self, order_id: int) -> OrderResponse:
        """Obtiene pedido por ID."""
        entity = self.order_repo.get_by_id_with_items(order_id)
        if not entity:
            raise OrderNotFoundError(order_id)
        return OrderMapper.to_response(entity)
    
    def get_by_user(self, user_id: int) -> list[OrderResponse]:
        """
        Obtiene pedidos de un usuario.
        
        TODO: Validar que usuario exista
        """
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(user_id)
        
        entities = self.order_repo.get_by_user(user_id)
        return OrderMapper.to_response_list(entities)
    
    def create(self, data: OrderCreate) -> OrderResponse:
        """
        Crea pedido completo.
        
        TODO: Implementar flujo completo:
        1. Validar usuario
        2. Validar productos y stock
        3. Crear OrderItems
        4. Calcular totales
        5. Reducir stock
        6. Guardar todo
        """
        # 1. Validar usuario
        user = self.user_repo.get_by_id(data.user_id)
        if not user:
            raise UserNotFoundError(data.user_id)
        
        # 2 y 3. Validar productos, stock y crear items
        order_items: list[OrderItem] = []
        products_to_update: list[tuple] = []
        subtotal = 0.0
        
        for item_data in data.items:
            product = self.product_repo.get_by_id(item_data.product_id)
            if not product:
                raise ProductNotFoundError(item_data.product_id)
            
            if product.stock < item_data.quantity:
                raise InsufficientStockError(
                    product_id=product.id,
                    requested=item_data.quantity,
                    available=product.stock
                )
            
            item = OrderItem(
                product_id=product.id,
                product_name=product.name,
                quantity=item_data.quantity,
                unit_price=product.price,
                subtotal=product.price * item_data.quantity
            )
            order_items.append(item)
            subtotal += item.subtotal
            products_to_update.append((product, item_data.quantity))
        
        # 4. Calcular totales
        tax = round(subtotal * settings.tax_rate, 2)
        shipping = (
            0.0 if subtotal >= settings.free_shipping_threshold
            else settings.shipping_cost
        )
        total = round(subtotal + tax + shipping, 2)
        
        # 5. Crear Order
        order = Order(
            user_id=data.user_id,
            status=OrderStatus.PENDING,
            subtotal=subtotal,
            tax=tax,
            shipping_cost=shipping,
            total=total,
            shipping_address=data.shipping_address,
            created_at=datetime.utcnow(),
            items=order_items
        )
        
        # 6. Reducir stock
        for product, quantity in products_to_update:
            product.stock -= quantity
        
        # 7. Guardar
        saved = self.order_repo.add(order)
        return OrderMapper.to_response(saved)
    
    def update_status(self, order_id: int, new_status: str) -> OrderResponse:
        """
        Actualiza estado del pedido.
        
        TODO: Validar transiciones de estado válidas
        """
        order = self.order_repo.get_by_id_with_items(order_id)
        if not order:
            raise OrderNotFoundError(order_id)
        
        order.status = new_status
        saved = self.order_repo.update(order)
        return OrderMapper.to_response(saved)
    
    def cancel(self, order_id: int) -> OrderResponse:
        """
        Cancela pedido y restaura stock.
        
        TODO: Solo permitir cancelar pedidos PENDING o CONFIRMED
        TODO: Restaurar stock de productos
        """
        order = self.order_repo.get_by_id_with_items(order_id)
        if not order:
            raise OrderNotFoundError(order_id)
        
        # Solo se pueden cancelar pedidos pending o confirmed
        if order.status not in [OrderStatus.PENDING, OrderStatus.CONFIRMED]:
            raise OrderCannotBeCancelledError(order_id, order.status)
        
        # Restaurar stock
        for item in order.items:
            product = self.product_repo.get_by_id(item.product_id)
            if product:
                product.stock += item.quantity
        
        order.status = OrderStatus.CANCELLED
        saved = self.order_repo.update(order)
        return OrderMapper.to_response(saved)
