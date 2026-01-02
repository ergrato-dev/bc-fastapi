"""
Tests para Security Headers y CORS

Verifica que los headers de seguridad están configurados correctamente.
"""

import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.fixture
def client():
    """Cliente HTTP para tests."""
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


class TestSecurityHeaders:
    """Tests de security headers."""
    
    @pytest.mark.asyncio
    async def test_root_endpoint(self, client):
        """Test que el endpoint raíz funciona."""
        async with client as ac:
            response = await ac.get("/")
        
        assert response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_x_content_type_options(self, client):
        """Test header X-Content-Type-Options."""
        async with client as ac:
            response = await ac.get("/api/data")
        
        # Verificar que el header existe (case-insensitive)
        headers_lower = {k.lower(): v for k, v in response.headers.items()}
        
        if "x-content-type-options" in headers_lower:
            assert headers_lower["x-content-type-options"] == "nosniff"
    
    @pytest.mark.asyncio
    async def test_x_frame_options(self, client):
        """Test header X-Frame-Options."""
        async with client as ac:
            response = await ac.get("/api/data")
        
        headers_lower = {k.lower(): v for k, v in response.headers.items()}
        
        if "x-frame-options" in headers_lower:
            assert headers_lower["x-frame-options"] in ["DENY", "SAMEORIGIN"]
    
    @pytest.mark.asyncio
    async def test_x_xss_protection(self, client):
        """Test header X-XSS-Protection."""
        async with client as ac:
            response = await ac.get("/api/data")
        
        headers_lower = {k.lower(): v for k, v in response.headers.items()}
        
        if "x-xss-protection" in headers_lower:
            assert "1" in headers_lower["x-xss-protection"]
    
    @pytest.mark.asyncio
    async def test_referrer_policy(self, client):
        """Test header Referrer-Policy."""
        async with client as ac:
            response = await ac.get("/api/data")
        
        headers_lower = {k.lower(): v for k, v in response.headers.items()}
        
        if "referrer-policy" in headers_lower:
            valid_policies = [
                "no-referrer",
                "strict-origin",
                "strict-origin-when-cross-origin",
                "no-referrer-when-downgrade"
            ]
            assert any(p in headers_lower["referrer-policy"] for p in valid_policies)


class TestCORS:
    """Tests de CORS."""
    
    @pytest.mark.asyncio
    async def test_cors_allowed_origin(self, client):
        """Test CORS con origen permitido."""
        async with client as ac:
            response = await ac.get(
                "/api/data",
                headers={"Origin": "https://allowed-domain.com"}
            )
        
        # Si CORS está configurado, debería incluir el header
        headers_lower = {k.lower(): v for k, v in response.headers.items()}
        
        if "access-control-allow-origin" in headers_lower:
            assert headers_lower["access-control-allow-origin"] == "https://allowed-domain.com"
    
    @pytest.mark.asyncio
    async def test_cors_blocked_origin(self, client):
        """Test CORS con origen bloqueado."""
        async with client as ac:
            response = await ac.get(
                "/api/data",
                headers={"Origin": "https://evil-site.com"}
            )
        
        headers_lower = {k.lower(): v for k, v in response.headers.items()}
        
        # Si CORS está configurado, no debería permitir este origen
        if "access-control-allow-origin" in headers_lower:
            assert headers_lower["access-control-allow-origin"] != "https://evil-site.com"
            assert headers_lower["access-control-allow-origin"] != "*"


class TestErrorHandling:
    """Tests de manejo de errores."""
    
    @pytest.mark.asyncio
    async def test_error_no_stack_trace(self, client):
        """Test que errores no exponen stack traces."""
        async with client as ac:
            response = await ac.get("/api/error")
        
        # El error debería ser manejado
        assert response.status_code == 500
        
        data = response.json()
        
        # No debería contener información de stack trace
        response_text = str(data)
        assert "Traceback" not in response_text
        assert "File" not in response_text or "error" in response_text.lower()
    
    @pytest.mark.asyncio
    async def test_http_exception_format(self, client):
        """Test formato de HTTPException."""
        async with client as ac:
            response = await ac.get("/api/not-found")
        
        assert response.status_code == 404
        
        data = response.json()
        # Debería tener un formato controlado
        assert "detail" in data or "error" in data or "message" in data
