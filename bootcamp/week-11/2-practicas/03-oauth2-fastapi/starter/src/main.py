# main.py
"""
Aplicación FastAPI con OAuth2 Password Flow.

Esta app demuestra cómo implementar autenticación OAuth2.
"""

from fastapi import FastAPI

from src.auth.router import router as auth_router

app = FastAPI(
    title="OAuth2 Demo API",
    description="API con autenticación OAuth2 Password Flow",
    version="1.0.0",
)

# Incluir router de autenticación
app.include_router(auth_router)


@app.get("/")
async def root():
    """Endpoint público de bienvenida."""
    return {
        "message": "Welcome to OAuth2 Demo API",
        "docs": "/docs",
        "login": "/auth/token",
    }
