"""
Port: NotificationRepository

Define el contrato para persistir notificaciones.
"""
from typing import Protocol

from src.domain.entities.notification import Notification, NotificationStatus


class NotificationRepository(Protocol):
    """
    Puerto para persistencia de notificaciones.
    
    TODO: Implementa este Protocol con los siguientes métodos:
    
    - async def save(notification: Notification) -> Notification
      Guarda una notificación (crea o actualiza).
    
    - async def get_by_id(notification_id: str) -> Notification | None
      Obtiene una notificación por su ID.
    
    - async def get_all() -> list[Notification]
      Obtiene todas las notificaciones.
    
    - async def get_by_status(status: NotificationStatus) -> list[Notification]
      Obtiene notificaciones por estado.
    
    - async def delete(notification_id: str) -> bool
      Elimina una notificación. Retorna True si existía.
    
    - async def count() -> int
      Cuenta el total de notificaciones.
    """
    
    async def save(self, notification: Notification) -> Notification:
        """Guarda o actualiza una notificación."""
        ...
    
    async def get_by_id(self, notification_id: str) -> Notification | None:
        """Obtiene una notificación por ID."""
        ...
    
    async def get_all(self) -> list[Notification]:
        """Obtiene todas las notificaciones."""
        ...
    
    async def get_by_status(self, status: NotificationStatus) -> list[Notification]:
        """Obtiene notificaciones filtradas por estado."""
        ...
    
    async def delete(self, notification_id: str) -> bool:
        """Elimina una notificación."""
        ...
    
    async def count(self) -> int:
        """Cuenta el total de notificaciones."""
        ...
