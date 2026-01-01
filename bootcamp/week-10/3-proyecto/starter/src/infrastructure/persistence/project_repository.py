"""
InMemoryProjectRepository - Adaptador de persistencia en memoria.
"""

from uuid import UUID

from domain.entities.project import Project


class InMemoryProjectRepository:
    """
    Adaptador: Repositorio de proyectos en memoria.
    
    TODO: Implementar todos los métodos del protocolo ProjectRepository.
    """
    
    def __init__(self) -> None:
        self._projects: dict[UUID, Project] = {}
    
    def save(self, project: Project) -> None:
        """TODO: Implementar."""
        pass
    
    def find_by_id(self, project_id: UUID) -> Project | None:
        """TODO: Implementar."""
        pass
    
    def find_all(self, skip: int = 0, limit: int = 100) -> list[Project]:
        """TODO: Implementar."""
        pass
    
    def find_by_owner(self, owner_id: UUID) -> list[Project]:
        """TODO: Implementar."""
        pass
    
    def delete(self, project_id: UUID) -> bool:
        """TODO: Implementar."""
        pass
