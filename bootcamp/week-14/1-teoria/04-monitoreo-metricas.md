# 📊 Monitoreo y Métricas con Prometheus

## 📋 Contenido

1. [¿Por qué Monitorear?](#por-qué-monitorear)
2. [Observabilidad: Los Tres Pilares](#observabilidad-los-tres-pilares)
3. [Introducción a Prometheus](#introducción-a-prometheus)
4. [Tipos de Métricas](#tipos-de-métricas)
5. [Prometheus FastAPI Instrumentator](#prometheus-fastapi-instrumentator)
6. [Métricas Personalizadas](#métricas-personalizadas)
7. [Dashboards y Alertas](#dashboards-y-alertas)

---

## ¿Por qué Monitorear?

En producción, necesitas responder preguntas como:

- ¿Cuántas requests está recibiendo mi API?
- ¿Cuál es el tiempo de respuesta promedio?
- ¿Hay errores? ¿Cuántos? ¿De qué tipo?
- ¿La base de datos está respondiendo lento?
- ¿Estamos cerca de quedarnos sin memoria?

![Monitoring Stack](../0-assets/04-monitoring-stack.svg)

### Sin Monitoreo vs Con Monitoreo

```
Sin monitoreo:
┌─────────┐     "La API está              ┌─────────┐
│  Usuario │───▶ lenta" ◀─── Queja ◀─────│ Soporte │
└─────────┘                               └─────────┘
     │                                         │
     │        ???                              │
     ▼                                         ▼
┌─────────┐                              "No sé qué pasa,
│   API   │                               voy a revisar logs"
└─────────┘                               (30 min después...)

Con monitoreo:
┌─────────┐                               ┌─────────────┐
│  Usuario │                               │  Dashboard  │
└─────────┘                               │ p95: 2.5s ⚠️│
     │                                    │ errors: 5%  │
     │                                    └─────────────┘
     ▼                                          │
┌─────────┐──────metrics────────▶ ┌────────────▼────────────┐
│   API   │                       │ DB connection pool full │
└─────────┘                       │ Scaling up...           │
                                  └─────────────────────────┘
```

---

## Observabilidad: Los Tres Pilares

![Observability Triad](../0-assets/05-observability-triad.svg)

### 1. Logs (Semana 14 - ✅)

**¿Qué pasó?** - Eventos discretos con contexto.

```json
{"event": "order_created", "order_id": 123, "user_id": 456}
```

### 2. Métricas (Esta sección)

**¿Cuánto?** - Valores numéricos agregables.

```
http_requests_total{method="GET", path="/api/users"} 1523
http_request_duration_seconds{quantile="0.95"} 0.25
```

### 3. Traces (Avanzado - fuera de scope)

**¿Dónde?** - Seguimiento de requests a través de servicios.

```
Request → API Gateway → Auth Service → User Service → Database
         [20ms]         [5ms]          [15ms]        [50ms]
```

---

## Introducción a Prometheus

**Prometheus** es el estándar de facto para métricas en aplicaciones modernas.

### Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                      PROMETHEUS                          │
│                                                          │
│  ┌──────────┐    scrape     ┌──────────┐                │
│  │ Prometheus│◀────────────│  FastAPI  │                │
│  │  Server   │   /metrics   │   App     │                │
│  └──────────┘               └──────────┘                │
│       │                                                  │
│       │ query                                            │
│       ▼                                                  │
│  ┌──────────┐                                           │
│  │ Grafana  │◀──── Dashboard                            │
│  └──────────┘                                           │
│       │                                                  │
│       │ alert                                            │
│       ▼                                                  │
│  ┌──────────┐                                           │
│  │Alertmanager│──── Email/Slack                         │
│  └──────────┘                                           │
└─────────────────────────────────────────────────────────┘
```

### Modelo Pull vs Push

```
PULL (Prometheus):
Prometheus ──scrape──▶ App /metrics
           cada 15s

PUSH (otros sistemas):
App ──push──▶ Metrics Server
    cada request
```

Prometheus usa **pull**: el servidor "raspa" (scrape) las métricas de tus aplicaciones periódicamente.

---

## Tipos de Métricas

### 1. Counter (Contador)

Valor que **solo incrementa** (o se resetea a 0).

```python
# Ejemplos
http_requests_total = 1523      # Total de requests
errors_total = 45               # Total de errores
orders_created_total = 890      # Órdenes creadas

# Nunca decrementa
# 1523 → 1524 → 1525 ✅
# 1523 → 1522 ❌
```

**Uso**: Contar eventos (requests, errores, jobs completados).

### 2. Gauge (Medidor)

Valor que puede **subir o bajar**.

```python
# Ejemplos
active_connections = 45         # Conexiones activas ahora
memory_usage_bytes = 512000000  # Uso de memoria actual
queue_size = 12                 # Items en cola

# Sube y baja
# 45 → 50 → 48 → 52 ✅
```

**Uso**: Estado actual (conexiones, memoria, temperatura).

### 3. Histogram (Histograma)

Distribución de valores en **buckets** (rangos).

```python
# Tiempo de respuesta en buckets
http_request_duration_seconds_bucket{le="0.1"} = 500   # ≤100ms
http_request_duration_seconds_bucket{le="0.5"} = 900   # ≤500ms
http_request_duration_seconds_bucket{le="1.0"} = 950   # ≤1s
http_request_duration_seconds_bucket{le="+Inf"} = 1000 # todos

# También incluye:
http_request_duration_seconds_sum = 234.5   # Suma total
http_request_duration_seconds_count = 1000  # Número de observaciones
```

**Uso**: Latencias, tamaños de respuesta.

### 4. Summary (Resumen)

Similar a histogram, pero calcula **percentiles** en el cliente.

```python
# Percentiles calculados
http_request_duration_seconds{quantile="0.5"} = 0.05   # p50 (mediana)
http_request_duration_seconds{quantile="0.9"} = 0.12   # p90
http_request_duration_seconds{quantile="0.99"} = 0.45  # p99
```

**Uso**: Cuando necesitas percentiles exactos (pero no agregables entre instancias).

### Comparación

| Tipo | Operaciones | Uso Principal | Agregable |
|------|-------------|---------------|-----------|
| Counter | Incrementar | Eventos totales | ✅ |
| Gauge | Set, Inc, Dec | Estado actual | ✅ |
| Histogram | Observe | Latencias (buckets) | ✅ |
| Summary | Observe | Latencias (percentiles) | ❌ |

---

## Prometheus FastAPI Instrumentator

La forma más fácil de añadir métricas a FastAPI.

### Instalación

```bash
uv add prometheus-fastapi-instrumentator
```

### Configuración Básica

```python
# src/main.py
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Instrumentar la aplicación
Instrumentator().instrument(app).expose(app)

# Esto añade automáticamente:
# - Endpoint /metrics
# - Métricas HTTP (requests, latencias, etc.)
```

### Métricas Incluidas Automáticamente

```
# Contador de requests por método, path y status
http_requests_total{method="GET", handler="/api/users", status="2xx"} 523

# Histograma de duración
http_request_duration_seconds_bucket{method="GET", handler="/api/users", le="0.1"} 400

# Tamaño de requests/responses
http_request_size_bytes_sum 1234567
http_response_size_bytes_sum 9876543

# Requests en progreso
http_requests_in_progress{method="GET", handler="/api/users"} 3
```

### Configuración Avanzada

```python
# src/metrics.py
from prometheus_fastapi_instrumentator import Instrumentator, metrics

def setup_metrics(app):
    """Configura métricas de Prometheus."""
    
    instrumentator = Instrumentator(
        should_group_status_codes=True,      # 2xx, 3xx, 4xx, 5xx
        should_ignore_untemplated=True,      # Ignorar paths no definidos
        should_respect_env_var=True,         # ENABLE_METRICS env var
        should_instrument_requests_inprogress=True,
        excluded_handlers=["/health", "/metrics"],  # No medir estos
        inprogress_name="http_requests_inprogress",
        inprogress_labels=True,
    )
    
    # Añadir métricas adicionales
    instrumentator.add(
        metrics.default(),          # Métricas por defecto
        metrics.latency(),          # Latencia detallada
        metrics.requests(),         # Contadores de requests
    )
    
    # Instrumentar y exponer
    instrumentator.instrument(app)
    instrumentator.expose(app, include_in_schema=False)  # Ocultar de OpenAPI
    
    return instrumentator
```

---

## Métricas Personalizadas

### Crear Métricas de Negocio

```python
# src/metrics.py
from prometheus_client import Counter, Histogram, Gauge

# Contador: órdenes creadas
orders_created = Counter(
    "orders_created_total",
    "Total de órdenes creadas",
    ["status", "payment_method"]
)

# Histograma: valor de órdenes
order_value = Histogram(
    "order_value_dollars",
    "Valor de órdenes en dólares",
    buckets=[10, 50, 100, 500, 1000, 5000]
)

# Gauge: usuarios activos
active_users = Gauge(
    "active_users_total",
    "Usuarios activos en este momento"
)

# Gauge: items en cola
queue_size = Gauge(
    "background_queue_size",
    "Items en cola de procesamiento",
    ["queue_name"]
)
```

### Usar las Métricas

```python
# src/services/order_service.py
from src.metrics import orders_created, order_value

async def create_order(order_data: OrderCreate) -> Order:
    order = await db.create_order(order_data)
    
    # Incrementar contador
    orders_created.labels(
        status="created",
        payment_method=order.payment_method
    ).inc()
    
    # Observar valor
    order_value.observe(order.total)
    
    return order


async def cancel_order(order_id: int) -> None:
    await db.cancel_order(order_id)
    
    orders_created.labels(
        status="cancelled",
        payment_method="n/a"
    ).inc()
```

### Métricas con Decoradores

```python
from prometheus_client import Counter, Histogram
import functools
import time

request_count = Counter(
    "function_calls_total", 
    "Total function calls",
    ["function"]
)

request_latency = Histogram(
    "function_duration_seconds",
    "Function duration",
    ["function"]
)


def track_metrics(func):
    """Decorador para trackear métricas de una función."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        request_count.labels(function=func.__name__).inc()
        
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            duration = time.perf_counter() - start
            request_latency.labels(function=func.__name__).observe(duration)
    
    return wrapper


# Uso
@track_metrics
async def process_payment(order_id: int) -> Payment:
    # ...
    pass
```

### Instrumentator con Métricas Custom

```python
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_fastapi_instrumentator.metrics import Info
from prometheus_client import Counter

# Métrica custom
failed_logins = Counter(
    "failed_login_attempts_total",
    "Failed login attempts",
    ["reason"]
)


def custom_metrics():
    """Añade métricas personalizadas al instrumentator."""
    
    def instrumentation(info: Info):
        # Acceder a request/response
        if info.modified_handler == "/auth/login":
            if info.response.status_code == 401:
                failed_logins.labels(reason="invalid_credentials").inc()
            elif info.response.status_code == 429:
                failed_logins.labels(reason="rate_limited").inc()
    
    return instrumentation


# Añadir al instrumentator
instrumentator.add(custom_metrics())
```

---

## Dashboards y Alertas

### Docker Compose con Prometheus + Grafana

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENABLE_METRICS=true

  prometheus:
    image: prom/prometheus:v2.48.0
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'

  grafana:
    image: grafana/grafana:10.2.0
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana

volumes:
  grafana_data:
```

### Configuración de Prometheus

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'fastapi'
    static_configs:
      - targets: ['api:8000']
    metrics_path: /metrics
```

### Queries Útiles en Prometheus/Grafana

```promql
# Requests por segundo
rate(http_requests_total[5m])

# Requests por segundo por endpoint
rate(http_requests_total{handler="/api/users"}[5m])

# Tasa de errores (%)
sum(rate(http_requests_total{status=~"5.."}[5m])) 
/ 
sum(rate(http_requests_total[5m])) * 100

# Latencia p95
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# Latencia p99 por endpoint
histogram_quantile(0.99, 
  sum(rate(http_request_duration_seconds_bucket[5m])) by (handler, le)
)

# Órdenes por minuto
rate(orders_created_total[1m]) * 60
```

### Alertas Básicas

```yaml
# prometheus_rules.yml
groups:
  - name: fastapi
    rules:
      # Alerta si tasa de errores > 5%
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) 
          / sum(rate(http_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }}"
      
      # Alerta si latencia p95 > 1s
      - alert: HighLatency
        expr: |
          histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High latency detected"
          description: "p95 latency is {{ $value }}s"
```

---

## Ejemplo Completo

```python
# src/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from prometheus_fastapi_instrumentator import Instrumentator

from src.metrics import setup_metrics, active_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    setup_metrics(app)
    yield
    # Shutdown


app = FastAPI(lifespan=lifespan)


# src/metrics.py
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram, Gauge

# Métricas de negocio
orders_total = Counter(
    "business_orders_total",
    "Total orders",
    ["status"]
)

order_processing_time = Histogram(
    "business_order_processing_seconds",
    "Order processing time",
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)

active_users = Gauge(
    "business_active_users",
    "Currently active users"
)


def setup_metrics(app: FastAPI):
    Instrumentator(
        excluded_handlers=["/health", "/metrics"]
    ).instrument(app).expose(app, include_in_schema=False)
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Prometheus** | Sistema de métricas pull-based |
| **Counter** | Valor que solo incrementa |
| **Gauge** | Valor que sube y baja |
| **Histogram** | Distribución en buckets |
| **Instrumentator** | Auto-instrumentación para FastAPI |
| **Grafana** | Visualización de métricas |

---

## 🔗 Recursos

- [Prometheus Documentation](https://prometheus.io/docs/)
- [prometheus-fastapi-instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)
- [Grafana FastAPI Dashboards](https://grafana.com/grafana/dashboards/)
- [RED Method](https://www.weave.works/blog/the-red-method-key-metrics-for-microservices-architecture/)

---

*Siguiente: [05 - Health Checks](05-health-checks.md)*
