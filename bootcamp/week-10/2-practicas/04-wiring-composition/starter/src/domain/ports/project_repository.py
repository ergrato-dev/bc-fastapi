"""
Port: ProjectRepository - Interfaz de persistencia.
"""

from typing import Protocol
from uuid import UUID


class ProjectRepository(Protocol):
    """Puerto para persistencia de proyectos."""
    
    def save(self, project) -> None:
        """Guardar proyecto."""
        ...
    
    def find_by_id(self, project_id: UUID):
        """Buscar por ID."""
        ...
