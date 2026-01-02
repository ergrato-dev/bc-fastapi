# test_protected.py
"""Tests para endpoints protegidos."""

import pytest
from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def get_auth_headers(email: str, password: str) -> dict:
    """Helper para obtener headers de autorización."""
    response = client.post(
        "/auth/token",
        data={"username": email, "password": password}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


class TestProtectedEndpoints:
    """Tests para endpoints que requieren autenticación."""
    
    def test_get_me_authenticated(self):
        """Usuario autenticado puede acceder a /users/me."""
        headers = get_auth_headers("user@example.com", "password123")
        response = client.get("/users/me", headers=headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "user@example.com"
        assert data["role"] == "user"
    
    def test_get_me_without_token(self):
        """Sin token debe retornar 401."""
        response = client.get("/users/me")
        assert response.status_code == 401
    
    def test_get_me_invalid_token(self):
        """Token inválido debe retornar 401."""
        headers = {"Authorization": "Bearer invalid_token_here"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == 401
    
    def test_get_me_malformed_header(self):
        """Header malformado debe retornar 401."""
        headers = {"Authorization": "NotBearer sometoken"}
        response = client.get("/users/me", headers=headers)
        assert response.status_code == 401


class TestRoleBasedAccess:
    """Tests para autorización basada en roles."""
    
    def test_admin_can_access_dashboard(self):
        """Admin puede acceder a /admin/dashboard."""
        headers = get_auth_headers("admin@example.com", "admin123")
        response = client.get("/admin/dashboard", headers=headers)
        
        assert response.status_code == 200
        assert "admin_features" in response.json()
    
    def test_user_cannot_access_admin(self):
        """Usuario regular NO puede acceder a /admin/dashboard."""
        headers = get_auth_headers("user@example.com", "password123")
        response = client.get("/admin/dashboard", headers=headers)
        
        assert response.status_code == 403
        assert "required" in response.json()["detail"].lower()
    
    def test_unauthenticated_cannot_access_admin(self):
        """Sin autenticación no se puede acceder a admin."""
        response = client.get("/admin/dashboard")
        assert response.status_code == 401


class TestInactiveUser:
    """Tests para usuarios inactivos."""
    
    def test_inactive_user_cannot_access_me(self):
        """Usuario inactivo no puede acceder a /users/me."""
        headers = get_auth_headers("disabled@example.com", "disabled123")
        response = client.get("/users/me", headers=headers)
        
        # Debe retornar 403 (Forbidden) porque el usuario está inactivo
        assert response.status_code == 403
        assert "inactive" in response.json()["detail"].lower()


class TestTokenClaims:
    """Tests para verificar claims del token."""
    
    def test_user_data_matches_token(self):
        """Los datos del usuario deben coincidir con el token."""
        # Login como admin
        headers = get_auth_headers("admin@example.com", "admin123")
        
        # Obtener datos del usuario
        response = client.get("/users/me", headers=headers)
        data = response.json()
        
        # Verificar que los datos coinciden
        assert data["email"] == "admin@example.com"
        assert data["role"] == "admin"
        assert data["full_name"] == "Admin User"
