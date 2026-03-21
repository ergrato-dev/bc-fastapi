"""
Adapter: InMemoryNotificationRepository

Implementación de NotificationRepository que almacena en memoria.
"""
from src.domain.entities.notification import Notification, NotificationStatus
from src.domain.ports.notification_repository import NotificationRepository


class InMemoryNotificationRepository:
    """
    Adapter que almacena notificaciones en memoria.
    
    Implementa el Protocol NotificationRepository.
    Ideal para desarrollo, testing y prototipos.
    
    En producción se reemplazaría por SQLAlchemyNotificationRepository
    o similar sin cambiar el resto de la aplicación.
    
    TODO: Implementa todos los métodos del Protocol.
    """
    
    def __init__(self):
        """Inicializa el almacenamiento en memoria."""
        self._notifications: dict[str, Notification] = {}
    
    async def save(self, notification: Notification) -> Notification:
        """
        Guarda o actualiza una notificación.
        
        Args:
            notification: Notificación a guardar
            
        Returns:
            La misma notificación (ya guardada)
            
        TODO: Implementar guardando en self._notifications usando notification.id como key.
        """
        # TODO: Implementar
        pass
    
    async def get_by_id(self, notification_id: str) -> Notification | None:
        """
        Obtiene una notificación por ID.
        
        Args:
            notification_id: ID a buscar
            
        Returns:
            La notificación o None si no existe
            
        TODO: Implementar buscando en self._notifications.
        """
        # TODO: Implementar
        pass
    
    async def get_all(self) -> list[Notification]:
        """
        Obtiene todas las notificaciones.
        
        Returns:
            Lista de todas las notificaciones
            
        TODO: Implementar retornando todos los valores.
        """
        # TODO: Implementar
        pass
    
    async def get_by_status(self, status: NotificationStatus) -> list[Notification]:
        """
        Obtiene notificaciones por estado.
        
        Args:
            status: Estado a filtrar
            
        Returns:
            Lista de notificaciones con ese estado
            
        TODO: Implementar filtrando por notification.status.
        """
        # TODO: Implementar
        pass
    
    async def delete(self, notification_id: str) -> bool:
        """
        Elimina una notificación.
        
        Args:
            notification_id: ID a eliminar
            
        Returns:
            True si existía y se eliminó, False si no existía
            
        TODO: Implementar usando pop() del diccionario.
        """
        # TODO: Implementar
        pass
    
    async def count(self) -> int:
        """
        Cuenta el total de notificaciones.
        
        Returns:
            Número de notificaciones almacenadas
            
        TODO: Implementar retornando len() del diccionario.
        """
        # TODO: Implementar
        pass
    
    async def clear(self) -> None:
        """
        Elimina todas las notificaciones.
        
        Útil para testing.
        """
        self._notifications.clear()
