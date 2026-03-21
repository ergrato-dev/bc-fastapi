"""
Port: NotificationSender

Define el contrato para enviar notificaciones.
"""
from typing import Protocol

from src.domain.entities.notification import Notification, NotificationChannel


class NotificationSender(Protocol):
    """
    Puerto para envío de notificaciones.
    
    Los adaptadores que implementen este puerto deben proveer
    la capacidad de enviar notificaciones a través de un canal específico.
    
    TODO: Implementa este Protocol con las siguientes propiedades y métodos:
    
    Propiedades:
    - channel: NotificationChannel (el canal que maneja este sender)
    
    Métodos:
    - async def send(notification: Notification) -> bool
      Envía una notificación individual. Retorna True si fue exitoso.
    
    - async def send_batch(notifications: list[Notification]) -> dict[str, bool]
      Envía múltiples notificaciones. Retorna dict con id -> resultado.
    """
    
    @property
    def channel(self) -> NotificationChannel:
        """Canal que maneja este sender."""
        ...
    
    async def send(self, notification: Notification) -> bool:
        """
        Envía una notificación.
        
        Args:
            notification: Notificación a enviar
            
        Returns:
            True si se envió correctamente, False si falló
        """
        ...
    
    async def send_batch(self, notifications: list[Notification]) -> dict[str, bool]:
        """
        Envía múltiples notificaciones.
        
        Args:
            notifications: Lista de notificaciones a enviar
            
        Returns:
            Diccionario {notification_id: success_status}
        """
        ...
