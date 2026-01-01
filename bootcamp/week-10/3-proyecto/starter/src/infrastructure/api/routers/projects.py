"""
Projects Router - Endpoints de proyectos.

TODO: Implementar todos los endpoints.
"""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status

from application.services.project_service import ProjectService
from application.commands.project_commands import CreateProjectCommand, AddTaskToProjectCommand
from infrastructure.api.schemas.project_schemas import (
    ProjectCreateRequest,
    ProjectResponse,
    ProjectListResponse,
)


router = APIRouter(prefix="/api/v1/projects", tags=["Projects"])


def get_project_service() -> ProjectService:
    """Placeholder - se configura en main.py."""
    raise NotImplementedError("Configure in main.py")


@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    request: ProjectCreateRequest,
    service: ProjectService = Depends(get_project_service),
) -> ProjectResponse:
    """Crear nuevo proyecto. TODO: Implementar."""
    pass


@router.get("/", response_model=ProjectListResponse)
async def list_projects(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    service: ProjectService = Depends(get_project_service),
) -> ProjectListResponse:
    """Listar proyectos. TODO: Implementar."""
    pass


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
) -> ProjectResponse:
    """Obtener proyecto. TODO: Implementar."""
    pass


@router.post("/{project_id}/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def add_task_to_project(
    project_id: UUID,
    task_id: UUID,
    service: ProjectService = Depends(get_project_service),
) -> None:
    """Agregar tarea a proyecto. TODO: Implementar."""
    pass
