# ============================================
# MAIN - E-COMMERCE API
# ============================================

from fastapi import FastAPI

from config import get_settings
from database import engine, Base
from handlers import register_exception_handlers
from routers import (
    users_router,
    categories_router,
    products_router,
    orders_router
)

# Configuración
settings = get_settings()

# Crear tablas
Base.metadata.create_all(bind=engine)

# Crear aplicación
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description
)

# Registrar exception handlers
register_exception_handlers(app)

# Incluir routers
app.include_router(users_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(orders_router)


@app.get("/")
def root():
    """Health check y documentación."""
    return {
        "message": settings.api_title,
        "version": settings.api_version,
        "docs": "/docs",
        "endpoints": {
            "users": "/users/",
            "categories": "/categories/",
            "products": "/products/",
            "orders": "/orders/"
        }
    }


# ============================================
# INSTRUCCIONES DE USO
# ============================================
# 1. Ejecutar: uvicorn main:app --reload
# 2. Abrir: http://localhost:8000/docs
# 3. Flujo de prueba:
#    a. POST /users/ - Crear usuario
#    b. POST /categories/ - Crear categoría
#    c. POST /products/ - Crear productos
#    d. POST /orders/ - Crear pedido
#    e. PATCH /orders/{id}/cancel - Cancelar pedido
