"""
Tests para entender scopes de fixtures.

Ejecuta con:
    uv run pytest tests/test_scopes.py -v -s --setup-show

Esto mostrará cuándo se ejecuta cada fixture.
"""

import pytest


# ============================================
# PASO 1: Scope function (default)
# ============================================
print("--- Paso 1: Scope function ---")

# Cada test recibe una instancia nueva
# Descomenta las siguientes líneas:

# def test_function_scope_first(sample_user):
#     """Primer test con sample_user."""
#     # sample_user tiene id=1 (counter reseteado por autouse)
#     assert sample_user.id == 1


# def test_function_scope_second(sample_user):
#     """Segundo test con sample_user."""
#     # También id=1 porque cada test tiene su propia instancia
#     assert sample_user.id == 1


# ============================================
# PASO 2: Scope module
# ============================================
print("--- Paso 2: Scope module ---")

# expensive_resource se crea UNA vez para todo el archivo
# Descomenta las siguientes líneas:

# def test_expensive_resource_first(expensive_resource):
#     """Primer uso de expensive_resource."""
#     expensive_resource["cache"]["key1"] = "value1"
#     assert "config" in expensive_resource


# def test_expensive_resource_second(expensive_resource):
#     """Segundo uso - misma instancia."""
#     # El cache modificado en el test anterior persiste
#     assert "key1" in expensive_resource["cache"]


# def test_expensive_resource_third(expensive_resource):
#     """Tercer uso - todavía la misma instancia."""
#     assert expensive_resource["cache"]["key1"] == "value1"


# ============================================
# PASO 3: Scope session
# ============================================
print("--- Paso 3: Scope session ---")

# global_config se crea UNA vez para toda la sesión
# Descomenta las siguientes líneas:

# def test_global_config_available(global_config):
#     """Config global disponible."""
#     assert global_config["app_name"] == "TestApp"
#     assert global_config["version"] == "1.0.0"


# ============================================
# PASO 4: Scope class
# ============================================
print("--- Paso 4: Scope class ---")

# Fixture con scope de clase
# Descomenta las siguientes líneas:

# @pytest.fixture(scope="class")
# def class_resource():
#     """Recurso compartido dentro de una clase."""
#     print("\n  🏛️ CLASS RESOURCE: Creating...")
#     resource = {"counter": 0}
#     yield resource
#     print("\n  🏛️ CLASS RESOURCE: Releasing...")


# class TestClassScope:
#     """Todos los tests en esta clase comparten class_resource."""
    
#     def test_increment_first(self, class_resource):
#         """Primer incremento."""
#         class_resource["counter"] += 1
#         assert class_resource["counter"] == 1
    
#     def test_increment_second(self, class_resource):
#         """Segundo incremento - mismo recurso."""
#         class_resource["counter"] += 1
#         assert class_resource["counter"] == 2
    
#     def test_check_final_value(self, class_resource):
#         """Verificar valor final."""
#         assert class_resource["counter"] == 2


# class TestAnotherClass:
#     """Esta clase tiene su propia instancia de class_resource."""
    
#     def test_fresh_resource(self, class_resource):
#         """Nueva instancia para esta clase."""
#         # Counter empieza en 0 para esta clase
#         assert class_resource["counter"] == 0


# ============================================
# PASO 5: Combinando scopes
# ============================================
print("--- Paso 5: Combinando scopes ---")

# Descomenta las siguientes líneas:

# def test_combining_scopes(global_config, expensive_resource, database):
#     """Test usando fixtures de diferentes scopes."""
#     # global_config: session scope (se crea una vez)
#     # expensive_resource: module scope (una vez por archivo)
#     # database: function scope (una vez por test)
    
#     assert global_config["debug"] is True
#     assert expensive_resource["config"] == "loaded"
#     assert database.is_connected() is True


# ============================================
# PASO 6: Autouse en acción
# ============================================
print("--- Paso 6: Autouse ---")

# La fixture reset_counters tiene autouse=True
# No necesitamos declararla, se ejecuta automáticamente
# Descomenta las siguientes líneas:

# def test_counters_are_reset():
#     """Los counters se resetean por autouse."""
#     from src.models import User, Product
    
#     # Gracias a autouse, los counters empiezan en 0
#     user = User.create("test@test.com", "Test")
#     assert user.id == 1  # Siempre 1, no acumulativo


# def test_counters_still_reset():
#     """Verificar que sigue reseteado."""
#     from src.models import Product
    
#     product = Product.create("Item", 10.0)
#     assert product.id == 1  # También 1
