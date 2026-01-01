"""
Schemas Pydantic para la API de tareas.

Los schemas de API son diferentes de los DTOs de aplicación.
Están optimizados para validación HTTP y documentación OpenAPI.
"""

from pydantic import BaseModel, Field
from enum import Enum


# ============================================
# PASO 1: Enums para validación
# ============================================
print("--- Paso 1: Enums para API ---")

# Descomenta las siguientes líneas:

# class PriorityEnum(str, Enum):
#     """Enum para validación de prioridad en API."""
#     LOW = "LOW"
#     MEDIUM = "MEDIUM"
#     HIGH = "HIGH"
#     CRITICAL = "CRITICAL"
# 
# 
# class TaskStatusEnum(str, Enum):
#     """Enum para validación de estado en API."""
#     TODO = "todo"
#     IN_PROGRESS = "in_progress"
#     DONE = "done"
#     CANCELLED = "cancelled"


# ============================================
# PASO 2: Request Schemas (Input)
# ============================================
print("--- Paso 2: Request Schemas ---")

# Descomenta las siguientes líneas:

# class CreateTaskRequest(BaseModel):
#     """Request body para crear tarea."""
#     
#     title: str = Field(
#         ...,
#         min_length=1,
#         max_length=200,
#         description="Título de la tarea",
#         examples=["Implementar login"],
#     )
#     description: str = Field(
#         default="",
#         max_length=2000,
#         description="Descripción detallada",
#     )
#     priority: PriorityEnum = Field(
#         default=PriorityEnum.MEDIUM,
#         description="Prioridad de la tarea",
#     )
#     project_id: str | None = Field(
#         default=None,
#         description="ID del proyecto (opcional)",
#     )
# 
# 
# class AssignTaskRequest(BaseModel):
#     """Request body para asignar tarea."""
#     
#     user_id: str = Field(
#         ...,
#         description="ID del usuario a asignar",
#     )


# ============================================
# PASO 3: Response Schemas (Output)
# ============================================
print("--- Paso 3: Response Schemas ---")

# Descomenta las siguientes líneas:

# class TaskResponse(BaseModel):
#     """Response body para una tarea."""
#     
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
#     model_config = {"from_attributes": True}
# 
# 
# class TaskListResponse(BaseModel):
#     """Response body para lista de tareas."""
#     
#     items: list[TaskResponse]
#     total: int
#     limit: int
#     offset: int
#     has_more: bool
# 
# 
# class ErrorResponse(BaseModel):
#     """Response body para errores."""
#     
#     error: str
#     detail: str | None = None


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Schemas ---")
    print("✅ Schemas definidos correctamente")
