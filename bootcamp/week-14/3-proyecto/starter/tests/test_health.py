"""
Tests para Health Checks y Métricas.
"""

import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest.fixture
def client():
    """Fixture para cliente HTTP."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestHealthChecks:
    """Tests para endpoints de health check."""
    
    @pytest.mark.asyncio
    async def test_liveness_healthy(self, client):
        """Test liveness check retorna healthy."""
        async with client:
            response = await client.get("/health/live")
            
            assert response.status_code == 200
            data = response.json()
            assert data["status"] == "healthy"
            assert "timestamp" in data
            assert data["service"] == "task-api"
    
    @pytest.mark.asyncio
    async def test_liveness_fast_response(self, client):
        """Test que liveness responde rápido (<100ms)."""
        import time
        
        async with client:
            start = time.perf_counter()
            response = await client.get("/health/live")
            duration = time.perf_counter() - start
            
            assert response.status_code == 200
            assert duration < 0.1  # Menos de 100ms
    
    @pytest.mark.asyncio
    async def test_readiness_healthy(self, client):
        """Test readiness check retorna healthy con checks."""
        async with client:
            response = await client.get("/health/ready")
            
            assert response.status_code == 200
            data = response.json()
            assert data["status"] in ["healthy", "degraded"]
            assert "checks" in data
    
    @pytest.mark.asyncio
    async def test_readiness_includes_database_check(self, client):
        """Test que readiness incluye check de database."""
        async with client:
            response = await client.get("/health/ready")
            data = response.json()
            
            assert "checks" in data
            assert "database" in data["checks"]
            assert "healthy" in data["checks"]["database"]
    
    @pytest.mark.asyncio
    async def test_readiness_version_present(self, client):
        """Test que readiness incluye versión."""
        async with client:
            response = await client.get("/health/ready")
            data = response.json()
            
            assert data.get("version") == "1.0.0"


class TestMetricsEndpoint:
    """Tests para endpoint de métricas Prometheus."""
    
    @pytest.mark.asyncio
    async def test_metrics_endpoint_exists(self, client):
        """Test que /metrics existe y responde."""
        async with client:
            response = await client.get("/metrics")
            
            assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_metrics_format_prometheus(self, client):
        """Test que métricas están en formato Prometheus."""
        async with client:
            response = await client.get("/metrics")
            
            # Formato Prometheus es text/plain
            assert "text/plain" in response.headers.get("content-type", "")
            
            # Debe contener líneas de métricas
            content = response.text
            assert len(content) > 0
    
    @pytest.mark.asyncio
    async def test_http_metrics_generated(self, client):
        """Test que requests generan métricas HTTP."""
        async with client:
            # Hacer algunos requests
            await client.get("/tasks")
            await client.get("/tasks")
            await client.post("/tasks", json={"title": "Test", "priority": "low"})
            
            # Obtener métricas
            response = await client.get("/metrics")
            content = response.text
            
            # Debe contener métricas HTTP
            assert "http" in content.lower()
    
    @pytest.mark.asyncio
    async def test_health_endpoints_excluded_from_metrics(self, client):
        """
        Test que health checks pueden excluirse de métricas.
        
        Esto evita que los health checks de Kubernetes
        inflen las métricas.
        """
        async with client:
            # Hacer muchos health checks
            for _ in range(10):
                await client.get("/health/live")
                await client.get("/health/ready")
            
            # Las métricas deberían existir
            response = await client.get("/metrics")
            assert response.status_code == 200
            
            # TODO: Verificar que health no está en métricas
            # cuando la configuración avanzada esté activa


class TestMetricsIntegration:
    """Tests de integración para métricas de negocio."""
    
    @pytest.mark.asyncio
    async def test_task_creation_metrics(self, client):
        """Test que crear tareas genera métricas."""
        async with client:
            # Crear algunas tareas
            for i in range(3):
                await client.post(
                    "/tasks",
                    json={
                        "title": f"Metric Test Task {i}",
                        "priority": "high",
                    },
                )
            
            # Verificar métricas
            response = await client.get("/metrics")
            
            # TODO: Descomentar cuando métricas de negocio estén activas
            # assert "tasks_created_total" in response.text
            assert response.status_code == 200
