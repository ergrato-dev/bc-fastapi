"""
Task Manager API - Schemas Pydantic
Semana 04 - Proyecto

Define los schemas para validación y serialización.
"""

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    """Estados posibles de una tarea"""
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskPriority(str, Enum):
    """Niveles de prioridad"""
    low = "low"
    medium = "medium"
    high = "high"


# ============================================
# ERROR SCHEMAS
# ============================================

class ErrorDetail(BaseModel):
    """Detalle de error interno"""
    code: str = Field(..., description="Código único del error")
    message: str = Field(..., description="Mensaje descriptivo")
    details: dict | None = Field(None, description="Detalles adicionales")


class ErrorResponse(BaseModel):
    """Respuesta de error estándar"""
    error: ErrorDetail
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "error": {
                    "code": "TASK_NOT_FOUND",
                    "message": "Task with id 99 not found",
                    "details": None
                }
            }
        }
    }


# ============================================
# TASK SCHEMAS - TODO: Completar
# ============================================

class TaskCreate(BaseModel):
    """
    Schema para crear una tarea.
    
    TODO: Implementar campos:
    - title: str (2-100 caracteres, requerido)
    - description: str | None (máx 500 caracteres)
    - priority: TaskPriority (default: medium)
    
    TODO: Agregar ejemplos con model_config
    """
    # TODO: Implementar campos
    pass


class TaskUpdate(BaseModel):
    """
    Schema para actualizar una tarea (PUT).
    
    TODO: Implementar campos (todos opcionales):
    - title: str | None
    - description: str | None
    - priority: TaskPriority | None
    
    TODO: Agregar ejemplos
    """
    # TODO: Implementar campos
    pass


class StatusUpdate(BaseModel):
    """
    Schema para cambiar el status (PATCH).
    
    TODO: Implementar:
    - status: TaskStatus (requerido)
    """
    # TODO: Implementar campo
    pass


class TaskResponse(BaseModel):
    """
    Schema de respuesta para una tarea.
    
    TODO: Implementar campos:
    - id: int
    - title: str
    - description: str | None
    - status: TaskStatus
    - priority: TaskPriority
    - created_at: datetime
    - updated_at: datetime | None
    - completed_at: datetime | None
    
    TODO: Agregar ejemplo completo
    """
    # TODO: Implementar campos
    pass


class TaskListResponse(BaseModel):
    """
    Schema para listado paginado de tareas.
    
    TODO: Implementar:
    - tasks: list[TaskResponse]
    - total: int
    - skip: int
    - limit: int
    """
    # TODO: Implementar campos
    pass


class TaskStats(BaseModel):
    """
    Schema para estadísticas de tareas.
    
    TODO: Implementar:
    - total: int
    - by_status: dict[str, int]
    - by_priority: dict[str, int]
    """
    # TODO: Implementar campos
    pass
