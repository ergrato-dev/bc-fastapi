"""
Driven Adapter: Repository en memoria para tareas.

Este adapter implementa el Port TaskRepository definido
en el dominio. Es un "Driven Adapter" porque es invocado
por la aplicación (no invoca a la aplicación).
"""

from uuid import UUID

from domain.entities.task import Task
from domain.value_objects.task_status import TaskStatus


# ============================================
# PASO 1: Implementar InMemoryTaskRepository
# ============================================
print("--- Paso 1: Implementar InMemoryTaskRepository ---")

# Este adapter implementa el Port sin heredar explícitamente
# (duck typing con Protocol)

# Descomenta las siguientes líneas:

# class InMemoryTaskRepository:
#     """
#     Driven Adapter: Persistencia en memoria.
#     
#     Implementa el Port TaskRepository definido en el dominio.
#     Usa duck typing (no hereda de TaskRepository).
#     """
#     
#     def __init__(self) -> None:
#         self._tasks: dict[UUID, Task] = {}
#     
#     async def save(self, task: Task) -> None:
#         """Guardar o actualizar una tarea."""
#         self._tasks[task.id] = task
#     
#     async def get_by_id(self, task_id: UUID) -> Task | None:
#         """Obtener tarea por ID."""
#         return self._tasks.get(task_id)
#     
#     async def get_all(self) -> list[Task]:
#         """Obtener todas las tareas."""
#         return list(self._tasks.values())
#     
#     async def get_by_project(self, project_id: UUID) -> list[Task]:
#         """Obtener tareas de un proyecto."""
#         return [
#             task for task in self._tasks.values()
#             if task.project_id == project_id
#         ]
#     
#     async def get_by_assignee(self, user_id: UUID) -> list[Task]:
#         """Obtener tareas asignadas a un usuario."""
#         return [
#             task for task in self._tasks.values()
#             if task.assignee_id == user_id
#         ]
#     
#     async def get_by_status(self, status: TaskStatus) -> list[Task]:
#         """Obtener tareas por estado."""
#         return [
#             task for task in self._tasks.values()
#             if task.status == status
#         ]
#     
#     async def delete(self, task_id: UUID) -> bool:
#         """Eliminar una tarea."""
#         if task_id in self._tasks:
#             del self._tasks[task_id]
#             return True
#         return False
#     
#     async def exists(self, task_id: UUID) -> bool:
#         """Verificar si una tarea existe."""
#         return task_id in self._tasks
#     
#     # Métodos adicionales para testing/debug
#     def clear(self) -> None:
#         """Limpiar todos los datos."""
#         self._tasks.clear()
#     
#     def count(self) -> int:
#         """Contar tareas."""
#         return len(self._tasks)


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de InMemoryTaskRepository ---")
    print("✅ Repository implementado correctamente")
