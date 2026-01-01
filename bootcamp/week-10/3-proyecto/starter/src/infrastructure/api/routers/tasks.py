"""
Tasks Router - Endpoints de tareas.

TODO: Implementar todos los endpoints conectando con TaskService.
"""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status

from application.services.task_service import TaskService
from application.commands.task_commands import (
    CreateTaskCommand,
    StartTaskCommand,
    CompleteTaskCommand,
    AssignTaskCommand,
    DeleteTaskCommand,
)
from application.queries.task_queries import GetTaskQuery, ListTasksQuery
from infrastructure.api.schemas.task_schemas import (
    TaskCreateRequest,
    TaskAssignRequest,
    TaskResponse,
    TaskListResponse,
)


router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])


def get_task_service() -> TaskService:
    """Placeholder - se configura en main.py."""
    raise NotImplementedError("Configure in main.py")


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    request: TaskCreateRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """
    Crear nueva tarea.
    
    TODO: Implementar:
    1. Crear CreateTaskCommand desde request
    2. Llamar service.create_task(command)
    3. Convertir DTO a Response
    """
    # TODO: Implementar
    pass


@router.get("/", response_model=TaskListResponse)
async def list_tasks(
    status_filter: str | None = Query(None, alias="status"),
    priority: str | None = None,
    project_id: UUID | None = None,
    assignee_id: UUID | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    service: TaskService = Depends(get_task_service),
) -> TaskListResponse:
    """
    Listar tareas con filtros.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: UUID,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """
    Obtener tarea por ID.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


@router.put("/{task_id}/start", response_model=TaskResponse)
async def start_task(
    task_id: UUID,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """
    Iniciar tarea.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


@router.put("/{task_id}/complete", response_model=TaskResponse)
async def complete_task(
    task_id: UUID,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """
    Completar tarea.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


@router.put("/{task_id}/assign", response_model=TaskResponse)
async def assign_task(
    task_id: UUID,
    request: TaskAssignRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """
    Asignar tarea a usuario.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: UUID,
    service: TaskService = Depends(get_task_service),
) -> None:
    """
    Eliminar tarea.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass
