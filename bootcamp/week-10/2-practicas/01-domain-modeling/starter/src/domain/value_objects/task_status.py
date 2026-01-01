"""
Value Object TaskStatus - Estados posibles de una tarea.

Un Value Object:
- Es inmutable (no cambia después de crearse)
- Se compara por valor, no por identidad
- Representa un concepto del dominio
"""

from enum import Enum


# ============================================
# PASO 1: Definir TaskStatus como Enum
# ============================================
print("--- Paso 1: Definir TaskStatus ---")

# Los Enums en Python son perfectos para Value Objects
# con un conjunto fijo de valores

# Descomenta las siguientes líneas:

# class TaskStatus(Enum):
#     """
#     Estados posibles de una tarea.
#     
#     Máquina de estados:
#     - TODO -> IN_PROGRESS, CANCELLED
#     - IN_PROGRESS -> DONE, CANCELLED
#     - DONE -> (estado final)
#     - CANCELLED -> (estado final)
#     """
#     
#     TODO = "todo"
#     IN_PROGRESS = "in_progress"
#     DONE = "done"
#     CANCELLED = "cancelled"
#     
#     def can_transition_to(self, new_status: "TaskStatus") -> bool:
#         """
#         Verificar si la transición a otro estado es válida.
#         
#         Args:
#             new_status: Estado destino
#             
#         Returns:
#             True si la transición es válida
#         """
#         valid_transitions = {
#             TaskStatus.TODO: {TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED},
#             TaskStatus.IN_PROGRESS: {TaskStatus.DONE, TaskStatus.CANCELLED},
#             TaskStatus.DONE: set(),  # Estado final
#             TaskStatus.CANCELLED: set(),  # Estado final
#         }
#         return new_status in valid_transitions[self]
#     
#     def is_final(self) -> bool:
#         """Verificar si es un estado final."""
#         return self in (TaskStatus.DONE, TaskStatus.CANCELLED)


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de TaskStatus ---")
    
    # Descomentar para probar:
    # status = TaskStatus.TODO
    # print(f"Estado: {status.value}")
    # print(f"Puede ir a IN_PROGRESS: {status.can_transition_to(TaskStatus.IN_PROGRESS)}")
    # print(f"Puede ir a DONE: {status.can_transition_to(TaskStatus.DONE)}")
    # print(f"Es final: {status.is_final()}")
    
    print("✅ Value Object TaskStatus implementado correctamente")
