"""
Tests de autenticación.

TODO: Completar los tests marcados con TODO
"""

import pytest
from src.auth import verify_password, get_password_hash, create_access_token, decode_token


class TestPasswordHashing:
    """Tests de hashing de contraseñas."""
    
    def test_hash_password(self):
        """Test que el hash funciona."""
        password = "secret123"
        hashed = get_password_hash(password)
        
        assert hashed != password
        assert len(hashed) > 0
    
    def test_verify_correct_password(self):
        """Test verificación de password correcta."""
        password = "secret123"
        hashed = get_password_hash(password)
        
        assert verify_password(password, hashed) is True
    
    def test_verify_wrong_password(self):
        """Test verificación de password incorrecta."""
        hashed = get_password_hash("secret123")
        
        assert verify_password("wrongpass", hashed) is False


class TestJWT:
    """Tests de JWT."""
    
    def test_create_access_token(self):
        """
        Test creación de token.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Crear token con datos
        # 2. Verificar que retorna string
        # 3. Verificar que tiene formato JWT (3 partes separadas por .)
        pass
    
    def test_decode_valid_token(self):
        """
        Test decodificación de token válido.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Crear token
        # 2. Decodificar
        # 3. Verificar datos
        pass
    
    def test_decode_invalid_token(self):
        """
        Test decodificación de token inválido.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Intentar decodificar token inválido
        # 2. Verificar que retorna None
        pass


class TestAuthEndpoints:
    """Tests de endpoints de autenticación."""
    
    def test_register_user(self, client):
        """
        Test registro de usuario.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. POST /auth/register con datos válidos
        # 2. Verificar status 201
        # 3. Verificar datos de respuesta
        pass
    
    def test_register_duplicate_username(self, client, test_user):
        """
        Test registro con username duplicado.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. POST /auth/register con username existente
        # 2. Verificar status 400
        pass
    
    def test_login_success(self, client, test_user):
        """
        Test login exitoso.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. POST /auth/login con credenciales correctas
        # 2. Verificar status 200
        # 3. Verificar que retorna token
        pass
    
    def test_login_wrong_password(self, client, test_user):
        """
        Test login con password incorrecto.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        pass
    
    def test_get_me(self, client, auth_headers, test_user):
        """
        Test obtener usuario actual.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. GET /auth/me con headers de auth
        # 2. Verificar que retorna datos del usuario
        pass
    
    def test_get_me_no_auth(self, client):
        """Test get_me sin autenticación."""
        response = client.get("/auth/me")
        assert response.status_code == 401
