"""
Entidad Task - Representa una tarea en el sistema.

Una Entidad tiene:
- Identidad única (id) que la distingue de otras
- Ciclo de vida (se crea, modifica, elimina)
- Comportamiento que encapsula reglas de negocio
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from domain.value_objects.task_status import TaskStatus
from domain.value_objects.priority import Priority
from domain.exceptions import (
    TaskNotAssignableError,
    TaskNotStartableError,
    TaskNotCompletableError,
)


# ============================================
# PASO 1: Definir la entidad Task
# ============================================
print("--- Paso 1: Definir la entidad Task ---")

# Una entidad usa @dataclass para reducir boilerplate
# pero agrega comportamiento con métodos

# Descomenta las siguientes líneas:

# @dataclass
# class Task:
#     """
#     Entidad Task.
#     
#     Representa una tarea con identidad única y comportamiento
#     que encapsula las reglas de negocio del dominio.
#     """
#     
#     # Campos obligatorios
#     id: UUID
#     title: str
#     description: str
#     
#     # Campos con valores por defecto
#     status: TaskStatus = field(default=TaskStatus.TODO)
#     priority: Priority = field(default=Priority.MEDIUM)
#     project_id: UUID | None = field(default=None)
#     assignee_id: UUID | None = field(default=None)
#     created_at: datetime = field(default_factory=datetime.now)
#     updated_at: datetime = field(default_factory=datetime.now)


# ============================================
# PASO 2: Factory Method
# ============================================
print("--- Paso 2: Factory Method ---")

# El factory method es el punto de entrada para crear entidades
# Garantiza que la entidad se crea en un estado válido

# Agrega este método dentro de la clase Task:

#     @classmethod
#     def create(
#         cls,
#         title: str,
#         description: str = "",
#         priority: Priority = Priority.MEDIUM,
#         project_id: UUID | None = None,
#     ) -> "Task":
#         """
#         Factory method para crear una nueva tarea.
#         
#         Usar este método en lugar del constructor directamente
#         para garantizar que la tarea se crea en un estado válido.
#         
#         Args:
#             title: Título de la tarea (requerido, no vacío)
#             description: Descripción opcional
#             priority: Prioridad (default: MEDIUM)
#             project_id: ID del proyecto (opcional)
#             
#         Returns:
#             Nueva instancia de Task
#             
#         Raises:
#             ValueError: Si el título está vacío
#         """
#         if not title or not title.strip():
#             raise ValueError("Task title cannot be empty")
#         
#         return cls(
#             id=uuid4(),
#             title=title.strip(),
#             description=description.strip(),
#             priority=priority,
#             project_id=project_id,
#         )


# ============================================
# PASO 3: Métodos de Comportamiento (Commands)
# ============================================
print("--- Paso 3: Métodos de Comportamiento ---")

# Los métodos de comportamiento encapsulan las reglas de negocio
# Modifican el estado de la entidad de forma controlada

# Agrega estos métodos dentro de la clase Task:

#     def assign_to(self, user_id: UUID) -> None:
#         """
#         Asignar la tarea a un usuario.
#         
#         Regla de negocio: Solo se pueden asignar tareas
#         que estén en estado TODO.
#         
#         Args:
#             user_id: ID del usuario a asignar
#             
#         Raises:
#             TaskNotAssignableError: Si la tarea no está en TODO
#         """
#         if self.status != TaskStatus.TODO:
#             raise TaskNotAssignableError(
#                 f"Cannot assign task {self.id}: status is {self.status.value}"
#             )
#         
#         self.assignee_id = user_id
#         self._touch()
#     
#     def unassign(self) -> None:
#         """Quitar la asignación de la tarea."""
#         self.assignee_id = None
#         self._touch()
#     
#     def start(self) -> None:
#         """
#         Iniciar trabajo en la tarea.
#         
#         Regla de negocio: Solo se pueden iniciar tareas en TODO.
#         """
#         if self.status != TaskStatus.TODO:
#             raise TaskNotStartableError(
#                 f"Cannot start task {self.id}: status is {self.status.value}"
#             )
#         
#         self.status = TaskStatus.IN_PROGRESS
#         self._touch()
#     
#     def complete(self) -> None:
#         """
#         Marcar la tarea como completada.
#         
#         Regla de negocio: No se pueden completar tareas canceladas.
#         """
#         if self.status == TaskStatus.CANCELLED:
#             raise TaskNotCompletableError(
#                 f"Cannot complete task {self.id}: task is cancelled"
#             )
#         
#         self.status = TaskStatus.DONE
#         self._touch()
#     
#     def cancel(self) -> None:
#         """Cancelar la tarea."""
#         if self.status == TaskStatus.DONE:
#             raise ValueError(f"Cannot cancel task {self.id}: already done")
#         
#         self.status = TaskStatus.CANCELLED
#         self._touch()
#     
#     def change_priority(self, new_priority: Priority) -> None:
#         """Cambiar la prioridad de la tarea."""
#         self.priority = new_priority
#         self._touch()


# ============================================
# PASO 4: Métodos de Consulta (Queries)
# ============================================
print("--- Paso 4: Métodos de Consulta ---")

# Los métodos de consulta NO modifican estado
# Solo devuelven información sobre la entidad

# Agrega estos métodos dentro de la clase Task:

#     def is_assignable(self) -> bool:
#         """Verificar si la tarea puede ser asignada."""
#         return self.status == TaskStatus.TODO
#     
#     def is_assigned(self) -> bool:
#         """Verificar si la tarea tiene asignado."""
#         return self.assignee_id is not None
#     
#     def is_completed(self) -> bool:
#         """Verificar si la tarea está completada."""
#         return self.status == TaskStatus.DONE
#     
#     def belongs_to_project(self, project_id: UUID) -> bool:
#         """Verificar si la tarea pertenece a un proyecto."""
#         return self.project_id == project_id


# ============================================
# PASO 5: Método privado auxiliar
# ============================================
print("--- Paso 5: Método privado auxiliar ---")

# Los métodos privados (con _) son auxiliares internos

# Agrega este método dentro de la clase Task:

#     def _touch(self) -> None:
#         """Actualizar timestamp de modificación."""
#         self.updated_at = datetime.now()


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Task ---")
    
    # Descomentar para probar:
    # task = Task.create(title="Mi primera tarea", priority=Priority.HIGH)
    # print(f"Task creada: {task.id}")
    # print(f"Estado: {task.status.value}")
    # print(f"Prioridad: {task.priority.name}")
    # 
    # # Probar asignación
    # from uuid import uuid4
    # user_id = uuid4()
    # task.assign_to(user_id)
    # print(f"Asignada a: {task.assignee_id}")
    # 
    # # Probar completar
    # task.start()
    # task.complete()
    # print(f"Estado final: {task.status.value}")
    
    print("✅ Entidad Task implementada correctamente")
