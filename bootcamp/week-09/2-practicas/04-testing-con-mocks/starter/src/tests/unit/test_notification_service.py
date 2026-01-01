"""
Tests para NotificationService.

Estos tests usan fake adapters, ejecutan rápido y sin I/O.
"""
import pytest

from src.domain.entities import NotificationChannel, NotificationStatus
from src.application import NotificationService
from src.tests.fakes import FakeNotificationRepository, SpyNotificationSender


# ============================================
# PASO 4: Implementar tests
# ============================================

# Descomenta las siguientes líneas:

# class TestNotificationServiceSendEmail:
#     """Tests para envío de email."""
#     
#     @pytest.mark.asyncio
#     async def test_send_email_success(
#         self,
#         notification_service: NotificationService,
#         fake_repository: FakeNotificationRepository,
#         spy_email_sender: SpyNotificationSender,
#     ):
#         """Email se envía y guarda correctamente."""
#         # Act
#         result = await notification_service.send_notification(
#             recipient="user@example.com",
#             channel=NotificationChannel.EMAIL,
#             message="Hello!",
#             subject="Test",
#         )
#         
#         # Assert - Notificación creada
#         assert result.id is not None
#         assert result.recipient == "user@example.com"
#         assert result.status == NotificationStatus.SENT
#         
#         # Assert - Guardada en repository
#         saved = await fake_repository.get_by_id(result.id)
#         assert saved is not None
#         assert saved.status == NotificationStatus.SENT
#         
#         # Assert - Sender fue llamado
#         assert spy_email_sender.was_called()
#         assert spy_email_sender.call_count() == 1
#         assert spy_email_sender.was_called_with_recipient("user@example.com")
#     
#     @pytest.mark.asyncio
#     async def test_send_email_failure(
#         self,
#         notification_service: NotificationService,
#         spy_email_sender: SpyNotificationSender,
#     ):
#         """Email fallido se marca como FAILED."""
#         # Arrange - Configurar fallo
#         spy_email_sender.should_fail = True
#         
#         # Act
#         result = await notification_service.send_notification(
#             recipient="user@example.com",
#             channel=NotificationChannel.EMAIL,
#             message="Hello!",
#         )
#         
#         # Assert
#         assert result.status == NotificationStatus.FAILED
#         assert result.error_message is not None
#         assert spy_email_sender.was_called()
# 
# 
# class TestNotificationServiceSendSMS:
#     """Tests para envío de SMS."""
#     
#     @pytest.mark.asyncio
#     async def test_send_sms_success(
#         self,
#         notification_service: NotificationService,
#         spy_sms_sender: SpyNotificationSender,
#     ):
#         """SMS se envía correctamente."""
#         # Act
#         result = await notification_service.send_notification(
#             recipient="+1234567890",
#             channel=NotificationChannel.SMS,
#             message="Hello SMS!",
#         )
#         
#         # Assert
#         assert result.status == NotificationStatus.SENT
#         assert spy_sms_sender.was_called()
#         assert spy_sms_sender.call_count() == 1
# 
# 
# class TestNotificationServiceUnsupportedChannel:
#     """Tests para canales no soportados."""
#     
#     @pytest.mark.asyncio
#     async def test_unsupported_channel_fails(
#         self,
#         notification_service: NotificationService,
#     ):
#         """Canal no soportado marca como FAILED."""
#         # Act
#         result = await notification_service.send_notification(
#             recipient="device-token",
#             channel=NotificationChannel.PUSH,  # No configurado
#             message="Push notification",
#         )
#         
#         # Assert
#         assert result.status == NotificationStatus.FAILED
#         assert "no soportado" in (result.error_message or "")
# 
# 
# class TestNotificationServiceGetNotification:
#     """Tests para obtener notificaciones."""
#     
#     @pytest.mark.asyncio
#     async def test_get_existing_notification(
#         self,
#         notification_service: NotificationService,
#     ):
#         """Obtiene notificación existente."""
#         # Arrange
#         created = await notification_service.send_notification(
#             recipient="user@example.com",
#             channel=NotificationChannel.EMAIL,
#             message="Test",
#         )
#         
#         # Act
#         result = await notification_service.get_notification(created.id)  # type: ignore
#         
#         # Assert
#         assert result is not None
#         assert result.id == created.id
#     
#     @pytest.mark.asyncio
#     async def test_get_nonexistent_notification(
#         self,
#         notification_service: NotificationService,
#     ):
#         """Retorna None para ID inexistente."""
#         result = await notification_service.get_notification(99999)
#         assert result is None


# Placeholders temporales - tests básicos que funcionan
class TestNotificationServiceBasic:
    """Tests básicos."""
    
    @pytest.mark.asyncio
    async def test_send_email_creates_notification(
        self,
        notification_service: NotificationService,
        fake_repository: FakeNotificationRepository,
    ):
        """Verifica que se crea la notificación."""
        result = await notification_service.send_notification(
            recipient="user@example.com",
            channel=NotificationChannel.EMAIL,
            message="Hello!",
        )
        
        assert result.id is not None
        assert result.recipient == "user@example.com"
    
    @pytest.mark.asyncio
    async def test_spy_records_calls(
        self,
        notification_service: NotificationService,
        spy_email_sender: SpyNotificationSender,
    ):
        """Verifica que el spy registra llamadas."""
        await notification_service.send_notification(
            recipient="user@example.com",
            channel=NotificationChannel.EMAIL,
            message="Hello!",
        )
        
        assert spy_email_sender.was_called()
        assert spy_email_sender.call_count() == 1
