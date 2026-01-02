# 💬 Práctica 02: Chat Rooms

## 🎯 Objetivo

Implementar un sistema de chat con múltiples salas usando Connection Manager. Los usuarios pueden unirse a salas, enviar mensajes y ver quién está conectado.

---

## 📋 Requisitos Previos

- Práctica 01: WebSocket Básico
- Teoría 03: Connection Manager

---

## 🗂️ Estructura

```
02-chat-rooms/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py              # Servidor con Connection Manager
    ├── manager.py           # Connection Manager con rooms
    └── templates/
        └── chat.html        # Cliente de chat
```

---

## 📝 Instrucciones

### Paso 1: Connection Manager básico

Abre `starter/manager.py` y descomenta la sección del **Paso 1**.

Implementarás la clase `ConnectionManager` con:
- Lista de conexiones activas
- Métodos `connect()` y `disconnect()`
- Método `broadcast()`

### Paso 2: Soporte para Rooms

Descomenta la sección del **Paso 2** en `manager.py`.

Agregarás:
- Diccionario de salas
- Método `join_room()`
- Método `leave_room()`
- Método `broadcast_to_room()`

### Paso 3: Endpoint WebSocket

Abre `starter/main.py` y descomenta el **Paso 3**.

Crearás el endpoint `/ws/{room}/{username}` que:
- Une al usuario a la sala
- Notifica a otros usuarios
- Procesa mensajes
- Maneja desconexiones

### Paso 4: Lista de usuarios

Descomenta el **Paso 4** para agregar:
- Lista de usuarios por sala
- Endpoint HTTP para ver usuarios
- Notificaciones de join/leave

### Paso 5: Cliente HTML

El cliente `templates/chat.html` ya está listo. Descomenta el endpoint que lo sirve.

---

## ✅ Verificación

1. Ejecuta el servidor:
```bash
cd starter
uv sync
uv run fastapi dev main.py
```

2. Abre dos pestañas en http://localhost:8000

3. Prueba:
   - Unirse a la misma sala con diferentes usuarios
   - Enviar mensajes (deben verse en ambas pestañas)
   - Cambiar de sala
   - Ver lista de usuarios conectados

---

## 🎯 Criterios de Éxito

- [ ] Connection Manager gestiona conexiones
- [ ] Usuarios pueden unirse a salas
- [ ] Mensajes se envían solo a la sala correcta
- [ ] Lista de usuarios actualizada
- [ ] Notificaciones de join/leave funcionan
