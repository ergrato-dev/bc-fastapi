"""
Port: TaskRepository.

Define la interfaz para persistencia de tareas.
La implementación está en Infrastructure Layer.
"""

from typing import Protocol
from uuid import UUID
from dataclasses import dataclass

from domain.entities.task import Task
from domain.value_objects.task_status import TaskStatus, Priority


@dataclass
class TaskFilters:
    """Filtros para buscar tareas."""
    status: TaskStatus | None = None
    priority: Priority | None = None
    project_id: UUID | None = None
    assignee_id: UUID | None = None


class TaskRepository(Protocol):
    """
    Puerto: Repositorio de tareas.
    
    Define el contrato que debe cumplir cualquier
    implementación de persistencia de tareas.
    
    TODO: Implementar un adaptador que cumpla esta interfaz
    en infrastructure/persistence/task_repository.py
    """
    
    def save(self, task: Task) -> None:
        """
        Guardar o actualizar una tarea.
        
        Si la tarea existe (mismo id), actualiza.
        Si no existe, crea nueva.
        """
        ...
    
    def find_by_id(self, task_id: UUID) -> Task | None:
        """
        Buscar tarea por ID.
        
        Returns:
            Task si existe, None si no.
        """
        ...
    
    def find_all(
        self,
        filters: TaskFilters | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Task]:
        """
        Buscar tareas con filtros opcionales.
        
        Args:
            filters: Filtros a aplicar
            skip: Número de registros a saltar (paginación)
            limit: Número máximo de registros
            
        Returns:
            Lista de tareas que cumplen los filtros.
        """
        ...
    
    def delete(self, task_id: UUID) -> bool:
        """
        Eliminar tarea por ID.
        
        Returns:
            True si se eliminó, False si no existía.
        """
        ...
    
    def count(self, filters: TaskFilters | None = None) -> int:
        """
        Contar tareas que cumplen los filtros.
        
        Returns:
            Número de tareas.
        """
        ...
