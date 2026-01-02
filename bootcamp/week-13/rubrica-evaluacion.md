# 📊 Rúbrica de Evaluación - Semana 13

## WebSockets y Server-Sent Events

---

## 🎯 Competencias a Evaluar

| Competencia | Descripción |
|-------------|-------------|
| **CE1** | Implementar WebSockets en FastAPI |
| **CE2** | Gestionar conexiones múltiples |
| **CE3** | Implementar Server-Sent Events |
| **CE4** | Autenticar conexiones en tiempo real |
| **CE5** | Testear aplicaciones WebSocket/SSE |

---

## 📝 Evidencias de Aprendizaje

### 1. Conocimiento (30%) 🧠

#### Cuestionario Teórico

| Criterio | Excelente (10) | Bueno (8) | Suficiente (6) | Insuficiente (0-5) |
|----------|----------------|-----------|----------------|-------------------|
| Diferencias HTTP/WS/SSE | Explica correctamente las 3 tecnologías | Explica 2 correctamente | Explica 1 correctamente | No distingue |
| Ciclo de vida WebSocket | Describe handshake, comunicación, cierre | Describe 2 fases | Describe 1 fase | No comprende |
| Casos de uso | Identifica cuándo usar cada tecnología | Identifica 2 casos | Identifica 1 caso | No identifica |

### 2. Desempeño (40%) 💪

#### Prácticas Guiadas

| Práctica | Criterios | Puntos |
|----------|-----------|--------|
| **01-websocket-basico** | Echo server funcional, manejo de conexión/desconexión | 25 |
| **02-chat-rooms** | Múltiples salas, broadcast correcto, join/leave | 25 |
| **03-sse-notifications** | Stream funcional, reconexión, event types | 25 |
| **04-realtime-dashboard** | Datos en vivo, múltiples métricas, actualización | 25 |

**Escala de evaluación por práctica:**

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| Excelente | 23-25 | Completo, funcional, código limpio |
| Bueno | 18-22 | Funcional con mejoras menores |
| Suficiente | 15-17 | Funcionalidad básica |
| Insuficiente | 0-14 | No funciona o incompleto |

### 3. Producto (30%) 📦

#### Proyecto: Chat en Tiempo Real

| Criterio | Excelente (10) | Bueno (8) | Suficiente (6) | Insuficiente (0-5) |
|----------|----------------|-----------|----------------|-------------------|
| **Conexión WebSocket** | Handshake correcto, reconexión automática | Handshake correcto | Conexión básica | No conecta |
| **Salas de Chat** | Join/leave, múltiples salas, lista de usuarios | Múltiples salas funcionales | Una sala funcional | No implementa salas |
| **Mensajes** | Broadcast, privados, historial | Broadcast y privados | Solo broadcast | No envía mensajes |
| **Autenticación** | JWT en WebSocket, validación | Token validado | Autenticación básica | Sin autenticación |
| **Testing** | Tests unitarios y de integración | Tests de integración | Tests básicos | Sin tests |
| **Cliente HTML** | UI funcional, responsive, UX buena | UI funcional | UI básica | Sin cliente |

---

## 📋 Checklist de Evaluación

### WebSocket Básico
- [ ] Endpoint `/ws` funcional
- [ ] Recibe y envía mensajes
- [ ] Maneja desconexión gracefully
- [ ] Log de conexiones

### Connection Manager
- [ ] Clase ConnectionManager implementada
- [ ] Métodos connect/disconnect
- [ ] Broadcast a todos
- [ ] Send personal message

### Chat Rooms
- [ ] Múltiples salas
- [ ] Join/leave room
- [ ] Broadcast por sala
- [ ] Lista de usuarios por sala

### Server-Sent Events
- [ ] Endpoint SSE funcional
- [ ] Event types correctos
- [ ] Retry configurado
- [ ] Streaming de datos

### Autenticación
- [ ] Token en query param o header
- [ ] Validación de JWT
- [ ] Rechazo de conexiones inválidas
- [ ] Manejo de token expirado

### Testing
- [ ] Tests de conexión WebSocket
- [ ] Tests de envío/recepción
- [ ] Tests de broadcast
- [ ] Tests de SSE

---

## 🎯 Criterios de Aprobación

| Evidencia | Peso | Mínimo para Aprobar |
|-----------|------|---------------------|
| Conocimiento | 30% | 70% (21/30 puntos) |
| Desempeño | 40% | 70% (28/40 puntos) |
| Producto | 30% | 70% (21/30 puntos) |
| **Total** | **100%** | **70% (70/100 puntos)** |

---

## 📊 Rúbrica de Código

### Calidad del Código WebSocket

| Aspecto | Excelente | Bueno | Suficiente | Insuficiente |
|---------|-----------|-------|------------|--------------|
| **Manejo de errores** | Try/except completo, logging | Try/except básico | Manejo parcial | Sin manejo |
| **Async/await** | Uso correcto y eficiente | Uso correcto | Funcional | Incorrecto |
| **Tipado** | Type hints completos | Type hints en funciones | Parcial | Sin tipado |
| **Clean code** | Código limpio, documentado | Código limpio | Funcional | Difícil de leer |

---

## 🏆 Niveles de Logro

| Nivel | Puntuación | Descripción |
|-------|------------|-------------|
| 🥇 Sobresaliente | 90-100 | Domina comunicación en tiempo real |
| 🥈 Notable | 80-89 | Implementa correctamente WS y SSE |
| 🥉 Aprobado | 70-79 | Funcionalidad básica correcta |
| ❌ No Aprobado | 0-69 | No cumple requisitos mínimos |

---

## 📝 Notas Adicionales

- Los WebSockets deben manejar reconexión
- El código debe ser asíncrono (async/await)
- Se valora el manejo de errores y edge cases
- El cliente HTML debe ser funcional pero no necesita ser elaborado
- Los tests deben cubrir casos de éxito y error
