"""
Tasks Router - CRUD de Tareas.

Este módulo implementa endpoints para gestión de tareas
con rate limiting y métricas.
"""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Task, TaskStatus
from src.schemas import TaskCreate, TaskUpdate, TaskResponse, TaskList
from src.security.rate_limit import limiter
from src.observability.metrics import record_task_created, record_task_completed


router = APIRouter(prefix="/tasks", tags=["tasks"])


# Datos en memoria para simplificar (en producción usar DB)
fake_tasks_db: dict[int, dict] = {
    1: {
        "id": 1,
        "title": "Implementar rate limiting",
        "description": "Añadir slowapi al proyecto",
        "status": "completed",
        "priority": "high",
        "owner_id": 1,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
        "completed_at": datetime.now(timezone.utc),
    },
    2: {
        "id": 2,
        "title": "Configurar logging",
        "description": "Usar structlog para logs JSON",
        "status": "in_progress",
        "priority": "medium",
        "owner_id": 1,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
        "completed_at": None,
    },
}
next_id = 3


# ============================================
# LIST TASKS
# ============================================

@router.get("", response_model=TaskList)
# TODO: Añadir rate limiting
# @limiter.limit("60/minute")
async def list_tasks(
    request: Request,
    status_filter: TaskStatus | None = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
):
    """
    Lista todas las tareas con paginación.
    
    - **status**: Filtrar por estado (opcional)
    - **page**: Número de página
    - **size**: Tamaño de página
    """
    tasks = list(fake_tasks_db.values())
    
    # Filtrar por status si se especifica
    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter.value]
    
    # Paginación
    total = len(tasks)
    start = (page - 1) * size
    end = start + size
    items = tasks[start:end]
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size,
        "pages": (total + size - 1) // size,
    }


# ============================================
# GET TASK
# ============================================

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    """Obtiene una tarea por ID."""
    if task_id not in fake_tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )
    return fake_tasks_db[task_id]


# ============================================
# CREATE TASK
# ============================================

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
# TODO: Añadir rate limiting
# @limiter.limit("20/minute")
async def create_task(
    request: Request,
    task: TaskCreate,
):
    """
    Crea una nueva tarea.
    
    Rate limit: 20 requests por minuto.
    """
    global next_id
    
    now = datetime.now(timezone.utc)
    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "status": TaskStatus.PENDING.value,
        "priority": task.priority.value,
        "owner_id": 1,  # TODO: obtener del usuario autenticado
        "created_at": now,
        "updated_at": now,
        "completed_at": None,
    }
    
    fake_tasks_db[next_id] = new_task
    next_id += 1
    
    # TODO: Registrar métrica de tarea creada
    # record_task_created(priority=task.priority.value)
    
    return new_task


# ============================================
# UPDATE TASK
# ============================================

@router.put("/{task_id}", response_model=TaskResponse)
# TODO: Añadir rate limiting
# @limiter.limit("30/minute")
async def update_task(
    request: Request,
    task_id: int,
    task_update: TaskUpdate,
):
    """
    Actualiza una tarea existente.
    
    Rate limit: 30 requests por minuto.
    """
    if task_id not in fake_tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )
    
    task = fake_tasks_db[task_id]
    update_data = task_update.model_dump(exclude_unset=True)
    
    # Verificar si se está completando la tarea
    was_completed = task["status"] == TaskStatus.COMPLETED.value
    
    for key, value in update_data.items():
        if hasattr(value, "value"):  # Es un Enum
            task[key] = value.value
        else:
            task[key] = value
    
    task["updated_at"] = datetime.now(timezone.utc)
    
    # Si se completa la tarea, registrar timestamp y métrica
    is_completed = task["status"] == TaskStatus.COMPLETED.value
    if is_completed and not was_completed:
        task["completed_at"] = datetime.now(timezone.utc)
        # TODO: Registrar métrica de tarea completada
        # completion_hours = (task["completed_at"] - task["created_at"]).total_seconds() / 3600
        # record_task_completed(completion_hours=completion_hours)
    
    return task


# ============================================
# DELETE TASK
# ============================================

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
# TODO: Añadir rate limiting
# @limiter.limit("30/minute")
async def delete_task(request: Request, task_id: int):
    """
    Elimina una tarea.
    
    Rate limit: 30 requests por minuto.
    """
    if task_id not in fake_tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )
    
    del fake_tasks_db[task_id]
