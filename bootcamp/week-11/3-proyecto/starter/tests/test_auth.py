# test_auth.py
"""Tests para autenticación."""

import pytest


class TestRegister:
    """Tests para registro de usuarios."""
    
    def test_register_success(self, client):
        """Registro exitoso crea usuario."""
        response = client.post(
            "/auth/register",
            json={
                "email": "newuser@example.com",
                "password": "securepassword123",
                "full_name": "New User"
            }
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == "newuser@example.com"
        assert data["full_name"] == "New User"
        assert data["role"] == "user"
        assert "password" not in data
        assert "hashed_password" not in data
    
    def test_register_duplicate_email(self, client, test_user):
        """No se puede registrar con email existente."""
        response = client.post(
            "/auth/register",
            json={
                "email": test_user["email"],
                "password": "anotherpassword",
                "full_name": "Another User"
            }
        )
        
        assert response.status_code == 400
        assert "already registered" in response.json()["detail"].lower()
    
    def test_register_invalid_email(self, client):
        """Email inválido retorna error de validación."""
        response = client.post(
            "/auth/register",
            json={
                "email": "not-an-email",
                "password": "securepassword123",
                "full_name": "Test User"
            }
        )
        
        assert response.status_code == 422
    
    def test_register_short_password(self, client):
        """Password muy corto retorna error."""
        response = client.post(
            "/auth/register",
            json={
                "email": "user@example.com",
                "password": "short",
                "full_name": "Test User"
            }
        )
        
        assert response.status_code == 422


class TestLogin:
    """Tests para login."""
    
    def test_login_success(self, client, test_user):
        """Login exitoso retorna tokens."""
        response = client.post(
            "/auth/token",
            data={
                "username": test_user["email"],
                "password": test_user["password"]
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"
    
    def test_login_wrong_password(self, client, test_user):
        """Password incorrecto retorna 401."""
        response = client.post(
            "/auth/token",
            data={
                "username": test_user["email"],
                "password": "wrongpassword"
            }
        )
        
        assert response.status_code == 401
    
    def test_login_nonexistent_user(self, client):
        """Usuario inexistente retorna 401."""
        response = client.post(
            "/auth/token",
            data={
                "username": "nonexistent@example.com",
                "password": "somepassword"
            }
        )
        
        assert response.status_code == 401
    
    def test_access_token_is_valid_jwt(self, client, test_user):
        """Access token tiene formato JWT."""
        response = client.post(
            "/auth/token",
            data={
                "username": test_user["email"],
                "password": test_user["password"]
            }
        )
        
        token = response.json()["access_token"]
        # JWT tiene 3 partes separadas por puntos
        assert token.count(".") == 2


class TestRefreshToken:
    """Tests para refresh token."""
    
    def test_refresh_success(self, client, test_user):
        """Refresh token genera nuevos tokens."""
        # Primero hacer login
        login_response = client.post(
            "/auth/token",
            data={
                "username": test_user["email"],
                "password": test_user["password"]
            }
        )
        refresh_token = login_response.json()["refresh_token"]
        
        # Usar refresh token
        response = client.post(
            "/auth/refresh",
            json={"refresh_token": refresh_token}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
    
    def test_refresh_invalid_token(self, client):
        """Refresh token inválido retorna 401."""
        response = client.post(
            "/auth/refresh",
            json={"refresh_token": "invalid.token.here"}
        )
        
        assert response.status_code == 401
    
    def test_refresh_with_access_token(self, client, test_user):
        """No se puede usar access token para refresh."""
        login_response = client.post(
            "/auth/token",
            data={
                "username": test_user["email"],
                "password": test_user["password"]
            }
        )
        access_token = login_response.json()["access_token"]
        
        response = client.post(
            "/auth/refresh",
            json={"refresh_token": access_token}
        )
        
        assert response.status_code == 401
