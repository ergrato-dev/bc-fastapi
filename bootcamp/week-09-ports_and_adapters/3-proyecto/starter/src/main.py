"""
Main - Punto de entrada de la aplicación.
"""
from fastapi import FastAPI

from src.config import settings
from src.presentation.routers import notifications_router

app = FastAPI(
    title="Notification Service",
    description="API de notificaciones multi-canal con Ports & Adapters",
    version="1.0.0",
    debug=settings.debug,
)

# Routers
app.include_router(notifications_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Health check."""
    return {
        "service": "notification-service",
        "status": "ok",
        "env": settings.env.value,
    }


@app.get("/health")
async def health():
    """Health check detallado."""
    return {
        "status": "healthy",
        "provider": settings.notification_provider,
    }
