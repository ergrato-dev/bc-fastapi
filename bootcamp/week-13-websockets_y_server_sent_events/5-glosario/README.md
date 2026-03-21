# 📖 Glosario - Semana 13: WebSockets y Server-Sent Events

## A

### Accept (WebSocket)
Método para aceptar una conexión WebSocket entrante. En FastAPI se usa `await websocket.accept()`.

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Acepta la conexión
```

### Async Generator
Generador asíncrono que produce valores de forma lazy. Usado en SSE para streaming.

```python
async def event_generator():
    while True:
        yield {"data": "event"}
        await asyncio.sleep(1)
```

---

## B

### Bidirectional Communication
Comunicación en ambas direcciones. WebSocket permite enviar y recibir datos simultáneamente (full-duplex).

### Broadcast
Enviar un mensaje a múltiples clientes conectados simultáneamente.

```python
async def broadcast(self, message: dict):
    for connection in self.connections:
        await connection.send_json(message)
```

---

## C

### Close Code
Código numérico que indica la razón del cierre de una conexión WebSocket.

| Código | Significado |
|--------|-------------|
| 1000 | Normal closure |
| 1001 | Going away |
| 1008 | Policy violation |
| 4001 | Custom: Invalid token |

### Connection Manager
Patrón para gestionar múltiples conexiones WebSocket activas.

```python
class ConnectionManager:
    def __init__(self):
        self.connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)
```

---

## D

### Disconnect
Evento que ocurre cuando un cliente cierra su conexión WebSocket.

```python
from fastapi import WebSocketDisconnect

try:
    while True:
        data = await websocket.receive_text()
except WebSocketDisconnect:
    # Cliente desconectado
    manager.disconnect(websocket)
```

---

## E

### EventSource
API del navegador para conectarse a endpoints SSE.

```javascript
const eventSource = new EventSource('/events');
eventSource.onmessage = (event) => {
    console.log(event.data);
};
```

### EventSourceResponse
Clase de `sse-starlette` para crear respuestas SSE en FastAPI.

```python
from sse_starlette.sse import EventSourceResponse

@app.get("/events")
async def sse_endpoint():
    return EventSourceResponse(event_generator())
```

---

## F

### Full-Duplex
Comunicación bidireccional simultánea. WebSocket es full-duplex; HTTP tradicional es half-duplex.

---

## H

### Handshake
Proceso inicial de negociación para establecer una conexión WebSocket.

1. Cliente envía HTTP Upgrade request
2. Servidor responde con 101 Switching Protocols
3. Conexión WebSocket establecida

### Heartbeat
Mensaje periódico para mantener la conexión activa y detectar desconexiones.

```python
# Cliente envía ping
ws.send_json({"type": "ping"})

# Servidor responde pong
await websocket.send_json({"type": "pong"})
```

---

## K

### Keepalive
Mecanismo para mantener conexiones activas enviando datos periódicamente.

```python
async def subscribe(self):
    while True:
        try:
            event = await asyncio.wait_for(queue.get(), timeout=30)
            yield event
        except asyncio.TimeoutError:
            yield {"type": "keepalive"}  # Previene timeout
```

---

## L

### Long Polling
Técnica legacy donde el cliente hace requests HTTP que el servidor mantiene abiertos hasta tener datos.

| Técnica | Conexiones | Latencia | Complejidad |
|---------|------------|----------|-------------|
| Polling | Muchas | Alta | Baja |
| Long Polling | Pocas | Media | Media |
| SSE | Una | Baja | Media |
| WebSocket | Una | Muy baja | Alta |

---

## M

### Message Queue
Cola para almacenar mensajes pendientes de envío.

```python
from asyncio import Queue

queue: Queue[dict] = Queue()
await queue.put(message)
event = await queue.get()
```

---

## O

### onmessage
Event handler en JavaScript para recibir mensajes WebSocket o SSE.

```javascript
// WebSocket
ws.onmessage = (event) => JSON.parse(event.data);

// SSE
eventSource.onmessage = (event) => JSON.parse(event.data);
```

---

## P

### Ping/Pong
Mecanismo de heartbeat en WebSocket. El protocolo WebSocket incluye frames de control ping/pong.

### Protocol Upgrade
Proceso HTTP para cambiar a WebSocket.

```http
GET /ws HTTP/1.1
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
```

---

## R

### Reconnection
Proceso de reconexión automática tras una desconexión.

```javascript
// SSE tiene reconnection automática
const eventSource = new EventSource('/events');
eventSource.onerror = () => {
    // Browser reconecta automáticamente
};

// WebSocket requiere implementación manual
function connect() {
    ws = new WebSocket(url);
    ws.onclose = () => setTimeout(connect, 1000);
}
```

### Room
Agrupación lógica de conexiones para chat o broadcast segmentado.

```python
rooms: dict[str, list[WebSocket]] = defaultdict(list)

async def join_room(websocket, room_id):
    rooms[room_id].append(websocket)
```

---

## S

### Server-Sent Events (SSE)
Tecnología para streaming unidireccional servidor→cliente sobre HTTP.

```python
@app.get("/events")
async def sse():
    async def generate():
        while True:
            yield {"data": json.dumps({"time": time.time()})}
            await asyncio.sleep(1)
    return EventSourceResponse(generate())
```

### Streaming Response
Respuesta HTTP que envía datos incrementalmente sin cerrar la conexión.

---

## T

### Text Frame
Frame WebSocket que contiene datos de texto (UTF-8).

```python
# Enviar texto
await websocket.send_text("Hello")

# Recibir texto
data = await websocket.receive_text()
```

### Token Authentication (WebSocket)
Autenticación en WebSocket usando token en query string.

```python
@app.websocket("/ws")
async def ws_endpoint(
    websocket: WebSocket,
    token: str = Query(...)
):
    user = validate_token(token)
```

---

## U

### Unidirectional
Comunicación en una sola dirección. SSE es unidireccional (servidor→cliente).

---

## W

### WebSocket
Protocolo de comunicación full-duplex sobre una conexión TCP persistente.

```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
```

### WebSocketDisconnect
Excepción de FastAPI/Starlette cuando un cliente WebSocket se desconecta.

```python
from fastapi import WebSocketDisconnect

try:
    data = await websocket.receive_text()
except WebSocketDisconnect:
    print("Client disconnected")
```

### ws:// / wss://
Esquemas de URL para WebSocket. `wss://` es la versión segura (sobre TLS).

```
ws://localhost:8000/ws     # Sin encriptación
wss://example.com/ws       # Con TLS (producción)
```

---

## Comparativa Rápida

| Característica | WebSocket | SSE |
|----------------|-----------|-----|
| Dirección | Bidireccional | Servidor→Cliente |
| Protocolo | ws:// / wss:// | HTTP |
| Reconexión | Manual | Automática |
| Binario | ✅ Sí | ❌ No |
| Firewall-friendly | ⚠️ A veces | ✅ Sí |
| Complejidad | Alta | Media |
| Caso de uso | Chat, gaming | Notificaciones, feeds |

---

*Última actualización: Enero 2026*
