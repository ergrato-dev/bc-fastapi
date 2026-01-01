"""
Port: TaskRepository - Interfaz de persistencia.
"""

from typing import Protocol
from uuid import UUID


class TaskRepository(Protocol):
    """Puerto para persistencia de tareas."""
    
    def save(self, task) -> None:
        """Guardar tarea."""
        ...
    
    def find_by_id(self, task_id: UUID):
        """Buscar por ID."""
        ...
    
    def find_all(self, skip: int = 0, limit: int = 100) -> list:
        """Listar tareas."""
        ...
    
    def delete(self, task_id: UUID) -> bool:
        """Eliminar tarea."""
        ...
