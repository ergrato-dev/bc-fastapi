"""
Tests de integración para la API.

Estos tests verifican los endpoints usando un cliente HTTP
con fakes inyectados para las dependencias.
"""
import pytest
from httpx import AsyncClient


class TestNotificationsAPI:
    """Tests de integración para /api/v1/notifications."""
    
    @pytest.mark.asyncio
    async def test_health_check(self, test_client: AsyncClient):
        """
        Test: GET / retorna status ok.
        """
        response = await test_client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
    
    @pytest.mark.asyncio
    async def test_get_channels(self, test_client: AsyncClient):
        """
        Test: GET /api/v1/notifications/channels retorna canales.
        
        Este test pasará cuando implementes el endpoint.
        """
        response = await test_client.get("/api/v1/notifications/channels")
        
        assert response.status_code == 200
        channels = response.json()
        assert isinstance(channels, list)
        assert "email" in channels or "EMAIL" in channels
    
    @pytest.mark.asyncio
    async def test_send_notification(self, test_client: AsyncClient):
        """
        Test: POST /api/v1/notifications crea una notificación.
        
        Este test pasará cuando implementes el endpoint y el servicio.
        """
        response = await test_client.post(
            "/api/v1/notifications",
            json={
                "recipient": "user@example.com",
                "channel": "email",
                "message": "Test message",
                "subject": "Test subject",
            },
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["recipient"] == "user@example.com"
        assert "id" in data
    
    @pytest.mark.asyncio
    async def test_get_notification(self, test_client: AsyncClient):
        """
        Test: GET /api/v1/notifications/{id} retorna la notificación.
        """
        # Arrange - crear primero
        create_response = await test_client.post(
            "/api/v1/notifications",
            json={
                "recipient": "user@example.com",
                "channel": "email",
                "message": "Test",
            },
        )
        notification_id = create_response.json()["id"]
        
        # Act
        response = await test_client.get(
            f"/api/v1/notifications/{notification_id}"
        )
        
        # Assert
        assert response.status_code == 200
        assert response.json()["id"] == notification_id
    
    @pytest.mark.asyncio
    async def test_get_notification_not_found(self, test_client: AsyncClient):
        """
        Test: GET /api/v1/notifications/{id} retorna 404 si no existe.
        """
        response = await test_client.get(
            "/api/v1/notifications/unknown-id"
        )
        
        assert response.status_code == 404
    
    @pytest.mark.asyncio
    async def test_list_notifications(self, test_client: AsyncClient):
        """
        Test: GET /api/v1/notifications retorna lista.
        """
        # Arrange - crear algunas
        for i in range(3):
            await test_client.post(
                "/api/v1/notifications",
                json={
                    "recipient": f"user{i}@example.com",
                    "channel": "email",
                    "message": f"Test {i}",
                },
            )
        
        # Act
        response = await test_client.get("/api/v1/notifications")
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 3
    
    @pytest.mark.asyncio
    async def test_delete_notification(self, test_client: AsyncClient):
        """
        Test: DELETE /api/v1/notifications/{id} elimina la notificación.
        """
        # Arrange - crear primero
        create_response = await test_client.post(
            "/api/v1/notifications",
            json={
                "recipient": "user@example.com",
                "channel": "email",
                "message": "To delete",
            },
        )
        notification_id = create_response.json()["id"]
        
        # Act
        delete_response = await test_client.delete(
            f"/api/v1/notifications/{notification_id}"
        )
        
        # Assert
        assert delete_response.status_code == 204
        
        # Verificar que ya no existe
        get_response = await test_client.get(
            f"/api/v1/notifications/{notification_id}"
        )
        assert get_response.status_code == 404
