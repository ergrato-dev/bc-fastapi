"""
Factories de dependencias - Composition Root.

Este módulo es responsable de CREAR y CONECTAR
todas las dependencias de la aplicación.

Es parte del Composition Root junto con main.py.
"""

from functools import lru_cache

from domain.ports.task_repository import TaskRepository
from domain.ports.project_repository import ProjectRepository
from application.services.task_service import TaskService
from infrastructure.persistence.task_repository import InMemoryTaskRepository
from infrastructure.persistence.project_repository import InMemoryProjectRepository
from infrastructure.config import get_settings


# ============================================
# PASO 1: Factories de Repositories (Singleton)
# ============================================
print("--- Paso 1: Factories de Repositories ---")

# @lru_cache hace que sea singleton (una sola instancia)
# Esto es importante porque el repository mantiene estado

# Descomenta las siguientes líneas:

# @lru_cache
# def get_task_repository() -> TaskRepository:
#     """
#     Factory: Obtener TaskRepository.
#     
#     Usa @lru_cache para singleton.
#     Retorna el tipo abstracto (Port), no la implementación.
#     """
#     settings = get_settings()
#     
#     if settings.persistence_type == "memory":
#         return InMemoryTaskRepository()
#     
#     # Futuro: agregar más implementaciones
#     # elif settings.persistence_type == "sqlite":
#     #     return SQLiteTaskRepository(settings.database_url)
#     
#     return InMemoryTaskRepository()
# 
# 
# @lru_cache
# def get_project_repository() -> ProjectRepository:
#     """Factory: Obtener ProjectRepository."""
#     return InMemoryProjectRepository()


# ============================================
# PASO 2: Factory de TaskService
# ============================================
print("--- Paso 2: Factory de TaskService ---")

# El service NO es singleton porque es stateless
# Se crea nuevo en cada request (pero usa repos singleton)

# Descomenta las siguientes líneas:

# def get_task_service() -> TaskService:
#     """
#     Factory: Obtener TaskService.
#     
#     NO usa @lru_cache porque el service es stateless.
#     Compone el service con sus dependencias (repositories).
#     """
#     return TaskService(
#         task_repository=get_task_repository(),
#         project_repository=get_project_repository(),
#     )


# ============================================
# PASO 3: Reset para testing
# ============================================
print("--- Paso 3: Reset para testing ---")

# Descomenta las siguientes líneas:

# def reset_repositories() -> None:
#     """
#     Resetear repositories (para tests).
#     
#     Limpia el cache de lru_cache para crear nuevas instancias.
#     """
#     get_task_repository.cache_clear()
#     get_project_repository.cache_clear()


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Dependencies ---")
    print("✅ Factories definidas correctamente")
