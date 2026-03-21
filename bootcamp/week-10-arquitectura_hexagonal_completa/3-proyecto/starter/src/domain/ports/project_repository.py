"""
Port: ProjectRepository.

Define la interfaz para persistencia de proyectos.
"""

from typing import Protocol
from uuid import UUID

from domain.entities.project import Project


class ProjectRepository(Protocol):
    """
    Puerto: Repositorio de proyectos.
    
    TODO: Implementar un adaptador que cumpla esta interfaz
    en infrastructure/persistence/project_repository.py
    """
    
    def save(self, project: Project) -> None:
        """Guardar o actualizar un proyecto."""
        ...
    
    def find_by_id(self, project_id: UUID) -> Project | None:
        """Buscar proyecto por ID."""
        ...
    
    def find_all(self, skip: int = 0, limit: int = 100) -> list[Project]:
        """Listar todos los proyectos."""
        ...
    
    def find_by_owner(self, owner_id: UUID) -> list[Project]:
        """Buscar proyectos por propietario."""
        ...
    
    def delete(self, project_id: UUID) -> bool:
        """Eliminar proyecto por ID."""
        ...
