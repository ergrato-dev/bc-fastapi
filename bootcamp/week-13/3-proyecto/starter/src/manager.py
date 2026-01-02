"""
Connection Manager para WebSocket.

TODO: Completar la clase ConnectionManager
"""

from fastapi import WebSocket
from typing import Any
from datetime import datetime
from collections import defaultdict


class ConnectionManager:
    """
    Gestor de conexiones WebSocket con soporte para salas.
    
    TODO: Implementar todos los métodos marcados
    """
    
    def __init__(self):
        # Conexiones por sala: {room_id: [(websocket, user_id, username), ...]}
        self.rooms: dict[int, list[tuple[WebSocket, int, str]]] = defaultdict(list)
        
        # Mapeo inverso para cleanup: {websocket: (room_id, user_id, username)}
        self.connections: dict[WebSocket, tuple[int, int, str]] = {}
    
    async def connect(
        self,
        websocket: WebSocket,
        room_id: int,
        user_id: int,
        username: str
    ) -> None:
        """
        Conecta un usuario a una sala.
        
        TODO: Implementar
        
        Args:
            websocket: Conexión WebSocket
            room_id: ID de la sala
            user_id: ID del usuario
            username: Nombre del usuario
        """
        # TODO: Implementar
        # 1. Aceptar conexión
        # 2. Registrar en self.rooms
        # 3. Registrar en self.connections
        pass
    
    def disconnect(self, websocket: WebSocket) -> tuple[int, int, str] | None:
        """
        Desconecta un usuario.
        
        TODO: Implementar
        
        Returns:
            Tupla (room_id, user_id, username) o None
        """
        # TODO: Implementar
        # 1. Obtener info de self.connections
        # 2. Remover de self.rooms
        # 3. Remover de self.connections
        # 4. Limpiar sala si está vacía
        # 5. Retornar info
        pass
    
    async def send_personal(
        self,
        websocket: WebSocket,
        message: dict[str, Any]
    ) -> None:
        """
        Envía mensaje a un usuario específico.
        
        TODO: Implementar
        """
        # TODO: Implementar
        pass
    
    async def broadcast_to_room(
        self,
        room_id: int,
        message: dict[str, Any],
        exclude: WebSocket | None = None
    ) -> None:
        """
        Envía mensaje a todos los usuarios de una sala.
        
        TODO: Implementar
        
        Args:
            room_id: ID de la sala
            message: Mensaje a enviar
            exclude: WebSocket a excluir (opcional)
        """
        # TODO: Implementar
        # 1. Iterar sobre conexiones de la sala
        # 2. Excluir websocket si se especifica
        # 3. Enviar mensaje JSON a cada uno
        pass
    
    def get_room_users(self, room_id: int) -> list[dict[str, Any]]:
        """
        Retorna lista de usuarios conectados a una sala.
        
        TODO: Implementar
        
        Returns:
            Lista de dicts con user_id y username
        """
        # TODO: Implementar
        pass
    
    def get_room_usernames(self, room_id: int) -> list[str]:
        """
        Retorna lista de usernames en una sala.
        
        TODO: Implementar
        """
        # TODO: Implementar
        pass
    
    def get_user_count(self, room_id: int) -> int:
        """Retorna cantidad de usuarios en una sala."""
        return len(self.rooms.get(room_id, []))
    
    def is_user_in_room(self, room_id: int, user_id: int) -> bool:
        """Verifica si un usuario está en una sala."""
        for _, uid, _ in self.rooms.get(room_id, []):
            if uid == user_id:
                return True
        return False


# Instancia global
manager = ConnectionManager()


# ============================================
# Helpers para mensajes
# ============================================

def create_chat_message(
    user_id: int,
    username: str,
    content: str,
    message_id: int | None = None
) -> dict[str, Any]:
    """Crea un mensaje de chat formateado."""
    return {
        "type": "message",
        "user_id": user_id,
        "username": username,
        "content": content,
        "message_id": message_id,
        "timestamp": datetime.utcnow().isoformat()
    }


def create_system_message(event: str, data: dict[str, Any]) -> dict[str, Any]:
    """Crea un mensaje del sistema."""
    return {
        "type": "system",
        "event": event,
        "data": data,
        "timestamp": datetime.utcnow().isoformat()
    }


def create_user_list_message(room_id: int, users: list[str]) -> dict[str, Any]:
    """Crea mensaje con lista de usuarios."""
    return {
        "type": "user_list",
        "room_id": room_id,
        "users": users,
        "count": len(users),
        "timestamp": datetime.utcnow().isoformat()
    }
