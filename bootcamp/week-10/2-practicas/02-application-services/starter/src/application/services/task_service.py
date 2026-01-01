"""
Application Service: Fachada para operaciones de tareas.

Un Application Service agrupa use cases relacionados
para simplificar el uso desde la capa de infraestructura.
"""

from application.use_cases.create_task import CreateTaskUseCase, CreateTaskCommand
from application.use_cases.assign_task import AssignTaskUseCase, AssignTaskCommand
from application.use_cases.complete_task import CompleteTaskUseCase, CompleteTaskCommand
from application.use_cases.get_tasks import GetTasksUseCase, GetTasksQuery
from application.dtos.task_dtos import TaskDTO, TaskListDTO
from domain.ports.task_repository import TaskRepository
from domain.ports.project_repository import ProjectRepository


# ============================================
# PASO 1: Definir TaskService
# ============================================
print("--- Paso 1: Definir TaskService ---")

# El Application Service es una fachada que simplifica
# el uso de múltiples Use Cases

# Descomenta las siguientes líneas:

# class TaskService:
#     """
#     Application Service: Fachada para tareas.
#     
#     Agrupa use cases relacionados para simplificar
#     el uso desde la capa de infraestructura (API, CLI, etc).
#     """
#     
#     def __init__(
#         self,
#         task_repository: TaskRepository,
#         project_repository: ProjectRepository,
#     ) -> None:
#         """Crear instancias de los use cases."""
#         self._create_uc = CreateTaskUseCase(task_repository, project_repository)
#         self._assign_uc = AssignTaskUseCase(task_repository)
#         self._complete_uc = CompleteTaskUseCase(task_repository)
#         self._get_uc = GetTasksUseCase(task_repository)
#         self._task_repo = task_repository
#     
#     async def create_task(
#         self,
#         title: str,
#         description: str = "",
#         priority: str = "MEDIUM",
#         project_id: str | None = None,
#     ) -> TaskDTO:
#         """Crear una nueva tarea."""
#         command = CreateTaskCommand(
#             title=title,
#             description=description,
#             priority=priority,
#             project_id=project_id,
#         )
#         return await self._create_uc.execute(command)
#     
#     async def assign_task(self, task_id: str, user_id: str) -> TaskDTO:
#         """Asignar tarea a usuario."""
#         command = AssignTaskCommand(task_id=task_id, user_id=user_id)
#         return await self._assign_uc.execute(command)
#     
#     async def complete_task(self, task_id: str) -> TaskDTO:
#         """Completar una tarea."""
#         command = CompleteTaskCommand(task_id=task_id)
#         return await self._complete_uc.execute(command)
#     
#     async def get_tasks(
#         self,
#         project_id: str | None = None,
#         assignee_id: str | None = None,
#         status: str | None = None,
#         limit: int = 100,
#         offset: int = 0,
#     ) -> TaskListDTO:
#         """Obtener tareas con filtros."""
#         query = GetTasksQuery(
#             project_id=project_id,
#             assignee_id=assignee_id,
#             status=status,
#             limit=limit,
#             offset=offset,
#         )
#         return await self._get_uc.execute(query)
#     
#     async def get_task_by_id(self, task_id: str) -> TaskDTO | None:
#         """Obtener una tarea por ID."""
#         from uuid import UUID
#         task = await self._task_repo.get_by_id(UUID(task_id))
#         return TaskDTO.from_entity(task) if task else None
#     
#     async def delete_task(self, task_id: str) -> bool:
#         """Eliminar una tarea."""
#         from uuid import UUID
#         return await self._task_repo.delete(UUID(task_id))


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de TaskService ---")
    print("✅ TaskService definido correctamente")
