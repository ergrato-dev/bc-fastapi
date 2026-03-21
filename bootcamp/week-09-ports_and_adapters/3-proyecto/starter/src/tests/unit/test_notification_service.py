"""
Tests unitarios para NotificationService.

Estos tests verifican que el servicio funciona correctamente
usando fakes en lugar de implementaciones reales.
"""
import pytest

from src.domain.entities.notification import (
    NotificationChannel,
    NotificationStatus,
)
from src.application.services.notification_service import NotificationService
from src.tests.fakes.fake_sender import FakeNotificationSender
from src.tests.fakes.fake_repository import FakeNotificationRepository


class TestNotificationService:
    """Tests para NotificationService."""
    
    @pytest.mark.asyncio
    async def test_send_notification_creates_and_saves(
        self,
        notification_service: NotificationService,
        fake_repository: FakeNotificationRepository,
    ):
        """
        Test: send_notification crea y guarda la notificación.
        
        Este test pasará cuando implementes send_notification().
        """
        # Act
        result = await notification_service.send_notification(
            recipient="user@example.com",
            channel=NotificationChannel.EMAIL,
            message="Test message",
            subject="Test subject",
        )
        
        # Assert
        assert result is not None
        assert result.id is not None
        assert result.recipient == "user@example.com"
        assert result.channel == NotificationChannel.EMAIL
        
        # Verificar que se guardó
        saved = await fake_repository.get_by_id(result.id)
        assert saved is not None
    
    @pytest.mark.asyncio
    async def test_send_notification_calls_sender(
        self,
        notification_service: NotificationService,
        fake_email_sender: FakeNotificationSender,
    ):
        """
        Test: send_notification llama al sender correcto.
        """
        # Act
        await notification_service.send_notification(
            recipient="user@example.com",
            channel=NotificationChannel.EMAIL,
            message="Test",
        )
        
        # Assert
        assert fake_email_sender.was_called()
        assert fake_email_sender.call_count() == 1
    
    @pytest.mark.asyncio
    async def test_send_notification_updates_status_on_success(
        self,
        notification_service: NotificationService,
    ):
        """
        Test: send_notification actualiza estado a SENT si tiene éxito.
        """
        # Act
        result = await notification_service.send_notification(
            recipient="user@example.com",
            channel=NotificationChannel.EMAIL,
            message="Test",
        )
        
        # Assert
        assert result.status == NotificationStatus.SENT
    
    @pytest.mark.asyncio
    async def test_send_notification_updates_status_on_failure(
        self,
        fake_senders: dict,
        fake_repository: FakeNotificationRepository,
    ):
        """
        Test: send_notification actualiza estado a FAILED si falla.
        """
        # Arrange - configurar sender para que falle
        fake_senders[NotificationChannel.EMAIL].set_should_fail(True)
        service = NotificationService(
            senders=fake_senders,
            repository=fake_repository,
        )
        
        # Act
        result = await service.send_notification(
            recipient="user@example.com",
            channel=NotificationChannel.EMAIL,
            message="Test",
        )
        
        # Assert
        assert result.status == NotificationStatus.FAILED
    
    @pytest.mark.asyncio
    async def test_get_available_channels(
        self,
        notification_service: NotificationService,
    ):
        """
        Test: get_available_channels retorna los canales configurados.
        """
        # Act
        channels = notification_service.get_available_channels()
        
        # Assert
        assert NotificationChannel.EMAIL in channels
        assert NotificationChannel.SMS in channels
    
    @pytest.mark.asyncio
    async def test_get_notification_returns_saved(
        self,
        notification_service: NotificationService,
    ):
        """
        Test: get_notification retorna una notificación guardada.
        """
        # Arrange
        created = await notification_service.send_notification(
            recipient="user@example.com",
            channel=NotificationChannel.EMAIL,
            message="Test",
        )
        
        # Act
        result = await notification_service.get_notification(created.id)
        
        # Assert
        assert result is not None
        assert result.id == created.id
    
    @pytest.mark.asyncio
    async def test_get_notification_returns_none_for_unknown(
        self,
        notification_service: NotificationService,
    ):
        """
        Test: get_notification retorna None para ID desconocido.
        """
        # Act
        result = await notification_service.get_notification("unknown-id")
        
        # Assert
        assert result is None
