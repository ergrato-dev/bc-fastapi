# 📊 Proyecto Semana 14: API con Observabilidad y Monitoreo

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplo Genérico de Referencia

> Los ejemplos usan **"Warehouse"** (Almacén) que NO está en el pool.
> **Debes adaptar TODO a tu dominio asignado.**

| Concepto | Ejemplo Genérico | Adapta a tu Dominio |
|----------|-----------------|---------------------|
| Business Metrics | `items_transferred_total` | `{your_action}_total` |
| Log Context | `zone_id`, `item_sku` | `{your_context_1}`, `{your_context_2}` |
| Health Check | `database`, `redis_cache` | `database`, `{your_service}` |

---

## 🎯 Objetivo

Implementar **observabilidad completa**:

- Logging estructurado con contexto
- Métricas de negocio con Prometheus
- Health checks detallados
- Rate limiting

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Logging Estructurado

```python
# Ejemplo genérico (Warehouse)
import structlog
from uuid import uuid4

def configure_logging():
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

logger = structlog.get_logger()

# Middleware para request context
@app.middleware("http")
async def add_request_context(request: Request, call_next):
    request_id = str(uuid4())
    
    # Bind context para todos los logs de este request
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(
        request_id=request_id,
        path=request.url.path,
        method=request.method,
    )
    
    logger.info("request_started")
    
    response = await call_next(request)
    
    logger.info(
        "request_completed",
        status_code=response.status_code
    )
    
    response.headers["X-Request-ID"] = request_id
    return response
```

### Logging en Servicios

```python
# Ejemplo genérico
class ItemService:
    def __init__(self, repository: IItemRepository):
        self.repository = repository
        self.logger = structlog.get_logger()
    
    async def transfer_item(
        self, 
        item_id: int, 
        target_zone_id: int, 
        quantity: int
    ) -> Item:
        # Log con contexto de negocio
        self.logger.info(
            "transfer_started",
            item_id=item_id,
            target_zone_id=target_zone_id,
            quantity=quantity
        )
        
        item = await self.repository.find_by_id(item_id)
        
        if not item:
            self.logger.warning(
                "transfer_failed",
                reason="item_not_found",
                item_id=item_id
            )
            raise ItemNotFoundError(item_id)
        
        # Bind contexto adicional
        self.logger.bind(
            item_sku=item.sku,
            source_zone_id=item.zone_id
        )
        
        if item.quantity < quantity:
            self.logger.warning(
                "transfer_failed",
                reason="insufficient_stock",
                available=item.quantity,
                requested=quantity
            )
            raise InsufficientStockError(item_id, item.quantity, quantity)
        
        # Realizar transferencia
        item.quantity -= quantity
        updated = await self.repository.save(item)
        
        self.logger.info(
            "transfer_completed",
            new_quantity=updated.quantity
        )
        
        return updated
```

### Métricas con Prometheus

```python
# Ejemplo genérico
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

# Métricas de negocio
ITEMS_TRANSFERRED = Counter(
    "warehouse_items_transferred_total",
    "Total items transferred between zones",
    ["source_zone", "target_zone"]
)

TRANSFER_DURATION = Histogram(
    "warehouse_transfer_duration_seconds",
    "Time spent processing transfers",
    buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

STOCK_LEVELS = Gauge(
    "warehouse_stock_level",
    "Current stock level by zone and item",
    ["zone_id", "item_sku"]
)

LOW_STOCK_ALERTS = Counter(
    "warehouse_low_stock_alerts_total",
    "Total low stock alerts triggered",
    ["zone_id"]
)

# Endpoint de métricas
@app.get("/metrics")
async def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

# Uso en servicio
class ItemService:
    async def transfer_item(self, ...):
        with TRANSFER_DURATION.time():
            # ... lógica de transferencia
            
            ITEMS_TRANSFERRED.labels(
                source_zone=str(item.zone_id),
                target_zone=str(target_zone_id)
            ).inc(quantity)
            
            STOCK_LEVELS.labels(
                zone_id=str(item.zone_id),
                item_sku=item.sku
            ).set(item.quantity)
            
            if item.quantity < 10:
                LOW_STOCK_ALERTS.labels(zone_id=str(item.zone_id)).inc()
```

### Health Checks

```python
# Ejemplo genérico
from enum import Enum
from pydantic import BaseModel

class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

class ComponentHealth(BaseModel):
    name: str
    status: HealthStatus
    latency_ms: float | None = None
    message: str | None = None

class HealthResponse(BaseModel):
    status: HealthStatus
    components: list[ComponentHealth]
    version: str

async def check_database() -> ComponentHealth:
    try:
        start = time.monotonic()
        async with get_session() as session:
            await session.execute(text("SELECT 1"))
        latency = (time.monotonic() - start) * 1000
        
        return ComponentHealth(
            name="database",
            status=HealthStatus.HEALTHY,
            latency_ms=latency
        )
    except Exception as e:
        return ComponentHealth(
            name="database",
            status=HealthStatus.UNHEALTHY,
            message=str(e)
        )

async def check_redis() -> ComponentHealth:
    try:
        start = time.monotonic()
        await redis.ping()
        latency = (time.monotonic() - start) * 1000
        
        return ComponentHealth(
            name="redis_cache",
            status=HealthStatus.HEALTHY,
            latency_ms=latency
        )
    except Exception as e:
        return ComponentHealth(
            name="redis_cache",
            status=HealthStatus.DEGRADED,  # No crítico
            message=str(e)
        )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    components = await asyncio.gather(
        check_database(),
        check_redis()
    )
    
    # Estado general basado en componentes
    if any(c.status == HealthStatus.UNHEALTHY for c in components):
        overall = HealthStatus.UNHEALTHY
    elif any(c.status == HealthStatus.DEGRADED for c in components):
        overall = HealthStatus.DEGRADED
    else:
        overall = HealthStatus.HEALTHY
    
    return HealthResponse(
        status=overall,
        components=components,
        version=settings.APP_VERSION
    )

@app.get("/health/live")
async def liveness():
    """Kubernetes liveness probe"""
    return {"status": "alive"}

@app.get("/health/ready")
async def readiness():
    """Kubernetes readiness probe"""
    db_health = await check_database()
    if db_health.status == HealthStatus.UNHEALTHY:
        raise HTTPException(503, "Database not ready")
    return {"status": "ready"}
```

### Rate Limiting

```python
# Ejemplo genérico
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Rate limit por endpoint
@app.post("/items/")
@limiter.limit("10/minute")  # 10 creaciones por minuto
async def create_item(request: Request, data: ItemCreate):
    ...

@app.get("/items/")
@limiter.limit("100/minute")  # 100 lecturas por minuto
async def list_items(request: Request):
    ...

# Rate limit personalizado por usuario
def get_user_key(request: Request) -> str:
    """Usa user_id del token si está autenticado"""
    if hasattr(request.state, "user"):
        return f"user:{request.state.user.id}"
    return get_remote_address(request)

@app.post("/items/{item_id}/transfer")
@limiter.limit("5/minute", key_func=get_user_key)
async def transfer_item(request: Request, item_id: int, ...):
    ...
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── observability/
│   ├── __init__.py
│   ├── logging.py
│   ├── metrics.py
│   └── health.py
├── middleware/
│   ├── __init__.py
│   ├── request_context.py
│   └── rate_limit.py
├── services/
├── routers/
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Logging estructurado | 15 |
| Métricas funcionan | 15 |
| Health checks | 10 |
| **Adaptación al Dominio** (35%) | |
| Métricas de negocio relevantes | 12 |
| Logs con contexto específico | 13 |
| Originalidad (no copia ejemplo) | 10 |
| **Calidad del Código** (25%) | |
| Rate limiting adecuado | 10 |
| Observabilidad útil | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No copies** las métricas "items_transferred/low_stock"
- ✅ **Diseña** métricas específicas de tu dominio
- ✅ **Crea** contextos de logging relevantes

---

## 📚 Recursos

- [structlog Documentation](https://www.structlog.org/)
- [Prometheus Python Client](https://github.com/prometheus/client_python)
- [SlowAPI Rate Limiting](https://slowapi.readthedocs.io/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
