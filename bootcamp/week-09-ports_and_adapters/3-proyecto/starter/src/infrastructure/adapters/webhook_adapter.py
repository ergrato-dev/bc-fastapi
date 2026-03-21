"""
Adapter: WebhookNotificationSender

Implementación de NotificationSender para webhooks HTTP.
"""
from src.domain.entities.notification import Notification, NotificationChannel
from src.domain.ports.notification_sender import NotificationSender
from src.config import settings


class WebhookNotificationSender:
    """
    Adapter que envía notificaciones via webhook HTTP.
    
    Implementa el Protocol NotificationSender.
    Hace POST a una URL con el payload de la notificación.
    
    TODO: Implementa los métodos para cumplir con el Protocol.
    """
    
    def __init__(self, timeout: int | None = None):
        """
        Inicializa el adapter con configuración.
        
        Args:
            timeout: Timeout en segundos para las peticiones HTTP
        """
        self._timeout = timeout or settings.webhook_timeout
    
    @property
    def channel(self) -> NotificationChannel:
        """Este adapter maneja el canal WEBHOOK."""
        return NotificationChannel.WEBHOOK
    
    async def send(self, notification: Notification) -> bool:
        """
        Envía una notificación via webhook.
        
        Args:
            notification: Notificación con URL como recipient
            
        Returns:
            True si el webhook respondió 2xx, False si falló
            
        TODO: Implementar:
        1. Validar que recipient sea una URL válida
        2. Construir payload JSON con datos de la notificación
        3. En desarrollo: simular envío
        4. En producción: usar httpx para hacer POST
        5. Retornar True si respuesta es 2xx
        
        Nota: Para este proyecto, simula el envío con un print.
        """
        # TODO: Implementar
        pass
    
    async def send_batch(self, notifications: list[Notification]) -> dict[str, bool]:
        """
        Envía múltiples webhooks.
        
        Args:
            notifications: Lista de notificaciones
            
        Returns:
            Dict {notification_id: success}
            
        TODO: Implementar iterando y usando send().
        """
        # TODO: Implementar
        pass
