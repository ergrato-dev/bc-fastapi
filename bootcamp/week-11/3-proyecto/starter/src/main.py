# main.py
"""
Sistema de Autenticación JWT - Proyecto Semana 11

Una API completa con autenticación OAuth2, JWT y RBAC.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import create_tables
from src.auth.router import router as auth_router
from src.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Crea las tablas al iniciar la app."""
    create_tables()
    yield


app = FastAPI(
    title="Auth System API",
    description="Sistema de autenticación con JWT, OAuth2 y RBAC",
    version="1.0.0",
    lifespan=lifespan,
)

# Routers
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/", tags=["Root"])
async def root():
    """Endpoint de bienvenida."""
    return {
        "message": "Welcome to Auth System API",
        "docs": "/docs",
        "endpoints": {
            "register": "POST /auth/register",
            "login": "POST /auth/token",
            "refresh": "POST /auth/refresh",
            "profile": "GET /users/me",
        },
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
