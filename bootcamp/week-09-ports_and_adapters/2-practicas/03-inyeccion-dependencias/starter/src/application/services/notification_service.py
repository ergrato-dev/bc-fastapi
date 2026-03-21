"""
NotificationService - Servicio de aplicación.

Este servicio orquesta la lógica de negocio usando SOLO Ports,
nunca adapters concretos.
"""
from src.domain.entities import Notification, NotificationChannel, NotificationStatus
from src.domain.ports import NotificationSender, NotificationRepository


# ============================================
# PASO 2: Implementar NotificationService
# ============================================
# El servicio recibe Ports (Protocols) en el constructor,
# NO adapters concretos. Esto permite cambiar implementaciones.

# Descomenta las siguientes líneas:

# class NotificationService:
#     """
#     Servicio de notificaciones.
#     
#     Depende de Ports (abstracciones), no de Adapters (implementaciones).
#     """
#     
#     def __init__(
#         self,
#         repository: NotificationRepository,
#         email_sender: NotificationSender,
#         sms_sender: NotificationSender,
#     ):
#         """
#         Constructor con inyección de dependencias.
#         
#         Args:
#             repository: Port para persistencia
#             email_sender: Port para envío de emails
#             sms_sender: Port para envío de SMS
#         """
#         self._repository = repository
#         self._senders: dict[NotificationChannel, NotificationSender] = {
#             NotificationChannel.EMAIL: email_sender,
#             NotificationChannel.SMS: sms_sender,
#         }
#     
#     async def send_notification(
#         self,
#         recipient: str,
#         channel: NotificationChannel,
#         message: str,
#         subject: str | None = None,
#     ) -> Notification:
#         """
#         Envía una notificación y la persiste.
#         
#         1. Crea la notificación
#         2. La guarda como PENDING
#         3. Intenta enviarla
#         4. Actualiza el estado según resultado
#         """
#         # Crear notificación
#         notification = Notification(
#             recipient=recipient,
#             channel=channel,
#             message=message,
#             subject=subject,
#         )
#         
#         # Guardar como pendiente
#         notification = await self._repository.save(notification)
#         
#         # Obtener sender para el canal
#         sender = self._senders.get(channel)
#         if sender is None:
#             notification.mark_as_failed(f"Canal {channel.value} no soportado")
#             return await self._repository.save(notification)
#         
#         # Intentar enviar
#         success = await sender.send(notification)
#         
#         if success:
#             notification.mark_as_sent()
#         else:
#             notification.mark_as_failed("Error en el envío")
#         
#         # Guardar estado final
#         return await self._repository.save(notification)
#     
#     async def get_notification(self, notification_id: int) -> Notification | None:
#         """Obtiene una notificación por ID."""
#         return await self._repository.get_by_id(notification_id)
#     
#     async def get_pending_notifications(self) -> list[Notification]:
#         """Obtiene notificaciones pendientes."""
#         return await self._repository.get_by_status(NotificationStatus.PENDING)


# Placeholder temporal
class NotificationService:
    """Placeholder."""
    def __init__(
        self,
        repository: NotificationRepository,
        email_sender: NotificationSender,
        sms_sender: NotificationSender,
    ):
        pass
    
    async def send_notification(
        self,
        recipient: str,
        channel: NotificationChannel,
        message: str,
        subject: str | None = None,
    ) -> Notification:
        return Notification(recipient=recipient, channel=channel, message=message)
    
    async def get_notification(self, notification_id: int) -> Notification | None:
        return None
