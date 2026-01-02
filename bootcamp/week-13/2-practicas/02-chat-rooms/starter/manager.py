"""
Connection Manager con soporte para Rooms
=========================================

Este módulo implementa la gestión de conexiones WebSocket
con soporte para múltiples salas de chat.
"""

from fastapi import WebSocket
from typing import Any
from datetime import datetime
from collections import defaultdict


# ============================================
# PASO 1: Connection Manager básico
# ============================================
print("--- Paso 1: Connection Manager básico ---")

# Implementación básica sin rooms
# Descomenta las siguientes líneas:

# class SimpleConnectionManager:
#     """
#     Gestor de conexiones simple (sin rooms).
#     
#     Mantiene una lista de conexiones activas
#     y permite broadcast a todos.
#     """
#     
#     def __init__(self):
#         self.active_connections: list[WebSocket] = []
#     
#     async def connect(self, websocket: WebSocket) -> None:
#         """Acepta y registra una conexión."""
#         await websocket.accept()
#         self.active_connections.append(websocket)
#     
#     def disconnect(self, websocket: WebSocket) -> None:
#         """Elimina una conexión de la lista."""
#         if websocket in self.active_connections:
#             self.active_connections.remove(websocket)
#     
#     async def broadcast(self, message: dict[str, Any]) -> None:
#         """Envía mensaje a todas las conexiones."""
#         for connection in self.active_connections:
#             try:
#                 await connection.send_json(message)
#             except Exception:
#                 # La conexión puede estar cerrada
#                 pass
#     
#     @property
#     def count(self) -> int:
#         """Número de conexiones activas."""
#         return len(self.active_connections)


# ============================================
# PASO 2: Connection Manager con Rooms
# ============================================
print("--- Paso 2: Connection Manager con Rooms ---")

# Implementación completa con soporte para salas
# Descomenta las siguientes líneas:

# class RoomConnectionManager:
#     """
#     Gestor de conexiones con soporte para salas.
#     
#     Permite agrupar conexiones en rooms para
#     broadcast segmentado.
#     """
#     
#     def __init__(self):
#         # Conexiones por sala: {"room": [(websocket, username), ...]}
#         self.rooms: dict[str, list[tuple[WebSocket, str]]] = defaultdict(list)
#         
#         # Mapeo inverso para cleanup rápido
#         self.connection_info: dict[WebSocket, tuple[str, str]] = {}
#     
#     async def connect(
#         self,
#         websocket: WebSocket,
#         room: str,
#         username: str
#     ) -> None:
#         """
#         Conecta un usuario a una sala.
#         
#         Args:
#             websocket: Conexión WebSocket
#             room: Nombre de la sala
#             username: Nombre del usuario
#         """
#         await websocket.accept()
#         
#         # Registrar en la sala
#         self.rooms[room].append((websocket, username))
#         
#         # Guardar info para cleanup
#         self.connection_info[websocket] = (room, username)
#     
#     def disconnect(self, websocket: WebSocket) -> tuple[str, str] | None:
#         """
#         Desconecta un usuario.
#         
#         Returns:
#             Tupla (room, username) del usuario desconectado
#         """
#         info = self.connection_info.pop(websocket, None)
#         
#         if info:
#             room, username = info
#             
#             # Remover de la sala
#             self.rooms[room] = [
#                 (ws, user) for ws, user in self.rooms[room]
#                 if ws != websocket
#             ]
#             
#             # Limpiar sala vacía
#             if not self.rooms[room]:
#                 del self.rooms[room]
#             
#             return info
#         
#         return None
#     
#     async def broadcast_to_room(
#         self,
#         room: str,
#         message: dict[str, Any],
#         exclude: WebSocket | None = None
#     ) -> None:
#         """
#         Envía mensaje a todos los usuarios de una sala.
#         
#         Args:
#             room: Nombre de la sala
#             message: Mensaje a enviar
#             exclude: WebSocket a excluir (opcional)
#         """
#         if room not in self.rooms:
#             return
#         
#         for websocket, _ in self.rooms[room]:
#             if websocket != exclude:
#                 try:
#                     await websocket.send_json(message)
#                 except Exception:
#                     pass
#     
#     async def send_to_user(
#         self,
#         websocket: WebSocket,
#         message: dict[str, Any]
#     ) -> None:
#         """Envía mensaje a un usuario específico."""
#         try:
#             await websocket.send_json(message)
#         except Exception:
#             pass
#     
#     def get_room_users(self, room: str) -> list[str]:
#         """Retorna lista de usuarios en una sala."""
#         return [username for _, username in self.rooms.get(room, [])]
#     
#     def get_room_count(self, room: str) -> int:
#         """Retorna cantidad de usuarios en una sala."""
#         return len(self.rooms.get(room, []))
#     
#     def get_all_rooms(self) -> list[dict[str, Any]]:
#         """Retorna info de todas las salas activas."""
#         return [
#             {
#                 "name": room,
#                 "users_count": len(users),
#                 "users": [user for _, user in users]
#             }
#             for room, users in self.rooms.items()
#         ]


# ============================================
# PASO 3: Instancia global del manager
# ============================================
print("--- Paso 3: Instancia global ---")

# Crear la instancia que usará la aplicación
# Descomenta la siguiente línea:

# manager = RoomConnectionManager()


# ============================================
# PASO 4: Helpers para mensajes
# ============================================
print("--- Paso 4: Helpers para mensajes ---")

# Funciones helper para crear mensajes estructurados
# Descomenta las siguientes líneas:

# def create_chat_message(
#     username: str,
#     content: str,
#     room: str
# ) -> dict[str, Any]:
#     """Crea un mensaje de chat."""
#     return {
#         "type": "message",
#         "username": username,
#         "content": content,
#         "room": room,
#         "timestamp": datetime.now().isoformat()
#     }
# 
# 
# def create_system_message(
#     event: str,
#     data: dict[str, Any]
# ) -> dict[str, Any]:
#     """Crea un mensaje del sistema."""
#     return {
#         "type": "system",
#         "event": event,
#         "data": data,
#         "timestamp": datetime.now().isoformat()
#     }
# 
# 
# def create_user_list_message(
#     room: str,
#     users: list[str]
# ) -> dict[str, Any]:
#     """Crea mensaje con lista de usuarios."""
#     return {
#         "type": "user_list",
#         "room": room,
#         "users": users,
#         "count": len(users),
#         "timestamp": datetime.now().isoformat()
#     }
