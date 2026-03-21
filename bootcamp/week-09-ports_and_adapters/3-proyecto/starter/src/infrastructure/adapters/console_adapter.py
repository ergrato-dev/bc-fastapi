"""
Adapter: ConsoleNotificationSender

Implementación de NotificationSender que imprime a consola.
Útil para desarrollo y debugging.
"""
from src.domain.entities.notification import Notification, NotificationChannel
from src.domain.ports.notification_sender import NotificationSender


class ConsoleNotificationSender:
    """
    Adapter que envía notificaciones a la consola.
    
    Implementa el Protocol NotificationSender.
    Ideal para desarrollo y testing manual.
    
    TODO: Implementa los métodos para cumplir con el Protocol.
    """
    
    @property
    def channel(self) -> NotificationChannel:
        """Este adapter maneja todos los canales (para desarrollo)."""
        return NotificationChannel.EMAIL  # Default para consola
    
    async def send(self, notification: Notification) -> bool:
        """
        Imprime la notificación a consola.
        
        Args:
            notification: Notificación a "enviar"
            
        Returns:
            Siempre True (la consola no falla)
            
        TODO: Implementar:
        1. Imprimir separador visual
        2. Imprimir detalles de la notificación
        3. Retornar True
        """
        # TODO: Implementar
        pass
    
    async def send_batch(self, notifications: list[Notification]) -> dict[str, bool]:
        """
        Imprime múltiples notificaciones.
        
        Args:
            notifications: Lista de notificaciones
            
        Returns:
            Dict con todos los IDs mapeados a True
            
        TODO: Implementar usando send() para cada notificación.
        """
        # TODO: Implementar
        pass
