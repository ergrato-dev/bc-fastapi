"""
Main - Punto de entrada de la aplicación.
"""
from fastapi import FastAPI

from src.config import settings
from src.presentation.routers import notifications_router


app = FastAPI(
    title="Notification Service",
    description="API de notificaciones con Ports & Adapters",
    version="1.0.0",
    debug=settings.debug,
)

# Registrar routers
app.include_router(notifications_router)


@app.get("/")
async def root():
    """Health check."""
    return {
        "status": "ok",
        "env": settings.env.value,
        "provider": settings.notification_provider,
    }


@app.get("/health")
async def health():
    """Health check detallado."""
    return {"status": "healthy"}
