# ============================================
# ORDER SERVICE - FLUJO COMPLETO
# ============================================
print("--- Service: Order Service - Flujo Completo ---")

# Este es el CORAZÓN de la práctica.
# Aquí se orquesta todo el flujo de crear un pedido.

# Descomenta las siguientes líneas:

# from datetime import datetime

# from models.order import Order, OrderItem, OrderStatus
# from schemas.order import OrderCreate
# from repositories.user import UserRepository
# from repositories.product import ProductRepository
# from repositories.order import OrderRepository
# from exceptions.user import UserNotFoundError
# from exceptions.product import ProductNotFoundError, InsufficientStockError


# class OrderService:
#     """
#     Service que orquesta la creación de pedidos.
#     
#     Coordina múltiples repositories y aplica reglas de negocio.
#     """
#     
#     # Constantes de negocio
#     TAX_RATE = 0.16  # 16% IVA
#     FREE_SHIPPING_THRESHOLD = 100.0  # Envío gratis si > $100
#     SHIPPING_COST = 10.0  # Costo de envío estándar
#     
#     def __init__(
#         self,
#         user_repo: UserRepository,
#         product_repo: ProductRepository,
#         order_repo: OrderRepository
#     ):
#         self.user_repo = user_repo
#         self.product_repo = product_repo
#         self.order_repo = order_repo
#     
#     def create_order(self, data: OrderCreate) -> Order:
#         """
#         Crea un pedido completo.
#         
#         Flujo:
#         1. Validar usuario existe
#         2. Validar productos y stock
#         3. Crear OrderItems
#         4. Calcular totales
#         5. Crear Order
#         6. Reducir stock
#         7. Persistir todo
#         
#         Args:
#             data: OrderCreate DTO con user_id, items y dirección
#             
#         Returns:
#             Order creado con todos sus items
#             
#         Raises:
#             UserNotFoundError: Si usuario no existe
#             ProductNotFoundError: Si algún producto no existe
#             InsufficientStockError: Si no hay stock suficiente
#         """
#         # ============================================
#         # PASO 1: Validar usuario
#         # ============================================
#         user = self.user_repo.get_by_id(data.user_id)
#         if not user:
#             raise UserNotFoundError(data.user_id)
#         
#         # ============================================
#         # PASO 2 y 3: Validar productos y crear items
#         # ============================================
#         order_items: list[OrderItem] = []
#         products_to_update: list[tuple] = []  # (product, quantity)
#         subtotal = 0.0
#         
#         for item_data in data.items:
#             # Obtener producto
#             product = self.product_repo.get_by_id(item_data.product_id)
#             if not product:
#                 raise ProductNotFoundError(item_data.product_id)
#             
#             # Validar stock
#             if product.stock < item_data.quantity:
#                 raise InsufficientStockError(
#                     product_id=product.id,
#                     requested=item_data.quantity,
#                     available=product.stock
#                 )
#             
#             # Crear OrderItem con snapshot del producto
#             item = OrderItem(
#                 product_id=product.id,
#                 product_name=product.name,  # Snapshot
#                 quantity=item_data.quantity,
#                 unit_price=product.price,   # Snapshot
#                 subtotal=product.price * item_data.quantity
#             )
#             order_items.append(item)
#             subtotal += item.subtotal
#             
#             # Guardar para actualizar stock después
#             products_to_update.append((product, item_data.quantity))
#         
#         # ============================================
#         # PASO 4: Calcular totales
#         # ============================================
#         tax = round(subtotal * self.TAX_RATE, 2)
#         shipping = (
#             0.0 if subtotal >= self.FREE_SHIPPING_THRESHOLD
#             else self.SHIPPING_COST
#         )
#         total = round(subtotal + tax + shipping, 2)
#         
#         # ============================================
#         # PASO 5: Crear Order
#         # ============================================
#         order = Order(
#             user_id=data.user_id,
#             status=OrderStatus.PENDING,
#             subtotal=subtotal,
#             tax=tax,
#             shipping_cost=shipping,
#             total=total,
#             shipping_address=data.shipping_address,
#             created_at=datetime.utcnow(),
#             items=order_items  # SQLAlchemy manejará la relación
#         )
#         
#         # ============================================
#         # PASO 6: Reducir stock
#         # ============================================
#         for product, quantity in products_to_update:
#             product.stock -= quantity
#             # No commit aún - será parte de la misma transacción
#         
#         # ============================================
#         # PASO 7: Persistir todo
#         # ============================================
#         # El commit del order_repo incluirá todo
#         saved_order = self.order_repo.add(order)
#         
#         return saved_order
#     
#     def get_order(self, order_id: int) -> Order:
#         """Obtiene una orden por ID."""
#         order = self.order_repo.get_by_id_with_items(order_id)
#         if not order:
#             raise ValueError(f"Order {order_id} not found")
#         return order
