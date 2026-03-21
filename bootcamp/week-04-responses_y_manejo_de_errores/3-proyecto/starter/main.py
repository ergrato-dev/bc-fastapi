"""
Task Manager API - Archivo Principal
Semana 04 - Proyecto

API REST para gestión de tareas con:
- Response models
- Status codes apropiados
- Manejo de errores consistente
- Documentación OpenAPI completa
"""

from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Path, Query, status
from fastapi.responses import JSONResponse

from models import (
    TaskStatus,
    TaskPriority,
    TaskCreate,
    TaskUpdate,
    StatusUpdate,
    TaskResponse,
    TaskListResponse,
    TaskStats,
    ErrorResponse,
)
from database import tasks_db, get_next_id
from exceptions import (
    TaskManagerException,
    TaskNotFoundError,
    InvalidStatusTransitionError,
    DuplicateTaskError,
    task_manager_exception_handler,
)


# ============================================
# APP CONFIGURATION - TODO: Completar metadata
# ============================================

# TODO: Agregar metadata completa:
# - title: "Task Manager API"
# - description: Descripción con markdown
# - version: "1.0.0"
# - contact, license_info
# - openapi_tags

tags_metadata = [
    # TODO: Definir tags para tasks, stats, health
]

app = FastAPI(
    title="Task Manager API",
    # TODO: Completar configuración
)


# ============================================
# EXCEPTION HANDLERS - TODO: Registrar
# ============================================

# TODO: Registrar el exception handler
# app.add_exception_handler(TaskManagerException, task_manager_exception_handler)


# ============================================
# HELPER FUNCTIONS
# ============================================

def validate_status_transition(current: TaskStatus, target: TaskStatus) -> bool:
    """
    Valida si una transición de estado es permitida.
    
    Reglas:
    - pending -> in_progress: OK
    - pending -> completed: NO (debe pasar por in_progress)
    - in_progress -> completed: OK
    - in_progress -> pending: OK
    - completed -> pending: NO
    - completed -> in_progress: OK
    """
    # TODO: Implementar lógica de validación
    invalid_transitions = [
        (TaskStatus.pending, TaskStatus.completed),
        (TaskStatus.completed, TaskStatus.pending),
    ]
    return (current, target) not in invalid_transitions


def check_duplicate_title(title: str, exclude_id: int | None = None) -> bool:
    """Check if a task with the same title exists"""
    for task_id, task in tasks_db.items():
        if task["title"].lower() == title.lower():
            if exclude_id is None or task_id != exclude_id:
                return True
    return False


# ============================================
# ENDPOINTS - TODO: Implementar
# ============================================

@app.get(
    "/tasks",
    # TODO: Agregar tags, response_model, summary, description, responses
)
async def list_tasks(
    status_filter: Annotated[
        TaskStatus | None,
        Query(alias="status", description="Filtrar por estado")
    ] = None,
    priority_filter: Annotated[
        TaskPriority | None,
        Query(alias="priority", description="Filtrar por prioridad")
    ] = None,
    skip: Annotated[int, Query(ge=0, description="Offset para paginación")] = 0,
    limit: Annotated[int, Query(ge=1, le=100, description="Límite de resultados")] = 10,
):
    """
    Lista todas las tareas con filtros opcionales.
    
    TODO: Implementar:
    1. Filtrar por status si se proporciona
    2. Filtrar por priority si se proporciona
    3. Aplicar paginación (skip, limit)
    4. Retornar TaskListResponse con total, skip, limit
    """
    # TODO: Implementar lógica
    pass


@app.get(
    "/tasks/{task_id}",
    # TODO: Agregar tags, response_model, responses (200, 404)
)
async def get_task(
    task_id: Annotated[int, Path(ge=1, description="ID de la tarea")]
):
    """
    Obtiene una tarea por su ID.
    
    TODO: Implementar:
    1. Buscar tarea en tasks_db
    2. Si no existe, lanzar TaskNotFoundError
    3. Retornar TaskResponse
    """
    # TODO: Implementar lógica
    pass


@app.post(
    "/tasks",
    # TODO: status_code=201, response_model, responses
)
async def create_task(task: TaskCreate):
    """
    Crea una nueva tarea.
    
    TODO: Implementar:
    1. Verificar título duplicado -> DuplicateTaskError
    2. Crear tarea con ID auto-generado
    3. Establecer status=pending, timestamps
    4. Guardar en tasks_db
    5. Retornar TaskResponse con 201
    """
    # TODO: Implementar lógica
    pass


@app.put(
    "/tasks/{task_id}",
    # TODO: response_model, responses (200, 404, 409)
)
async def update_task(
    task_id: Annotated[int, Path(ge=1)],
    task_update: TaskUpdate
):
    """
    Actualiza una tarea completa.
    
    TODO: Implementar:
    1. Verificar que la tarea existe
    2. Si cambia título, verificar duplicados
    3. Actualizar campos proporcionados
    4. Actualizar updated_at
    5. Retornar TaskResponse
    """
    # TODO: Implementar lógica
    pass


@app.patch(
    "/tasks/{task_id}/status",
    # TODO: response_model, responses (200, 400, 404)
)
async def update_task_status(
    task_id: Annotated[int, Path(ge=1)],
    status_update: StatusUpdate
):
    """
    Cambia el status de una tarea.
    
    TODO: Implementar:
    1. Verificar que la tarea existe
    2. Validar transición de estado
    3. Si inválida -> InvalidStatusTransitionError
    4. Si cambia a completed -> registrar completed_at
    5. Actualizar updated_at
    6. Retornar TaskResponse
    """
    # TODO: Implementar lógica
    pass


@app.delete(
    "/tasks/{task_id}",
    # TODO: status_code=204, responses (204, 404)
)
async def delete_task(
    task_id: Annotated[int, Path(ge=1)]
):
    """
    Elimina una tarea.
    
    TODO: Implementar:
    1. Verificar que la tarea existe
    2. Eliminar de tasks_db
    3. Retornar None con 204
    """
    # TODO: Implementar lógica
    pass


@app.get(
    "/tasks/stats",
    # TODO: response_model=TaskStats, tags
)
async def get_task_stats():
    """
    Obtiene estadísticas de las tareas.
    
    TODO: Implementar:
    1. Contar total de tareas
    2. Contar por status
    3. Contar por priority
    4. Retornar TaskStats
    """
    # TODO: Implementar lógica
    pass


# ============================================
# HEALTH CHECK
# ============================================

@app.get(
    "/health",
    tags=["health"],
    summary="Health check",
    response_description="Estado del servicio"
)
async def health_check():
    """Verifica que el servicio está funcionando."""
    return {
        "status": "healthy",
        "service": "task-manager-api",
        "version": "1.0.0"
    }
