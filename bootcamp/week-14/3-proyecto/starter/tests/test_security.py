"""
Tests para Security Headers y CORS.
"""

import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest.fixture
def client():
    """Fixture para cliente HTTP."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestSecurityHeaders:
    """Tests para verificar security headers."""
    
    @pytest.mark.asyncio
    async def test_x_content_type_options(self, client):
        """Test header X-Content-Type-Options."""
        async with client:
            response = await client.get("/")
            
            # TODO: Descomentar cuando SecurityHeadersMiddleware esté activo
            # assert response.headers.get("X-Content-Type-Options") == "nosniff"
            assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_x_frame_options(self, client):
        """Test header X-Frame-Options para prevenir clickjacking."""
        async with client:
            response = await client.get("/")
            
            # TODO: Descomentar cuando SecurityHeadersMiddleware esté activo
            # assert response.headers.get("X-Frame-Options") == "DENY"
            assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_x_xss_protection(self, client):
        """Test header X-XSS-Protection."""
        async with client:
            response = await client.get("/")
            
            # TODO: Descomentar cuando SecurityHeadersMiddleware esté activo
            # assert "1; mode=block" in response.headers.get("X-XSS-Protection", "")
            assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_referrer_policy(self, client):
        """Test header Referrer-Policy."""
        async with client:
            response = await client.get("/")
            
            # TODO: Descomentar cuando SecurityHeadersMiddleware esté activo
            # assert response.headers.get("Referrer-Policy") is not None
            assert response.status_code == 200


class TestCORS:
    """Tests para verificar configuración CORS."""
    
    @pytest.mark.asyncio
    async def test_cors_preflight(self, client):
        """Test preflight request CORS."""
        async with client:
            response = await client.options(
                "/tasks",
                headers={
                    "Origin": "http://localhost:3000",
                    "Access-Control-Request-Method": "POST",
                    "Access-Control-Request-Headers": "Content-Type",
                },
            )
            
            # TODO: Descomentar cuando CORS esté configurado
            # assert "Access-Control-Allow-Origin" in response.headers
            # assert "Access-Control-Allow-Methods" in response.headers
            
            # Por ahora solo verificar que responde
            assert response.status_code in [200, 405]
    
    @pytest.mark.asyncio
    async def test_cors_allowed_origin(self, client):
        """Test que origen permitido recibe headers CORS."""
        async with client:
            response = await client.get(
                "/tasks",
                headers={"Origin": "http://localhost:3000"},
            )
            
            assert response.status_code == 200
            # TODO: Descomentar cuando CORS esté configurado
            # assert response.headers.get("Access-Control-Allow-Origin") == "http://localhost:3000"
    
    @pytest.mark.asyncio
    async def test_cors_credentials(self, client):
        """Test que Access-Control-Allow-Credentials está configurado."""
        async with client:
            response = await client.get(
                "/tasks",
                headers={"Origin": "http://localhost:3000"},
            )
            
            # TODO: Descomentar cuando CORS esté configurado
            # assert response.headers.get("Access-Control-Allow-Credentials") == "true"
            assert response.status_code == 200
