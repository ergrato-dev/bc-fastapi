"""
FakeNotificationRepository - Fake para testing.
"""
from src.domain.entities.notification import Notification, NotificationStatus


class FakeNotificationRepository:
    """
    Fake repository para testing.
    
    Implementación en memoria que cumple con NotificationRepository.
    """
    
    def __init__(self):
        self._notifications: dict[str, Notification] = {}
    
    async def save(self, notification: Notification) -> Notification:
        """Guarda en memoria."""
        self._notifications[notification.id] = notification
        return notification
    
    async def get_by_id(self, notification_id: str) -> Notification | None:
        """Obtiene por ID."""
        return self._notifications.get(notification_id)
    
    async def get_all(self) -> list[Notification]:
        """Retorna todas."""
        return list(self._notifications.values())
    
    async def get_by_status(self, status: NotificationStatus) -> list[Notification]:
        """Filtra por estado."""
        return [
            n for n in self._notifications.values()
            if n.status == status
        ]
    
    async def delete(self, notification_id: str) -> bool:
        """Elimina si existe."""
        if notification_id in self._notifications:
            del self._notifications[notification_id]
            return True
        return False
    
    async def count(self) -> int:
        """Cuenta notificaciones."""
        return len(self._notifications)
    
    async def clear(self) -> None:
        """Limpia todo."""
        self._notifications.clear()
