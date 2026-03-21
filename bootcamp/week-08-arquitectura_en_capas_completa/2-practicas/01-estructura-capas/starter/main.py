# ============================================
# PUNTO DE ENTRADA - MAIN
# ============================================
print("--- Main: Aplicación FastAPI ---")

# Este es el punto de entrada de la aplicación.
# Configura FastAPI e incluye los routers.

# Descomenta las siguientes líneas:

# from fastapi import FastAPI

# from config import get_settings
# from database import engine, Base
# from routers.categories import router as categories_router

# # Obtener configuración
# settings = get_settings()

# # Crear tablas
# Base.metadata.create_all(bind=engine)

# # Crear aplicación
# app = FastAPI(
#     title=settings.api_title,
#     version=settings.api_version
# )

# # Incluir routers
# app.include_router(categories_router)


# @app.get("/")
# def root():
#     """Endpoint raíz - health check."""
#     return {
#         "message": "Categories API",
#         "version": settings.api_version,
#         "docs": "/docs"
#     }


# ============================================
# INSTRUCCIONES DE EJECUCIÓN
# ============================================
# 1. Descomentar todo el código de este archivo
# 2. Descomentar código en los demás archivos
# 3. Ejecutar: uvicorn main:app --reload
# 4. Abrir: http://localhost:8000/docs
