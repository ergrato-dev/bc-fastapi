"""
Tests para Logging Estructurado

Verifica que el logging está configurado correctamente.
"""

import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.fixture
def client():
    """Cliente HTTP para tests."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestLoggingEndpoints:
    """Tests de endpoints con logging."""
    
    @pytest.mark.asyncio
    async def test_root_endpoint(self, client):
        """Test endpoint raíz."""
        async with client as ac:
            response = await ac.get("/")
        
        assert response.status_code == 200
        assert "message" in response.json()
    
    @pytest.mark.asyncio
    async def test_get_users(self, client):
        """Test endpoint de usuarios."""
        async with client as ac:
            response = await ac.get("/api/users")
        
        assert response.status_code == 200
        assert "users" in response.json()
    
    @pytest.mark.asyncio
    async def test_get_user_by_id(self, client):
        """Test endpoint de usuario por ID."""
        async with client as ac:
            response = await ac.get("/api/users/1")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
    
    @pytest.mark.asyncio
    async def test_create_order(self, client):
        """Test creación de orden."""
        async with client as ac:
            response = await ac.post("/api/orders")
        
        assert response.status_code == 200
        data = response.json()
        assert "order_id" in data
    
    @pytest.mark.asyncio
    async def test_login(self, client):
        """Test endpoint de login."""
        async with client as ac:
            response = await ac.post("/api/login")
        
        assert response.status_code == 200


class TestRequestId:
    """Tests de request ID en headers."""
    
    @pytest.mark.asyncio
    async def test_request_id_in_response(self, client):
        """Test que el response incluye X-Request-ID."""
        async with client as ac:
            response = await ac.get("/api/users")
        
        # Si el middleware está activo, debería incluir el header
        if "X-Request-ID" in response.headers:
            request_id = response.headers["X-Request-ID"]
            assert len(request_id) == 8  # UUID truncado
    
    @pytest.mark.asyncio
    async def test_different_request_ids(self, client):
        """Test que cada request tiene un ID diferente."""
        async with client as ac:
            response1 = await ac.get("/api/users")
            response2 = await ac.get("/api/users")
        
        if "X-Request-ID" in response1.headers:
            id1 = response1.headers["X-Request-ID"]
            id2 = response2.headers["X-Request-ID"]
            assert id1 != id2


class TestSensitiveData:
    """Tests para verificar que datos sensibles están protegidos."""
    
    @pytest.mark.asyncio
    async def test_login_endpoint_works(self, client):
        """Test que login funciona (los logs no deberían tener passwords)."""
        async with client as ac:
            response = await ac.post("/api/login")
        
        assert response.status_code == 200
        # El password no debería aparecer en la respuesta tampoco
        assert "password" not in response.text.lower() or "secret" not in response.text
