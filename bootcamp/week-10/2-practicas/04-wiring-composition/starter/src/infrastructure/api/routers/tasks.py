"""
Tasks Router - Adaptador driving (API REST).
"""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from application.services.task_service import TaskService, CreateTaskCommand


# ============================================
# Schemas (Pydantic)
# ============================================

class TaskCreateRequest(BaseModel):
    """Request para crear tarea."""
    title: str
    description: str


class TaskResponse(BaseModel):
    """Response de tarea."""
    id: UUID
    title: str
    description: str
    status: str


# ============================================
# Dependency Placeholder
# ============================================

def get_task_service() -> TaskService:
    """
    Placeholder - será reemplazado por dependency_overrides.
    """
    raise NotImplementedError("Debe configurarse en main.py")


# ============================================
# Router
# ============================================

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    request: TaskCreateRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """Crear una nueva tarea."""
    command = CreateTaskCommand(
        title=request.title,
        description=request.description,
    )
    dto = service.create_task(command)
    return TaskResponse(
        id=dto.id,
        title=dto.title,
        description=dto.description,
        status=dto.status,
    )


@router.get("/", response_model=list[TaskResponse])
async def list_tasks(
    skip: int = 0,
    limit: int = 100,
    service: TaskService = Depends(get_task_service),
) -> list[TaskResponse]:
    """Listar tareas."""
    dtos = service.get_tasks(skip=skip, limit=limit)
    return [
        TaskResponse(
            id=dto.id,
            title=dto.title,
            description=dto.description,
            status=dto.status,
        )
        for dto in dtos
    ]


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: UUID,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """Obtener tarea por ID."""
    dto = service.get_task(task_id)
    if dto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )
    return TaskResponse(
        id=dto.id,
        title=dto.title,
        description=dto.description,
        status=dto.status,
    )
