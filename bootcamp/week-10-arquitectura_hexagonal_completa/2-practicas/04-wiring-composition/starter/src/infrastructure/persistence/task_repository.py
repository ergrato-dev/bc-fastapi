"""
InMemoryTaskRepository - Adaptador de persistencia.
"""

from uuid import UUID
from domain.entities.task import Task


class InMemoryTaskRepository:
    """Adaptador: Repository en memoria."""
    
    def __init__(self) -> None:
        self._tasks: dict[UUID, Task] = {}
    
    def save(self, task: Task) -> None:
        self._tasks[task.id] = task
    
    def find_by_id(self, task_id: UUID) -> Task | None:
        return self._tasks.get(task_id)
    
    def find_all(self, skip: int = 0, limit: int = 100) -> list[Task]:
        tasks = list(self._tasks.values())
        return tasks[skip : skip + limit]
    
    def delete(self, task_id: UUID) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
