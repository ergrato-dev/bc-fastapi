"""
NotificationService - Servicio de aplicación.

Coordina el envío de notificaciones usando los ports definidos.
"""
from src.domain.entities.notification import (
    Notification,
    NotificationChannel,
    NotificationStatus,
)
from src.domain.ports.notification_sender import NotificationSender
from src.domain.ports.notification_repository import NotificationRepository


class NotificationService:
    """
    Servicio de aplicación para gestionar notificaciones.
    
    Este servicio:
    - Depende SOLO de abstracciones (Ports/Protocols)
    - Coordina el flujo de envío de notificaciones
    - Es fácil de testear con fakes/mocks
    
    TODO: Implementa los métodos marcados con TODO
    """
    
    def __init__(
        self,
        senders: dict[NotificationChannel, NotificationSender],
        repository: NotificationRepository,
    ):
        """
        Inicializa el servicio con sus dependencias.
        
        Args:
            senders: Diccionario de senders por canal
            repository: Repositorio para persistencia
        """
        self._senders = senders
        self._repository = repository
    
    async def send_notification(
        self,
        recipient: str,
        channel: NotificationChannel,
        message: str,
        subject: str | None = None,
        metadata: dict | None = None,
    ) -> Notification:
        """
        Envía una notificación.
        
        Args:
            recipient: Destinatario
            channel: Canal de envío
            message: Mensaje a enviar
            subject: Asunto (opcional)
            metadata: Datos adicionales (opcional)
            
        Returns:
            Notificación creada con su estado actualizado
            
        Raises:
            ValueError: Si el canal no está soportado
            
        TODO: Implementa este método:
        1. Crear la entidad Notification
        2. Guardar en el repositorio con estado PENDING
        3. Obtener el sender correspondiente al canal
        4. Enviar la notificación
        5. Actualizar el estado según resultado (SENT o FAILED)
        6. Guardar el estado actualizado
        7. Retornar la notificación
        """
        # TODO: Implementar
        pass
    
    async def send_batch(
        self,
        notifications_data: list[dict],
    ) -> list[Notification]:
        """
        Envía múltiples notificaciones.
        
        Args:
            notifications_data: Lista de dicts con datos de cada notificación
            
        Returns:
            Lista de notificaciones con sus estados
            
        TODO: Implementa este método usando send_notification para cada una.
        """
        # TODO: Implementar
        pass
    
    async def get_notification(self, notification_id: str) -> Notification | None:
        """
        Obtiene una notificación por ID.
        
        Args:
            notification_id: ID de la notificación
            
        Returns:
            La notificación o None si no existe
            
        TODO: Implementar usando el repositorio.
        """
        # TODO: Implementar
        pass
    
    async def get_all_notifications(self) -> list[Notification]:
        """
        Obtiene todas las notificaciones.
        
        Returns:
            Lista de todas las notificaciones
            
        TODO: Implementar usando el repositorio.
        """
        # TODO: Implementar
        pass
    
    async def get_by_status(
        self,
        status: NotificationStatus,
    ) -> list[Notification]:
        """
        Obtiene notificaciones por estado.
        
        Args:
            status: Estado a filtrar
            
        Returns:
            Lista de notificaciones con ese estado
            
        TODO: Implementar usando el repositorio.
        """
        # TODO: Implementar
        pass
    
    async def retry_failed(self) -> list[Notification]:
        """
        Reintenta enviar notificaciones fallidas.
        
        Returns:
            Lista de notificaciones reintentadas
            
        TODO: Implementar:
        1. Obtener notificaciones con estado FAILED
        2. Reintentar envío de cada una
        3. Retornar la lista actualizada
        """
        # TODO: Implementar
        pass
    
    async def delete_notification(self, notification_id: str) -> bool:
        """
        Elimina una notificación.
        
        Args:
            notification_id: ID de la notificación a eliminar
            
        Returns:
            True si se eliminó, False si no existía
            
        TODO: Implementar usando el repositorio.
        """
        # TODO: Implementar
        pass
    
    def get_available_channels(self) -> list[NotificationChannel]:
        """
        Obtiene los canales disponibles.
        
        Returns:
            Lista de canales con sender configurado
        """
        return list(self._senders.keys())
    
    def has_channel(self, channel: NotificationChannel) -> bool:
        """Verifica si un canal está disponible."""
        return channel in self._senders
