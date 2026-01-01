"""
Adapter: SMSNotificationSender

Implementación de NotificationSender para envío de SMS.
"""
from src.domain.entities.notification import Notification, NotificationChannel
from src.domain.ports.notification_sender import NotificationSender
from src.config import settings


class SMSNotificationSender:
    """
    Adapter que envía notificaciones por SMS.
    
    Implementa el Protocol NotificationSender.
    En producción usaría Twilio, Nexmo, o similar.
    
    TODO: Implementa los métodos para cumplir con el Protocol.
    """
    
    def __init__(
        self,
        account_sid: str | None = None,
        auth_token: str | None = None,
        from_number: str | None = None,
    ):
        """
        Inicializa el adapter con credenciales SMS.
        
        Args:
            account_sid: ID de cuenta (ej: Twilio SID)
            auth_token: Token de autenticación
            from_number: Número remitente
        """
        self._account_sid = account_sid or settings.twilio_sid
        self._auth_token = auth_token or settings.twilio_token
        self._from_number = from_number or settings.twilio_from
    
    @property
    def channel(self) -> NotificationChannel:
        """Este adapter maneja el canal SMS."""
        return NotificationChannel.SMS
    
    async def send(self, notification: Notification) -> bool:
        """
        Envía un SMS.
        
        Args:
            notification: Notificación con número de teléfono
            
        Returns:
            True si se envió, False si falló
            
        TODO: Implementar:
        1. Validar que recipient sea un número de teléfono
        2. En desarrollo: simular envío
        3. En producción: usar API de Twilio/Nexmo
        4. Manejar excepciones
        
        Nota: Para este proyecto, simula el envío con un print.
        """
        # TODO: Implementar
        pass
    
    async def send_batch(self, notifications: list[Notification]) -> dict[str, bool]:
        """
        Envía múltiples SMS.
        
        Args:
            notifications: Lista de notificaciones
            
        Returns:
            Dict {notification_id: success}
            
        TODO: Implementar iterando y usando send().
        """
        # TODO: Implementar
        pass
