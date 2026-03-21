"""
ProjectService - Orquestador de casos de uso de proyectos.
"""

from uuid import UUID

from domain.entities.project import Project
from domain.ports.project_repository import ProjectRepository
from domain.ports.task_repository import TaskRepository
from domain.ports.user_repository import UserRepository
from domain.exceptions import ProjectNotFoundError, UserNotFoundError, TaskNotFoundError

from application.commands.project_commands import CreateProjectCommand, AddTaskToProjectCommand
from application.dtos.project_dto import ProjectDTO, ProjectListDTO


class ProjectService:
    """Application Service para Project."""
    
    def __init__(
        self,
        project_repository: ProjectRepository,
        task_repository: TaskRepository,
        user_repository: UserRepository,
    ) -> None:
        self._project_repo = project_repository
        self._task_repo = task_repository
        self._user_repo = user_repository
    
    def create_project(self, command: CreateProjectCommand) -> ProjectDTO:
        """
        Caso de uso: Crear nuevo proyecto.
        
        TODO: Implementar:
        1. Validar que el owner (usuario) existe
        2. Crear la entidad Project usando Project.create()
        3. Guardar en el repositorio
        4. Retornar ProjectDTO
        """
        # TODO: Implementar
        pass
    
    def get_project(self, project_id: UUID) -> ProjectDTO:
        """
        Caso de uso: Obtener proyecto por ID.
        
        TODO: Implementar
        """
        # TODO: Implementar
        pass
    
    def list_projects(self, skip: int = 0, limit: int = 100) -> ProjectListDTO:
        """
        Caso de uso: Listar proyectos.
        
        TODO: Implementar
        """
        # TODO: Implementar
        pass
    
    def add_task_to_project(self, command: AddTaskToProjectCommand) -> None:
        """
        Caso de uso: Agregar tarea a proyecto.
        
        TODO: Implementar:
        1. Buscar proyecto
        2. Buscar tarea
        3. Asignar project_id a la tarea
        4. Guardar tarea
        """
        # TODO: Implementar
        pass
    
    def _to_dto(self, project: Project) -> ProjectDTO:
        """Convertir entidad Project a DTO."""
        return ProjectDTO(
            id=project.id,
            name=project.name,
            description=project.description,
            owner_id=project.owner_id,
            created_at=project.created_at,
            updated_at=project.updated_at,
        )
