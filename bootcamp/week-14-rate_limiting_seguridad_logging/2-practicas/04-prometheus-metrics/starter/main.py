"""
Prometheus Metrics Practice - Main Application.

Esta aplicación demuestra:
- Instrumentación automática con Prometheus
- Métricas personalizadas de negocio
- Health checks (liveness/readiness)
"""

import random
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from metrics import (
    instrumentator,
    record_order_created,
    record_order_value,
    set_active_users,
    user_logged_in,
)
from health import get_liveness, get_readiness, HealthStatus


# ============================================
# PASO 2: Configurar Aplicación con Métricas
# ============================================
print("--- Paso 2: Configurar App con Prometheus ---")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager para la aplicación."""
    # Startup: inicializar métricas
    set_active_users(0)
    print("📊 Métricas inicializadas")
    yield
    # Shutdown
    print("📊 Cerrando aplicación")


app = FastAPI(
    title="Prometheus Metrics API",
    description="API con métricas Prometheus y health checks",
    version="1.0.0",
    lifespan=lifespan,
)


# Instrumentar la aplicación con Prometheus
# El método instrument expone automáticamente /metrics
# Descomenta las siguientes líneas:
# instrumentator.instrument(app).expose(
#     app,
#     endpoint="/metrics",
#     include_in_schema=True,  # Incluir en OpenAPI docs
#     tags=["monitoring"],
# )

# Versión simple para que funcione:
instrumentator.instrument(app).expose(app)


# ============================================
# Health Check Endpoints
# ============================================

@app.get(
    "/health/live",
    tags=["health"],
    summary="Liveness check",
    description="Verifica si la aplicación está corriendo",
)
async def liveness():
    """
    Liveness probe para Kubernetes.
    
    - Simple y rápido
    - Si falla, el container se reinicia
    """
    result = await get_liveness()
    return JSONResponse(
        content=result,
        status_code=200 if result["status"] == HealthStatus.HEALTHY else 503,
    )


@app.get(
    "/health/ready",
    tags=["health"],
    summary="Readiness check",
    description="Verifica si la aplicación puede recibir tráfico",
)
async def readiness():
    """
    Readiness probe para Kubernetes.
    
    - Verifica todas las dependencias
    - Si falla, no recibe tráfico pero NO se reinicia
    """
    result = await get_readiness()
    
    if result["status"] == HealthStatus.HEALTHY:
        status_code = 200
    elif result["status"] == HealthStatus.DEGRADED:
        status_code = 200  # Degraded pero funcional
    else:
        status_code = 503
    
    return JSONResponse(content=result, status_code=status_code)


# ============================================
# API Endpoints (Generan métricas)
# ============================================

@app.get("/api/users", tags=["api"])
async def list_users():
    """Lista usuarios (genera métricas HTTP automáticas)."""
    return {"users": ["alice", "bob", "charlie"]}


@app.get("/api/users/{user_id}", tags=["api"])
async def get_user(user_id: int):
    """Obtiene un usuario por ID."""
    return {"id": user_id, "name": f"User {user_id}"}


@app.post("/api/orders", tags=["api"])
async def create_order():
    """
    Crea una orden (registra métricas de negocio).
    
    Esta función demuestra cómo registrar métricas personalizadas
    cuando ocurren eventos de negocio.
    """
    # Simular creación de orden
    order_id = random.randint(1000, 9999)
    order_value = random.uniform(10, 500)
    
    # Registrar métricas de negocio
    # Descomenta las siguientes líneas cuando actives las métricas:
    # record_order_created(status="created")
    # record_order_value(order_value)
    
    return {
        "order_id": order_id,
        "value": round(order_value, 2),
        "status": "created",
    }


@app.post("/api/auth/login", tags=["api"])
async def login():
    """
    Simula login (actualiza gauge de usuarios activos).
    """
    # Registrar usuario activo
    user_logged_in()
    
    return {"status": "logged_in", "token": "fake-jwt-token"}


@app.get("/api/slow", tags=["api"])
async def slow_endpoint():
    """
    Endpoint lento para ver métricas de latencia.
    
    El histograma de latencia mostrará valores más altos.
    """
    import asyncio
    
    # Simular operación lenta
    await asyncio.sleep(random.uniform(0.1, 0.5))
    
    return {"status": "completed", "operation": "slow"}


# ============================================
# Root Endpoint
# ============================================

@app.get("/", tags=["root"])
async def root():
    """Endpoint raíz con información de la API."""
    return {
        "service": "Prometheus Metrics API",
        "version": "1.0.0",
        "endpoints": {
            "metrics": "/metrics",
            "health": {
                "liveness": "/health/live",
                "readiness": "/health/ready",
            },
            "api": ["/api/users", "/api/orders", "/api/auth/login"],
        },
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
