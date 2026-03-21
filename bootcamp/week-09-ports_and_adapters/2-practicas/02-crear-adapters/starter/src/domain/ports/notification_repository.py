"""Port: NotificationRepository - Protocol completo."""
from typing import Protocol
from datetime import datetime

from ..entities import Notification, NotificationStatus, NotificationChannel


class NotificationRepository(Protocol):
    """Port para persistencia de notificaciones."""
    
    async def save(self, notification: Notification) -> Notification:
        """Guarda una notificación."""
        ...
    
    async def get_by_id(self, notification_id: int) -> Notification | None:
        """Obtiene por ID."""
        ...
    
    async def get_by_recipient(
        self,
        recipient: str,
        limit: int = 100,
        offset: int = 0
    ) -> list[Notification]:
        """Obtiene por destinatario."""
        ...
    
    async def get_by_status(
        self,
        status: NotificationStatus,
        limit: int = 100
    ) -> list[Notification]:
        """Obtiene por estado."""
        ...
    
    async def delete(self, notification_id: int) -> bool:
        """Elimina una notificación."""
        ...
