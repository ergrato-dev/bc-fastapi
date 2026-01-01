"""
Value Objects del dominio.

Los Value Objects son inmutables y se comparan por valor, no por identidad.
"""

from enum import Enum, IntEnum


class TaskStatus(Enum):
    """
    Estado de una tarea.
    
    TODO: Implementar las transiciones válidas:
    - PENDING → IN_PROGRESS (start)
    - IN_PROGRESS → COMPLETED (complete)
    - PENDING → CANCELLED (cancel)
    - IN_PROGRESS → CANCELLED (cancel)
    """
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    
    # TODO: Implementar método can_transition_to(self, new_status) -> bool
    # que valide si la transición es permitida


class Priority(IntEnum):
    """
    Prioridad de una tarea.
    
    Usa IntEnum para poder comparar (HIGH > LOW).
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4
