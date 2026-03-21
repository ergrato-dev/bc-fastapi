# 🏥 Health Checks en FastAPI

## 📋 Contenido

1. [¿Qué son los Health Checks?](#qué-son-los-health-checks)
2. [Tipos de Health Checks](#tipos-de-health-checks)
3. [Implementación Básica](#implementación-básica)
4. [Health Checks Avanzados](#health-checks-avanzados)
5. [Integración con Orquestadores](#integración-con-orquestadores)
6. [Patrones y Mejores Prácticas](#patrones-y-mejores-prácticas)

---

## ¿Qué son los Health Checks?

Los **health checks** son endpoints que permiten verificar el estado de tu aplicación y sus dependencias.

### ¿Por qué son importantes?

```
Sin health checks:
┌──────────────────┐
│   Load Balancer  │
│                  │
│  ┌────┐ ┌────┐   │     Envía tráfico a instancia caída
│  │ ✅ │ │ 💀 │◀──┼──── Usuario recibe error 500
│  └────┘ └────┘   │
└──────────────────┘

Con health checks:
┌──────────────────┐
│   Load Balancer  │
│   /health ───────┼──── Verifica cada 10s
│  ┌────┐ ┌────┐   │
│  │ ✅ │ │ ❌ │   │     Detecta instancia caída
│  └─▲──┘ └────┘   │     Remueve del pool
│    │             │
│    └─────────────┼──── Solo envía tráfico aquí
└──────────────────┘
```

### Casos de Uso

| Componente | Uso del Health Check |
|------------|---------------------|
| **Load Balancer** | Decidir a qué instancias enviar tráfico |
| **Kubernetes** | Decidir si reiniciar un pod |
| **Docker Swarm** | Verificar contenedores saludables |
| **CI/CD** | Verificar deployment exitoso |
| **Monitoreo** | Alertar cuando algo falla |

---

## Tipos de Health Checks

### 1. Liveness Check

**¿La aplicación está viva?**

- Verifica que el proceso responde
- Si falla, el orquestador **reinicia** el contenedor
- Debe ser **rápido** y **simple**

```python
@app.get("/health/live")
async def liveness():
    """La aplicación está corriendo."""
    return {"status": "alive"}
```

### 2. Readiness Check

**¿La aplicación está lista para recibir tráfico?**

- Verifica que las dependencias están disponibles
- Si falla, el load balancer **deja de enviar tráfico** (pero no reinicia)
- Puede ser más **complejo**

```python
@app.get("/health/ready")
async def readiness():
    """La aplicación puede procesar requests."""
    db_ok = await check_database()
    cache_ok = await check_redis()
    
    if db_ok and cache_ok:
        return {"status": "ready"}
    
    raise HTTPException(status_code=503, detail="Not ready")
```

### 3. Startup Check

**¿La aplicación terminó de inicializar?**

- Usado en aplicaciones con inicialización lenta
- Evita que liveness mate la app antes de que arranque

```python
startup_complete = False

@asynccontextmanager
async def lifespan(app: FastAPI):
    global startup_complete
    # Inicialización lenta
    await load_ml_model()
    await warm_up_cache()
    startup_complete = True
    yield

@app.get("/health/startup")
async def startup():
    if startup_complete:
        return {"status": "started"}
    raise HTTPException(status_code=503, detail="Starting up")
```

### Comparación

| Tipo | Pregunta | Falla = | Complejidad |
|------|----------|---------|-------------|
| **Liveness** | ¿Está vivo? | Reiniciar | Simple |
| **Readiness** | ¿Puede trabajar? | No enviar tráfico | Media |
| **Startup** | ¿Terminó de arrancar? | Esperar | Simple |

---

## Implementación Básica

### Health Check Simple

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    """Basic health check."""
    return {"status": "healthy"}
```

### Con Información Adicional

```python
from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()

# Guardar tiempo de inicio
START_TIME = datetime.utcnow()

@app.get("/health")
async def health_check():
    """Health check con metadata."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "uptime_seconds": (datetime.utcnow() - START_TIME).total_seconds(),
        "version": os.getenv("APP_VERSION", "unknown"),
        "environment": os.getenv("ENVIRONMENT", "development"),
    }
```

---

## Health Checks Avanzados

### Verificar Dependencias

```python
# src/health.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from redis.asyncio import Redis
from pydantic import BaseModel
from enum import Enum

router = APIRouter(prefix="/health", tags=["health"])


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"


class ComponentHealth(BaseModel):
    name: str
    status: HealthStatus
    message: str | None = None
    latency_ms: float | None = None


class HealthResponse(BaseModel):
    status: HealthStatus
    components: list[ComponentHealth]
    timestamp: str


async def check_database(db_session) -> ComponentHealth:
    """Verifica conexión a base de datos."""
    import time
    start = time.perf_counter()
    
    try:
        await db_session.execute(text("SELECT 1"))
        latency = (time.perf_counter() - start) * 1000
        
        return ComponentHealth(
            name="database",
            status=HealthStatus.HEALTHY,
            latency_ms=round(latency, 2)
        )
    except Exception as e:
        return ComponentHealth(
            name="database",
            status=HealthStatus.UNHEALTHY,
            message=str(e)
        )


async def check_redis(redis: Redis) -> ComponentHealth:
    """Verifica conexión a Redis."""
    import time
    start = time.perf_counter()
    
    try:
        await redis.ping()
        latency = (time.perf_counter() - start) * 1000
        
        return ComponentHealth(
            name="redis",
            status=HealthStatus.HEALTHY,
            latency_ms=round(latency, 2)
        )
    except Exception as e:
        return ComponentHealth(
            name="redis",
            status=HealthStatus.UNHEALTHY,
            message=str(e)
        )


async def check_external_api(url: str) -> ComponentHealth:
    """Verifica API externa."""
    import httpx
    import time
    start = time.perf_counter()
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            latency = (time.perf_counter() - start) * 1000
            
            if response.status_code == 200:
                return ComponentHealth(
                    name="external_api",
                    status=HealthStatus.HEALTHY,
                    latency_ms=round(latency, 2)
                )
            else:
                return ComponentHealth(
                    name="external_api",
                    status=HealthStatus.DEGRADED,
                    message=f"Status {response.status_code}"
                )
    except Exception as e:
        return ComponentHealth(
            name="external_api",
            status=HealthStatus.UNHEALTHY,
            message=str(e)
        )
```

### Endpoint Completo

```python
# src/health.py (continuación)
from fastapi import Depends
from datetime import datetime
from src.database import get_db
from src.cache import get_redis

@router.get("/ready", response_model=HealthResponse)
async def readiness_check(
    db = Depends(get_db),
    redis = Depends(get_redis)
):
    """
    Readiness check - verifica todas las dependencias.
    
    Retorna 200 si está listo, 503 si no.
    """
    components = await asyncio.gather(
        check_database(db),
        check_redis(redis),
        check_external_api("https://api.example.com/health"),
    )
    
    # Determinar estado general
    statuses = [c.status for c in components]
    
    if all(s == HealthStatus.HEALTHY for s in statuses):
        overall = HealthStatus.HEALTHY
    elif any(s == HealthStatus.UNHEALTHY for s in statuses):
        overall = HealthStatus.UNHEALTHY
    else:
        overall = HealthStatus.DEGRADED
    
    response = HealthResponse(
        status=overall,
        components=components,
        timestamp=datetime.utcnow().isoformat()
    )
    
    if overall == HealthStatus.UNHEALTHY:
        raise HTTPException(status_code=503, detail=response.model_dump())
    
    return response


@router.get("/live")
async def liveness_check():
    """
    Liveness check - simple, solo verifica que el proceso responde.
    
    No debe verificar dependencias externas.
    """
    return {"status": "alive"}
```

### Respuesta de Ejemplo

```json
// GET /health/ready - 200 OK
{
  "status": "healthy",
  "components": [
    {
      "name": "database",
      "status": "healthy",
      "latency_ms": 2.34
    },
    {
      "name": "redis",
      "status": "healthy",
      "latency_ms": 0.89
    },
    {
      "name": "external_api",
      "status": "healthy",
      "latency_ms": 145.67
    }
  ],
  "timestamp": "2024-01-15T10:30:45.123456Z"
}

// GET /health/ready - 503 Service Unavailable
{
  "detail": {
    "status": "unhealthy",
    "components": [
      {
        "name": "database",
        "status": "unhealthy",
        "message": "Connection refused"
      },
      {
        "name": "redis",
        "status": "healthy",
        "latency_ms": 1.23
      }
    ],
    "timestamp": "2024-01-15T10:30:45.123456Z"
  }
}
```

---

## Integración con Orquestadores

### Kubernetes

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  template:
    spec:
      containers:
        - name: api
          image: my-fastapi-app:latest
          ports:
            - containerPort: 8000
          
          # Liveness: ¿Está vivo? Si no, reiniciar
          livenessProbe:
            httpGet:
              path: /health/live
              port: 8000
            initialDelaySeconds: 10
            periodSeconds: 15
            timeoutSeconds: 5
            failureThreshold: 3
          
          # Readiness: ¿Puede recibir tráfico?
          readinessProbe:
            httpGet:
              path: /health/ready
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3
          
          # Startup: ¿Terminó de arrancar?
          startupProbe:
            httpGet:
              path: /health/startup
              port: 8000
            initialDelaySeconds: 0
            periodSeconds: 5
            timeoutSeconds: 5
            failureThreshold: 30  # 30 * 5s = 150s máximo para arrancar
```

### Docker Compose

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/ready"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy

  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### AWS ELB / ALB

```python
# Health check endpoint para AWS
@app.get("/health")
async def health_for_elb():
    """
    AWS ELB espera:
    - 200-399 = healthy
    - Otro = unhealthy
    """
    return {"status": "ok"}
```

---

## Patrones y Mejores Prácticas

### 1. Separar Liveness y Readiness

```python
# ❌ MAL: Un solo endpoint para todo
@app.get("/health")
async def health():
    await check_database()  # Si DB cae, reinicia el pod innecesariamente
    return {"status": "ok"}


# ✅ BIEN: Separados
@app.get("/health/live")
async def liveness():
    return {"status": "alive"}  # Simple, rápido

@app.get("/health/ready")
async def readiness():
    await check_database()  # Verifica dependencias
    return {"status": "ready"}
```

### 2. Timeouts en Health Checks

```python
import asyncio

async def check_with_timeout(check_func, timeout: float = 5.0):
    """Ejecuta check con timeout."""
    try:
        return await asyncio.wait_for(check_func(), timeout=timeout)
    except asyncio.TimeoutError:
        return ComponentHealth(
            name=check_func.__name__,
            status=HealthStatus.UNHEALTHY,
            message=f"Timeout after {timeout}s"
        )
```

### 3. No Verificar Todo en Liveness

```python
# ❌ MAL: Liveness verifica dependencias externas
@app.get("/health/live")
async def liveness():
    await check_database()      # Si DB cae temporalmente...
    await check_redis()         # ...el pod se reinicia
    await check_external_api()  # ...innecesariamente
    return {"status": "alive"}


# ✅ BIEN: Liveness solo verifica que la app responde
@app.get("/health/live")
async def liveness():
    # Opcionalmente verificar memoria/CPU
    return {"status": "alive"}
```

### 4. Cachear Resultados de Health Checks

```python
from datetime import datetime, timedelta
from typing import Any

_health_cache: dict[str, Any] = {}
_cache_ttl = timedelta(seconds=10)


async def cached_health_check():
    """Health check con cache para evitar sobrecarga."""
    now = datetime.utcnow()
    
    if "result" in _health_cache:
        cached_at = _health_cache["timestamp"]
        if now - cached_at < _cache_ttl:
            return _health_cache["result"]
    
    # Ejecutar checks
    result = await perform_health_checks()
    
    # Cachear resultado
    _health_cache["result"] = result
    _health_cache["timestamp"] = now
    
    return result
```

### 5. Degraded State

```python
@app.get("/health/ready")
async def readiness():
    components = await check_all_components()
    
    critical = ["database"]  # Sin esto no funcionamos
    optional = ["redis", "external_api"]  # Podemos funcionar sin esto
    
    critical_ok = all(
        c.status == HealthStatus.HEALTHY 
        for c in components 
        if c.name in critical
    )
    
    if not critical_ok:
        # Crítico caído = no estamos listos
        raise HTTPException(status_code=503, detail="Critical dependency down")
    
    optional_ok = all(
        c.status == HealthStatus.HEALTHY 
        for c in components 
        if c.name in optional
    )
    
    if optional_ok:
        return {"status": "healthy", "components": components}
    else:
        # Funcionamos pero degradados
        return {"status": "degraded", "components": components}
```

### 6. Endpoint de Diagnóstico (Solo Dev/Admin)

```python
from fastapi import Depends, Security
from src.auth import get_admin_user

@app.get("/health/detailed")
async def detailed_health(admin = Security(get_admin_user)):
    """
    Health check detallado - solo para admins.
    Incluye información sensible para debugging.
    """
    return {
        "status": "healthy",
        "components": await check_all_components(),
        "system": {
            "python_version": sys.version,
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
        },
        "config": {
            "database_pool_size": settings.db_pool_size,
            "redis_url": settings.redis_url.split("@")[-1],  # Sin password
        }
    }
```

---

## Ejemplo Completo

```python
# src/routers/health.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import asyncio

from src.database import get_db
from src.schemas.health import HealthResponse, ComponentHealth, HealthStatus

router = APIRouter(prefix="/health", tags=["Health"])

START_TIME = datetime.utcnow()


@router.get("/live")
async def liveness():
    """Liveness probe - is the app alive?"""
    return {"status": "alive"}


@router.get("/ready", response_model=HealthResponse)
async def readiness(db: AsyncSession = Depends(get_db)):
    """Readiness probe - can the app handle traffic?"""
    
    components = []
    
    # Check database
    try:
        await db.execute(text("SELECT 1"))
        components.append(ComponentHealth(
            name="database",
            status=HealthStatus.HEALTHY
        ))
    except Exception as e:
        components.append(ComponentHealth(
            name="database",
            status=HealthStatus.UNHEALTHY,
            message=str(e)
        ))
    
    # Determine overall status
    if any(c.status == HealthStatus.UNHEALTHY for c in components):
        overall = HealthStatus.UNHEALTHY
        status_code = 503
    else:
        overall = HealthStatus.HEALTHY
        status_code = 200
    
    response = HealthResponse(
        status=overall,
        components=components,
        uptime_seconds=(datetime.utcnow() - START_TIME).total_seconds()
    )
    
    if status_code == 503:
        raise HTTPException(status_code=503, detail=response.model_dump())
    
    return response


# src/schemas/health.py
from pydantic import BaseModel
from enum import Enum

class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"

class ComponentHealth(BaseModel):
    name: str
    status: HealthStatus
    message: str | None = None

class HealthResponse(BaseModel):
    status: HealthStatus
    components: list[ComponentHealth]
    uptime_seconds: float
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Liveness** | ¿La app está viva? (simple, rápido) |
| **Readiness** | ¿Puede recibir tráfico? (verifica deps) |
| **Startup** | ¿Terminó de arrancar? |
| **503** | Status code cuando no está listo |
| **Degraded** | Funciona pero con capacidad reducida |

---

## 🔗 Recursos

- [Kubernetes Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Health Check Patterns](https://microservices.io/patterns/observability/health-check-api.html)
- [12 Factor App - Admin Processes](https://12factor.net/admin-processes)

---

*Fin de la teoría - Semana 14*
