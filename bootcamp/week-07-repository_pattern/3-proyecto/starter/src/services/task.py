# ============================================
# Task Service
# ============================================
from datetime import datetime

from ..models.task import Task, Priority
from ..schemas.task import TaskCreate, TaskUpdate
from ..unit_of_work import UnitOfWork
from .user import UserNotFoundError


class TaskNotFoundError(Exception):
    """Tarea no encontrada"""
    pass


class TaskService:
    """
    Servicio de tareas con lógica de negocio.
    
    Usa UnitOfWork para acceder a repositorios.
    
    TODO: Implementar métodos:
    - create_task(data) -> Task
    - get_task(id) -> Task
    - get_tasks(filters) -> list[Task]
    - get_user_tasks(user_id) -> list[Task]
    - update_task(id, data) -> Task
    - delete_task(id) -> None
    - complete_task(id) -> Task
    - reopen_task(id) -> Task
    """
    
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    def create_task(self, data: TaskCreate) -> Task:
        """
        Crea una nueva tarea.
        
        Validaciones:
        - El usuario (user_id) debe existir
        """
        # TODO: Implementar
        # 1. Verificar que el usuario existe
        # 2. Crear Task con los datos
        # 3. Agregar via uow.tasks.add()
        pass
    
    def get_task(self, task_id: int) -> Task:
        """
        Obtiene tarea por ID.
        
        Raises:
            TaskNotFoundError: Si no existe
        """
        # TODO: Implementar
        pass
    
    def get_tasks(
        self,
        skip: int = 0,
        limit: int = 100,
        completed: bool | None = None,
        priority: Priority | None = None
    ) -> list[Task]:
        """
        Obtiene tareas con filtros opcionales.
        
        Args:
            skip: Offset para paginación
            limit: Límite de resultados
            completed: Filtrar por completadas/pendientes
            priority: Filtrar por prioridad
        """
        # TODO: Implementar con filtros
        pass
    
    def get_user_tasks(self, user_id: int) -> list[Task]:
        """
        Obtiene todas las tareas de un usuario.
        
        Raises:
            UserNotFoundError: Si el usuario no existe
        """
        # TODO: Implementar
        pass
    
    def update_task(self, task_id: int, data: TaskUpdate) -> Task:
        """
        Actualiza tarea existente.
        
        Si se marca como completada, establece completed_at.
        Si se reabre, limpia completed_at.
        """
        # TODO: Implementar
        pass
    
    def delete_task(self, task_id: int) -> None:
        """
        Elimina tarea.
        
        Raises:
            TaskNotFoundError: Si no existe
        """
        # TODO: Implementar
        pass
    
    def complete_task(self, task_id: int) -> Task:
        """
        Marca tarea como completada.
        
        Establece is_completed=True y completed_at=now
        """
        # TODO: Implementar
        pass
    
    def reopen_task(self, task_id: int) -> Task:
        """
        Reabre tarea completada.
        
        Establece is_completed=False y completed_at=None
        """
        # TODO: Implementar
        pass
