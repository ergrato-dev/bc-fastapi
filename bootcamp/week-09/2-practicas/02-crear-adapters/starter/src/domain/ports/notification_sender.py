"""Port: NotificationSender - Protocol completo."""
from typing import Protocol

from ..entities import Notification, NotificationChannel


class NotificationSender(Protocol):
    """Port para envío de notificaciones."""
    
    @property
    def channel(self) -> NotificationChannel:
        """Canal que implementa este sender."""
        ...
    
    async def send(self, notification: Notification) -> bool:
        """Envía una notificación."""
        ...
    
    async def send_batch(
        self,
        notifications: list[Notification]
    ) -> dict[int, bool]:
        """Envía múltiples notificaciones."""
        ...
