"""InMemoryNotificationRepository - repositorio en memoria."""
from src.domain.entities import Notification, NotificationStatus


class InMemoryNotificationRepository:
    """Repositorio en memoria."""
    
    def __init__(self):
        self._data: dict[int, Notification] = {}
        self._next_id = 1
    
    async def save(self, notification: Notification) -> Notification:
        if notification.id is None:
            notification.id = self._next_id
            self._next_id += 1
        self._data[notification.id] = notification
        return notification
    
    async def get_by_id(self, notification_id: int) -> Notification | None:
        return self._data.get(notification_id)
    
    async def get_by_status(
        self, status: NotificationStatus, limit: int = 100
    ) -> list[Notification]:
        return [n for n in self._data.values() if n.status == status][:limit]
