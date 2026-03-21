"""
Tests for /items endpoints.

Instrucciones:
1. Descomenta cada sección de tests
2. Ejecuta `uv run pytest tests/test_items.py -v`
3. Verifica que todos los tests pasen
"""

import pytest


# ============================================
# PASO 1: GET /items/ - Listar items
# ============================================
print("--- Paso 1: Tests de listado ---")

# Descomenta las siguientes líneas:

# def test_list_items_empty(client):
#     """Lista vacía cuando no hay items."""
#     response = client.get("/items/")
#     assert response.status_code == 200
#     assert response.json() == []


# def test_list_items_with_data(client, test_item):
#     """Lista con items existentes."""
#     response = client.get("/items/")
#     assert response.status_code == 200
#     items = response.json()
#     assert len(items) == 1
#     assert items[0]["name"] == "Test Item"


# def test_list_items_pagination(client, db_session, test_user):
#     """Test de paginación."""
#     from src.models import Item
    
#     # Crear múltiples items
#     for i in range(5):
#         item = Item(name=f"Item {i}", price=10.0, owner_id=test_user.id)
#         db_session.add(item)
#     db_session.commit()
    
#     # Sin límite
#     response = client.get("/items/")
#     assert len(response.json()) == 5
    
#     # Con límite
#     response = client.get("/items/", params={"limit": 2})
#     assert len(response.json()) == 2
    
#     # Con skip
#     response = client.get("/items/", params={"skip": 3})
#     assert len(response.json()) == 2


# ============================================
# PASO 2: GET /items/{id} - Obtener un item
# ============================================
print("--- Paso 2: Tests de obtener item ---")

# Descomenta las siguientes líneas:

# def test_get_item_success(client, test_item):
#     """Obtener item existente."""
#     response = client.get(f"/items/{test_item.id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == test_item.id
#     assert data["name"] == "Test Item"
#     assert data["price"] == 29.99


# def test_get_item_not_found(client):
#     """Item no existente retorna 404."""
#     response = client.get("/items/99999")
#     assert response.status_code == 404
#     assert "not found" in response.json()["detail"].lower()


# ============================================
# PASO 3: POST /items/ - Crear item
# ============================================
print("--- Paso 3: Tests de crear item ---")

# Descomenta las siguientes líneas:

# def test_create_item_success(client, auth_headers):
#     """Crear item con autenticación."""
#     item_data = {
#         "name": "New Item",
#         "description": "A new item",
#         "price": 49.99
#     }
#     response = client.post("/items/", json=item_data, headers=auth_headers)
#     assert response.status_code == 201
#     data = response.json()
#     assert data["name"] == "New Item"
#     assert data["price"] == 49.99
#     assert "id" in data


# def test_create_item_without_auth(client):
#     """Crear item sin autenticación falla."""
#     item_data = {"name": "Test", "price": 10.0}
#     response = client.post("/items/", json=item_data)
#     assert response.status_code == 401


# def test_create_item_invalid_data(client, auth_headers):
#     """Crear item con datos inválidos."""
#     # Precio negativo
#     response = client.post(
#         "/items/",
#         json={"name": "Test", "price": -10.0},
#         headers=auth_headers
#     )
#     assert response.status_code == 422
    
#     # Nombre vacío
#     response = client.post(
#         "/items/",
#         json={"name": "", "price": 10.0},
#         headers=auth_headers
#     )
#     assert response.status_code == 422


# ============================================
# PASO 4: PUT /items/{id} - Actualizar item
# ============================================
print("--- Paso 4: Tests de actualizar item ---")

# Descomenta las siguientes líneas:

# def test_update_item_success(client, test_item, auth_headers):
#     """Actualizar item propio."""
#     update_data = {"name": "Updated Name", "price": 99.99}
#     response = client.put(
#         f"/items/{test_item.id}",
#         json=update_data,
#         headers=auth_headers
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Updated Name"
#     assert data["price"] == 99.99


# def test_update_item_partial(client, test_item, auth_headers):
#     """Actualización parcial (solo algunos campos)."""
#     response = client.put(
#         f"/items/{test_item.id}",
#         json={"price": 199.99},
#         headers=auth_headers
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data["price"] == 199.99
#     assert data["name"] == "Test Item"  # No cambió


# def test_update_item_not_owner(client, test_item, other_user_headers):
#     """No puede actualizar item de otro usuario."""
#     response = client.put(
#         f"/items/{test_item.id}",
#         json={"name": "Hacked"},
#         headers=other_user_headers
#     )
#     assert response.status_code == 403


# def test_update_item_not_found(client, auth_headers):
#     """Actualizar item inexistente."""
#     response = client.put(
#         "/items/99999",
#         json={"name": "Test"},
#         headers=auth_headers
#     )
#     assert response.status_code == 404


# ============================================
# PASO 5: DELETE /items/{id} - Eliminar item
# ============================================
print("--- Paso 5: Tests de eliminar item ---")

# Descomenta las siguientes líneas:

# def test_delete_item_success(client, test_item, auth_headers):
#     """Eliminar item propio."""
#     response = client.delete(f"/items/{test_item.id}", headers=auth_headers)
#     assert response.status_code == 204
    
#     # Verificar que ya no existe
#     response = client.get(f"/items/{test_item.id}")
#     assert response.status_code == 404


# def test_delete_item_not_owner(client, test_item, other_user_headers):
#     """No puede eliminar item de otro usuario."""
#     response = client.delete(
#         f"/items/{test_item.id}",
#         headers=other_user_headers
#     )
#     assert response.status_code == 403


# def test_delete_item_not_found(client, auth_headers):
#     """Eliminar item inexistente."""
#     response = client.delete("/items/99999", headers=auth_headers)
#     assert response.status_code == 404


# def test_delete_item_without_auth(client, test_item):
#     """Eliminar sin autenticación."""
#     response = client.delete(f"/items/{test_item.id}")
#     assert response.status_code == 401
