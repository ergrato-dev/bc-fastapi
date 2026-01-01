"""
DTOs para tareas.

Los DTOs (Data Transfer Objects) transportan datos entre capas.
Son diferentes de las entidades de dominio.
"""

from dataclasses import dataclass

from domain.entities.task import Task


# ============================================
# PASO 1: DTO de salida para una tarea
# ============================================
print("--- Paso 1: Definir TaskDTO ---")

# Descomenta las siguientes líneas:

# @dataclass(frozen=True)
# class TaskDTO:
#     """
#     DTO de salida para una tarea.
#     
#     Representa la vista pública de una tarea.
#     - Todos los IDs son strings (no UUIDs)
#     - Fechas son strings ISO
#     - No expone detalles internos del dominio
#     """
#     id: str
#     title: str
#     description: str
#     status: str
#     priority: str
#     project_id: str | None
#     assignee_id: str | None
#     created_at: str
#     updated_at: str
#     
#     @classmethod
#     def from_entity(cls, task: Task) -> "TaskDTO":
#         """
#         Factory: Crear DTO desde entidad de dominio.
#         
#         Este método es el único punto de conversión
#         entre dominio y aplicación.
#         """
#         return cls(
#             id=str(task.id),
#             title=task.title,
#             description=task.description,
#             status=task.status.value,
#             priority=task.priority.name,
#             project_id=str(task.project_id) if task.project_id else None,
#             assignee_id=str(task.assignee_id) if task.assignee_id else None,
#             created_at=task.created_at.isoformat(),
#             updated_at=task.updated_at.isoformat(),
#         )


# ============================================
# PASO 2: DTO para lista paginada
# ============================================
print("--- Paso 2: Definir TaskListDTO ---")

# Descomenta las siguientes líneas:

# @dataclass(frozen=True)
# class TaskListDTO:
#     """DTO para lista paginada de tareas."""
#     items: list[TaskDTO]
#     total: int
#     limit: int
#     offset: int
#     
#     @property
#     def has_more(self) -> bool:
#         """Verificar si hay más resultados."""
#         return self.offset + len(self.items) < self.total


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de DTOs ---")
    print("✅ DTOs definidos correctamente")
