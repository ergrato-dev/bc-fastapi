"""ConsoleAdapter - imprime en consola."""
from src.domain.entities import Notification, NotificationChannel


class ConsoleAdapter:
    """Adapter que imprime en consola."""
    
    def __init__(self, channel: NotificationChannel = NotificationChannel.EMAIL):
        self._channel = channel
    
    @property
    def channel(self) -> NotificationChannel:
        return self._channel
    
    async def send(self, notification: Notification) -> bool:
        print(f"[{self._channel.value.upper()}] → {notification.recipient}")
        print(f"  Asunto: {notification.subject}")
        print(f"  Mensaje: {notification.message}")
        return True
