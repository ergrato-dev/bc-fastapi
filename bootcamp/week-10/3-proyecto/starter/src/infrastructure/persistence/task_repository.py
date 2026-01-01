"""
InMemoryTaskRepository - Adaptador de persistencia en memoria.

Implementa el puerto TaskRepository usando un diccionario en memoria.
"""

from uuid import UUID

from domain.entities.task import Task
from domain.ports.task_repository import TaskFilters


class InMemoryTaskRepository:
    """
    Adaptador: Repositorio de tareas en memoria.
    
    Implementa el protocolo TaskRepository.
    Almacena las tareas en un diccionario.
    
    TODO: Implementar todos los métodos del protocolo.
    """
    
    def __init__(self) -> None:
        self._tasks: dict[UUID, Task] = {}
    
    def save(self, task: Task) -> None:
        """
        Guardar o actualizar una tarea.
        
        TODO: Implementar:
        - Guardar la tarea en self._tasks usando task.id como clave
        """
        # TODO: Implementar
        pass
    
    def find_by_id(self, task_id: UUID) -> Task | None:
        """
        Buscar tarea por ID.
        
        TODO: Implementar:
        - Retornar self._tasks.get(task_id)
        """
        # TODO: Implementar
        pass
    
    def find_all(
        self,
        filters: TaskFilters | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Task]:
        """
        Buscar tareas con filtros opcionales.
        
        TODO: Implementar:
        1. Obtener todas las tareas
        2. Aplicar filtros si existen (status, priority, project_id, assignee_id)
        3. Aplicar paginación (skip, limit)
        4. Retornar lista filtrada
        """
        # TODO: Implementar
        pass
    
    def delete(self, task_id: UUID) -> bool:
        """
        Eliminar tarea por ID.
        
        TODO: Implementar:
        - Si existe, eliminar y retornar True
        - Si no existe, retornar False
        """
        # TODO: Implementar
        pass
    
    def count(self, filters: TaskFilters | None = None) -> int:
        """
        Contar tareas que cumplen los filtros.
        
        TODO: Implementar:
        - Similar a find_all pero retornar solo el count
        """
        # TODO: Implementar
        pass
