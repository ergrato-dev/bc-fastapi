# 📡 Semana 13: WebSockets y Server-Sent Events

## 📋 Descripción

Esta semana exploramos la **comunicación en tiempo real** con FastAPI. Aprenderás a implementar WebSockets para comunicación bidireccional y Server-Sent Events (SSE) para streaming de datos del servidor al cliente.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Entender las diferencias entre HTTP, WebSockets y SSE
- ✅ Implementar endpoints WebSocket en FastAPI
- ✅ Gestionar conexiones múltiples con Connection Manager
- ✅ Crear salas de chat y broadcast de mensajes
- ✅ Implementar Server-Sent Events para streaming
- ✅ Manejar reconexión y heartbeats
- ✅ Autenticar conexiones WebSocket
- ✅ Testear aplicaciones en tiempo real

---

## 📚 Requisitos Previos

- Semana 11: Autenticación JWT
- Semana 12: Testing con pytest
- Conocimientos de async/await
- HTML/JavaScript básico (para clientes de prueba)

---

## 🗂️ Estructura de la Semana

```
week-13/
├── README.md                      # Este archivo
├── rubrica-evaluacion.md          # Criterios de evaluación
├── 0-assets/                      # Diagramas SVG
│   ├── 01-http-vs-ws-vs-sse.svg
│   ├── 02-websocket-lifecycle.svg
│   ├── 03-connection-manager.svg
│   ├── 04-chat-architecture.svg
│   └── 05-sse-flow.svg
├── 1-teoria/
│   ├── 01-comunicacion-tiempo-real.md
│   ├── 02-websockets-fastapi.md
│   ├── 03-connection-manager.md
│   ├── 04-server-sent-events.md
│   └── 05-autenticacion-testing.md
├── 2-practicas/
│   ├── 01-websocket-basico/
│   ├── 02-chat-rooms/
│   ├── 03-sse-notifications/
│   └── 04-realtime-dashboard/
├── 3-proyecto/
│   ├── README.md
│   ├── starter/
│   └── solution/
├── 4-recursos/
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 📝 Contenidos

### Teoría (1-teoria/)

| # | Tema | Descripción | Tiempo |
|---|------|-------------|--------|
| 01 | Comunicación en Tiempo Real | HTTP vs WebSocket vs SSE | 25 min |
| 02 | WebSockets en FastAPI | Endpoints, envío/recepción | 30 min |
| 03 | Connection Manager | Gestión de conexiones múltiples | 30 min |
| 04 | Server-Sent Events | Streaming unidireccional | 25 min |
| 05 | Autenticación y Testing | Seguridad y pruebas | 25 min |

### Prácticas (2-practicas/)

| # | Práctica | Descripción | Tiempo |
|---|----------|-------------|--------|
| 01 | WebSocket Básico | Echo server, primer WebSocket | 30 min |
| 02 | Chat Rooms | Salas de chat con broadcast | 45 min |
| 03 | SSE Notifications | Sistema de notificaciones | 35 min |
| 04 | Realtime Dashboard | Dashboard con datos en vivo | 40 min |

### Proyecto (3-proyecto/)

**Chat en Tiempo Real con Rooms**
- Sistema de chat completo
- Múltiples salas
- Usuarios autenticados
- Historial de mensajes
- Indicador de usuarios conectados

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| Teoría | 2h 15min |
| Prácticas | 2h 30min |
| Proyecto | 1h 30min |
| **Total** | **6h 15min** |

---

## 📌 Entregables

1. **Ejercicios de prácticas** completados
2. **Proyecto**: Chat en tiempo real funcional
3. **Tests**: WebSocket y SSE testeados
4. **Cliente HTML**: Interfaz funcional

---

## 🔗 Navegación

| Anterior | Siguiente |
|----------|-----------|
| [⬅️ Semana 12: Testing](../week-12/README.md) | [Semana 14: Rate Limiting ➡️](../week-14/README.md) |

---

## 🛠️ Stack Técnico

| Tecnología | Versión | Uso |
|------------|---------|-----|
| FastAPI | 0.115+ | WebSocket endpoints |
| Starlette | 0.41+ | WebSocket base |
| websockets | 13.0+ | Cliente Python |
| sse-starlette | 2.0+ | Server-Sent Events |
| pytest | 8.3+ | Testing |
| httpx | 0.28+ | Testing HTTP |
| pytest-asyncio | 0.24+ | Testing async |

---

## 💡 Conceptos Clave

- **WebSocket**: Protocolo full-duplex sobre TCP
- **SSE**: Streaming HTTP unidireccional (server → client)
- **Connection Manager**: Patrón para gestionar múltiples conexiones
- **Broadcast**: Enviar mensaje a todos los conectados
- **Room/Channel**: Agrupación lógica de conexiones
- **Heartbeat**: Ping/pong para mantener conexión viva
