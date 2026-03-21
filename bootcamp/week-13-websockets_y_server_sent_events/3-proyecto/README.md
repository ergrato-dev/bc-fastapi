# 📡 Proyecto Semana 13: API con WebSockets y Server-Sent Events

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplo Genérico de Referencia

> Los ejemplos usan **"Warehouse"** (Almacén) que NO está en el pool.
> **Debes adaptar TODO a tu dominio asignado.**

| Concepto | Ejemplo Genérico | Adapta a tu Dominio |
|----------|-----------------|---------------------|
| Real-time Resource | `StockLevel` | `{YourRealtimeEntity}` |
| Event Type | `stock_updated` | `{your_entity}_updated` |
| Channel | `warehouse_zone_{id}` | `{your_channel}_{id}` |

---

## 🎯 Objetivo

Implementar **comunicación en tiempo real**:

- WebSockets para comunicación bidireccional
- Server-Sent Events para notificaciones
- Connection management
- Broadcast a múltiples clientes

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### WebSocket Manager

```python
# Ejemplo genérico (Warehouse)
from fastapi import WebSocket
from dataclasses import dataclass, field
import asyncio
import json

@dataclass
class ConnectionManager:
    """Gestiona conexiones WebSocket por zona"""
    connections: dict[int, list[WebSocket]] = field(default_factory=dict)
    
    async def connect(self, websocket: WebSocket, zone_id: int) -> None:
        """Registra nueva conexión a una zona"""
        await websocket.accept()
        if zone_id not in self.connections:
            self.connections[zone_id] = []
        self.connections[zone_id].append(websocket)
    
    def disconnect(self, websocket: WebSocket, zone_id: int) -> None:
        """Elimina conexión de una zona"""
        if zone_id in self.connections:
            self.connections[zone_id].remove(websocket)
            if not self.connections[zone_id]:
                del self.connections[zone_id]
    
    async def broadcast_to_zone(self, zone_id: int, message: dict) -> None:
        """Envía mensaje a todos los clientes de una zona"""
        if zone_id in self.connections:
            for connection in self.connections[zone_id]:
                try:
                    await connection.send_json(message)
                except Exception:
                    pass  # Cliente desconectado
    
    async def broadcast_all(self, message: dict) -> None:
        """Envía mensaje a todos los clientes conectados"""
        for zone_id in self.connections:
            await self.broadcast_to_zone(zone_id, message)

manager = ConnectionManager()
```

### WebSocket Endpoint

```python
# Ejemplo genérico
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws/zones/{zone_id}")
async def websocket_zone_updates(websocket: WebSocket, zone_id: int):
    """WebSocket para actualizaciones de stock por zona"""
    await manager.connect(websocket, zone_id)
    
    try:
        while True:
            # Recibir mensajes del cliente
            data = await websocket.receive_json()
            
            if data.get("type") == "request_stock":
                # Cliente solicita stock actual
                items = await item_service.get_by_zone(zone_id)
                await websocket.send_json({
                    "type": "stock_snapshot",
                    "items": [item.model_dump() for item in items]
                })
            
            elif data.get("type") == "update_quantity":
                # Cliente actualiza cantidad
                item_id = data["item_id"]
                new_quantity = data["quantity"]
                
                updated = await item_service.update_quantity(item_id, new_quantity)
                
                # Broadcast a todos los clientes de esta zona
                await manager.broadcast_to_zone(zone_id, {
                    "type": "stock_updated",
                    "item_id": item_id,
                    "new_quantity": new_quantity,
                    "updated_by": "operator"
                })
    
    except WebSocketDisconnect:
        manager.disconnect(websocket, zone_id)
```

### Server-Sent Events

```python
# Ejemplo genérico
from fastapi.responses import StreamingResponse
from datetime import datetime
import asyncio

async def stock_event_generator(zone_id: int):
    """Generador de eventos SSE para stock"""
    last_check = datetime.utcnow()
    
    while True:
        # Verificar cambios desde última revisión
        changes = await item_service.get_changes_since(zone_id, last_check)
        
        if changes:
            for change in changes:
                event_data = {
                    "type": "stock_change",
                    "item_id": change.item_id,
                    "old_quantity": change.old_quantity,
                    "new_quantity": change.new_quantity,
                    "timestamp": change.timestamp.isoformat()
                }
                yield f"event: stock_change\ndata: {json.dumps(event_data)}\n\n"
            
            last_check = datetime.utcnow()
        
        # Heartbeat cada 30 segundos
        yield f"event: heartbeat\ndata: {datetime.utcnow().isoformat()}\n\n"
        
        await asyncio.sleep(5)  # Polling interval

@app.get("/sse/zones/{zone_id}/stock")
async def stock_sse_endpoint(zone_id: int):
    """Endpoint SSE para actualizaciones de stock"""
    return StreamingResponse(
        stock_event_generator(zone_id),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )
```

### Event Broadcasting desde CRUD

```python
# Ejemplo genérico - Integración con operaciones CRUD
class ItemService:
    def __init__(
        self,
        repository: IItemRepository,
        ws_manager: ConnectionManager
    ):
        self.repository = repository
        self.ws_manager = ws_manager
    
    async def create(self, data: ItemCreate) -> Item:
        item = await self.repository.save(Item(**data.model_dump()))
        
        # Notificar a clientes WebSocket
        await self.ws_manager.broadcast_to_zone(item.zone_id, {
            "type": "item_created",
            "item": item.model_dump()
        })
        
        return item
    
    async def update_quantity(self, item_id: int, quantity: int) -> Item:
        item = await self.repository.find_by_id(item_id)
        old_quantity = item.quantity
        item.quantity = quantity
        
        updated = await self.repository.save(item)
        
        # Notificar cambio
        await self.ws_manager.broadcast_to_zone(updated.zone_id, {
            "type": "quantity_updated",
            "item_id": item_id,
            "old_quantity": old_quantity,
            "new_quantity": quantity
        })
        
        # Alerta si stock bajo
        if quantity < 10:
            await self.ws_manager.broadcast_all({
                "type": "low_stock_alert",
                "item_id": item_id,
                "item_name": updated.name,
                "current_quantity": quantity
            })
        
        return updated
```

### Cliente JavaScript de Referencia

```javascript
// Ejemplo cliente WebSocket
const socket = new WebSocket('ws://localhost:8000/ws/zones/1');

socket.onopen = () => {
    console.log('Connected to zone 1');
    socket.send(JSON.stringify({ type: 'request_stock' }));
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    switch(data.type) {
        case 'stock_snapshot':
            updateStockTable(data.items);
            break;
        case 'stock_updated':
            updateItemRow(data.item_id, data.new_quantity);
            break;
        case 'low_stock_alert':
            showAlert(`Low stock: ${data.item_name}`);
            break;
    }
};

// Ejemplo cliente SSE
const eventSource = new EventSource('/sse/zones/1/stock');

eventSource.addEventListener('stock_change', (e) => {
    const data = JSON.parse(e.data);
    console.log('Stock change:', data);
});

eventSource.addEventListener('heartbeat', (e) => {
    console.log('Server alive:', e.data);
});
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── websocket/
│   ├── __init__.py
│   ├── manager.py
│   ├── handlers.py
│   └── events.py
├── sse/
│   ├── __init__.py
│   └── generators.py
├── services/
├── routers/
├── static/           # HTML de prueba
│   └── ws-client.html
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| WebSocket funciona | 15 |
| SSE funciona | 15 |
| Broadcasting correcto | 10 |
| **Adaptación al Dominio** (35%) | |
| Eventos relevantes | 12 |
| Canales específicos | 13 |
| Originalidad (no copia ejemplo) | 10 |
| **Calidad del Código** (25%) | |
| Connection management | 10 |
| Manejo de errores | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No copies** los eventos "stock_updated/low_stock_alert"
- ✅ **Diseña** eventos específicos de tu dominio
- ✅ **Crea** canales relevantes para tu negocio

---

## 📚 Recursos

- [FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/)
- [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
