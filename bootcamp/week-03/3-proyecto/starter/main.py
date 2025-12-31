"""
API de Catálogo de Productos - Main
===================================

Punto de entrada de la aplicación.
"""

from fastapi import FastAPI
from routers import categories, products

app = FastAPI(
    title="API de Catálogo de Productos",
    description="API completa con CRUD, filtrado, paginación y ordenamiento",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Incluir routers
app.include_router(categories.router)
app.include_router(products.router)


@app.get("/", tags=["Root"])
async def root():
    """Endpoint raíz"""
    return {
        "message": "API de Catálogo de Productos",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health", tags=["Root"])
async def health_check():
    """Health check"""
    return {"status": "healthy"}
