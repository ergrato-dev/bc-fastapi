"""
Tests for /auth endpoints.

Instrucciones:
1. Descomenta cada sección de tests
2. Ejecuta `uv run pytest tests/test_auth.py -v`
"""

import pytest


# ============================================
# PASO 1: POST /auth/register - Registro
# ============================================
print("--- Paso 1: Tests de registro ---")

# Descomenta las siguientes líneas:

# def test_register_success(client):
#     """Registro exitoso de usuario."""
#     user_data = {
#         "email": "newuser@example.com",
#         "password": "securepassword123",
#         "full_name": "New User"
#     }
#     response = client.post("/auth/register", json=user_data)
#     assert response.status_code == 201
#     data = response.json()
#     assert data["email"] == "newuser@example.com"
#     assert data["full_name"] == "New User"
#     assert "id" in data
#     assert "password" not in data  # No exponer password
#     assert "hashed_password" not in data


# def test_register_duplicate_email(client, test_user):
#     """No puede registrar email duplicado."""
#     user_data = {
#         "email": test_user.email,  # Email ya existe
#         "password": "anotherpassword",
#     }
#     response = client.post("/auth/register", json=user_data)
#     assert response.status_code == 400
#     assert "already registered" in response.json()["detail"].lower()


# def test_register_invalid_email(client):
#     """Email inválido falla validación."""
#     user_data = {
#         "email": "not-an-email",
#         "password": "password123",
#     }
#     response = client.post("/auth/register", json=user_data)
#     assert response.status_code == 422


# def test_register_short_password(client):
#     """Password muy corto falla validación."""
#     user_data = {
#         "email": "test@example.com",
#         "password": "short",  # Menos de 6 caracteres
#     }
#     response = client.post("/auth/register", json=user_data)
#     assert response.status_code == 422


# ============================================
# PASO 2: POST /auth/token - Login
# ============================================
print("--- Paso 2: Tests de login ---")

# Descomenta las siguientes líneas:

# def test_login_success(client, test_user):
#     """Login exitoso retorna token."""
#     response = client.post(
#         "/auth/token",
#         data={
#             "username": test_user.email,
#             "password": "testpassword123",
#         }
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert "access_token" in data
#     assert data["token_type"] == "bearer"


# def test_login_wrong_password(client, test_user):
#     """Login con password incorrecto falla."""
#     response = client.post(
#         "/auth/token",
#         data={
#             "username": test_user.email,
#             "password": "wrongpassword",
#         }
#     )
#     assert response.status_code == 401
#     assert "incorrect" in response.json()["detail"].lower()


# def test_login_nonexistent_user(client):
#     """Login con usuario inexistente falla."""
#     response = client.post(
#         "/auth/token",
#         data={
#             "username": "nonexistent@example.com",
#             "password": "anypassword",
#         }
#     )
#     assert response.status_code == 401


# def test_login_inactive_user(client, db_session):
#     """Login con usuario inactivo falla."""
#     from src.models import User
#     from src.auth import get_password_hash
    
#     inactive_user = User(
#         email="inactive@example.com",
#         hashed_password=get_password_hash("password123"),
#         is_active=False,
#     )
#     db_session.add(inactive_user)
#     db_session.commit()
    
#     response = client.post(
#         "/auth/token",
#         data={
#             "username": "inactive@example.com",
#             "password": "password123",
#         }
#     )
#     assert response.status_code == 400
#     assert "inactive" in response.json()["detail"].lower()


# ============================================
# PASO 3: GET /users/me - Usuario actual
# ============================================
print("--- Paso 3: Tests de usuario actual ---")

# Descomenta las siguientes líneas:

# def test_get_current_user(client, test_user, auth_headers):
#     """Obtener datos del usuario actual."""
#     response = client.get("/users/me", headers=auth_headers)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["email"] == test_user.email
#     assert data["full_name"] == test_user.full_name


# def test_get_current_user_without_token(client):
#     """Sin token retorna 401."""
#     response = client.get("/users/me")
#     assert response.status_code == 401


# def test_get_current_user_invalid_token(client):
#     """Token inválido retorna 401."""
#     response = client.get(
#         "/users/me",
#         headers={"Authorization": "Bearer invalid-token"}
#     )
#     assert response.status_code == 401


# def test_get_current_user_expired_token(client):
#     """Token expirado retorna 401."""
#     from src.auth import create_access_token
#     from datetime import timedelta
    
#     expired_token = create_access_token(
#         data={"sub": "test@example.com"},
#         expires_delta=timedelta(minutes=-1)  # Ya expirado
#     )
    
#     response = client.get(
#         "/users/me",
#         headers={"Authorization": f"Bearer {expired_token}"}
#     )
#     assert response.status_code == 401


# ============================================
# PASO 4: Flujo completo de autenticación
# ============================================
print("--- Paso 4: Flujo completo ---")

# Descomenta las siguientes líneas:

# def test_full_auth_flow(client):
#     """Test del flujo completo: registro → login → acceso."""
#     # 1. Registrar usuario
#     register_response = client.post(
#         "/auth/register",
#         json={
#             "email": "flowtest@example.com",
#             "password": "flowpassword123",
#             "full_name": "Flow Test User"
#         }
#     )
#     assert register_response.status_code == 201
    
#     # 2. Login
#     login_response = client.post(
#         "/auth/token",
#         data={
#             "username": "flowtest@example.com",
#             "password": "flowpassword123",
#         }
#     )
#     assert login_response.status_code == 200
#     token = login_response.json()["access_token"]
    
#     # 3. Acceder a recurso protegido
#     me_response = client.get(
#         "/users/me",
#         headers={"Authorization": f"Bearer {token}"}
#     )
#     assert me_response.status_code == 200
#     assert me_response.json()["email"] == "flowtest@example.com"
    
#     # 4. Crear item (requiere auth)
#     item_response = client.post(
#         "/items/",
#         json={"name": "My Item", "price": 25.0},
#         headers={"Authorization": f"Bearer {token}"}
#     )
#     assert item_response.status_code == 201
