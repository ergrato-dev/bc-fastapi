"""
Port TaskRepository - Contrato para persistencia de tareas.

Un Port es una interfaz que define QUÉ necesita el dominio,
sin especificar CÓMO se implementa.

Usamos Protocol para duck typing estructural.
"""

from typing import Protocol
from uuid import UUID

from domain.entities.task import Task
from domain.value_objects.task_status import TaskStatus


# ============================================
# PASO 1: Definir el Port TaskRepository
# ============================================
print("--- Paso 1: Definir TaskRepository Port ---")

# Protocol permite duck typing: cualquier clase que tenga
# estos métodos con las mismas firmas es compatible

# Descomenta las siguientes líneas:

# class TaskRepository(Protocol):
#     """
#     Port: Define el contrato para persistencia de tareas.
#     
#     El dominio define QUÉ necesita, la infraestructura
#     implementa CÓMO se hace.
#     
#     Cualquier clase que implemente estos métodos es compatible,
#     sin necesidad de herencia explícita (duck typing).
#     """
#     
#     async def save(self, task: Task) -> None:
#         """
#         Guardar o actualizar una tarea.
#         
#         Si la tarea ya existe (mismo ID), se actualiza.
#         Si no existe, se crea.
#         """
#         ...
#     
#     async def get_by_id(self, task_id: UUID) -> Task | None:
#         """
#         Obtener tarea por ID.
#         
#         Returns:
#             Task si existe, None si no
#         """
#         ...
#     
#     async def get_all(self) -> list[Task]:
#         """Obtener todas las tareas."""
#         ...
#     
#     async def get_by_project(self, project_id: UUID) -> list[Task]:
#         """Obtener tareas de un proyecto específico."""
#         ...
#     
#     async def get_by_assignee(self, user_id: UUID) -> list[Task]:
#         """Obtener tareas asignadas a un usuario."""
#         ...
#     
#     async def get_by_status(self, status: TaskStatus) -> list[Task]:
#         """Obtener tareas por estado."""
#         ...
#     
#     async def delete(self, task_id: UUID) -> bool:
#         """
#         Eliminar una tarea.
#         
#         Returns:
#             True si existía y se eliminó, False si no existía
#         """
#         ...
#     
#     async def exists(self, task_id: UUID) -> bool:
#         """Verificar si una tarea existe."""
#         ...


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de TaskRepository Port ---")
    print("El Port es solo una interfaz, no se puede instanciar")
    print("✅ Port TaskRepository definido correctamente")
