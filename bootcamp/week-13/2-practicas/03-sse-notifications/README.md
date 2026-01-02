# 📨 Práctica 03: SSE Notifications

## 🎯 Objetivo

Implementar un sistema de notificaciones en tiempo real usando Server-Sent Events (SSE). El servidor enviará notificaciones a los clientes suscritos.

---

## 📋 Requisitos Previos

- Teoría 04: Server-Sent Events
- Conocimiento básico de async generators

---

## 🗂️ Estructura

```
03-sse-notifications/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py              # Servidor con SSE
    ├── notifications.py     # Servicio de notificaciones
    └── templates/
        └── index.html       # Cliente de notificaciones
```

---

## 📝 Instrucciones

### Paso 1: Configurar sse-starlette

Abre `starter/pyproject.toml` y verifica que incluye `sse-starlette`.

```bash
cd starter
uv sync
```

### Paso 2: Servicio de notificaciones

Abre `starter/notifications.py` y descomenta el **Paso 2**.

Implementarás:
- Cola de notificaciones por usuario
- Método `subscribe()` como generador async
- Método `notify()` para enviar notificaciones

### Paso 3: Endpoint SSE

Abre `starter/main.py` y descomenta el **Paso 3**.

Crearás el endpoint `/notifications/{user_id}` que:
- Usa `EventSourceResponse`
- Retorna stream de notificaciones

### Paso 4: Endpoints para enviar notificaciones

Descomenta el **Paso 4** para agregar:
- POST `/notify/{user_id}` - Notificación a usuario
- POST `/broadcast` - Notificación a todos

### Paso 5: Tipos de eventos

Descomenta el **Paso 5** para soportar diferentes tipos:
- `info`, `warning`, `error`, `success`

---

## ✅ Verificación

1. Ejecuta el servidor:
```bash
uv run fastapi dev main.py
```

2. Abre http://localhost:8000 en el navegador

3. En otra terminal, envía notificaciones:
```bash
# Notificación a usuario específico
curl -X POST "http://localhost:8000/notify/user1?type=info&message=Hola"

# Broadcast a todos
curl -X POST "http://localhost:8000/broadcast?type=success&message=Bienvenidos"
```

4. Verifica que las notificaciones aparecen en el navegador

---

## 🎯 Criterios de Éxito

- [ ] SSE endpoint funciona correctamente
- [ ] Notificaciones llegan en tiempo real
- [ ] Diferentes tipos de notificaciones
- [ ] Reconexión automática funciona
- [ ] Broadcast a todos los usuarios
