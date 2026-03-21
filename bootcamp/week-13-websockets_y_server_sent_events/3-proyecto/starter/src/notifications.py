"""
Servicio de notificaciones con SSE.

TODO: Completar el servicio de notificaciones
"""

import asyncio
from typing import Any, AsyncGenerator
from datetime import datetime
from collections import defaultdict


class NotificationService:
    """
    Servicio de notificaciones SSE.
    
    TODO: Implementar los métodos marcados
    """
    
    def __init__(self):
        # Cola de notificaciones por usuario
        self.queues: dict[int, asyncio.Queue] = defaultdict(asyncio.Queue)
        
        # Set de usuarios suscritos
        self.subscribers: set[int] = set()
    
    async def subscribe(
        self,
        user_id: int,
        keepalive_seconds: int = 30
    ) -> AsyncGenerator[dict[str, Any], None]:
        """
        Suscribe a un usuario y genera eventos SSE.
        
        TODO: Implementar
        
        Args:
            user_id: ID del usuario
            keepalive_seconds: Intervalo de keepalive
            
        Yields:
            Eventos SSE
        """
        # TODO: Implementar
        # 1. Registrar suscriptor
        # 2. Loop infinito con wait_for y timeout
        # 3. Yield eventos o keepalive
        # 4. Cleanup en finally
        pass
    
    async def notify_user(
        self,
        user_id: int,
        event_type: str,
        data: dict[str, Any]
    ) -> bool:
        """
        Envía notificación a un usuario.
        
        TODO: Implementar
        """
        # TODO: Implementar
        pass
    
    async def broadcast(
        self,
        event_type: str,
        data: dict[str, Any]
    ) -> int:
        """
        Envía notificación a todos los suscriptores.
        
        TODO: Implementar
        
        Returns:
            Número de usuarios notificados
        """
        # TODO: Implementar
        pass
    
    async def notify_new_message(
        self,
        room_id: int,
        room_name: str,
        username: str,
        content: str
    ) -> int:
        """Notifica nuevo mensaje en una sala."""
        return await self.broadcast(
            "new_message",
            {
                "room_id": room_id,
                "room_name": room_name,
                "username": username,
                "preview": content[:50] + "..." if len(content) > 50 else content
            }
        )
    
    async def notify_user_joined(
        self,
        room_id: int,
        room_name: str,
        username: str
    ) -> int:
        """Notifica que un usuario se unió a una sala."""
        return await self.broadcast(
            "user_joined",
            {
                "room_id": room_id,
                "room_name": room_name,
                "username": username
            }
        )
    
    async def notify_user_left(
        self,
        room_id: int,
        room_name: str,
        username: str
    ) -> int:
        """Notifica que un usuario salió de una sala."""
        return await self.broadcast(
            "user_left",
            {
                "room_id": room_id,
                "room_name": room_name,
                "username": username
            }
        )
    
    def get_subscribers_count(self) -> int:
        """Retorna número de suscriptores."""
        return len(self.subscribers)


# Instancia global
notification_service = NotificationService()
