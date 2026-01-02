# 🔌 Práctica 01: WebSocket Básico

## 🎯 Objetivo

Crear tu primer servidor WebSocket con FastAPI. Implementarás un echo server que recibe mensajes y los devuelve al cliente.

---

## 📋 Requisitos Previos

- Teoría 01: Comunicación en Tiempo Real
- Teoría 02: WebSockets en FastAPI

---

## 🗂️ Estructura

```
01-websocket-basico/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py              # Servidor WebSocket
    └── templates/
        └── index.html       # Cliente de prueba
```

---

## 📝 Instrucciones

### Paso 1: Configurar el proyecto

Abre `starter/pyproject.toml` y revisa las dependencias.

```bash
cd starter
uv sync
```

### Paso 2: Endpoint WebSocket básico

Abre `starter/main.py` y descomenta la sección del **Paso 2**.

Implementarás:
- Endpoint `/ws` que acepta conexiones
- Recibe mensajes de texto
- Responde con echo

### Paso 3: Manejo de conexión/desconexión

Descomenta la sección del **Paso 3**.

Agregarás:
- Log de conexiones
- Manejo de `WebSocketDisconnect`
- Mensaje de bienvenida

### Paso 4: Mensajes JSON estructurados

Descomenta la sección del **Paso 4**.

Implementarás:
- Recepción de JSON
- Procesamiento por tipo de mensaje
- Respuestas estructuradas

### Paso 5: Cliente HTML

El archivo `templates/index.html` ya está listo. Descomenta el endpoint que lo sirve.

---

## ✅ Verificación

1. Ejecuta el servidor:
```bash
uv run fastapi dev main.py
```

2. Abre http://localhost:8000 en el navegador

3. Prueba:
   - Enviar mensajes de texto
   - Ver respuestas del servidor
   - Desconectar y reconectar

---

## 🎯 Criterios de Éxito

- [ ] WebSocket acepta conexiones
- [ ] Echo funciona correctamente
- [ ] Maneja desconexiones sin errores
- [ ] Log de conexiones visible
- [ ] Cliente HTML funcional
