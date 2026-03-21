# ============================================
# PASO 6: Main - App con Service Layer
# ============================================
"""
Punto de entrada de la aplicación.

Estructura final:
- main.py: Configuración de FastAPI
- database.py: Configuración de DB
- models.py: Modelos SQLAlchemy
- schemas.py: Schemas Pydantic
- services/: Lógica de negocio
- routers/: Endpoints HTTP
"""

from fastapi import FastAPI

from database import engine, Base
from routers import authors, posts


# Crear tablas
Base.metadata.create_all(bind=engine)

# Crear aplicación
app = FastAPI(
    title="Blog API",
    description="API con arquitectura Service Layer",
    version="1.0.0"
)


# ============================================
# Registrar routers
# ============================================
# Descomenta cuando hayas completado los routers:

# app.include_router(authors.router)
# app.include_router(posts.router)


@app.get("/")
def root():
    """Health check"""
    return {
        "status": "healthy",
        "message": "Blog API con Service Layer",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


# ============================================
# Para ejecutar:
# uvicorn main:app --reload
# ============================================
