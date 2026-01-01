"""
TaskService - Orquestador de casos de uso de tareas.

Este servicio coordina las operaciones relacionadas con tareas.
Recibe Commands/Queries y retorna DTOs.
"""

from uuid import UUID

from domain.entities.task import Task
from domain.ports.task_repository import TaskRepository, TaskFilters
from domain.ports.project_repository import ProjectRepository
from domain.ports.user_repository import UserRepository
from domain.value_objects.task_status import TaskStatus, Priority
from domain.exceptions import TaskNotFoundError, ProjectNotFoundError, UserNotFoundError

from application.commands.task_commands import (
    CreateTaskCommand,
    StartTaskCommand,
    CompleteTaskCommand,
    AssignTaskCommand,
    DeleteTaskCommand,
)
from application.queries.task_queries import GetTaskQuery, ListTasksQuery
from application.dtos.task_dto import TaskDTO, TaskListDTO


class TaskService:
    """
    Application Service para Task.
    
    Orquesta los casos de uso relacionados con tareas.
    Depende de Ports (interfaces), no de implementaciones concretas.
    """
    
    def __init__(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
        user_repository: UserRepository,
    ) -> None:
        self._task_repo = task_repository
        self._project_repo = project_repository
        self._user_repo = user_repository
    
    # ============================================
    # COMMANDS (WRITE)
    # ============================================
    
    def create_task(self, command: CreateTaskCommand) -> TaskDTO:
        """
        Caso de uso: Crear nueva tarea.
        
        TODO: Implementar:
        1. Validar que el proyecto existe (si se proporciona project_id)
        2. Convertir priority string a Priority enum
        3. Crear la entidad Task usando Task.create()
        4. Guardar en el repositorio
        5. Retornar TaskDTO
        """
        # TODO: Implementar
        pass
    
    def start_task(self, command: StartTaskCommand) -> TaskDTO:
        """
        Caso de uso: Iniciar tarea.
        
        TODO: Implementar:
        1. Buscar tarea por ID
        2. Lanzar TaskNotFoundError si no existe
        3. Llamar task.start()
        4. Guardar cambios
        5. Retornar TaskDTO
        """
        # TODO: Implementar
        pass
    
    def complete_task(self, command: CompleteTaskCommand) -> TaskDTO:
        """
        Caso de uso: Completar tarea.
        
        TODO: Implementar:
        1. Buscar tarea por ID
        2. Lanzar TaskNotFoundError si no existe
        3. Llamar task.complete()
        4. Guardar cambios
        5. Retornar TaskDTO
        """
        # TODO: Implementar
        pass
    
    def assign_task(self, command: AssignTaskCommand) -> TaskDTO:
        """
        Caso de uso: Asignar tarea a usuario.
        
        TODO: Implementar:
        1. Buscar tarea por ID
        2. Buscar usuario por ID
        3. Lanzar errores si no existen
        4. Llamar task.assign_to(user_id)
        5. Guardar cambios
        6. Retornar TaskDTO
        """
        # TODO: Implementar
        pass
    
    def delete_task(self, command: DeleteTaskCommand) -> bool:
        """
        Caso de uso: Eliminar tarea.
        
        TODO: Implementar:
        1. Verificar que la tarea existe
        2. Eliminar del repositorio
        3. Retornar True si se eliminó
        """
        # TODO: Implementar
        pass
    
    # ============================================
    # QUERIES (READ)
    # ============================================
    
    def get_task(self, query: GetTaskQuery) -> TaskDTO:
        """
        Caso de uso: Obtener tarea por ID.
        
        TODO: Implementar:
        1. Buscar tarea por ID
        2. Lanzar TaskNotFoundError si no existe
        3. Retornar TaskDTO
        """
        # TODO: Implementar
        pass
    
    def list_tasks(self, query: ListTasksQuery) -> TaskListDTO:
        """
        Caso de uso: Listar tareas con filtros.
        
        TODO: Implementar:
        1. Construir TaskFilters desde query
        2. Obtener tareas del repositorio
        3. Contar total
        4. Retornar TaskListDTO
        """
        # TODO: Implementar
        pass
    
    # ============================================
    # HELPERS
    # ============================================
    
    def _to_dto(self, task: Task) -> TaskDTO:
        """Convertir entidad Task a DTO."""
        return TaskDTO(
            id=task.id,
            title=task.title,
            description=task.description,
            status=task.status.value,
            priority=task.priority.name.lower(),
            project_id=task.project_id,
            assignee_id=task.assignee_id,
            due_date=task.due_date,
            created_at=task.created_at,
            updated_at=task.updated_at,
        )
    
    def _parse_priority(self, priority_str: str) -> Priority:
        """Convertir string a Priority enum."""
        mapping = {
            "low": Priority.LOW,
            "medium": Priority.MEDIUM,
            "high": Priority.HIGH,
            "urgent": Priority.URGENT,
        }
        return mapping.get(priority_str.lower(), Priority.MEDIUM)
    
    def _parse_status(self, status_str: str | None) -> TaskStatus | None:
        """Convertir string a TaskStatus enum."""
        if status_str is None:
            return None
        mapping = {
            "pending": TaskStatus.PENDING,
            "in_progress": TaskStatus.IN_PROGRESS,
            "completed": TaskStatus.COMPLETED,
            "cancelled": TaskStatus.CANCELLED,
        }
        return mapping.get(status_str.lower())
