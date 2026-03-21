"""
InMemoryProjectRepository - Adaptador de persistencia.
"""

from uuid import UUID


class InMemoryProjectRepository:
    """Adaptador: Repository de proyectos en memoria."""
    
    def __init__(self) -> None:
        self._projects: dict[UUID, object] = {}
    
    def save(self, project) -> None:
        self._projects[project.id] = project
    
    def find_by_id(self, project_id: UUID):
        return self._projects.get(project_id)
