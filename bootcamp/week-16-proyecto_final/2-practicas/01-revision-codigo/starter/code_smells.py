"""
============================================
PRÁCTICA 01: Revisión de Código
Archivo: code_smells.py
============================================

Este archivo muestra code smells comunes y cómo refactorizarlos.
Estudia cada ejemplo y aplica las mejoras a tu proyecto.
"""

# ============================================
# CODE SMELL 1: Función demasiado larga
# ============================================
print("--- Code Smell 1: Función demasiado larga ---")

# ❌ MAL - Función que hace demasiadas cosas
"""
async def create_order(order_data: dict, user_id: int, db: Session):
    # Validar usuario
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    if not user.is_active:
        raise HTTPException(400, "User is not active")
    
    # Validar productos
    for item in order_data["items"]:
        product = db.query(Product).filter(Product.id == item["product_id"]).first()
        if not product:
            raise HTTPException(404, f"Product {item['product_id']} not found")
        if product.stock < item["quantity"]:
            raise HTTPException(400, f"Not enough stock for {product.name}")
    
    # Calcular totales
    total = 0
    for item in order_data["items"]:
        product = db.query(Product).filter(Product.id == item["product_id"]).first()
        total += product.price * item["quantity"]
    
    # Aplicar descuento
    if user.is_premium:
        total *= 0.9
    
    # Crear orden
    order = Order(user_id=user_id, total=total)
    db.add(order)
    
    # Crear items
    for item in order_data["items"]:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item["product_id"],
            quantity=item["quantity"]
        )
        db.add(order_item)
    
    # Actualizar stock
    for item in order_data["items"]:
        product = db.query(Product).filter(Product.id == item["product_id"]).first()
        product.stock -= item["quantity"]
    
    # Enviar email
    send_confirmation_email(user.email, order)
    
    db.commit()
    return order
"""

# ✅ BIEN - Separar en funciones con responsabilidad única
"""
class OrderService:
    def __init__(self, db: Session, user_repo: UserRepository, product_repo: ProductRepository):
        self.db = db
        self.user_repo = user_repo
        self.product_repo = product_repo
    
    async def create_order(self, order_data: OrderCreate, user_id: int) -> Order:
        user = await self._validate_user(user_id)
        await self._validate_stock(order_data.items)
        
        total = self._calculate_total(order_data.items, user.is_premium)
        order = await self._save_order(user_id, order_data.items, total)
        
        await self._update_stock(order_data.items)
        await self._send_confirmation(user.email, order)
        
        return order
    
    async def _validate_user(self, user_id: int) -> User:
        user = await self.user_repo.get_by_id(user_id)
        if not user or not user.is_active:
            raise UserNotFoundError(user_id)
        return user
    
    async def _validate_stock(self, items: list[OrderItem]) -> None:
        for item in items:
            product = await self.product_repo.get_by_id(item.product_id)
            if product.stock < item.quantity:
                raise InsufficientStockError(product.name)
    
    def _calculate_total(self, items: list, is_premium: bool) -> float:
        total = sum(item.price * item.quantity for item in items)
        return total * 0.9 if is_premium else total
"""

print("✅ Refactorizar funciones largas en métodos pequeños con una responsabilidad")


# ============================================
# CODE SMELL 2: Magic Numbers
# ============================================
print("\n--- Code Smell 2: Magic Numbers ---")

# ❌ MAL - Números mágicos sin contexto
"""
if user.login_attempts > 5:
    lock_account(user)

if order.total > 100:
    apply_discount(order, 0.1)

token = create_token(user, 3600)
"""

# ✅ BIEN - Constantes con nombres descriptivos
"""
# config.py
MAX_LOGIN_ATTEMPTS = 5
FREE_SHIPPING_THRESHOLD = 100
BULK_DISCOUNT_PERCENTAGE = 0.1
ACCESS_TOKEN_EXPIRE_SECONDS = 3600

# usage
if user.login_attempts > MAX_LOGIN_ATTEMPTS:
    lock_account(user)

if order.total > FREE_SHIPPING_THRESHOLD:
    apply_discount(order, BULK_DISCOUNT_PERCENTAGE)

token = create_token(user, ACCESS_TOKEN_EXPIRE_SECONDS)
"""

print("✅ Reemplazar números mágicos con constantes descriptivas")


# ============================================
# CODE SMELL 3: Código Duplicado
# ============================================
print("\n--- Code Smell 3: Código Duplicado ---")

# ❌ MAL - Lógica duplicada en múltiples endpoints
"""
@router.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}")
async def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # update logic...

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # delete logic...
"""

# ✅ BIEN - Extraer a dependency o service
"""
# dependencies/user.py
async def get_user_or_404(
    user_id: int,
    db: AsyncSession = Depends(get_db)
) -> User:
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# routers/users.py
@router.get("/users/{user_id}")
async def get_user(user: User = Depends(get_user_or_404)):
    return user

@router.put("/users/{user_id}")
async def update_user(
    data: UserUpdate,
    user: User = Depends(get_user_or_404),
    db: AsyncSession = Depends(get_db)
):
    # update logic using 'user'...

@router.delete("/users/{user_id}")
async def delete_user(
    user: User = Depends(get_user_or_404),
    db: AsyncSession = Depends(get_db)
):
    # delete logic using 'user'...
"""

print("✅ Extraer código duplicado a funciones o dependencies reutilizables")


# ============================================
# CODE SMELL 4: Anidamiento Excesivo
# ============================================
print("\n--- Code Smell 4: Anidamiento Excesivo ---")

# ❌ MAL - Múltiples niveles de if anidados
"""
def process_order(order):
    if order:
        if order.is_valid:
            if order.user:
                if order.user.is_active:
                    if order.total > 0:
                        # Finally do something
                        process_payment(order)
                    else:
                        raise ValueError("Invalid total")
                else:
                    raise ValueError("User not active")
            else:
                raise ValueError("No user")
        else:
            raise ValueError("Invalid order")
    else:
        raise ValueError("No order")
"""

# ✅ BIEN - Early returns (guard clauses)
"""
def process_order(order: Order) -> None:
    if not order:
        raise ValueError("No order")
    
    if not order.is_valid:
        raise ValueError("Invalid order")
    
    if not order.user:
        raise ValueError("No user")
    
    if not order.user.is_active:
        raise ValueError("User not active")
    
    if order.total <= 0:
        raise ValueError("Invalid total")
    
    # Happy path - sin anidamiento
    process_payment(order)
"""

print("✅ Usar early returns para evitar anidamiento profundo")


# ============================================
# CODE SMELL 5: God Class / God Function
# ============================================
print("\n--- Code Smell 5: God Class ---")

# ❌ MAL - Clase que hace todo
"""
class OrderManager:
    def create_order(self): ...
    def update_order(self): ...
    def delete_order(self): ...
    def send_order_email(self): ...
    def generate_invoice(self): ...
    def process_payment(self): ...
    def update_inventory(self): ...
    def notify_warehouse(self): ...
    def calculate_shipping(self): ...
    def apply_coupon(self): ...
    def validate_address(self): ...
    # ... 50 métodos más
"""

# ✅ BIEN - Separar por responsabilidades
"""
class OrderService:
    def create(self, data: OrderCreate) -> Order: ...
    def update(self, order_id: int, data: OrderUpdate) -> Order: ...
    def delete(self, order_id: int) -> None: ...

class OrderNotificationService:
    def send_confirmation(self, order: Order) -> None: ...
    def send_shipped_notification(self, order: Order) -> None: ...

class PaymentService:
    def process(self, order: Order) -> Payment: ...
    def refund(self, payment: Payment) -> None: ...

class InventoryService:
    def reserve(self, items: list[OrderItem]) -> None: ...
    def release(self, items: list[OrderItem]) -> None: ...

class ShippingService:
    def calculate_cost(self, order: Order) -> float: ...
    def validate_address(self, address: Address) -> bool: ...
"""

print("✅ Dividir clases grandes en clases más pequeñas y enfocadas")


# ============================================
# CODE SMELL 6: Comentarios Obvios
# ============================================
print("\n--- Code Smell 6: Comentarios Innecesarios ---")

# ❌ MAL - Comentarios que repiten el código
"""
# Increment counter by 1
counter += 1

# Get user by id
user = get_user_by_id(user_id)

# Check if user is None
if user is None:
    # Raise not found exception
    raise HTTPException(404)

# Loop through items
for item in items:
    # Process each item
    process(item)
"""

# ✅ BIEN - Código autoexplicativo, comentarios solo para el "por qué"
"""
counter += 1

user = get_user_by_id(user_id)
if not user:
    raise HTTPException(404)

for item in items:
    process(item)

# Usamos cache aquí porque esta query es muy costosa
# y los datos no cambian frecuentemente (cada 24h max)
cached_data = cache.get_or_set("expensive_query", fetch_data, ttl=86400)
"""

print("✅ El código debe ser autoexplicativo; comentar solo el 'por qué'")


# ============================================
# CODE SMELL 7: Boolean Parameters
# ============================================
print("\n--- Code Smell 7: Boolean Parameters ---")

# ❌ MAL - Booleanos que obscurecen el significado
"""
send_email(user, True, False, True)

create_user(data, True)
"""

# ✅ BIEN - Usar enums, kwargs con nombres, o métodos separados
"""
# Opción 1: Keyword arguments
send_email(
    user,
    include_attachments=True,
    use_template=False,
    track_opens=True
)

# Opción 2: Métodos separados
def create_user(data: UserCreate) -> User: ...
def create_admin_user(data: UserCreate) -> User: ...

# Opción 3: Enums
class EmailType(Enum):
    PLAIN = "plain"
    HTML = "html"
    TEMPLATE = "template"

send_email(user, email_type=EmailType.TEMPLATE)
"""

print("✅ Evitar parámetros booleanos; usar kwargs o enums")


# ============================================
# RESUMEN
# ============================================
print("\n" + "="*50)
print("📊 RESUMEN DE CODE SMELLS")
print("="*50)
print("""
1. Función demasiado larga → Dividir en funciones pequeñas
2. Magic numbers → Usar constantes con nombres
3. Código duplicado → Extraer a funciones/dependencies
4. Anidamiento excesivo → Usar early returns
5. God class → Separar por responsabilidades (SRP)
6. Comentarios obvios → Código autoexplicativo
7. Boolean parameters → Usar kwargs o enums

Aplica estos principios a tu proyecto final.
""")
