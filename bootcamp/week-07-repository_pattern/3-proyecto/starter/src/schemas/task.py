# ============================================
# Schemas de Tarea
# ============================================
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from ..models.task import Priority


class TaskCreate(BaseModel):
    """
    Schema para crear tarea
    
    TODO: Implementar campos:
    - title: str (1-200 chars)
    - description: str | None
    - priority: Priority (default MEDIUM)
    - user_id: int
    """
    # TODO: Implementar
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    priority: Priority = Priority.MEDIUM
    user_id: int


class TaskUpdate(BaseModel):
    """
    Schema para actualizar tarea
    
    TODO: Implementar campos opcionales:
    - title: str | None
    - description: str | None
    - is_completed: bool | None
    - priority: Priority | None
    """
    # TODO: Implementar campos opcionales
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
    priority: Priority | None = None


class TaskResponse(BaseModel):
    """
    Schema de respuesta de tarea
    
    TODO: Implementar campos:
    - id: int
    - title: str
    - description: str | None
    - is_completed: bool
    - priority: Priority
    - user_id: int
    - created_at: datetime
    - completed_at: datetime | None
    """
    model_config = ConfigDict(from_attributes=True)
    
    # TODO: Implementar
    id: int
    title: str
    description: str | None
    is_completed: bool
    priority: Priority
    user_id: int
    created_at: datetime
    completed_at: datetime | None
