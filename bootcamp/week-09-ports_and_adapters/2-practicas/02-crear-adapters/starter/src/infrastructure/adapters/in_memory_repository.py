"""
Adapter: InMemoryNotificationRepository

Implementación en memoria del NotificationRepository Protocol.
Útil para desarrollo y testing.
"""
from datetime import datetime

from src.domain.entities import Notification, NotificationStatus, NotificationChannel


# ============================================
# PASO 4: Implementar InMemoryNotificationRepository
# ============================================

# Descomenta las siguientes líneas:

# class InMemoryNotificationRepository:
#     """
#     Repositorio en memoria para notificaciones.
#     
#     Implementa NotificationRepository Protocol.
#     Los datos se pierden al reiniciar la aplicación.
#     """
#     
#     def __init__(self):
#         self._notifications: dict[int, Notification] = {}
#         self._next_id = 1
#     
#     async def save(self, notification: Notification) -> Notification:
#         """Guarda o actualiza una notificación."""
#         if notification.id is None:
#             notification.id = self._next_id
#             self._next_id += 1
#         
#         self._notifications[notification.id] = notification
#         return notification
#     
#     async def get_by_id(self, notification_id: int) -> Notification | None:
#         """Obtiene por ID."""
#         return self._notifications.get(notification_id)
#     
#     async def get_by_recipient(
#         self,
#         recipient: str,
#         limit: int = 100,
#         offset: int = 0
#     ) -> list[Notification]:
#         """Obtiene por destinatario."""
#         filtered = [
#             n for n in self._notifications.values()
#             if n.recipient == recipient
#         ]
#         return filtered[offset:offset + limit]
#     
#     async def get_by_status(
#         self,
#         status: NotificationStatus,
#         limit: int = 100
#     ) -> list[Notification]:
#         """Obtiene por estado."""
#         filtered = [
#             n for n in self._notifications.values()
#             if n.status == status
#         ]
#         return filtered[:limit]
#     
#     async def delete(self, notification_id: int) -> bool:
#         """Elimina una notificación."""
#         if notification_id in self._notifications:
#             del self._notifications[notification_id]
#             return True
#         return False
#     
#     # Métodos auxiliares para testing
#     
#     def clear(self) -> None:
#         """Limpia todos los datos."""
#         self._notifications.clear()
#         self._next_id = 1
#     
#     def count(self) -> int:
#         """Retorna el número de notificaciones."""
#         return len(self._notifications)


# Placeholder temporal
class InMemoryNotificationRepository:
    """Placeholder."""
    def __init__(self):
        self._notifications: dict[int, Notification] = {}
        self._next_id = 1
    
    async def save(self, notification: Notification) -> Notification:
        return notification
    
    async def get_by_id(self, notification_id: int) -> Notification | None:
        return None
    
    async def get_by_recipient(
        self, recipient: str, limit: int = 100, offset: int = 0
    ) -> list[Notification]:
        return []
    
    async def get_by_status(
        self, status: NotificationStatus, limit: int = 100
    ) -> list[Notification]:
        return []
    
    async def delete(self, notification_id: int) -> bool:
        return False
