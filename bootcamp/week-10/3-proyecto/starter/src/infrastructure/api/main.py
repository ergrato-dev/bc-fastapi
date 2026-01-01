"""
Main - Composition Root de la aplicación.

TODO: Ensamblar toda la aplicación FastAPI.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI

from infrastructure.config import get_settings
from infrastructure.api.routers import tasks, projects, users
from infrastructure.api.error_handlers import domain_error_handler
from infrastructure.api import dependencies
from domain.exceptions import DomainError


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle de la aplicación."""
    settings = get_settings()
    print(f"🚀 Starting {settings.app_name} v{settings.app_version}")
    print(f"📦 Persistence: {settings.persistence_type}")
    
    yield
    
    print("👋 Shutting down...")


def create_app() -> FastAPI:
    """
    Factory: Crear la aplicación FastAPI.
    
    TODO: Implementar:
    1. Crear instancia de FastAPI
    2. Registrar exception handlers
    3. Configurar dependency_overrides para conectar services
    4. Incluir routers
    5. Agregar health check
    """
    settings = get_settings()
    
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Sistema de Gestión de Tareas - Arquitectura Hexagonal",
        lifespan=lifespan,
        debug=settings.debug,
    )
    
    # TODO: Registrar exception handler
    # app.add_exception_handler(DomainError, domain_error_handler)
    
    # TODO: Configurar dependency overrides
    # Conectar los placeholders de los routers con nuestras factories
    # app.dependency_overrides[tasks.get_task_service] = dependencies.get_task_service
    # app.dependency_overrides[projects.get_project_service] = dependencies.get_project_service
    # app.dependency_overrides[users.get_user_service] = dependencies.get_user_service
    
    # TODO: Incluir routers
    # app.include_router(tasks.router)
    # app.include_router(projects.router)
    # app.include_router(users.router)
    
    # Health check
    @app.get("/health", tags=["Health"])
    async def health_check():
        return {
            "status": "healthy",
            "app": settings.app_name,
            "version": settings.app_version,
        }
    
    return app


# Crear la aplicación
app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    settings = get_settings()
    uvicorn.run(
        "infrastructure.api.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
