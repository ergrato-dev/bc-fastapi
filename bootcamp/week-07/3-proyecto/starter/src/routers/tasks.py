# ============================================
# Tasks Router
# ============================================
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.task import Priority
from ..schemas.task import TaskCreate, TaskUpdate, TaskResponse
from ..unit_of_work import UnitOfWork
from ..services.task import TaskService, TaskNotFoundError
from ..services.user import UserNotFoundError

router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_uow(db: Session = Depends(get_db)) -> UnitOfWork:
    """Dependency para obtener UnitOfWork"""
    return UnitOfWork(db)


def get_task_service(uow: UnitOfWork = Depends(get_uow)) -> TaskService:
    """Dependency para obtener TaskService"""
    return TaskService(uow)


# ============================================
# TODO: Implementar endpoints
# ============================================

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    data: TaskCreate,
    service: TaskService = Depends(get_task_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Crear nueva tarea.
    
    TODO: Implementar
    Manejar UserNotFoundError -> 404
    """
    pass


@router.get("/", response_model=list[TaskResponse])
def list_tasks(
    skip: int = 0,
    limit: int = 100,
    completed: bool | None = None,
    priority: Priority | None = None,
    service: TaskService = Depends(get_task_service)
):
    """
    Listar tareas con filtros opcionales.
    
    TODO: Implementar
    """
    pass


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    """
    Obtener tarea por ID.
    
    TODO: Implementar
    Manejar TaskNotFoundError -> 404
    """
    pass


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    data: TaskUpdate,
    service: TaskService = Depends(get_task_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Actualizar tarea.
    
    TODO: Implementar
    """
    pass


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Eliminar tarea.
    
    TODO: Implementar
    """
    pass


@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Marcar tarea como completada.
    
    TODO: Implementar
    """
    pass


@router.patch("/{task_id}/reopen", response_model=TaskResponse)
def reopen_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Reabrir tarea completada.
    
    TODO: Implementar
    """
    pass
