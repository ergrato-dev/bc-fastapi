# ============================================
# Blog API - Main Application
# ============================================
"""
Punto de entrada de la aplicación Blog API.

Arquitectura:
- Routers: Manejan HTTP (requests/responses)
- Services: Contienen lógica de negocio
- Models: Definen estructura de datos
- Schemas: Validación con Pydantic
"""

from fastapi import FastAPI

from config import settings
from database import engine, Base
from routers import authors_router, posts_router, tags_router


# Crear tablas
Base.metadata.create_all(bind=engine)

# Crear aplicación
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description=settings.API_DESCRIPTION
)

# Registrar routers
app.include_router(authors_router)
app.include_router(posts_router)
app.include_router(tags_router)


@app.get("/", tags=["Health"])
def root():
    """Health check y bienvenida"""
    return {
        "message": "Welcome to Blog API",
        "version": settings.API_VERSION,
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# ============================================
# Para ejecutar:
# uvicorn main:app --reload
# ============================================
