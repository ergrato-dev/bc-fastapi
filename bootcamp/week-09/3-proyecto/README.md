# 📬 Proyecto: Notification Service

## 🎯 Objetivo

Construir un **sistema de notificaciones multi-canal** aplicando el patrón **Ports & Adapters** para mantener el dominio desacoplado de la infraestructura.

---

## 📋 Descripción

Crearás una API REST que permite enviar notificaciones a través de múltiples canales:

- 📧 **Email** - Envío de correos electrónicos
- 📱 **SMS** - Mensajes de texto
- 🔔 **Push** - Notificaciones push
- 🔗 **Webhook** - Llamadas HTTP a URLs externas

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                      │
│                   (FastAPI Routers, DTOs)                   │
├─────────────────────────────────────────────────────────────┤
│                     APPLICATION LAYER                       │
│                 (NotificationService, DTOs)                 │
├─────────────────────────────────────────────────────────────┤
│                       DOMAIN LAYER                          │
│              (Entities, Ports/Protocols)                    │
├─────────────────────────────────────────────────────────────┤
│                   INFRASTRUCTURE LAYER                      │
│        (Adapters: Email, SMS, Push, Webhook, DB)           │
└─────────────────────────────────────────────────────────────┘
```

---

## ⏱️ Duración Estimada

2 horas

---

## 📁 Estructura del Proyecto

```
starter/
├── pyproject.toml
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── src/
    ├── main.py
    ├── config.py
    ├── domain/
    │   ├── entities/
    │   │   └── notification.py
    │   └── ports/
    │       ├── notification_sender.py
    │       ├── notification_repository.py
    │       └── template_renderer.py
    ├── application/
    │   ├── services/
    │   │   └── notification_service.py
    │   └── dtos/
    │       └── notification_dtos.py
    ├── infrastructure/
    │   ├── adapters/
    │   │   ├── email_adapter.py
    │   │   ├── sms_adapter.py
    │   │   ├── push_adapter.py
    │   │   ├── webhook_adapter.py
    │   │   └── console_adapter.py
    │   ├── persistence/
    │   │   └── in_memory_repository.py
    │   └── templates/
    │       └── simple_renderer.py
    ├── presentation/
    │   ├── dependencies.py
    │   └── routers/
    │       └── notifications.py
    └── tests/
        ├── conftest.py
        ├── fakes/
        └── unit/
```

---

## 🚀 Instrucciones

### 1. Configurar el entorno

```bash
cd starter
cp .env.example .env
docker compose up -d
```

### 2. Implementar los Ports

Completa los TODOs en `src/domain/ports/`.

### 3. Implementar los Adapters

Completa los TODOs en `src/infrastructure/adapters/`.

### 4. Implementar el Service

Completa los TODOs en `src/application/services/notification_service.py`.

### 5. Configurar Dependencies

Completa los TODOs en `src/presentation/dependencies.py`.

### 6. Ejecutar tests

```bash
docker compose exec api uv run pytest -v
```

### 7. Probar la API

```bash
# Enviar notificación
curl -X POST http://localhost:8000/api/v1/notifications \
  -H "Content-Type: application/json" \
  -d '{"recipient": "user@example.com", "channel": "email", "message": "Hello!", "subject": "Test"}'

# Obtener notificación
curl http://localhost:8000/api/v1/notifications/1
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Ports definidos con Protocols | 5 |
| 4 Adapters implementados | 5 |
| Service usa solo Ports | 5 |
| Tests con fake adapters | 5 |
| API REST funcionando | 5 |
| Código limpio y documentado | 5 |
| **Total** | **30** |

---

## 📚 Recursos

- [Documentación de Protocols](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
