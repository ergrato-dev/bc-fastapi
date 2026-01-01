"""
Use Case: Obtener tareas con filtros.

Este es un Query Use Case (lectura), no modifica estado.
"""

from dataclasses import dataclass
from uuid import UUID

from domain.ports.task_repository import TaskRepository
from domain.value_objects.task_status import TaskStatus
from application.dtos.task_dtos import TaskDTO, TaskListDTO


# ============================================
# PASO 1: Definir el Query
# ============================================
print("--- Paso 1: Definir GetTasksQuery ---")

# Un Query es similar a un Command pero para lecturas

# Descomenta las siguientes líneas:

# @dataclass(frozen=True)
# class GetTasksQuery:
#     """
#     Query: Parámetros para buscar tareas.
#     
#     A diferencia de Commands, las Queries no modifican estado.
#     """
#     project_id: str | None = None
#     assignee_id: str | None = None
#     status: str | None = None
#     limit: int = 100
#     offset: int = 0


# ============================================
# PASO 2: Definir el Use Case
# ============================================
print("--- Paso 2: Definir GetTasksUseCase ---")

# Descomenta las siguientes líneas:

# class GetTasksUseCase:
#     """Use Case: Obtener lista de tareas con filtros."""
#     
#     def __init__(self, task_repository: TaskRepository) -> None:
#         self._task_repo = task_repository
#     
#     async def execute(self, query: GetTasksQuery) -> TaskListDTO:
#         """
#         Ejecutar búsqueda de tareas.
#         
#         Aplica filtros según los parámetros del query.
#         """
#         # Obtener tareas según filtros
#         if query.project_id:
#             tasks = await self._task_repo.get_by_project(
#                 UUID(query.project_id)
#             )
#         elif query.assignee_id:
#             tasks = await self._task_repo.get_by_assignee(
#                 UUID(query.assignee_id)
#             )
#         elif query.status:
#             tasks = await self._task_repo.get_by_status(
#                 TaskStatus(query.status)
#             )
#         else:
#             tasks = await self._task_repo.get_all()
#         
#         # Aplicar paginación
#         total = len(tasks)
#         paginated = tasks[query.offset : query.offset + query.limit]
#         
#         # Mapear a DTOs
#         return TaskListDTO(
#             items=[TaskDTO.from_entity(t) for t in paginated],
#             total=total,
#             limit=query.limit,
#             offset=query.offset,
#         )


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de GetTasksUseCase ---")
    print("✅ Use Case GetTasks definido correctamente")
