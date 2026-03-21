"""
TaskService - Orchestrador de casos de uso.
"""

from uuid import UUID
from dataclasses import dataclass

from domain.ports.task_repository import TaskRepository
from domain.ports.project_repository import ProjectRepository


@dataclass
class CreateTaskCommand:
    """Comando para crear tarea."""
    title: str
    description: str
    project_id: UUID | None = None


@dataclass
class TaskDTO:
    """DTO de respuesta."""
    id: UUID
    title: str
    description: str
    status: str


class TaskService:
    """Orchestrador de casos de uso de tareas."""
    
    def __init__(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ) -> None:
        self._task_repo = task_repository
        self._project_repo = project_repository
    
    def create_task(self, command: CreateTaskCommand) -> TaskDTO:
        """Crear una nueva tarea."""
        from domain.entities.task import Task
        
        task = Task.create(
            title=command.title,
            description=command.description,
        )
        self._task_repo.save(task)
        
        return TaskDTO(
            id=task.id,
            title=task.title,
            description=task.description,
            status=task.status.value,
        )
    
    def get_tasks(self, skip: int = 0, limit: int = 100) -> list[TaskDTO]:
        """Obtener lista de tareas."""
        tasks = self._task_repo.find_all(skip=skip, limit=limit)
        return [
            TaskDTO(
                id=t.id,
                title=t.title,
                description=t.description,
                status=t.status.value,
            )
            for t in tasks
        ]
    
    def get_task(self, task_id: UUID) -> TaskDTO | None:
        """Obtener tarea por ID."""
        task = self._task_repo.find_by_id(task_id)
        if task is None:
            return None
        
        return TaskDTO(
            id=task.id,
            title=task.title,
            description=task.description,
            status=task.status.value,
        )
