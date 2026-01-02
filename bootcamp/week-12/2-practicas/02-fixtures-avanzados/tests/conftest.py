"""
Fixtures compartidas para todos los tests.

Este archivo es automáticamente detectado por pytest
y sus fixtures están disponibles en todos los tests.
"""

import pytest
from src.models import User, Product, Order, Database


# ============================================
# FIXTURES BÁSICAS
# ============================================

@pytest.fixture
def sample_user():
    """
    Fixture básica: retorna un usuario de prueba.
    
    Scope: function (default) - se crea para cada test.
    """
    print("\n  🧑 Creating sample user")
    return User.create(email="test@example.com", name="Test User")


@pytest.fixture
def sample_product():
    """
    Fixture básica: retorna un producto de prueba.
    """
    print("\n  📦 Creating sample product")
    return Product.create(name="Test Product", price=29.99, stock=100)


# ============================================
# FIXTURES CON YIELD (Setup/Teardown)
# ============================================

@pytest.fixture
def database():
    """
    Fixture con setup y teardown usando yield.
    
    - Antes del yield: SETUP (conectar)
    - yield: proporciona el valor al test
    - Después del yield: TEARDOWN (desconectar)
    """
    print("\n  ⬆️ DATABASE SETUP")
    db = Database()
    db.connect()
    
    yield db  # El test recibe este valor
    
    print("\n  ⬇️ DATABASE TEARDOWN")
    db.clear()
    db.disconnect()


@pytest.fixture
def populated_database(database):
    """
    Fixture que usa otra fixture.
    
    Recibe la database conectada y la puebla con datos.
    """
    print("\n  📊 Populating database...")
    
    # Crear usuarios
    user1 = User.create("alice@example.com", "Alice")
    user2 = User.create("bob@example.com", "Bob")
    database.add_user(user1)
    database.add_user(user2)
    
    # Crear productos
    prod1 = Product.create("Laptop", 999.99, 10)
    prod2 = Product.create("Mouse", 29.99, 50)
    database.add_product(prod1)
    database.add_product(prod2)
    
    return database


# ============================================
# FIXTURE FACTORY
# ============================================

@pytest.fixture
def make_user():
    """
    Factory fixture: permite crear múltiples usuarios personalizados.
    
    Uso:
        def test_something(make_user):
            user1 = make_user("alice@test.com", "Alice")
            user2 = make_user("bob@test.com", "Bob", is_active=False)
    """
    created_users = []
    
    def _make_user(email: str, name: str, is_active: bool = True) -> User:
        user = User.create(email, name)
        user.is_active = is_active
        created_users.append(user)
        print(f"\n  🏭 Factory created user: {email}")
        return user
    
    yield _make_user
    
    # Cleanup: mostrar cuántos usuarios se crearon
    print(f"\n  🧹 Factory cleanup: {len(created_users)} users created")


@pytest.fixture
def make_product():
    """Factory fixture para productos."""
    created_products = []
    
    def _make_product(name: str, price: float, stock: int = 0) -> Product:
        product = Product.create(name, price, stock)
        created_products.append(product)
        return product
    
    yield _make_product
    
    print(f"\n  🧹 Factory cleanup: {len(created_products)} products created")


# ============================================
# FIXTURES CON SCOPE
# ============================================

@pytest.fixture(scope="module")
def expensive_resource():
    """
    Fixture con scope='module'.
    
    Se crea UNA VEZ por módulo de tests (archivo).
    Útil para recursos costosos de crear.
    """
    print("\n  ⏳ EXPENSIVE RESOURCE: Creating (once per module)...")
    resource = {"config": "loaded", "cache": {}}
    
    yield resource
    
    print("\n  ⏳ EXPENSIVE RESOURCE: Releasing (end of module)")


@pytest.fixture(scope="session")
def global_config():
    """
    Fixture con scope='session'.
    
    Se crea UNA VEZ para toda la sesión de tests.
    """
    print("\n  🌍 GLOBAL CONFIG: Loading (once per session)...")
    
    return {
        "app_name": "TestApp",
        "version": "1.0.0",
        "debug": True,
    }


# ============================================
# FIXTURES PARAMETRIZADAS
# ============================================

@pytest.fixture(params=["admin", "user", "guest"])
def user_role(request):
    """
    Fixture parametrizada.
    
    Los tests que usen esta fixture se ejecutarán 3 veces,
    una por cada valor en params.
    """
    print(f"\n  👤 User role: {request.param}")
    return request.param


@pytest.fixture(params=[
    {"email": "alice@test.com", "name": "Alice"},
    {"email": "bob@test.com", "name": "Bob"},
    {"email": "charlie@test.com", "name": "Charlie"},
])
def user_data(request):
    """Fixture parametrizada con diccionarios."""
    return request.param


# ============================================
# AUTOUSE FIXTURE
# ============================================

@pytest.fixture(autouse=True)
def reset_counters():
    """
    Fixture con autouse=True.
    
    Se ejecuta automáticamente antes de CADA test,
    sin necesidad de declararla como parámetro.
    """
    # Setup: reset counters antes del test
    User.reset_counter()
    Product.reset_counter()
    Order.reset_counter()
    
    yield
    
    # Teardown: nada adicional necesario
