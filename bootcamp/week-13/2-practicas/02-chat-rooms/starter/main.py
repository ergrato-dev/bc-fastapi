"""
Práctica 02: Chat Rooms
======================

Sistema de chat con múltiples salas usando WebSocket
y Connection Manager.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Chat Rooms")

templates = Jinja2Templates(directory="templates")


# ============================================
# PASO 1: Importar el manager
# ============================================
print("--- Paso 1: Importar manager ---")

# Importar el Connection Manager
# Descomenta las siguientes líneas:

# from manager import (
#     manager,
#     create_chat_message,
#     create_system_message,
#     create_user_list_message
# )


# ============================================
# PASO 2: Endpoint para servir el cliente
# ============================================
print("--- Paso 2: Servir cliente HTML ---")

# Endpoint para la página principal
# Descomenta las siguientes líneas:

# @app.get("/", response_class=HTMLResponse)
# async def get_chat(request: Request):
#     """Sirve el cliente de chat."""
#     return templates.TemplateResponse(
#         "chat.html",
#         {"request": request}
#     )


# ============================================
# PASO 3: WebSocket endpoint para chat
# ============================================
print("--- Paso 3: WebSocket endpoint ---")

# Endpoint principal de chat con rooms
# Descomenta las siguientes líneas:

# @app.websocket("/ws/{room}/{username}")
# async def websocket_chat(
#     websocket: WebSocket,
#     room: str,
#     username: str
# ):
#     """
#     WebSocket para chat en salas.
#     
#     Args:
#         room: Nombre de la sala
#         username: Nombre del usuario
#     """
#     # Conectar usuario a la sala
#     await manager.connect(websocket, room, username)
#     
#     # Enviar mensaje de bienvenida al usuario
#     await manager.send_to_user(websocket, {
#         "type": "welcome",
#         "room": room,
#         "username": username,
#         "users": manager.get_room_users(room)
#     })
#     
#     # Notificar a la sala que alguien entró
#     await manager.broadcast_to_room(
#         room,
#         create_system_message("user_joined", {
#             "username": username,
#             "room": room,
#             "users_count": manager.get_room_count(room)
#         }),
#         exclude=websocket  # No enviar al mismo usuario
#     )
#     
#     # Enviar lista actualizada de usuarios a todos
#     await manager.broadcast_to_room(
#         room,
#         create_user_list_message(room, manager.get_room_users(room))
#     )
#     
#     try:
#         while True:
#             # Recibir mensaje del cliente
#             data = await websocket.receive_json()
#             
#             message_type = data.get("type", "message")
#             
#             match message_type:
#                 case "message":
#                     # Broadcast del mensaje a la sala
#                     content = data.get("content", "")
#                     await manager.broadcast_to_room(
#                         room,
#                         create_chat_message(username, content, room)
#                     )
#                 
#                 case "typing":
#                     # Notificar que está escribiendo
#                     await manager.broadcast_to_room(
#                         room,
#                         {
#                             "type": "typing",
#                             "username": username,
#                             "room": room
#                         },
#                         exclude=websocket
#                     )
#                 
#                 case "get_users":
#                     # Enviar lista de usuarios
#                     await manager.send_to_user(
#                         websocket,
#                         create_user_list_message(room, manager.get_room_users(room))
#                     )
#     
#     except WebSocketDisconnect:
#         # Desconectar usuario
#         info = manager.disconnect(websocket)
#         
#         if info:
#             room, username = info
#             
#             # Notificar a la sala que alguien salió
#             await manager.broadcast_to_room(
#                 room,
#                 create_system_message("user_left", {
#                     "username": username,
#                     "room": room,
#                     "users_count": manager.get_room_count(room)
#                 })
#             )
#             
#             # Actualizar lista de usuarios
#             await manager.broadcast_to_room(
#                 room,
#                 create_user_list_message(room, manager.get_room_users(room))
#             )


# ============================================
# PASO 4: Endpoints HTTP auxiliares
# ============================================
print("--- Paso 4: Endpoints HTTP ---")

# Endpoints para info de salas y usuarios
# Descomenta las siguientes líneas:

# @app.get("/api/rooms")
# async def get_rooms():
#     """Retorna lista de salas activas."""
#     return {
#         "rooms": manager.get_all_rooms()
#     }
# 
# 
# @app.get("/api/rooms/{room}/users")
# async def get_room_users(room: str):
#     """Retorna usuarios de una sala."""
#     return {
#         "room": room,
#         "users": manager.get_room_users(room),
#         "count": manager.get_room_count(room)
#     }


# ============================================
# Punto de entrada
# ============================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
