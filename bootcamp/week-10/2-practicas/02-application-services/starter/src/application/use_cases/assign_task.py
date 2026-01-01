"""
Use Case: Asignar tarea a un usuario.
"""

from dataclasses import dataclass
from uuid import UUID

from domain.ports.task_repository import TaskRepository
from domain.exceptions import TaskNotFoundError
from application.dtos.task_dtos import TaskDTO


# ============================================
# PASO 1: Definir el Command
# ============================================
print("--- Paso 1: Definir AssignTaskCommand ---")

# Descomenta las siguientes líneas:

# @dataclass(frozen=True)
# class AssignTaskCommand:
#     """Command: Datos para asignar una tarea."""
#     task_id: str
#     user_id: str


# ============================================
# PASO 2: Definir el Use Case
# ============================================
print("--- Paso 2: Definir AssignTaskUseCase ---")

# Descomenta las siguientes líneas:

# class AssignTaskUseCase:
#     """Use Case: Asignar una tarea a un usuario."""
#     
#     def __init__(self, task_repository: TaskRepository) -> None:
#         self._task_repo = task_repository
#     
#     async def execute(self, command: AssignTaskCommand) -> TaskDTO:
#         """
#         Ejecutar asignación de tarea.
#         
#         Nota: La regla de negocio (solo asignar tareas TODO)
#         está en la entidad Task.assign_to(), no aquí.
#         """
#         task_uuid = UUID(command.task_id)
#         user_uuid = UUID(command.user_id)
#         
#         # 1. Obtener tarea
#         task = await self._task_repo.get_by_id(task_uuid)
#         if not task:
#             raise TaskNotFoundError(command.task_id)
#         
#         # 2. Asignar (la validación está en el dominio)
#         task.assign_to(user_uuid)
#         
#         # 3. Persistir
#         await self._task_repo.save(task)
#         
#         # 4. Retornar DTO
#         return TaskDTO.from_entity(task)


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de AssignTaskUseCase ---")
    print("✅ Use Case AssignTask definido correctamente")
