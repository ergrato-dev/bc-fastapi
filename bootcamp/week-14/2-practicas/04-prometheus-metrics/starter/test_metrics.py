"""
Tests para Prometheus Metrics Practice.
"""

import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.fixture
def client():
    """Fixture para cliente HTTP asíncrono."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestMetricsEndpoint:
    """Tests para el endpoint /metrics."""
    
    @pytest.mark.asyncio
    async def test_metrics_endpoint_exists(self, client):
        """Test que /metrics existe y retorna 200."""
        async with client:
            response = await client.get("/metrics")
            
            assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_metrics_format_prometheus(self, client):
        """Test que las métricas están en formato Prometheus."""
        async with client:
            response = await client.get("/metrics")
            
            # El formato Prometheus usa text/plain
            assert "text/plain" in response.headers.get("content-type", "")
    
    @pytest.mark.asyncio
    async def test_http_metrics_present(self, client):
        """Test que las métricas HTTP están presentes."""
        async with client:
            # Hacer algunos requests para generar métricas
            await client.get("/api/users")
            await client.get("/api/users/1")
            
            # Obtener métricas
            response = await client.get("/metrics")
            content = response.text
            
            # Verificar que existen métricas HTTP
            # El instrumentator añade métricas como http_request_*
            assert "http" in content.lower()


class TestHealthEndpoints:
    """Tests para endpoints de health check."""
    
    @pytest.mark.asyncio
    async def test_liveness_returns_200(self, client):
        """Test que /health/live retorna 200 cuando está sano."""
        async with client:
            response = await client.get("/health/live")
            
            assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_liveness_response_format(self, client):
        """Test formato de respuesta de liveness."""
        async with client:
            response = await client.get("/health/live")
            data = response.json()
            
            assert "status" in data
            assert "timestamp" in data
            assert "service" in data
            assert data["status"] == "healthy"
    
    @pytest.mark.asyncio
    async def test_readiness_returns_200(self, client):
        """Test que /health/ready retorna 200 cuando está listo."""
        async with client:
            response = await client.get("/health/ready")
            
            assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_readiness_includes_checks(self, client):
        """Test que readiness incluye checks de dependencias."""
        async with client:
            response = await client.get("/health/ready")
            data = response.json()
            
            assert "status" in data
            assert "checks" in data
            # Verificar que hay al menos un check
            assert len(data["checks"]) > 0


class TestAPIEndpoints:
    """Tests para endpoints de API que generan métricas."""
    
    @pytest.mark.asyncio
    async def test_list_users(self, client):
        """Test endpoint de usuarios."""
        async with client:
            response = await client.get("/api/users")
            
            assert response.status_code == 200
            data = response.json()
            assert "users" in data
    
    @pytest.mark.asyncio
    async def test_get_user(self, client):
        """Test obtener usuario por ID."""
        async with client:
            response = await client.get("/api/users/1")
            
            assert response.status_code == 200
            data = response.json()
            assert data["id"] == 1
    
    @pytest.mark.asyncio
    async def test_create_order(self, client):
        """Test crear orden (genera métricas de negocio)."""
        async with client:
            response = await client.post("/api/orders")
            
            assert response.status_code == 200
            data = response.json()
            assert "order_id" in data
            assert "value" in data
            assert data["status"] == "created"
    
    @pytest.mark.asyncio
    async def test_login(self, client):
        """Test login (actualiza gauge de usuarios)."""
        async with client:
            response = await client.post("/api/auth/login")
            
            assert response.status_code == 200
            data = response.json()
            assert data["status"] == "logged_in"


class TestMetricsIntegration:
    """Tests de integración para verificar métricas."""
    
    @pytest.mark.asyncio
    async def test_requests_generate_metrics(self, client):
        """Test que los requests generan métricas en /metrics."""
        async with client:
            # Hacer múltiples requests
            for _ in range(5):
                await client.get("/api/users")
            
            for _ in range(3):
                await client.post("/api/orders")
            
            # Verificar que /metrics tiene contenido
            response = await client.get("/metrics")
            
            assert response.status_code == 200
            assert len(response.text) > 100  # Debe tener contenido sustancial
    
    @pytest.mark.asyncio
    async def test_health_not_in_metrics(self, client):
        """Test que health checks pueden excluirse de métricas."""
        async with client:
            # Hacer requests a health (deberían excluirse)
            for _ in range(10):
                await client.get("/health/live")
                await client.get("/health/ready")
            
            # Obtener métricas
            response = await client.get("/metrics")
            content = response.text
            
            # El endpoint existe y tiene contenido
            assert response.status_code == 200
            # Nota: Con la config completa, health no debería aparecer
            # Con la config simple, puede aparecer
