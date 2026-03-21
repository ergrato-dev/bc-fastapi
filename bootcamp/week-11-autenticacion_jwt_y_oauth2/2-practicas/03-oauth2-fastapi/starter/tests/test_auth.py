# test_auth.py
"""Tests para autenticación OAuth2."""

import pytest
from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


class TestTokenEndpoint:
    """Tests para el endpoint /auth/token."""
    
    def test_login_success(self):
        """Login exitoso debe retornar access_token."""
        response = client.post(
            "/auth/token",
            data={
                "username": "user@example.com",
                "password": "password123"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    
    def test_login_returns_refresh_token(self):
        """Login debe incluir refresh_token."""
        response = client.post(
            "/auth/token",
            data={
                "username": "user@example.com",
                "password": "password123"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "refresh_token" in data
        assert data["refresh_token"] is not None
    
    def test_login_wrong_password(self):
        """Password incorrecto debe retornar 401."""
        response = client.post(
            "/auth/token",
            data={
                "username": "user@example.com",
                "password": "wrong_password"
            }
        )
        
        assert response.status_code == 401
        assert "Incorrect" in response.json()["detail"]
    
    def test_login_unknown_user(self):
        """Usuario desconocido debe retornar 401."""
        response = client.post(
            "/auth/token",
            data={
                "username": "unknown@example.com",
                "password": "password123"
            }
        )
        
        assert response.status_code == 401
    
    def test_login_missing_password(self):
        """Sin password debe retornar 422."""
        response = client.post(
            "/auth/token",
            data={
                "username": "user@example.com"
            }
        )
        
        assert response.status_code == 422
    
    def test_login_admin_user(self):
        """Admin debe poder hacer login."""
        response = client.post(
            "/auth/token",
            data={
                "username": "admin@example.com",
                "password": "admin123"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
    
    def test_access_token_is_valid_jwt(self):
        """El access_token debe ser un JWT válido."""
        response = client.post(
            "/auth/token",
            data={
                "username": "user@example.com",
                "password": "password123"
            }
        )
        
        token = response.json()["access_token"]
        # JWT tiene 3 partes separadas por puntos
        assert token.count(".") == 2


class TestPublicEndpoints:
    """Tests para endpoints públicos."""
    
    def test_root_endpoint(self):
        """El endpoint raíz debe ser accesible sin auth."""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
