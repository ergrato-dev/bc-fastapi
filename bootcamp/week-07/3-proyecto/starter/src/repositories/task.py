# ============================================
# Task Repository
# ============================================
from sqlalchemy import select
from sqlalchemy.orm import Session

from .base import BaseRepository
from ..models.task import Task, Priority


class TaskRepository(BaseRepository[Task]):
    """
    Repositorio específico para tareas.
    
    Hereda operaciones CRUD de BaseRepository
    y añade métodos específicos con filtros.
    
    TODO: Implementar métodos:
    - get_by_user(user_id) -> list[Task]
    - get_completed(user_id?) -> list[Task]
    - get_pending(user_id?) -> list[Task]
    - get_by_priority(priority, user_id?) -> list[Task]
    - count_by_user(user_id) -> int
    - count_pending(user_id?) -> int
    """
    
    def __init__(self, db: Session):
        super().__init__(db, Task)
    
    def get_by_user(self, user_id: int) -> list[Task]:
        """Obtiene todas las tareas de un usuario"""
        # TODO: Implementar
        pass
    
    def get_completed(self, user_id: int | None = None) -> list[Task]:
        """
        Obtiene tareas completadas.
        Si se pasa user_id, filtra por usuario.
        """
        # TODO: Implementar con filtro opcional
        pass
    
    def get_pending(self, user_id: int | None = None) -> list[Task]:
        """
        Obtiene tareas pendientes (no completadas).
        Si se pasa user_id, filtra por usuario.
        """
        # TODO: Implementar con filtro opcional
        pass
    
    def get_by_priority(
        self,
        priority: Priority,
        user_id: int | None = None
    ) -> list[Task]:
        """
        Obtiene tareas por prioridad.
        Si se pasa user_id, filtra por usuario.
        """
        # TODO: Implementar con filtro opcional
        pass
    
    def count_by_user(self, user_id: int) -> int:
        """Cuenta tareas de un usuario"""
        # TODO: Implementar
        pass
    
    def count_pending(self, user_id: int | None = None) -> int:
        """
        Cuenta tareas pendientes.
        Si se pasa user_id, filtra por usuario.
        """
        # TODO: Implementar
        pass
