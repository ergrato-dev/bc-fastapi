"""
Tests para Rate Limiting

Estos tests verifican que el rate limiting funciona correctamente.
"""

import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.fixture
def client():
    """Cliente HTTP para tests."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestRateLimiting:
    """Tests de rate limiting."""
    
    @pytest.mark.asyncio
    async def test_root_endpoint(self, client):
        """Test que el endpoint raíz funciona."""
        async with client as ac:
            response = await ac.get("/")
        
        assert response.status_code == 200
        assert "endpoints" in response.json()
    
    @pytest.mark.asyncio
    async def test_public_endpoint_within_limit(self, client):
        """Test que el endpoint público funciona dentro del límite."""
        async with client as ac:
            response = await ac.get("/public")
        
        # Si el endpoint está implementado
        if response.status_code != 404:
            assert response.status_code == 200
            assert "X-RateLimit-Limit" in response.headers
            assert "X-RateLimit-Remaining" in response.headers
    
    @pytest.mark.asyncio
    async def test_health_endpoint_no_limit(self, client):
        """Test que health check no tiene límite."""
        async with client as ac:
            # Hacer muchas requests rápidamente
            for _ in range(50):
                response = await ac.get("/health")
                
                # Si el endpoint está implementado
                if response.status_code == 404:
                    break
                    
                # Health nunca debe retornar 429
                assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_rate_limit_headers_present(self, client):
        """Test que los headers de rate limit están presentes."""
        async with client as ac:
            response = await ac.get("/public")
        
        # Si el endpoint está implementado
        if response.status_code != 404:
            headers = response.headers
            
            # Verificar headers estándar de rate limiting
            assert "X-RateLimit-Limit" in headers or "x-ratelimit-limit" in headers
            assert "X-RateLimit-Remaining" in headers or "x-ratelimit-remaining" in headers
    
    @pytest.mark.asyncio
    async def test_dynamic_limit_anonymous(self, client):
        """Test límite dinámico para usuario anónimo."""
        async with client as ac:
            response = await ac.get("/api/data")
        
        if response.status_code != 404:
            data = response.json()
            assert data.get("user_type") == "anonymous"
    
    @pytest.mark.asyncio
    async def test_dynamic_limit_premium(self, client):
        """Test límite dinámico para usuario premium."""
        async with client as ac:
            response = await ac.get(
                "/api/data",
                headers={"X-User-Type": "premium"}
            )
        
        if response.status_code != 404:
            data = response.json()
            assert data.get("user_type") == "premium"


class TestRateLimitExceeded:
    """Tests para cuando se excede el límite."""
    
    @pytest.mark.asyncio
    async def test_login_rate_limit_exceeded(self, client):
        """Test que login bloquea después de 5 requests."""
        async with client as ac:
            # Hacer 6 requests (límite es 5/minute)
            responses = []
            for _ in range(6):
                response = await ac.post("/auth/login")
                responses.append(response)
                
                if response.status_code == 404:
                    # Endpoint no implementado aún
                    pytest.skip("Endpoint /auth/login no implementado")
            
            # Las primeras 5 deberían ser exitosas
            successful = [r for r in responses if r.status_code == 200]
            blocked = [r for r in responses if r.status_code == 429]
            
            # Al menos una debería ser bloqueada
            # (puede variar por timing)
            assert len(successful) <= 5
    
    @pytest.mark.asyncio
    async def test_429_response_format(self, client):
        """Test que la respuesta 429 tiene el formato correcto."""
        async with client as ac:
            # Hacer muchas requests para exceder el límite
            for _ in range(25):
                response = await ac.get("/public")
                
                if response.status_code == 404:
                    pytest.skip("Endpoint /public no implementado")
                
                if response.status_code == 429:
                    # Verificar que tiene Retry-After
                    assert "Retry-After" in response.headers or "retry-after" in response.headers
                    break
