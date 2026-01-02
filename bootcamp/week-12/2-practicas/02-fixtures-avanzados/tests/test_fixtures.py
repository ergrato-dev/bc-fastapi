"""
Tests para practicar fixtures básicas.

Instrucciones:
1. Descomenta cada sección de tests
2. Ejecuta con `uv run pytest -v -s` para ver output
3. Observa el orden de setup/teardown
"""

import pytest
from src.models import User, Product, Order


# ============================================
# PASO 1: Usar fixtures básicas
# ============================================
print("--- Paso 1: Fixtures básicas ---")

# Las fixtures se reciben como parámetros del test
# Descomenta las siguientes líneas:

# def test_sample_user_has_email(sample_user):
#     """Test usando fixture sample_user de conftest.py."""
#     assert sample_user.email == "test@example.com"
#     assert sample_user.is_active is True


# def test_sample_product_has_price(sample_product):
#     """Test usando fixture sample_product."""
#     assert sample_product.price == 29.99
#     assert sample_product.stock == 100


# ============================================
# PASO 2: Fixtures con yield (setup/teardown)
# ============================================
print("--- Paso 2: Fixtures con yield ---")

# Observa los prints de setup/teardown al ejecutar
# Descomenta las siguientes líneas:

# def test_database_is_connected(database):
#     """Verifica que database está conectada."""
#     assert database.is_connected() is True


# def test_database_can_add_user(database):
#     """Verifica que podemos añadir usuarios."""
#     user = User.create("new@test.com", "New User")
#     database.add_user(user)
    
#     retrieved = database.get_user(user.id)
#     assert retrieved is not None
#     assert retrieved.email == "new@test.com"


# def test_database_is_empty_each_test(database):
#     """Cada test recibe una database limpia."""
#     # Gracias al teardown, la database se limpia entre tests
#     assert len(database.users) == 0


# ============================================
# PASO 3: Fixtures que dependen de otras
# ============================================
print("--- Paso 3: Fixtures compuestas ---")

# Descomenta las siguientes líneas:

# def test_populated_database_has_users(populated_database):
#     """La database poblada tiene usuarios."""
#     assert len(populated_database.users) == 2


# def test_populated_database_has_products(populated_database):
#     """La database poblada tiene productos."""
#     assert len(populated_database.products) == 2
#     # Verificar que un producto existe
#     laptop = populated_database.get_product(1)
#     assert laptop.name == "Laptop"


# ============================================
# PASO 4: Factory fixtures
# ============================================
print("--- Paso 4: Factory fixtures ---")

# Las factories permiten crear múltiples instancias personalizadas
# Descomenta las siguientes líneas:

# def test_make_user_factory(make_user):
#     """Crear usuarios con factory."""
#     alice = make_user("alice@test.com", "Alice")
#     bob = make_user("bob@test.com", "Bob")
#     inactive = make_user("inactive@test.com", "Inactive", is_active=False)
    
#     assert alice.email == "alice@test.com"
#     assert bob.email == "bob@test.com"
#     assert inactive.is_active is False


# def test_make_product_factory(make_product):
#     """Crear productos con factory."""
#     laptop = make_product("Laptop", 999.99, stock=10)
#     mouse = make_product("Mouse", 29.99, stock=50)
    
#     assert laptop.price == 999.99
#     assert mouse.stock == 50


# def test_factory_with_database(database, make_user):
#     """Combinar factory con database."""
#     user = make_user("combo@test.com", "Combo User")
#     database.add_user(user)
    
#     retrieved = database.get_user(user.id)
#     assert retrieved.name == "Combo User"


# ============================================
# PASO 5: Fixtures parametrizadas
# ============================================
print("--- Paso 5: Fixtures parametrizadas ---")

# Este test se ejecuta 3 veces (una por cada rol)
# Descomenta las siguientes líneas:

# def test_user_role_is_valid(user_role):
#     """Test ejecutado para cada rol."""
#     assert user_role in ["admin", "user", "guest"]


# def test_user_data_parametrized(user_data):
#     """Test ejecutado para cada conjunto de datos."""
#     assert "email" in user_data
#     assert "name" in user_data
#     assert "@" in user_data["email"]


# ============================================
# PASO 6: Múltiples fixtures
# ============================================
print("--- Paso 6: Múltiples fixtures ---")

# Un test puede usar múltiples fixtures
# Descomenta las siguientes líneas:

# def test_multiple_fixtures(database, sample_user, sample_product):
#     """Test usando múltiples fixtures."""
#     database.add_user(sample_user)
#     database.add_product(sample_product)
    
#     assert database.get_user(sample_user.id) is not None
#     assert database.get_product(sample_product.id) is not None


# def test_order_with_fixtures(database, make_user, make_product):
#     """Crear orden con fixtures."""
#     user = make_user("buyer@test.com", "Buyer")
#     product = make_product("Item", 50.00, stock=10)
    
#     database.add_user(user)
#     database.add_product(product)
    
#     order = Order.create(user_id=user.id)
#     order.add_item(product, quantity=2)
    
#     assert order.total == 100.00
#     assert len(order.items) == 1
