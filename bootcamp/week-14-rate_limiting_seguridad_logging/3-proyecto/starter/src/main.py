"""
Secure Observable API - Main Application.

Este es el punto de entrada de la aplicación que integra:
- Rate Limiting
- Security Headers
- Structured Logging
- Prometheus Metrics
- Health Checks

TODO: Integrar todos los componentes.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

from src.config import get_settings
from src.database import init_db
from src.routers import tasks_router, auth_router
from src.security.rate_limit import limiter, rate_limit_exceeded_handler
from src.security.headers import SecurityHeadersMiddleware
from src.observability.logging import setup_logging, get_logger, RequestLoggingMiddleware
from src.observability.metrics import instrumentator
from src.observability.health import get_liveness, get_readiness, HealthStatus


settings = get_settings()


# ============================================
# Lifecycle
# ============================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifecycle manager - startup y shutdown.
    
    TODO: Añadir inicialización de componentes.
    """
    # Startup
    setup_logging()
    logger = get_logger("startup")
    logger.info("starting_application", environment=settings.environment)
    
    # Inicializar base de datos
    init_db()
    logger.info("database_initialized")
    
    yield
    
    # Shutdown
    logger.info("shutting_down_application")


# ============================================
# Application
# ============================================

app = FastAPI(
    title="Secure Observable Task API",
    description="API de gestión de tareas con seguridad y observabilidad",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
)


# ============================================
# TODO 1: Configurar Rate Limiting
# ============================================
# Añadir estado del limiter y handler de excepciones

# TODO: Descomentar
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)


# ============================================
# TODO 2: Configurar CORS
# ============================================
# Configurar CORS con los orígenes desde settings

# TODO: Descomentar y configurar
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.allowed_origins_list,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
#     expose_headers=["X-Request-ID", "X-RateLimit-Limit", "X-RateLimit-Remaining"],
# )


# ============================================
# TODO 3: Añadir Security Headers Middleware
# ============================================

# TODO: Descomentar
# app.add_middleware(SecurityHeadersMiddleware)


# ============================================
# TODO 4: Añadir Request Logging Middleware
# ============================================

# TODO: Descomentar
# app.add_middleware(RequestLoggingMiddleware)


# ============================================
# TODO 5: Configurar Prometheus Metrics
# ============================================

# TODO: Descomentar para configuración avanzada
# instrumentator.instrument(app).expose(
#     app,
#     endpoint="/metrics",
#     include_in_schema=True,
#     tags=["monitoring"],
# )

# Versión básica
instrumentator.instrument(app).expose(app)


# ============================================
# Routers
# ============================================

app.include_router(tasks_router)
app.include_router(auth_router)


# ============================================
# Health Check Endpoints
# ============================================

@app.get("/health/live", tags=["health"])
async def liveness():
    """
    Liveness probe - verifica si la aplicación está corriendo.
    
    Kubernetes usa esto para saber si debe reiniciar el container.
    """
    result = await get_liveness()
    return JSONResponse(
        content=result,
        status_code=200 if result["status"] == HealthStatus.HEALTHY else 503,
    )


@app.get("/health/ready", tags=["health"])
async def readiness():
    """
    Readiness probe - verifica si puede recibir tráfico.
    
    Kubernetes usa esto para saber si debe enviar tráfico.
    """
    result = await get_readiness()
    
    if result["status"] == HealthStatus.UNHEALTHY:
        status_code = 503
    else:
        status_code = 200
    
    return JSONResponse(content=result, status_code=status_code)


# ============================================
# Root Endpoint
# ============================================

@app.get("/", tags=["root"])
async def root():
    """Endpoint raíz con información de la API."""
    return {
        "service": "Secure Observable Task API",
        "version": "1.0.0",
        "environment": settings.environment,
        "docs": "/docs" if settings.debug else "disabled",
        "endpoints": {
            "tasks": "/tasks",
            "auth": "/auth/login",
            "health": {
                "liveness": "/health/live",
                "readiness": "/health/ready",
            },
            "metrics": "/metrics",
        },
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
