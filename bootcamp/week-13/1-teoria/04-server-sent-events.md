# 📨 Server-Sent Events (SSE)

## 🎯 Objetivos

- Entender qué son los Server-Sent Events
- Implementar SSE en FastAPI
- Manejar reconexión y event IDs
- Conocer casos de uso ideales para SSE

---

## 1. ¿Qué son los Server-Sent Events?

### Definición

SSE es una tecnología que permite al servidor **enviar eventos al cliente** sobre una conexión HTTP persistente. A diferencia de WebSocket, es **unidireccional** (solo server → client).

```
Cliente                    Servidor
   |                          |
   |------- GET /events ----->|
   |                          |
   |<====== Event 1 ==========|
   |<====== Event 2 ==========|
   |<====== Event 3 ==========|
   |          ...             |
```

### Ventajas sobre WebSocket

| Ventaja | Descripción |
|---------|-------------|
| **Simplicidad** | Solo HTTP, sin protocolo especial |
| **Reconexión automática** | El navegador reconecta automáticamente |
| **Firewall-friendly** | HTTP estándar, siempre pasa |
| **Event ID** | Permite resumir desde el último evento |
| **Menor overhead** | Más ligero que WebSocket para casos unidireccionales |

### Cuándo Usar SSE

- ✅ **Notificaciones del servidor**
- ✅ **Feeds de noticias/actualizaciones**
- ✅ **Progreso de tareas largas**
- ✅ **Streaming de logs**
- ✅ **Actualizaciones de precios**
- ❌ **Chat bidireccional** (usar WebSocket)
- ❌ **Juegos en tiempo real** (usar WebSocket)

---

## 2. Formato de Eventos SSE

### Estructura Básica

```
event: nombre_evento
data: contenido del mensaje
id: identificador_unico
retry: 3000

```

**Campos:**

| Campo | Requerido | Descripción |
|-------|-----------|-------------|
| `data` | ✅ Sí | Contenido del mensaje |
| `event` | ❌ No | Tipo de evento (default: "message") |
| `id` | ❌ No | ID para reconexión |
| `retry` | ❌ No | Tiempo de reconexión en ms |

### Ejemplos de Eventos

```
# Evento simple (solo data)
data: Hola mundo

# Evento con tipo
event: notification
data: {"title": "Nueva alerta", "body": "Tienes un mensaje"}

# Evento con ID (para reconexión)
id: 123
event: update
data: {"price": 150.50}

# Datos multilinea
data: Primera línea
data: Segunda línea
data: Tercera línea

# Comentario (keepalive)
: esto es un comentario, el cliente lo ignora

```

> ⚠️ **Importante:** Cada evento termina con **dos saltos de línea** (`\n\n`).

---

## 3. SSE en FastAPI

### Usando sse-starlette

```bash
uv add sse-starlette
```

```python
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
import asyncio

app = FastAPI()


async def event_generator():
    """Generador de eventos SSE."""
    counter = 0
    while True:
        counter += 1
        yield {
            "event": "counter",
            "data": f"Contador: {counter}",
            "id": str(counter)
        }
        await asyncio.sleep(1)


@app.get("/events")
async def sse_endpoint():
    """Endpoint SSE que envía eventos cada segundo."""
    return EventSourceResponse(event_generator())
```

### Cliente JavaScript

```javascript
// Crear conexión SSE
const eventSource = new EventSource("/events");

// Evento por defecto (type: "message")
eventSource.onmessage = (event) => {
    console.log("Mensaje:", event.data);
};

// Evento específico (type: "counter")
eventSource.addEventListener("counter", (event) => {
    console.log("Contador:", event.data);
    console.log("ID:", event.lastEventId);
});

// Manejo de errores
eventSource.onerror = (error) => {
    console.error("Error SSE:", error);
    // El navegador intentará reconectar automáticamente
};

// Cerrar conexión
// eventSource.close();
```

---

## 4. Implementación Manual (sin librería)

### StreamingResponse

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json

app = FastAPI()


async def event_stream():
    """Generador de eventos SSE manual."""
    counter = 0
    
    while True:
        counter += 1
        
        # Formato SSE manual
        event_data = {
            "counter": counter,
            "timestamp": asyncio.get_event_loop().time()
        }
        
        # Construir mensaje SSE
        message = f"event: update\n"
        message += f"id: {counter}\n"
        message += f"data: {json.dumps(event_data)}\n\n"
        
        yield message
        
        await asyncio.sleep(1)


@app.get("/stream")
async def stream_events():
    """Endpoint SSE usando StreamingResponse."""
    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Para nginx
        }
    )
```

---

## 5. SSE con Datos Reales

### Sistema de Notificaciones

```python
from fastapi import FastAPI, Depends
from sse_starlette.sse import EventSourceResponse
from collections import defaultdict
import asyncio
from typing import AsyncGenerator

app = FastAPI()


class NotificationService:
    """Servicio de notificaciones con SSE."""
    
    def __init__(self):
        # Cola de notificaciones por usuario
        self.queues: dict[str, asyncio.Queue] = defaultdict(asyncio.Queue)
    
    async def subscribe(self, user_id: str) -> AsyncGenerator[dict, None]:
        """
        Suscribe a un usuario y genera eventos.
        """
        queue = self.queues[user_id]
        
        try:
            while True:
                # Esperar notificación o timeout (para keepalive)
                try:
                    notification = await asyncio.wait_for(
                        queue.get(),
                        timeout=30.0  # Keepalive cada 30s
                    )
                    yield {
                        "event": notification["type"],
                        "data": notification["data"],
                        "id": notification.get("id")
                    }
                except asyncio.TimeoutError:
                    # Enviar comentario como keepalive
                    yield {"comment": "keepalive"}
        
        finally:
            # Cleanup cuando el cliente se desconecta
            if user_id in self.queues and self.queues[user_id].empty():
                del self.queues[user_id]
    
    async def notify(
        self, 
        user_id: str, 
        notification_type: str,
        data: dict
    ) -> None:
        """Envía notificación a un usuario."""
        if user_id in self.queues:
            await self.queues[user_id].put({
                "type": notification_type,
                "data": data,
                "id": f"{user_id}-{asyncio.get_event_loop().time()}"
            })
    
    async def broadcast(
        self, 
        notification_type: str, 
        data: dict
    ) -> None:
        """Envía notificación a todos los usuarios suscritos."""
        for user_id in list(self.queues.keys()):
            await self.notify(user_id, notification_type, data)


# Instancia global
notification_service = NotificationService()


@app.get("/notifications/{user_id}")
async def subscribe_notifications(user_id: str):
    """Suscribirse a notificaciones de un usuario."""
    return EventSourceResponse(
        notification_service.subscribe(user_id)
    )


@app.post("/notify/{user_id}")
async def send_notification(
    user_id: str,
    notification_type: str,
    message: str
):
    """Enviar notificación a un usuario."""
    await notification_service.notify(
        user_id,
        notification_type,
        {"message": message}
    )
    return {"status": "sent"}


@app.post("/broadcast")
async def broadcast_notification(
    notification_type: str,
    message: str
):
    """Enviar notificación a todos."""
    await notification_service.broadcast(
        notification_type,
        {"message": message}
    )
    return {"status": "broadcasted"}
```

---

## 6. Progreso de Tareas Largas

### Caso de Uso: Procesamiento con Progreso

```python
from fastapi import FastAPI, BackgroundTasks
from sse_starlette.sse import EventSourceResponse
import asyncio
import uuid

app = FastAPI()

# Almacén de tareas en progreso
tasks_progress: dict[str, dict] = {}


async def process_long_task(task_id: str):
    """Simula una tarea larga con progreso."""
    total_steps = 10
    
    for step in range(total_steps):
        await asyncio.sleep(1)  # Simular trabajo
        
        progress = (step + 1) / total_steps * 100
        tasks_progress[task_id] = {
            "status": "processing",
            "progress": progress,
            "step": step + 1,
            "total_steps": total_steps,
            "message": f"Procesando paso {step + 1} de {total_steps}"
        }
    
    tasks_progress[task_id] = {
        "status": "completed",
        "progress": 100,
        "message": "¡Tarea completada!"
    }


@app.post("/tasks")
async def create_task(background_tasks: BackgroundTasks):
    """Crea una nueva tarea larga."""
    task_id = str(uuid.uuid4())
    
    tasks_progress[task_id] = {
        "status": "pending",
        "progress": 0,
        "message": "Iniciando tarea..."
    }
    
    background_tasks.add_task(process_long_task, task_id)
    
    return {"task_id": task_id}


@app.get("/tasks/{task_id}/progress")
async def task_progress(task_id: str):
    """Stream de progreso de una tarea."""
    
    async def progress_generator():
        last_progress = -1
        
        while True:
            if task_id not in tasks_progress:
                yield {
                    "event": "error",
                    "data": {"message": "Tarea no encontrada"}
                }
                break
            
            current = tasks_progress[task_id]
            
            # Solo enviar si cambió
            if current["progress"] != last_progress:
                last_progress = current["progress"]
                yield {
                    "event": "progress",
                    "data": current
                }
            
            # Terminar si completó o falló
            if current["status"] in ("completed", "failed"):
                # Cleanup
                del tasks_progress[task_id]
                break
            
            await asyncio.sleep(0.5)
    
    return EventSourceResponse(progress_generator())
```

### Cliente HTML

```html
<!DOCTYPE html>
<html>
<head>
    <title>Progreso de Tarea</title>
    <style>
        .progress-bar {
            width: 100%;
            height: 30px;
            background: #eee;
            border-radius: 5px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: #4CAF50;
            transition: width 0.3s;
        }
    </style>
</head>
<body>
    <h1>Procesamiento de Tarea</h1>
    <button onclick="startTask()">Iniciar Tarea</button>
    
    <div class="progress-bar">
        <div class="progress-fill" id="progress" style="width: 0%"></div>
    </div>
    <p id="status">Click para iniciar</p>

    <script>
        async function startTask() {
            // 1. Crear tarea
            const response = await fetch('/tasks', { method: 'POST' });
            const { task_id } = await response.json();
            
            // 2. Suscribirse al progreso
            const eventSource = new EventSource(`/tasks/${task_id}/progress`);
            
            eventSource.addEventListener('progress', (event) => {
                const data = JSON.parse(event.data);
                
                document.getElementById('progress').style.width = data.progress + '%';
                document.getElementById('status').textContent = data.message;
                
                if (data.status === 'completed') {
                    eventSource.close();
                }
            });
            
            eventSource.addEventListener('error', (event) => {
                const data = JSON.parse(event.data);
                document.getElementById('status').textContent = 'Error: ' + data.message;
                eventSource.close();
            });
        }
    </script>
</body>
</html>
```

---

## 7. Reconexión y Last-Event-ID

### Manejo de Reconexión

```python
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import asyncio

app = FastAPI()

# Almacén de eventos (en producción: Redis, DB, etc.)
event_store: list[dict] = []
event_counter = 0


async def event_generator(last_event_id: str | None):
    """
    Generador que soporta reconexión.
    
    Si last_event_id está presente, envía eventos perdidos.
    """
    global event_counter
    
    # Si hay last_event_id, buscar eventos perdidos
    if last_event_id:
        start_id = int(last_event_id) + 1
        for event in event_store:
            if int(event["id"]) >= start_id:
                yield event
    
    # Continuar con nuevos eventos
    while True:
        await asyncio.sleep(2)
        
        event_counter += 1
        event = {
            "event": "update",
            "data": f"Evento número {event_counter}",
            "id": str(event_counter),
            "retry": 5000  # Reconectar en 5s si falla
        }
        
        # Guardar evento (limitar a últimos 100)
        event_store.append(event)
        if len(event_store) > 100:
            event_store.pop(0)
        
        yield event


@app.get("/events")
async def sse_with_reconnection(request: Request):
    """
    Endpoint SSE con soporte para reconexión.
    
    El navegador envía Last-Event-ID automáticamente.
    """
    # El navegador envía este header en reconexión
    last_event_id = request.headers.get("Last-Event-ID")
    
    return EventSourceResponse(
        event_generator(last_event_id)
    )
```

---

## 8. SSE vs WebSocket: Decisión Final

### Tabla de Decisión

| Escenario | SSE | WebSocket |
|-----------|-----|-----------|
| Notificaciones push | ✅ | ⚠️ |
| Feed de noticias | ✅ | ⚠️ |
| Chat en tiempo real | ❌ | ✅ |
| Streaming de logs | ✅ | ⚠️ |
| Juegos multijugador | ❌ | ✅ |
| Progreso de tareas | ✅ | ⚠️ |
| Colaboración docs | ❌ | ✅ |
| Dashboard métricas | ✅ | ✅ |

**Regla general:**
- **Solo server → client:** Usar SSE
- **Bidireccional:** Usar WebSocket

---

## ✅ Resumen

| Concepto | Descripción |
|----------|-------------|
| **SSE** | Streaming HTTP unidireccional |
| **EventSourceResponse** | Respuesta SSE en FastAPI |
| **event** | Tipo de evento |
| **data** | Contenido del mensaje |
| **id** | ID para reconexión |
| **retry** | Tiempo de reconexión |
| **Last-Event-ID** | Header para resumir eventos |

**Próximo:** Autenticación y testing de WebSocket/SSE.
