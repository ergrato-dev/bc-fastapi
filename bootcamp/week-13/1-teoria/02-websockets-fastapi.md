# 🔌 WebSockets en FastAPI

## 🎯 Objetivos

- Crear endpoints WebSocket en FastAPI
- Enviar y recibir mensajes
- Manejar conexión y desconexión
- Entender el ciclo de vida de un WebSocket

---

## 1. Tu Primer WebSocket

### Endpoint Básico

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Endpoint WebSocket básico.
    
    1. Acepta la conexión
    2. Recibe mensajes en loop
    3. Responde con echo
    """
    # 1. Aceptar la conexión (handshake)
    await websocket.accept()
    
    try:
        while True:
            # 2. Esperar mensaje del cliente
            data = await websocket.receive_text()
            
            # 3. Enviar respuesta
            await websocket.send_text(f"Echo: {data}")
    
    except WebSocketDisconnect:
        print("Cliente desconectado")
```

### Cliente HTML para Probar

```html
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Test</title>
</head>
<body>
    <h1>WebSocket Echo</h1>
    <input type="text" id="message" placeholder="Escribe un mensaje">
    <button onclick="sendMessage()">Enviar</button>
    <div id="messages"></div>

    <script>
        // Conectar al WebSocket
        const ws = new WebSocket("ws://localhost:8000/ws");
        
        // Cuando recibimos un mensaje
        ws.onmessage = function(event) {
            const div = document.getElementById("messages");
            div.innerHTML += `<p>Servidor: ${event.data}</p>`;
        };
        
        // Cuando se abre la conexión
        ws.onopen = function() {
            console.log("Conectado!");
        };
        
        // Cuando se cierra la conexión
        ws.onclose = function() {
            console.log("Desconectado!");
        };
        
        // Función para enviar mensaje
        function sendMessage() {
            const input = document.getElementById("message");
            ws.send(input.value);
            input.value = "";
        }
    </script>
</body>
</html>
```

---

## 2. Ciclo de Vida del WebSocket

### Fases de la Conexión

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # ========================================
    # FASE 1: CONEXIÓN (Handshake)
    # ========================================
    print(f"Nueva conexión desde: {websocket.client}")
    
    # Puedes rechazar la conexión aquí
    # await websocket.close(code=1008)  # Policy Violation
    # return
    
    await websocket.accept()
    print("Conexión aceptada")
    
    # ========================================
    # FASE 2: COMUNICACIÓN
    # ========================================
    try:
        # Enviar mensaje de bienvenida
        await websocket.send_json({
            "type": "welcome",
            "message": "Conectado al servidor"
        })
        
        while True:
            # Esperar y procesar mensajes
            data = await websocket.receive_json()
            
            # Procesar según tipo de mensaje
            if data.get("type") == "ping":
                await websocket.send_json({"type": "pong"})
            else:
                await websocket.send_json({
                    "type": "echo",
                    "data": data
                })
    
    # ========================================
    # FASE 3: DESCONEXIÓN
    # ========================================
    except WebSocketDisconnect as e:
        print(f"Cliente desconectado. Código: {e.code}")
    
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close(code=1011)  # Internal Error
```

### Códigos de Cierre WebSocket

| Código | Nombre | Descripción |
|--------|--------|-------------|
| 1000 | Normal Closure | Cierre normal |
| 1001 | Going Away | Servidor/cliente se va |
| 1002 | Protocol Error | Error de protocolo |
| 1003 | Unsupported Data | Datos no soportados |
| 1008 | Policy Violation | Violación de política |
| 1011 | Internal Error | Error interno del servidor |

---

## 3. Tipos de Mensajes

### Texto vs JSON vs Binario

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    while True:
        # ========================================
        # RECIBIR MENSAJES
        # ========================================
        
        # Opción 1: Texto plano
        text = await websocket.receive_text()
        
        # Opción 2: JSON (deserializa automáticamente)
        data = await websocket.receive_json()
        
        # Opción 3: Binario (bytes)
        binary = await websocket.receive_bytes()
        
        # Opción 4: Genérico (detecta tipo)
        message = await websocket.receive()
        # message = {"type": "websocket.receive", "text": "..."} 
        # o {"type": "websocket.receive", "bytes": b"..."}
        
        # ========================================
        # ENVIAR MENSAJES
        # ========================================
        
        # Opción 1: Texto plano
        await websocket.send_text("Hola mundo")
        
        # Opción 2: JSON (serializa automáticamente)
        await websocket.send_json({"mensaje": "hola", "numero": 42})
        
        # Opción 3: Binario
        await websocket.send_bytes(b"\x00\x01\x02")
```

### Protocolo de Mensajes Estructurado

Es buena práctica definir un formato de mensajes:

```python
from pydantic import BaseModel
from typing import Literal, Any


class WebSocketMessage(BaseModel):
    """Formato estándar de mensaje WebSocket."""
    type: str
    data: Any = None
    

class ChatMessage(BaseModel):
    """Mensaje de chat."""
    type: Literal["chat"] = "chat"
    room: str
    user: str
    content: str


class SystemMessage(BaseModel):
    """Mensaje del sistema."""
    type: Literal["system"] = "system"
    event: str  # "user_joined", "user_left", etc.
    data: dict = {}


# Uso en el endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    while True:
        raw_data = await websocket.receive_json()
        
        match raw_data.get("type"):
            case "chat":
                message = ChatMessage(**raw_data)
                # Procesar mensaje de chat
            case "ping":
                await websocket.send_json({"type": "pong"})
            case _:
                await websocket.send_json({
                    "type": "error",
                    "message": "Tipo de mensaje desconocido"
                })
```

---

## 4. Parámetros en WebSocket

### Path Parameters

```python
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: int
):
    """WebSocket con parámetro en la ruta."""
    await websocket.accept()
    
    await websocket.send_json({
        "message": f"Bienvenido cliente {client_id}"
    })
    
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Cliente {client_id}: {data}")
```

### Query Parameters

```python
@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str | None = None,
    room: str = "general"
):
    """WebSocket con query parameters."""
    # Validar token si es necesario
    if token and not validate_token(token):
        await websocket.close(code=1008)
        return
    
    await websocket.accept()
    
    await websocket.send_json({
        "message": f"Conectado a sala: {room}"
    })
    
    # ...
```

**Cliente JavaScript:**
```javascript
// Con path parameter
const ws = new WebSocket("ws://localhost:8000/ws/123");

// Con query parameters
const ws = new WebSocket("ws://localhost:8000/ws?token=abc&room=tech");
```

---

## 5. Manejo de Errores

### Try/Except Completo

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import logging

app = FastAPI()
logger = logging.getLogger(__name__)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    client_id = id(websocket)
    
    try:
        await websocket.accept()
        logger.info(f"Cliente {client_id} conectado")
        
        while True:
            try:
                # Recibir con timeout implícito
                data = await websocket.receive_json()
                
                # Validar datos
                if not isinstance(data, dict):
                    await websocket.send_json({
                        "type": "error",
                        "message": "Formato inválido, se espera JSON object"
                    })
                    continue
                
                # Procesar mensaje
                await process_message(websocket, data)
                
            except ValueError as e:
                # Error de deserialización JSON
                await websocket.send_json({
                    "type": "error",
                    "message": f"JSON inválido: {str(e)}"
                })
    
    except WebSocketDisconnect as e:
        logger.info(f"Cliente {client_id} desconectado (código: {e.code})")
    
    except Exception as e:
        logger.error(f"Error con cliente {client_id}: {e}")
        try:
            await websocket.close(code=1011)
        except:
            pass  # Ya estaba cerrado


async def process_message(websocket: WebSocket, data: dict):
    """Procesa un mensaje del cliente."""
    message_type = data.get("type", "unknown")
    
    match message_type:
        case "chat":
            await websocket.send_json({
                "type": "chat",
                "message": data.get("message", "")
            })
        case "ping":
            await websocket.send_json({"type": "pong"})
        case _:
            await websocket.send_json({
                "type": "error",
                "message": f"Tipo desconocido: {message_type}"
            })
```

---

## 6. Múltiples Endpoints WebSocket

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws/chat")
async def chat_websocket(websocket: WebSocket):
    """WebSocket para chat."""
    await websocket.accept()
    # Lógica de chat...


@app.websocket("/ws/notifications")
async def notifications_websocket(websocket: WebSocket):
    """WebSocket para notificaciones."""
    await websocket.accept()
    # Lógica de notificaciones...


@app.websocket("/ws/game/{game_id}")
async def game_websocket(websocket: WebSocket, game_id: str):
    """WebSocket para juego específico."""
    await websocket.accept()
    # Lógica de juego...
```

---

## 7. Información del Cliente

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Información disponible antes de accept()
    print(f"URL: {websocket.url}")
    print(f"Headers: {websocket.headers}")
    print(f"Query Params: {websocket.query_params}")
    print(f"Path Params: {websocket.path_params}")
    print(f"Cookies: {websocket.cookies}")
    
    # Client info (IP, puerto)
    if websocket.client:
        print(f"Client IP: {websocket.client.host}")
        print(f"Client Port: {websocket.client.port}")
    
    await websocket.accept()
    
    # ...
```

---

## 8. Ejemplo Completo: Echo Server Mejorado

```python
"""
Echo Server WebSocket con manejo completo.
"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from datetime import datetime
import json

app = FastAPI(title="WebSocket Echo Server")

# Cliente HTML inline
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Echo</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 2rem auto; }
        #messages { border: 1px solid #ccc; height: 300px; overflow-y: auto; padding: 1rem; }
        .server { color: green; }
        .client { color: blue; }
        .system { color: gray; font-style: italic; }
        input, button { padding: 0.5rem; margin: 0.5rem 0; }
        input { width: 70%; }
    </style>
</head>
<body>
    <h1>🔌 WebSocket Echo Server</h1>
    <div id="status">Estado: Desconectado</div>
    <div id="messages"></div>
    <input type="text" id="message" placeholder="Escribe un mensaje..." onkeypress="handleKey(event)">
    <button onclick="send()">Enviar</button>
    <button onclick="sendPing()">Ping</button>

    <script>
        let ws;
        const messages = document.getElementById('messages');
        const status = document.getElementById('status');
        
        function connect() {
            ws = new WebSocket(`ws://${location.host}/ws`);
            
            ws.onopen = () => {
                status.textContent = 'Estado: ✅ Conectado';
                addMessage('Conectado al servidor', 'system');
            };
            
            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                addMessage(`[${data.type}] ${JSON.stringify(data.data || data.message)}`, 'server');
            };
            
            ws.onclose = () => {
                status.textContent = 'Estado: ❌ Desconectado';
                addMessage('Desconectado del servidor', 'system');
                setTimeout(connect, 3000);
            };
            
            ws.onerror = (error) => {
                addMessage('Error de conexión', 'system');
            };
        }
        
        function addMessage(text, type) {
            const div = document.createElement('div');
            div.className = type;
            div.textContent = `[${new Date().toLocaleTimeString()}] ${text}`;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }
        
        function send() {
            const input = document.getElementById('message');
            if (input.value && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({type: 'message', content: input.value}));
                addMessage(input.value, 'client');
                input.value = '';
            }
        }
        
        function sendPing() {
            if (ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({type: 'ping'}));
                addMessage('Ping enviado', 'client');
            }
        }
        
        function handleKey(e) {
            if (e.key === 'Enter') send();
        }
        
        connect();
    </script>
</body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(HTML)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Enviar bienvenida
    await websocket.send_json({
        "type": "welcome",
        "message": "Conectado al Echo Server",
        "timestamp": datetime.now().isoformat()
    })
    
    try:
        while True:
            data = await websocket.receive_json()
            
            match data.get("type"):
                case "ping":
                    await websocket.send_json({
                        "type": "pong",
                        "timestamp": datetime.now().isoformat()
                    })
                
                case "message":
                    await websocket.send_json({
                        "type": "echo",
                        "data": data.get("content"),
                        "timestamp": datetime.now().isoformat()
                    })
                
                case _:
                    await websocket.send_json({
                        "type": "error",
                        "message": f"Tipo desconocido: {data.get('type')}"
                    })
    
    except WebSocketDisconnect:
        print("Cliente desconectado")
```

---

## ✅ Resumen

| Concepto | Descripción |
|----------|-------------|
| `@app.websocket("/ws")` | Decorador para endpoint WS |
| `await websocket.accept()` | Acepta la conexión (handshake) |
| `await websocket.receive_*()` | Recibe mensaje (text/json/bytes) |
| `await websocket.send_*()` | Envía mensaje |
| `WebSocketDisconnect` | Excepción de desconexión |
| `await websocket.close(code)` | Cierra conexión |

**Próximo:** Connection Manager para múltiples conexiones.
