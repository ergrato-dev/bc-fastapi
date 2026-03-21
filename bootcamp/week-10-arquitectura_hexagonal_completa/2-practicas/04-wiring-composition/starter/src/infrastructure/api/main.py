"""
Punto de entrada de la aplicación - Composition Root.

Este es el COMPOSITION ROOT donde se ensambla toda
la aplicación FastAPI, conectando todas las capas.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI

from infrastructure.config import get_settings
from infrastructure.api.routers import tasks
from infrastructure.api.error_handlers import domain_error_handler
from infrastructure.api.dependencies import get_task_service
from domain.exceptions import DomainError


# ============================================
# PASO 1: Lifespan (startup/shutdown)
# ============================================
print("--- Paso 1: Lifespan ---")

# Descomenta las siguientes líneas:

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """
#     Lifecycle de la aplicación.
#     
#     - startup: Inicializar recursos
#     - shutdown: Liberar recursos
#     """
#     # Startup
#     settings = get_settings()
#     print(f"🚀 Starting {settings.app_name} v{settings.app_version}")
#     print(f"📦 Persistence: {settings.persistence_type}")
#     
#     yield  # La aplicación corre aquí
#     
#     # Shutdown
#     print("👋 Shutting down...")


# ============================================
# PASO 2: Factory de la aplicación
# ============================================
print("--- Paso 2: Factory create_app ---")

# Descomenta las siguientes líneas:

# def create_app() -> FastAPI:
#     """
#     Factory: Crear la aplicación FastAPI.
#     
#     Esta función es el corazón del Composition Root.
#     Crea y configura toda la aplicación.
#     """
#     settings = get_settings()
#     
#     # 1. Crear instancia de FastAPI
#     app = FastAPI(
#         title=settings.app_name,
#         version=settings.app_version,
#         description="Sistema de gestión de tareas - Arquitectura Hexagonal",
#         lifespan=lifespan,
#         debug=settings.debug,
#     )
#     
#     # 2. Registrar exception handlers
#     app.add_exception_handler(DomainError, domain_error_handler)
#     
#     # 3. Configurar dependency override
#     # Esto conecta el router con nuestras factories
#     from infrastructure.api.routers.tasks import get_task_service as router_dep
#     app.dependency_overrides[router_dep] = get_task_service
#     
#     # 4. Incluir routers
#     app.include_router(tasks.router)
#     
#     # 5. Health check
#     @app.get("/health", tags=["Health"])
#     async def health_check():
#         return {
#             "status": "healthy",
#             "app": settings.app_name,
#             "version": settings.app_version,
#         }
#     
#     return app


# ============================================
# PASO 3: Crear la aplicación
# ============================================
print("--- Paso 3: Crear app ---")

# Descomenta las siguientes líneas:

# app = create_app()


# ============================================
# PASO 4: Entry point para desarrollo
# ============================================
print("--- Paso 4: Entry point ---")

# Descomenta las siguientes líneas:

# if __name__ == "__main__":
#     import uvicorn
#     
#     settings = get_settings()
#     uvicorn.run(
#         "infrastructure.api.main:app",
#         host=settings.host,
#         port=settings.port,
#         reload=settings.debug,
#     )


# ============================================
# VERIFICACIÓN
# ============================================
print("\n--- Verificación de Main ---")
print("Para ejecutar: uv run uvicorn infrastructure.api.main:app --reload")
print("✅ Composition Root configurado")
