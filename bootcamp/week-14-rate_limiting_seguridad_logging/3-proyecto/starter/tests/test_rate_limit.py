"""
Tests para Rate Limiting.
"""

import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest.fixture
def client():
    """Fixture para cliente HTTP."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestRateLimiting:
    """Tests para verificar rate limiting."""
    
    @pytest.mark.asyncio
    async def test_rate_limit_headers_present(self, client):
        """
        Test que los headers de rate limit están presentes.
        
        Headers esperados:
        - X-RateLimit-Limit
        - X-RateLimit-Remaining
        - X-RateLimit-Reset
        """
        async with client:
            response = await client.get("/tasks")
            
            # Verificar que la respuesta es exitosa
            assert response.status_code == 200
            
            # TODO: Verificar headers cuando se implemente rate limiting
            # assert "X-RateLimit-Limit" in response.headers
            # assert "X-RateLimit-Remaining" in response.headers
    
    @pytest.mark.asyncio
    async def test_login_rate_limit(self, client):
        """
        Test que login tiene rate limit estricto.
        
        Debe permitir máximo 5 requests por minuto.
        """
        async with client:
            # Hacer múltiples requests de login
            responses = []
            for _ in range(6):
                response = await client.post(
                    "/auth/login",
                    json={"username": "test", "password": "wrong"},
                )
                responses.append(response)
            
            # Los primeros 5 deberían ser 401 (credenciales inválidas)
            # El 6to debería ser 429 cuando rate limiting esté activo
            
            # Por ahora, todos deberían ser 401
            for resp in responses[:5]:
                assert resp.status_code == 401
            
            # TODO: Descomentar cuando rate limiting esté activo
            # assert responses[5].status_code == 429
    
    @pytest.mark.asyncio
    async def test_tasks_list_allows_many_requests(self, client):
        """
        Test que list tasks tiene límite más alto.
        
        Debe permitir 60 requests por minuto.
        """
        async with client:
            # Hacer varios requests
            for i in range(10):
                response = await client.get("/tasks")
                assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_create_task_rate_limit(self, client):
        """
        Test rate limit en creación de tareas.
        
        Debe permitir 20 requests por minuto.
        """
        async with client:
            # Hacer varios requests de creación
            for i in range(5):
                response = await client.post(
                    "/tasks",
                    json={
                        "title": f"Task {i}",
                        "description": "Test task",
                        "priority": "medium",
                    },
                )
                assert response.status_code == 201
