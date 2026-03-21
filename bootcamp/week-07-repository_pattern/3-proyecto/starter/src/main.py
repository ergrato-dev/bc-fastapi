# ============================================
# Task Manager API - Main
# ============================================
from fastapi import FastAPI

from .config import settings
from .database import engine
from .models import Base
from .routers import users_router, tasks_router

# Crear tablas
Base.metadata.create_all(bind=engine)

# Crear app
app = FastAPI(
    title=settings.app_name,
    description="API de gestión de tareas con Repository Pattern",
    version="1.0.0"
)

# Registrar routers
app.include_router(users_router)
app.include_router(tasks_router)


@app.get("/")
def root():
    """Health check"""
    return {"status": "ok", "app": settings.app_name}


@app.get("/health")
def health():
    """Health check detallado"""
    return {
        "status": "healthy",
        "database": "connected"
    }
