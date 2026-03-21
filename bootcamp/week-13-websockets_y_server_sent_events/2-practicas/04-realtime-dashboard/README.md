# 📊 Práctica 04: Realtime Dashboard

## 🎯 Objetivo

Crear un dashboard con métricas en tiempo real combinando WebSocket y SSE. El dashboard mostrará datos de sistema, usuarios conectados y métricas personalizadas.

---

## 📋 Requisitos Previos

- Prácticas anteriores de WebSocket y SSE
- Teoría 05: Autenticación y Testing

---

## 🗂️ Estructura

```
04-realtime-dashboard/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py              # Servidor principal
    ├── metrics.py           # Generador de métricas
    └── templates/
        └── dashboard.html   # Dashboard interactivo
```

---

## 📝 Instrucciones

### Paso 1: Generador de métricas

Abre `starter/metrics.py` y descomenta el **Paso 1**.

Implementarás:
- Clase `MetricsCollector` que genera métricas
- Datos de CPU, memoria, conexiones
- Generador async para streaming

### Paso 2: Endpoint SSE para métricas

Abre `starter/main.py` y descomenta el **Paso 2**.

Crearás el endpoint `/metrics/stream` que:
- Envía métricas cada segundo
- Usa SSE para streaming

### Paso 3: WebSocket para actividad

Descomenta el **Paso 3**.

Implementarás WebSocket `/ws/activity` para:
- Notificar conexiones/desconexiones
- Mostrar actividad en tiempo real

### Paso 4: Dashboard HTML

El archivo `templates/dashboard.html` ya está listo. Descomenta los endpoints que lo soportan.

### Paso 5: Tests básicos

Opcional: Escribe tests para los endpoints.

---

## ✅ Verificación

1. Ejecuta el servidor:
```bash
cd starter
uv sync
uv run fastapi dev main.py
```

2. Abre http://localhost:8000

3. Verifica:
   - Métricas actualizándose cada segundo
   - Gráficos moviéndose
   - Contador de usuarios online
   - Actividad en tiempo real

---

## 🎯 Criterios de Éxito

- [ ] Métricas SSE funcionando
- [ ] WebSocket de actividad conectado
- [ ] Dashboard muestra datos en vivo
- [ ] Gráficos se actualizan
- [ ] Múltiples usuarios soportados
