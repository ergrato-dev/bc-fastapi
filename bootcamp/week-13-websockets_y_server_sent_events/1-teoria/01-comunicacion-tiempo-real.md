# 📡 Comunicación en Tiempo Real

## 🎯 Objetivos

- Entender las limitaciones del modelo HTTP tradicional
- Conocer las diferencias entre HTTP, WebSocket y SSE
- Identificar casos de uso para cada tecnología
- Comprender el concepto de comunicación bidireccional

---

## 1. El Problema del HTTP Tradicional

### Modelo Request-Response

HTTP fue diseñado como un protocolo **sin estado** y **unidireccional**:

```
Cliente                    Servidor
   |                          |
   |-------- Request -------->|
   |                          |
   |<------- Response --------|
   |                          |
   |-------- Request -------->|
   |                          |
   |<------- Response --------|
```

**Limitaciones:**

1. **El servidor no puede iniciar comunicación** - Solo responde a requests
2. **Overhead de conexión** - Cada request abre/cierra conexión (sin keep-alive)
3. **Headers repetidos** - Cada request incluye headers completos
4. **Latencia** - Esperar respuesta antes de nuevo request

### Soluciones Tradicionales (Workarounds)

#### Polling (Sondeo)

```python
# El cliente pregunta repetidamente
import time
import httpx

while True:
    response = httpx.get("/api/notifications")
    if response.json()["has_new"]:
        process_notifications(response.json()["data"])
    time.sleep(5)  # Esperar 5 segundos
```

**Problemas:**
- Desperdicio de recursos si no hay datos nuevos
- Latencia de hasta N segundos (intervalo de polling)
- Muchas conexiones innecesarias

#### Long Polling

```python
# El servidor mantiene la conexión hasta tener datos
@app.get("/api/notifications")
async def get_notifications():
    while True:
        notifications = await check_new_notifications()
        if notifications:
            return {"data": notifications}
        await asyncio.sleep(0.5)  # Verificar cada 500ms
```

**Mejora:** Menos requests, pero aún ineficiente.

---

## 2. WebSocket: Comunicación Bidireccional

### ¿Qué es WebSocket?

WebSocket es un **protocolo de comunicación full-duplex** sobre una única conexión TCP. Permite comunicación bidireccional entre cliente y servidor.

```
Cliente                    Servidor
   |                          |
   |==== WS Handshake =======>|
   |<==== WS Handshake =======|
   |                          |
   |<======= Mensaje =========|  (servidor inicia)
   |======== Mensaje ========>|  (cliente responde)
   |<======= Mensaje =========|
   |======== Mensaje ========>|
   |          ...             |
   |======== Close =========>|
```

### Características

| Característica | Descripción |
|----------------|-------------|
| **Full-duplex** | Ambos pueden enviar simultáneamente |
| **Persistente** | Una conexión para toda la sesión |
| **Bajo overhead** | Headers mínimos después del handshake |
| **Tiempo real** | Latencia mínima (~ms) |

### Handshake WebSocket

El handshake inicia como HTTP y "upgradea" a WebSocket:

```http
# Request del cliente
GET /ws HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13

# Response del servidor
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

### Casos de Uso

- 💬 **Chat en tiempo real**
- 🎮 **Juegos multijugador**
- 📊 **Dashboards en vivo**
- 🔔 **Notificaciones push**
- 📈 **Trading/finanzas**
- 🤝 **Colaboración en tiempo real** (Google Docs)

---

## 3. Server-Sent Events (SSE)

### ¿Qué es SSE?

SSE es un estándar que permite al servidor **enviar eventos al cliente** sobre una conexión HTTP persistente. Es **unidireccional** (solo server → client).

```
Cliente                    Servidor
   |                          |
   |-------- GET /events ---->|
   |                          |
   |<======= Event 1 =========|
   |<======= Event 2 =========|
   |<======= Event 3 =========|
   |          ...             |
```

### Formato de Eventos SSE

```
event: message
data: {"user": "Juan", "text": "Hola"}

event: notification
data: {"type": "alert", "message": "Nueva actualización"}

: esto es un comentario (keepalive)

data: mensaje sin tipo de evento
```

### Características

| Característica | Descripción |
|----------------|-------------|
| **Unidireccional** | Solo server → client |
| **HTTP estándar** | Funciona con infraestructura existente |
| **Reconexión automática** | El navegador reconecta automáticamente |
| **Event ID** | Permite resumir desde último evento |
| **Simple** | Más fácil de implementar que WebSocket |

### Casos de Uso

- 📰 **Feeds de noticias**
- 🔔 **Notificaciones del servidor**
- 📊 **Actualización de precios**
- 📈 **Métricas en tiempo real**
- 🔄 **Progreso de tareas largas**

---

## 4. Comparación: HTTP vs WebSocket vs SSE

### Tabla Comparativa

| Aspecto | HTTP | WebSocket | SSE |
|---------|------|-----------|-----|
| **Dirección** | Request-Response | Bidireccional | Server → Client |
| **Conexión** | Nueva por request | Persistente | Persistente |
| **Protocolo** | HTTP | WS (sobre TCP) | HTTP |
| **Overhead** | Alto (headers) | Bajo | Medio |
| **Reconexión** | Manual | Manual | Automática |
| **Binario** | Sí | Sí | No (solo texto) |
| **Firewall** | ✅ Siempre pasa | ⚠️ Puede bloquearse | ✅ Siempre pasa |
| **Complejidad** | Baja | Media | Baja |

### Diagrama de Decisión

```
¿Necesitas comunicación bidireccional?
├── SÍ → ¿Necesitas baja latencia?
│        ├── SÍ → WebSocket
│        └── NO → HTTP + Polling
└── NO → ¿El servidor necesita enviar datos?
         ├── SÍ → ¿Datos frecuentes?
         │        ├── SÍ → SSE
         │        └── NO → HTTP + Polling
         └── NO → HTTP tradicional
```

### Cuándo Usar Cada Uno

#### Usar HTTP Tradicional
- APIs REST estándar
- Operaciones CRUD
- Requests ocasionales
- Cuando no necesitas tiempo real

#### Usar WebSocket
- Chat en tiempo real
- Juegos multijugador
- Colaboración en tiempo real
- Cuando ambos lados envían datos frecuentemente

#### Usar SSE
- Notificaciones del servidor
- Feeds de actualizaciones
- Streaming de logs
- Cuando solo el servidor envía datos

---

## 5. WebSocket en el Ecosistema Python

### Librerías Disponibles

```python
# FastAPI/Starlette (lo que usaremos)
from fastapi import WebSocket

# websockets (cliente/servidor puro)
import websockets

# Socket.IO (con features adicionales)
import socketio

# aiohttp (alternativa async)
from aiohttp import web
```

### FastAPI WebSocket

FastAPI usa **Starlette** internamente para WebSockets:

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
```

---

## 6. Consideraciones de Arquitectura

### Escalabilidad

WebSockets mantienen conexiones abiertas, lo que implica:

```
Servidor con 10,000 conexiones WS
├── 10,000 file descriptors abiertos
├── Memoria por conexión (~KB)
└── Estado de sesión por conexión
```

**Soluciones:**
- Load balancing con sticky sessions
- Redis pub/sub para comunicación entre servidores
- Límites de conexiones por usuario

### Infraestructura

```
                    ┌─────────────────┐
                    │  Load Balancer  │
                    │ (sticky session)│
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐        ┌────▼────┐        ┌────▼────┐
    │ Server 1│        │ Server 2│        │ Server 3│
    │  (WS)   │        │  (WS)   │        │  (WS)   │
    └────┬────┘        └────┬────┘        └────┬────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Redis Pub/Sub │
                    │  (broadcast)    │
                    └─────────────────┘
```

---

## ✅ Resumen

| Tecnología | Dirección | Mejor Para |
|------------|-----------|------------|
| **HTTP** | Request-Response | APIs REST, CRUD |
| **WebSocket** | Bidireccional | Chat, juegos, colaboración |
| **SSE** | Server → Client | Notificaciones, feeds, streaming |

**Próximo:** Implementaremos WebSockets en FastAPI.
