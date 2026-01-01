"""NotificationService - Servicio a testear."""
from src.domain.entities import Notification, NotificationChannel, NotificationStatus
from src.domain.ports import NotificationSender, NotificationRepository


class NotificationService:
    """Servicio de notificaciones."""
    
    def __init__(
        self,
        repository: NotificationRepository,
        email_sender: NotificationSender,
        sms_sender: NotificationSender,
    ):
        self._repository = repository
        self._senders: dict[NotificationChannel, NotificationSender] = {
            NotificationChannel.EMAIL: email_sender,
            NotificationChannel.SMS: sms_sender,
        }
    
    async def send_notification(
        self,
        recipient: str,
        channel: NotificationChannel,
        message: str,
        subject: str | None = None,
    ) -> Notification:
        """Envía una notificación."""
        notification = Notification(
            recipient=recipient,
            channel=channel,
            message=message,
            subject=subject,
        )
        
        notification = await self._repository.save(notification)
        
        sender = self._senders.get(channel)
        if sender is None:
            notification.mark_as_failed(f"Canal {channel.value} no soportado")
            return await self._repository.save(notification)
        
        success = await sender.send(notification)
        
        if success:
            notification.mark_as_sent()
        else:
            notification.mark_as_failed("Error en el envío")
        
        return await self._repository.save(notification)
    
    async def get_notification(self, notification_id: int) -> Notification | None:
        """Obtiene una notificación por ID."""
        return await self._repository.get_by_id(notification_id)
    
    async def get_pending_notifications(self) -> list[Notification]:
        """Obtiene notificaciones pendientes."""
        return await self._repository.get_by_status(NotificationStatus.PENDING)
