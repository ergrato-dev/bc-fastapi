# ============================================
# FastAPI Application - Main Entry Point
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para configurar
# la aplicación FastAPI.
# ============================================

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import get_settings
from src.routers import health, tasks


# ============================================
# TODO 1: Lifespan handler (startup/shutdown)
# ============================================
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan handler.

    - Startup: Initialize database, connections
    - Shutdown: Close connections, cleanup
    """
    # Startup
    settings = get_settings()
    print(f"🚀 Starting application in {settings.environment} mode")

    # TODO: Inicializar base de datos
    # from src.database import init_db
    # init_db()

    yield

    # Shutdown
    print("👋 Shutting down application")
    # TODO: Cerrar conexiones si es necesario


# ============================================
# TODO 2: Crear instancia de FastAPI
# ============================================
settings = get_settings()

app = FastAPI(
    title="Tasks API",
    description="Production-ready Tasks API with Docker and CI/CD",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs" if not settings.is_production else None,
    redoc_url="/redoc" if not settings.is_production else None,
)


# ============================================
# TODO 3: Configurar CORS
# ============================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if not settings.is_production else ["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================
# TODO 4: Incluir routers
# ============================================
app.include_router(health.router)
app.include_router(tasks.router)


# ============================================
# TODO 5: Root endpoint
# ============================================
@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint with API information"""
    return {
        "name": "Tasks API",
        "version": "1.0.0",
        "docs": "/docs",
    }
