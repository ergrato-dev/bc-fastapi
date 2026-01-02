# 🔗 Connection Manager

## 🎯 Objetivos

- Gestionar múltiples conexiones WebSocket simultáneas
- Implementar el patrón Connection Manager
- Crear salas (rooms) para agrupar conexiones
- Implementar broadcast y mensajes directos

---

## 1. El Problema: Múltiples Conexiones

### Sin Connection Manager

```python
# ❌ MAL - No escala, no hay forma de enviar a otros clientes
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Solo podemos responder al mismo cliente
        await websocket.send_text(f"Echo: {data}")
```

**Problemas:**
- No podemos enviar mensajes a otros clientes
- No sabemos quién está conectado
- No hay forma de hacer broadcast

### La Solución: Connection Manager

```python
# ✅ BIEN - Centraliza la gestión de conexiones
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
```

---

## 2. Connection Manager Básico

### Implementación Completa

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Any
import json

app = FastAPI()


class ConnectionManager:
    """
    Gestor de conexiones WebSocket.
    
    Mantiene una lista de conexiones activas y proporciona
    métodos para broadcast y mensajes directos.
    """
    
    def __init__(self):
        # Lista de conexiones activas
        self.active_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket) -> None:
        """Acepta y registra una nueva conexión."""
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket) -> None:
        """Elimina una conexión de la lista."""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
    
    async def send_personal_message(
        self, 
        message: str, 
        websocket: WebSocket
    ) -> None:
        """Envía mensaje a un cliente específico."""
        await websocket.send_text(message)
    
    async def send_personal_json(
        self, 
        data: dict[str, Any], 
        websocket: WebSocket
    ) -> None:
        """Envía JSON a un cliente específico."""
        await websocket.send_json(data)
    
    async def broadcast(self, message: str) -> None:
        """Envía mensaje a todos los clientes conectados."""
        for connection in self.active_connections:
            await connection.send_text(message)
    
    async def broadcast_json(self, data: dict[str, Any]) -> None:
        """Envía JSON a todos los clientes conectados."""
        for connection in self.active_connections:
            await connection.send_json(data)
    
    @property
    def connection_count(self) -> int:
        """Retorna el número de conexiones activas."""
        return len(self.active_connections)


# Instancia global del manager
manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    
    # Notificar a todos que alguien se conectó
    await manager.broadcast_json({
        "type": "user_joined",
        "user": client_id,
        "online_count": manager.connection_count
    })
    
    try:
        while True:
            data = await websocket.receive_text()
            
            # Broadcast del mensaje a todos
            await manager.broadcast_json({
                "type": "message",
                "user": client_id,
                "content": data
            })
    
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        
        # Notificar a todos que alguien se desconectó
        await manager.broadcast_json({
            "type": "user_left",
            "user": client_id,
            "online_count": manager.connection_count
        })
```

---

## 3. Connection Manager con Rooms

### Chat con Salas

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from collections import defaultdict
from typing import Any

app = FastAPI()


class RoomConnectionManager:
    """
    Gestor de conexiones con soporte para salas/rooms.
    
    Permite agrupar conexiones en salas independientes
    para broadcast segmentado.
    """
    
    def __init__(self):
        # Conexiones por sala: {"room_name": [websocket1, websocket2]}
        self.rooms: dict[str, list[WebSocket]] = defaultdict(list)
        
        # Mapeo inverso: websocket -> room (para cleanup)
        self.connection_room: dict[WebSocket, str] = {}
    
    async def connect(
        self, 
        websocket: WebSocket, 
        room: str
    ) -> None:
        """Conecta un cliente a una sala específica."""
        await websocket.accept()
        self.rooms[room].append(websocket)
        self.connection_room[websocket] = room
    
    def disconnect(self, websocket: WebSocket) -> str | None:
        """
        Desconecta un cliente y retorna la sala donde estaba.
        """
        room = self.connection_room.pop(websocket, None)
        if room and websocket in self.rooms[room]:
            self.rooms[room].remove(websocket)
            
            # Limpiar sala vacía
            if not self.rooms[room]:
                del self.rooms[room]
        
        return room
    
    async def broadcast_to_room(
        self, 
        room: str, 
        message: dict[str, Any]
    ) -> None:
        """Envía mensaje a todos los clientes de una sala."""
        if room in self.rooms:
            for connection in self.rooms[room]:
                await connection.send_json(message)
    
    async def send_personal(
        self, 
        websocket: WebSocket, 
        message: dict[str, Any]
    ) -> None:
        """Envía mensaje a un cliente específico."""
        await websocket.send_json(message)
    
    def get_room_users_count(self, room: str) -> int:
        """Retorna cantidad de usuarios en una sala."""
        return len(self.rooms.get(room, []))
    
    def get_all_rooms(self) -> list[str]:
        """Retorna lista de salas activas."""
        return list(self.rooms.keys())


# Instancia global
manager = RoomConnectionManager()


@app.websocket("/ws/{room}/{username}")
async def websocket_endpoint(
    websocket: WebSocket, 
    room: str, 
    username: str
):
    await manager.connect(websocket, room)
    
    # Notificar a la sala que alguien entró
    await manager.broadcast_to_room(room, {
        "type": "user_joined",
        "room": room,
        "user": username,
        "users_count": manager.get_room_users_count(room)
    })
    
    try:
        while True:
            data = await websocket.receive_json()
            
            # Broadcast solo a la sala
            await manager.broadcast_to_room(room, {
                "type": "message",
                "room": room,
                "user": username,
                "content": data.get("content", "")
            })
    
    except WebSocketDisconnect:
        left_room = manager.disconnect(websocket)
        
        if left_room:
            await manager.broadcast_to_room(left_room, {
                "type": "user_left",
                "room": left_room,
                "user": username,
                "users_count": manager.get_room_users_count(left_room)
            })
```

---

## 4. Connection Manager Avanzado

### Con Identificación de Usuarios

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
import asyncio

app = FastAPI()


@dataclass
class ConnectedUser:
    """Representa un usuario conectado."""
    user_id: str
    username: str
    websocket: WebSocket
    room: str
    connected_at: datetime = field(default_factory=datetime.now)
    
    async def send(self, message: dict[str, Any]) -> bool:
        """Envía mensaje al usuario. Retorna False si falla."""
        try:
            await self.websocket.send_json(message)
            return True
        except Exception:
            return False


class AdvancedConnectionManager:
    """
    Connection Manager avanzado con:
    - Identificación de usuarios
    - Múltiples salas
    - Mensajes privados
    - Lista de usuarios online
    """
    
    def __init__(self):
        # Usuarios por sala
        self.rooms: dict[str, dict[str, ConnectedUser]] = {}
        
        # Índice global de usuarios (para mensajes privados)
        self.users: dict[str, ConnectedUser] = {}
    
    async def connect(
        self,
        websocket: WebSocket,
        user_id: str,
        username: str,
        room: str
    ) -> ConnectedUser:
        """Conecta un usuario a una sala."""
        await websocket.accept()
        
        user = ConnectedUser(
            user_id=user_id,
            username=username,
            websocket=websocket,
            room=room
        )
        
        # Registrar en sala
        if room not in self.rooms:
            self.rooms[room] = {}
        self.rooms[room][user_id] = user
        
        # Registrar globalmente
        self.users[user_id] = user
        
        return user
    
    def disconnect(self, user_id: str) -> ConnectedUser | None:
        """Desconecta un usuario."""
        user = self.users.pop(user_id, None)
        
        if user:
            room = user.room
            if room in self.rooms:
                self.rooms[room].pop(user_id, None)
                
                # Limpiar sala vacía
                if not self.rooms[room]:
                    del self.rooms[room]
        
        return user
    
    async def broadcast_to_room(
        self,
        room: str,
        message: dict[str, Any],
        exclude_user: str | None = None
    ) -> None:
        """
        Broadcast a una sala.
        Opcionalmente excluye a un usuario (ej: el que envió).
        """
        if room not in self.rooms:
            return
        
        # Enviar en paralelo
        tasks = []
        for user_id, user in self.rooms[room].items():
            if user_id != exclude_user:
                tasks.append(user.send(message))
        
        if tasks:
            await asyncio.gather(*tasks)
    
    async def send_to_user(
        self,
        user_id: str,
        message: dict[str, Any]
    ) -> bool:
        """Envía mensaje privado a un usuario."""
        user = self.users.get(user_id)
        if user:
            return await user.send(message)
        return False
    
    def get_room_users(self, room: str) -> list[dict[str, Any]]:
        """Retorna lista de usuarios en una sala."""
        if room not in self.rooms:
            return []
        
        return [
            {
                "user_id": user.user_id,
                "username": user.username,
                "connected_at": user.connected_at.isoformat()
            }
            for user in self.rooms[room].values()
        ]
    
    def get_online_users(self) -> list[str]:
        """Retorna IDs de usuarios online."""
        return list(self.users.keys())
    
    def is_user_online(self, user_id: str) -> bool:
        """Verifica si un usuario está online."""
        return user_id in self.users


manager = AdvancedConnectionManager()


@app.websocket("/ws/chat/{room}")
async def chat_websocket(
    websocket: WebSocket,
    room: str,
    user_id: str,
    username: str
):
    """Endpoint de chat con salas."""
    
    user = await manager.connect(websocket, user_id, username, room)
    
    # Notificar entrada
    await manager.broadcast_to_room(room, {
        "type": "user_joined",
        "user_id": user_id,
        "username": username,
        "users": manager.get_room_users(room)
    })
    
    try:
        while True:
            data = await websocket.receive_json()
            message_type = data.get("type", "message")
            
            match message_type:
                case "message":
                    # Broadcast a la sala
                    await manager.broadcast_to_room(room, {
                        "type": "message",
                        "user_id": user_id,
                        "username": username,
                        "content": data.get("content", ""),
                        "timestamp": datetime.now().isoformat()
                    })
                
                case "private":
                    # Mensaje privado
                    target_id = data.get("to")
                    await manager.send_to_user(target_id, {
                        "type": "private",
                        "from_user_id": user_id,
                        "from_username": username,
                        "content": data.get("content", ""),
                        "timestamp": datetime.now().isoformat()
                    })
                
                case "typing":
                    # Notificar que está escribiendo
                    await manager.broadcast_to_room(room, {
                        "type": "typing",
                        "user_id": user_id,
                        "username": username
                    }, exclude_user=user_id)
    
    except WebSocketDisconnect:
        disconnected_user = manager.disconnect(user_id)
        
        if disconnected_user:
            await manager.broadcast_to_room(room, {
                "type": "user_left",
                "user_id": user_id,
                "username": username,
                "users": manager.get_room_users(room)
            })
```

---

## 5. Manejo de Errores en Broadcast

### Broadcast Seguro

```python
import asyncio
from typing import Any


class SafeConnectionManager:
    """Manager con manejo robusto de errores."""
    
    def __init__(self):
        self.connections: dict[str, WebSocket] = {}
    
    async def safe_send(
        self,
        websocket: WebSocket,
        message: dict[str, Any]
    ) -> bool:
        """
        Envía mensaje de forma segura.
        Retorna True si tuvo éxito.
        """
        try:
            await websocket.send_json(message)
            return True
        except Exception as e:
            # La conexión probablemente está cerrada
            return False
    
    async def broadcast(
        self,
        message: dict[str, Any],
        remove_failed: bool = True
    ) -> list[str]:
        """
        Broadcast con manejo de errores.
        
        Args:
            message: Mensaje a enviar
            remove_failed: Si True, elimina conexiones fallidas
            
        Returns:
            Lista de IDs de conexiones fallidas
        """
        failed_connections: list[str] = []
        
        # Crear tareas para envío paralelo
        async def send_to_connection(conn_id: str, ws: WebSocket):
            success = await self.safe_send(ws, message)
            if not success:
                failed_connections.append(conn_id)
        
        # Ejecutar en paralelo
        tasks = [
            send_to_connection(conn_id, ws)
            for conn_id, ws in self.connections.items()
        ]
        
        await asyncio.gather(*tasks)
        
        # Limpiar conexiones fallidas
        if remove_failed:
            for conn_id in failed_connections:
                self.connections.pop(conn_id, None)
        
        return failed_connections
```

---

## 6. Patrón Singleton para el Manager

### Manager como Dependencia

```python
from fastapi import FastAPI, WebSocket, Depends
from functools import lru_cache


class ConnectionManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connections = []
        return cls._instance
    
    # ... métodos del manager


# Como dependencia de FastAPI
@lru_cache
def get_connection_manager() -> ConnectionManager:
    """Retorna la instancia singleton del manager."""
    return ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    manager: ConnectionManager = Depends(get_connection_manager)
):
    await manager.connect(websocket)
    # ...
```

---

## ✅ Resumen

| Concepto | Descripción |
|----------|-------------|
| **Connection Manager** | Patrón para gestionar múltiples WebSockets |
| **Broadcast** | Enviar mensaje a todas las conexiones |
| **Rooms/Channels** | Agrupar conexiones por sala |
| **Personal Message** | Enviar a un cliente específico |
| **Safe Broadcast** | Broadcast con manejo de errores |

**Próximo:** Server-Sent Events para streaming unidireccional.
