# 💬 Proyecto: Chat en Tiempo Real con Rooms

## 📋 Descripción

En este proyecto construirás un **sistema de chat completo** en tiempo real con múltiples salas, autenticación de usuarios, historial de mensajes y notificaciones.

---

## 🎯 Objetivos

- Implementar WebSocket con autenticación JWT
- Crear sistema de salas con Connection Manager
- Persistir historial de mensajes en base de datos
- Implementar notificaciones con SSE
- Testear WebSocket y SSE
- Crear cliente HTML funcional

---

## 🗂️ Estructura del Proyecto

```
3-proyecto/
├── README.md
├── starter/
│   ├── pyproject.toml
│   ├── src/
│   │   ├── main.py              # App FastAPI
│   │   ├── config.py            # Configuración
│   │   ├── database.py          # SQLAlchemy setup
│   │   ├── models.py            # Modelos de DB
│   │   ├── schemas.py           # Schemas Pydantic
│   │   ├── auth.py              # Autenticación JWT
│   │   ├── manager.py           # Connection Manager
│   │   ├── services.py          # Lógica de negocio
│   │   └── notifications.py     # Servicio SSE
│   ├── templates/
│   │   └── chat.html            # Cliente de chat
│   └── tests/
│       ├── conftest.py
│       ├── test_auth.py
│       ├── test_websocket.py
│       └── test_sse.py
└── solution/                    # (Solo para instructores)
```

---

## 📝 Requisitos Funcionales

### 1. Autenticación (RF-01)
- [ ] Registro de usuarios (`POST /auth/register`)
- [ ] Login con JWT (`POST /auth/login`)
- [ ] Token en WebSocket via query parameter
- [ ] Validación de token antes de aceptar conexión

### 2. Salas de Chat (RF-02)
- [ ] Crear sala (`POST /rooms`)
- [ ] Listar salas (`GET /rooms`)
- [ ] Unirse a sala via WebSocket (`/ws/chat/{room_id}`)
- [ ] Salir de sala (desconexión)
- [ ] Lista de usuarios por sala

### 3. Mensajes (RF-03)
- [ ] Enviar mensaje a sala (WebSocket)
- [ ] Broadcast a usuarios de la sala
- [ ] Persistir mensajes en DB
- [ ] Obtener historial (`GET /rooms/{room_id}/messages`)

### 4. Notificaciones (RF-04)
- [ ] SSE endpoint para notificaciones (`/notifications`)
- [ ] Notificar nuevo mensaje en sala
- [ ] Notificar usuario join/leave
- [ ] Notificar nueva sala creada

### 5. Testing (RF-05)
- [ ] Tests de autenticación
- [ ] Tests de WebSocket (conexión, mensajes)
- [ ] Tests de SSE
- [ ] Cobertura mínima 70%

---

## 🛠️ Stack Técnico

| Tecnología | Uso |
|------------|-----|
| FastAPI | Framework web |
| SQLAlchemy | ORM |
| SQLite | Base de datos |
| JWT (python-jose) | Autenticación |
| sse-starlette | Server-Sent Events |
| pytest | Testing |
| httpx | Cliente HTTP async |

---

## 📦 Entregables

1. **Código funcional** con todos los requisitos
2. **Tests** con cobertura ≥70%
3. **Cliente HTML** funcional
4. **Documentación** de API (automática con FastAPI)

---

## ⏱️ Tiempo Estimado

| Tarea | Tiempo |
|-------|--------|
| Auth + Modelos | 20 min |
| Connection Manager | 20 min |
| WebSocket Chat | 25 min |
| SSE Notifications | 15 min |
| Tests | 20 min |
| **Total** | **~1h 40min** |

---

## 🚀 Instrucciones

### 1. Setup inicial

```bash
cd starter
uv sync
```

### 2. Completar TODOs

Los archivos tienen comentarios `# TODO:` indicando qué implementar.

Orden recomendado:
1. `src/auth.py` - Autenticación JWT
2. `src/manager.py` - Connection Manager
3. `src/services.py` - Lógica de negocio
4. `src/main.py` - Endpoints WebSocket/SSE
5. `tests/` - Tests

### 3. Ejecutar servidor

```bash
uv run fastapi dev src/main.py
```

### 4. Probar

- Abrir http://localhost:8000 para el chat
- Abrir http://localhost:8000/docs para API docs

### 5. Ejecutar tests

```bash
uv run pytest -v --cov=src
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Auth funcional | 15 |
| WebSocket chat | 25 |
| Connection Manager | 20 |
| SSE notifications | 15 |
| Tests completos | 15 |
| Cliente HTML | 10 |
| **Total** | **100** |

---

## 💡 Tips

- Usa los ejemplos de las prácticas como referencia
- Implementa primero sin auth, luego agrega JWT
- Testea cada componente antes de integrar
- El cliente HTML ya está casi completo
