# 📊 Práctica 04: Prometheus Metrics y Health Checks

## 🎯 Objetivos

- Configurar prometheus-fastapi-instrumentator
- Exponer métricas en /metrics
- Crear métricas personalizadas de negocio
- Implementar health checks (liveness/readiness)

---

## 📋 Descripción

En esta práctica implementaremos monitoreo completo usando Prometheus. Añadiremos métricas automáticas HTTP, métricas personalizadas de negocio y health checks para orquestadores como Kubernetes.

---

## ⏱️ Duración

**35 minutos**

---

## 📁 Estructura

```
04-prometheus-metrics/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py
    ├── metrics.py
    ├── health.py
    └── test_metrics.py
```

---

## 🚀 Pasos

### Paso 1: Instalar y Configurar Instrumentator

**Abre `starter/metrics.py`** y descomenta la sección del Paso 1.

El Instrumentator añade automáticamente:
- Contadores de requests HTTP
- Histogramas de latencia
- Requests en progreso

---

### Paso 2: Exponer Endpoint /metrics

**Abre `starter/main.py`** y descomenta la sección del Paso 2.

El endpoint `/metrics` expone métricas en formato Prometheus.

---

### Paso 3: Métricas Personalizadas

Descomenta la sección del Paso 3 en `metrics.py`.

Crea métricas de negocio:
- Counter: órdenes creadas
- Histogram: valor de órdenes
- Gauge: usuarios activos

---

### Paso 4: Health Checks

**Abre `starter/health.py`** y descomenta la sección del Paso 4.

Implementa:
- `/health/live` - Liveness check (simple)
- `/health/ready` - Readiness check (verifica dependencias)

---

### Paso 5: Ejecutar y Probar

1. Inicia el servidor:
```bash
cd starter
uv sync
uv run uvicorn main:app --reload
```

2. Verifica métricas:
```bash
curl http://localhost:8000/metrics
```

3. Haz requests para generar métricas:
```bash
curl http://localhost:8000/api/orders
curl http://localhost:8000/api/orders
curl http://localhost:8000/api/orders
```

4. Verifica health checks:
```bash
curl http://localhost:8000/health/live
curl http://localhost:8000/health/ready
```

5. Ejecuta tests:
```bash
uv run pytest test_metrics.py -v
```

---

## ✅ Verificación

Tu implementación está correcta si:

- [ ] `/metrics` retorna métricas en formato Prometheus
- [ ] Las métricas HTTP aparecen automáticamente
- [ ] `orders_created_total` incrementa con cada orden
- [ ] `/health/live` retorna 200
- [ ] `/health/ready` verifica dependencias
- [ ] Los tests pasan

---

## 🔍 Output de /metrics Esperado

```
# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",handler="/api/users",status="2xx"} 5.0

# HELP http_request_duration_seconds HTTP request duration
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{method="GET",handler="/api/users",le="0.1"} 5.0

# HELP orders_created_total Total orders created
# TYPE orders_created_total counter
orders_created_total{status="created"} 3.0
```

---

## 📚 Recursos

- [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)
- [Prometheus Metrics Types](https://prometheus.io/docs/concepts/metric_types/)
- [Kubernetes Health Checks](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
