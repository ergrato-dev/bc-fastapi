"""
Adapter: PushNotificationSender

Implementación de NotificationSender para notificaciones push.
"""
from src.domain.entities.notification import Notification, NotificationChannel
from src.domain.ports.notification_sender import NotificationSender


class PushNotificationSender:
    """
    Adapter que envía notificaciones push.
    
    Implementa el Protocol NotificationSender.
    En producción usaría Firebase Cloud Messaging, Apple APNs, etc.
    
    TODO: Implementa los métodos para cumplir con el Protocol.
    """
    
    def __init__(self, credentials_path: str | None = None):
        """
        Inicializa el adapter con credenciales push.
        
        Args:
            credentials_path: Ruta al archivo de credenciales (ej: Firebase)
        """
        self._credentials_path = credentials_path
    
    @property
    def channel(self) -> NotificationChannel:
        """Este adapter maneja el canal PUSH."""
        return NotificationChannel.PUSH
    
    async def send(self, notification: Notification) -> bool:
        """
        Envía una notificación push.
        
        Args:
            notification: Notificación con device_id como recipient
            
        Returns:
            True si se envió, False si falló
            
        TODO: Implementar:
        1. El recipient debe ser un device_id o topic
        2. En desarrollo: simular envío
        3. En producción: usar Firebase/APNs
        
        Nota: Para este proyecto, simula el envío con un print.
        """
        # TODO: Implementar
        pass
    
    async def send_batch(self, notifications: list[Notification]) -> dict[str, bool]:
        """
        Envía múltiples notificaciones push.
        
        Args:
            notifications: Lista de notificaciones
            
        Returns:
            Dict {notification_id: success}
            
        TODO: Implementar iterando y usando send().
        """
        # TODO: Implementar
        pass
