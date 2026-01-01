"""
Dependencies - Factories para dependency injection.

TODO: Implementar las factories que conectan todo.
"""

from functools import lru_cache

from domain.ports.task_repository import TaskRepository
from domain.ports.project_repository import ProjectRepository
from domain.ports.user_repository import UserRepository

from application.services.task_service import TaskService
from application.services.project_service import ProjectService
from application.services.user_service import UserService

from infrastructure.persistence.task_repository import InMemoryTaskRepository
from infrastructure.persistence.project_repository import InMemoryProjectRepository
from infrastructure.persistence.user_repository import InMemoryUserRepository
from infrastructure.config import get_settings


# ============================================
# REPOSITORY FACTORIES (Singletons)
# ============================================

@lru_cache
def get_task_repository() -> TaskRepository:
    """Factory: TaskRepository."""
    # TODO: Implementar
    pass


@lru_cache
def get_project_repository() -> ProjectRepository:
    """Factory: ProjectRepository."""
    # TODO: Implementar
    pass


@lru_cache
def get_user_repository() -> UserRepository:
    """Factory: UserRepository."""
    # TODO: Implementar
    pass


# ============================================
# SERVICE FACTORIES
# ============================================

def get_task_service() -> TaskService:
    """
    Factory: TaskService.
    
    TODO: Implementar:
    - Crear TaskService con sus dependencias (repositories)
    """
    # TODO: Implementar
    pass


def get_project_service() -> ProjectService:
    """Factory: ProjectService."""
    # TODO: Implementar
    pass


def get_user_service() -> UserService:
    """Factory: UserService."""
    # TODO: Implementar
    pass


# ============================================
# RESET (para tests)
# ============================================

def reset_repositories() -> None:
    """Resetear todos los repositories (para tests)."""
    get_task_repository.cache_clear()
    get_project_repository.cache_clear()
    get_user_repository.cache_clear()
