# 🔐 Autenticación y Testing

## 🎯 Objetivos

- Autenticar conexiones WebSocket
- Proteger endpoints SSE
- Testear aplicaciones en tiempo real
- Implementar patrones de testing para WebSocket

---

## 1. Autenticación en WebSocket

### El Desafío

WebSocket no soporta headers personalizados en el handshake desde el navegador. Soluciones:

1. **Query parameter** - Token en la URL
2. **Primer mensaje** - Enviar token después de conectar
3. **Cookies** - Si ya hay sesión HTTP
4. **Subprotocolo** - Token en Sec-WebSocket-Protocol

### Método 1: Token en Query Parameter

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query, HTTPException
from jose import jwt, JWTError
from datetime import datetime

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def verify_token(token: str) -> dict | None:
    """Verifica y decodifica el JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Query(...)  # Token requerido en query
):
    """WebSocket con autenticación por query parameter."""
    
    # Verificar token ANTES de aceptar
    payload = verify_token(token)
    
    if not payload:
        await websocket.close(code=1008, reason="Invalid token")
        return
    
    # Token válido, aceptar conexión
    user_id = payload.get("sub")
    await websocket.accept()
    
    await websocket.send_json({
        "type": "authenticated",
        "user_id": user_id
    })
    
    try:
        while True:
            data = await websocket.receive_json()
            # Procesar con contexto de usuario autenticado
            await websocket.send_json({
                "type": "echo",
                "user_id": user_id,
                "data": data
            })
    
    except WebSocketDisconnect:
        print(f"Usuario {user_id} desconectado")
```

**Cliente JavaScript:**
```javascript
const token = localStorage.getItem('access_token');
const ws = new WebSocket(`ws://localhost:8000/ws?token=${token}`);
```

### Método 2: Token en Primer Mensaje

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket con autenticación por primer mensaje.
    
    El cliente debe enviar {"type": "auth", "token": "..."} 
    como primer mensaje.
    """
    await websocket.accept()
    
    # Esperar mensaje de autenticación (timeout 10s)
    try:
        auth_message = await asyncio.wait_for(
            websocket.receive_json(),
            timeout=10.0
        )
    except asyncio.TimeoutError:
        await websocket.close(code=1008, reason="Auth timeout")
        return
    
    # Validar mensaje de auth
    if auth_message.get("type") != "auth":
        await websocket.close(code=1008, reason="Auth required")
        return
    
    token = auth_message.get("token")
    payload = verify_token(token)
    
    if not payload:
        await websocket.send_json({
            "type": "auth_error",
            "message": "Invalid token"
        })
        await websocket.close(code=1008)
        return
    
    user_id = payload.get("sub")
    
    # Confirmar autenticación
    await websocket.send_json({
        "type": "auth_success",
        "user_id": user_id
    })
    
    # Ahora el cliente está autenticado
    try:
        while True:
            data = await websocket.receive_json()
            await process_authenticated_message(websocket, user_id, data)
    
    except WebSocketDisconnect:
        pass
```

**Cliente JavaScript:**
```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onopen = () => {
    // Enviar token como primer mensaje
    ws.send(JSON.stringify({
        type: 'auth',
        token: localStorage.getItem('access_token')
    }));
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    
    if (data.type === 'auth_success') {
        console.log('Autenticado como:', data.user_id);
    } else if (data.type === 'auth_error') {
        console.error('Error de auth:', data.message);
        ws.close();
    }
};
```

### Método 3: Dependencia Reutilizable

```python
from fastapi import FastAPI, WebSocket, Depends, Query, HTTPException
from typing import Annotated


async def get_current_user_ws(
    websocket: WebSocket,
    token: str = Query(None)
) -> dict:
    """
    Dependencia para obtener usuario en WebSocket.
    
    Similar a get_current_user de HTTP, pero para WS.
    """
    if not token:
        await websocket.close(code=1008, reason="Token required")
        raise HTTPException(status_code=401)
    
    payload = verify_token(token)
    
    if not payload:
        await websocket.close(code=1008, reason="Invalid token")
        raise HTTPException(status_code=401)
    
    return payload


@app.websocket("/ws/chat")
async def chat_websocket(
    websocket: WebSocket,
    current_user: Annotated[dict, Depends(get_current_user_ws)]
):
    """WebSocket con dependencia de autenticación."""
    await websocket.accept()
    
    user_id = current_user.get("sub")
    
    # Usuario ya autenticado
    await websocket.send_json({
        "type": "welcome",
        "user_id": user_id
    })
    
    # ...
```

---

## 2. Autenticación en SSE

### SSE con Token Bearer

```python
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sse_starlette.sse import EventSourceResponse

app = FastAPI()
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """Obtiene usuario actual del token."""
    token = credentials.credentials
    payload = verify_token(token)
    
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return payload


@app.get("/events")
async def sse_events(
    current_user: dict = Depends(get_current_user)
):
    """SSE protegido con JWT."""
    user_id = current_user.get("sub")
    
    async def event_generator():
        while True:
            # Eventos personalizados para el usuario
            yield {
                "event": "notification",
                "data": f"Hola usuario {user_id}"
            }
            await asyncio.sleep(5)
    
    return EventSourceResponse(event_generator())
```

**Cliente JavaScript con EventSource:**

EventSource no soporta headers personalizados. Opciones:

```javascript
// Opción 1: Usar fetch con ReadableStream
async function connectSSE(url, token) {
    const response = await fetch(url, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    
    while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        const text = decoder.decode(value);
        console.log('Event:', text);
    }
}

// Opción 2: Pasar token en query (menos seguro)
const eventSource = new EventSource(`/events?token=${token}`);
```

### SSE con Token en Query

```python
@app.get("/events")
async def sse_events(
    request: Request,
    token: str = Query(...)
):
    """SSE con token en query parameter."""
    payload = verify_token(token)
    
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = payload.get("sub")
    
    async def event_generator():
        # Verificar si cliente desconectó
        while not await request.is_disconnected():
            yield {
                "event": "update",
                "data": {"user_id": user_id}
            }
            await asyncio.sleep(5)
    
    return EventSourceResponse(event_generator())
```

---

## 3. Testing de WebSocket

### Configuración de pytest

```python
# conftest.py
import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from app.main import app


@pytest.fixture
def client():
    """Cliente síncrono para tests."""
    return TestClient(app)


@pytest.fixture
async def async_client():
    """Cliente asíncrono para tests."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
```

### Tests Básicos de WebSocket

```python
# test_websocket.py
import pytest
from fastapi.testclient import TestClient
from app.main import app


def test_websocket_connect():
    """Test de conexión básica."""
    client = TestClient(app)
    
    with client.websocket_connect("/ws") as websocket:
        # Conexión exitosa
        data = websocket.receive_json()
        assert data["type"] == "welcome"


def test_websocket_echo():
    """Test de echo de mensajes."""
    client = TestClient(app)
    
    with client.websocket_connect("/ws") as websocket:
        # Recibir bienvenida
        websocket.receive_json()
        
        # Enviar mensaje
        websocket.send_json({"type": "message", "content": "Hola"})
        
        # Recibir echo
        response = websocket.receive_json()
        assert response["type"] == "echo"
        assert response["content"] == "Hola"


def test_websocket_with_path_param():
    """Test con parámetro en ruta."""
    client = TestClient(app)
    
    with client.websocket_connect("/ws/user123") as websocket:
        data = websocket.receive_json()
        assert "user123" in str(data)


def test_websocket_with_query_param():
    """Test con query parameter."""
    client = TestClient(app)
    
    with client.websocket_connect("/ws?room=general") as websocket:
        data = websocket.receive_json()
        assert data["room"] == "general"
```

### Test de Autenticación WebSocket

```python
# test_websocket_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.auth import create_access_token


def test_websocket_without_token():
    """Test de rechazo sin token."""
    client = TestClient(app)
    
    # Debe rechazar la conexión
    with pytest.raises(Exception):
        with client.websocket_connect("/ws/secure") as websocket:
            pass


def test_websocket_with_invalid_token():
    """Test con token inválido."""
    client = TestClient(app)
    
    with pytest.raises(Exception):
        with client.websocket_connect("/ws/secure?token=invalid") as websocket:
            pass


def test_websocket_with_valid_token():
    """Test con token válido."""
    client = TestClient(app)
    
    # Crear token válido
    token = create_access_token(data={"sub": "user123"})
    
    with client.websocket_connect(f"/ws/secure?token={token}") as websocket:
        data = websocket.receive_json()
        assert data["type"] == "authenticated"
        assert data["user_id"] == "user123"
```

### Test de Broadcast

```python
# test_broadcast.py
import pytest
from fastapi.testclient import TestClient
from app.main import app, manager
import threading
import time


def test_broadcast_to_multiple_clients():
    """Test de broadcast a múltiples clientes."""
    client = TestClient(app)
    received_messages = []
    
    def connect_and_listen(client_id):
        with client.websocket_connect(f"/ws/{client_id}") as ws:
            # Recibir bienvenida
            ws.receive_json()
            
            # Esperar broadcast
            msg = ws.receive_json()
            received_messages.append((client_id, msg))
    
    # Conectar dos clientes en threads
    thread1 = threading.Thread(target=connect_and_listen, args=("client1",))
    thread2 = threading.Thread(target=connect_and_listen, args=("client2",))
    
    thread1.start()
    thread2.start()
    
    # Dar tiempo a conectar
    time.sleep(0.5)
    
    # Un cliente envía mensaje (trigger broadcast)
    with client.websocket_connect("/ws/sender") as ws:
        ws.receive_json()
        ws.send_json({"type": "broadcast", "content": "Hola a todos"})
    
    thread1.join(timeout=2)
    thread2.join(timeout=2)
    
    # Verificar que ambos recibieron
    assert len(received_messages) >= 2
```

---

## 4. Testing de SSE

### Test Básico de SSE

```python
# test_sse.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_sse_connection():
    """Test de conexión SSE."""
    transport = ASGITransport(app=app)
    
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        async with client.stream("GET", "/events") as response:
            assert response.status_code == 200
            assert "text/event-stream" in response.headers["content-type"]
            
            # Leer primer evento
            async for line in response.aiter_lines():
                if line.startswith("data:"):
                    data = line[5:].strip()
                    assert data  # Hay contenido
                    break


@pytest.mark.asyncio
async def test_sse_receives_events():
    """Test que SSE recibe eventos."""
    transport = ASGITransport(app=app)
    events_received = []
    
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        async with client.stream("GET", "/events", timeout=5.0) as response:
            event_count = 0
            
            async for line in response.aiter_lines():
                if line.startswith("data:"):
                    events_received.append(line)
                    event_count += 1
                    
                    if event_count >= 3:  # Recibir 3 eventos
                        break
    
    assert len(events_received) == 3
```

### Test de SSE con Autenticación

```python
@pytest.mark.asyncio
async def test_sse_requires_auth():
    """Test que SSE requiere autenticación."""
    transport = ASGITransport(app=app)
    
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/events/protected")
        assert response.status_code == 401


@pytest.mark.asyncio
async def test_sse_with_valid_token():
    """Test SSE con token válido."""
    transport = ASGITransport(app=app)
    token = create_access_token(data={"sub": "user123"})
    
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        headers = {"Authorization": f"Bearer {token}"}
        
        async with client.stream("GET", "/events/protected", headers=headers) as response:
            assert response.status_code == 200
            
            # Leer primer evento
            async for line in response.aiter_lines():
                if line.startswith("data:"):
                    break
```

---

## 5. Mocking en Tests de WebSocket

### Mock del Connection Manager

```python
# test_with_mocks.py
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def mock_manager():
    """Mock del ConnectionManager."""
    with patch("app.main.manager") as mock:
        mock.connect = AsyncMock()
        mock.disconnect = MagicMock()
        mock.broadcast = AsyncMock()
        mock.active_connections = []
        yield mock


def test_websocket_calls_manager_connect(mock_manager):
    """Verifica que se llama a manager.connect."""
    client = TestClient(app)
    
    with client.websocket_connect("/ws/test_user"):
        pass
    
    mock_manager.connect.assert_called_once()


def test_websocket_calls_manager_disconnect_on_close(mock_manager):
    """Verifica cleanup en desconexión."""
    client = TestClient(app)
    
    with client.websocket_connect("/ws/test_user") as ws:
        ws.close()
    
    mock_manager.disconnect.assert_called_once()
```

### Mock de Servicios Externos

```python
@pytest.fixture
def mock_notification_service():
    """Mock del servicio de notificaciones."""
    with patch("app.main.notification_service") as mock:
        mock.subscribe = AsyncMock(return_value=async_generator([
            {"event": "test", "data": "test_data"}
        ]))
        mock.notify = AsyncMock()
        yield mock


async def async_generator(items):
    """Helper para crear generador async."""
    for item in items:
        yield item
```

---

## 6. Test de Reconexión

```python
# test_reconnection.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_sse_last_event_id():
    """Test que SSE respeta Last-Event-ID."""
    transport = ASGITransport(app=app)
    
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Primera conexión - recibir algunos eventos
        events_first = []
        async with client.stream("GET", "/events") as response:
            count = 0
            last_id = None
            
            async for line in response.aiter_lines():
                if line.startswith("id:"):
                    last_id = line[3:].strip()
                if line.startswith("data:"):
                    events_first.append(line)
                    count += 1
                    if count >= 2:
                        break
        
        # Segunda conexión con Last-Event-ID
        headers = {"Last-Event-ID": last_id}
        async with client.stream("GET", "/events", headers=headers) as response:
            async for line in response.aiter_lines():
                if line.startswith("data:"):
                    # No debería recibir eventos anteriores
                    assert line not in events_first
                    break
```

---

## 7. Fixtures Útiles para Tests

```python
# conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.auth import create_access_token


@pytest.fixture
def client():
    """Cliente de test."""
    return TestClient(app)


@pytest.fixture
def auth_token():
    """Token JWT válido para tests."""
    return create_access_token(data={"sub": "test_user"})


@pytest.fixture
def auth_ws_url(auth_token):
    """URL de WebSocket con token."""
    return f"/ws?token={auth_token}"


@pytest.fixture
def websocket_client(client, auth_ws_url):
    """Cliente WebSocket autenticado."""
    return client.websocket_connect(auth_ws_url)


@pytest.fixture
async def sse_client(auth_token):
    """Cliente SSE autenticado."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client, {"Authorization": f"Bearer {auth_token}"}
```

---

## ✅ Resumen

| Aspecto | WebSocket | SSE |
|---------|-----------|-----|
| **Auth por Query** | `?token=...` | `?token=...` |
| **Auth por Header** | Solo primer mensaje | Bearer token |
| **Test conexión** | `websocket_connect()` | `client.stream()` |
| **Test mensajes** | `send_json/receive_json` | `aiter_lines()` |
| **Mock** | Patch manager | Patch generator |

**Próximo:** Prácticas guiadas de WebSocket y SSE.
