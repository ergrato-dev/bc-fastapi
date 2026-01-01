"""
FakeNotificationRepository - Fake para testing.

Este fake implementa el Protocol NotificationRepository
con almacenamiento en memoria.
"""
from src.domain.entities import Notification, NotificationStatus


# ============================================
# PASO 1: Implementar FakeNotificationRepository
# ============================================
# Este fake almacena datos en memoria para tests rápidos.

# Descomenta las siguientes líneas:

# class FakeNotificationRepository:
#     """
#     Fake repository para testing.
#     
#     Almacena notificaciones en memoria.
#     Implementa NotificationRepository Protocol.
#     """
#     
#     def __init__(self):
#         self._data: dict[int, Notification] = {}
#         self._next_id = 1
#     
#     async def save(self, notification: Notification) -> Notification:
#         """Guarda en memoria."""
#         if notification.id is None:
#             notification.id = self._next_id
#             self._next_id += 1
#         self._data[notification.id] = notification
#         return notification
#     
#     async def get_by_id(self, notification_id: int) -> Notification | None:
#         """Obtiene de memoria."""
#         return self._data.get(notification_id)
#     
#     async def get_by_status(
#         self,
#         status: NotificationStatus,
#         limit: int = 100
#     ) -> list[Notification]:
#         """Filtra por status."""
#         return [
#             n for n in self._data.values()
#             if n.status == status
#         ][:limit]
#     
#     # Métodos de ayuda para tests
#     
#     def clear(self) -> None:
#         """Limpia todos los datos."""
#         self._data.clear()
#         self._next_id = 1
#     
#     def count(self) -> int:
#         """Retorna cantidad de notificaciones."""
#         return len(self._data)
#     
#     def get_all(self) -> list[Notification]:
#         """Retorna todas las notificaciones."""
#         return list(self._data.values())


# Placeholder temporal
class FakeNotificationRepository:
    """Placeholder."""
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
    
    async def get_by_status(self, status: NotificationStatus, limit: int = 100) -> list[Notification]:
        return [n for n in self._data.values() if n.status == status][:limit]
    
    def clear(self) -> None:
        self._data.clear()
        self._next_id = 1
    
    def count(self) -> int:
        return len(self._data)
