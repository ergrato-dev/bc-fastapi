"""
Use Case: Completar una tarea.
"""

from dataclasses import dataclass
from uuid import UUID

from domain.ports.task_repository import TaskRepository
from domain.exceptions import TaskNotFoundError
from application.dtos.task_dtos import TaskDTO


# ============================================
# PASO 1: Command y Use Case
# ============================================

# Descomenta las siguientes líneas:

# @dataclass(frozen=True)
# class CompleteTaskCommand:
#     """Command: Datos para completar una tarea."""
#     task_id: str
# 
# 
# class CompleteTaskUseCase:
#     """Use Case: Marcar una tarea como completada."""
#     
#     def __init__(self, task_repository: TaskRepository) -> None:
#         self._task_repo = task_repository
#     
#     async def execute(self, command: CompleteTaskCommand) -> TaskDTO:
#         """Ejecutar completado de tarea."""
#         task_uuid = UUID(command.task_id)
#         
#         # 1. Obtener tarea
#         task = await self._task_repo.get_by_id(task_uuid)
#         if not task:
#             raise TaskNotFoundError(command.task_id)
#         
#         # 2. Completar (validación en dominio)
#         task.complete()
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
    print("✅ Use Case CompleteTask definido correctamente")
