"""
Router de tareas - Driving Adapter.

Este router es un "Driving Adapter" porque invoca
la aplicación desde el exterior (HTTP).
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status

from application.services.task_service import TaskService
from application.dtos.task_dtos import TaskDTO
from domain.exceptions import (
    TaskNotFoundError,
    TaskNotAssignableError,
    ProjectNotFoundError,
)
from infrastructure.api.schemas.task_schemas import (
    CreateTaskRequest,
    AssignTaskRequest,
    TaskResponse,
    TaskListResponse,
)


router = APIRouter(prefix="/tasks", tags=["Tasks"])


# ============================================
# PASO 1: Helper para convertir DTO a Response
# ============================================
print("--- Paso 1: Helper de conversión ---")

# Descomenta las siguientes líneas:

# def _dto_to_response(dto: TaskDTO) -> TaskResponse:
#     """Convertir DTO de aplicación a response de API."""
#     return TaskResponse(
#         id=dto.id,
#         title=dto.title,
#         description=dto.description,
#         status=dto.status,
#         priority=dto.priority,
#         project_id=dto.project_id,
#         assignee_id=dto.assignee_id,
#         created_at=dto.created_at,
#         updated_at=dto.updated_at,
#     )


# ============================================
# PASO 2: Dependency para obtener TaskService
# ============================================
print("--- Paso 2: Dependency ---")

# Esta función será reemplazada en el wiring
# Por ahora es un placeholder

# Descomenta las siguientes líneas:

# def get_task_service() -> TaskService:
#     """Placeholder - será configurado en main.py"""
#     raise NotImplementedError("Configure dependency in main.py")


# ============================================
# PASO 3: Endpoints
# ============================================
print("--- Paso 3: Endpoints ---")

# Descomenta las siguientes líneas:

# @router.post(
#     "/",
#     response_model=TaskResponse,
#     status_code=status.HTTP_201_CREATED,
#     summary="Crear tarea",
# )
# async def create_task(
#     request: CreateTaskRequest,
#     service: TaskService = Depends(get_task_service),
# ) -> TaskResponse:
#     """Crear una nueva tarea."""
#     try:
#         dto = await service.create_task(
#             title=request.title,
#             description=request.description,
#             priority=request.priority.value,
#             project_id=request.project_id,
#         )
#         return _dto_to_response(dto)
#     
#     except ProjectNotFoundError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e),
#         )
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=str(e),
#         )
# 
# 
# @router.get(
#     "/",
#     response_model=TaskListResponse,
#     summary="Listar tareas",
# )
# async def list_tasks(
#     project_id: str | None = Query(None),
#     assignee_id: str | None = Query(None),
#     status: str | None = Query(None),
#     limit: int = Query(20, ge=1, le=100),
#     offset: int = Query(0, ge=0),
#     service: TaskService = Depends(get_task_service),
# ) -> TaskListResponse:
#     """Obtener lista de tareas con filtros."""
#     result = await service.get_tasks(
#         project_id=project_id,
#         assignee_id=assignee_id,
#         status=status,
#         limit=limit,
#         offset=offset,
#     )
#     
#     return TaskListResponse(
#         items=[_dto_to_response(dto) for dto in result.items],
#         total=result.total,
#         limit=result.limit,
#         offset=result.offset,
#         has_more=result.has_more,
#     )
# 
# 
# @router.get(
#     "/{task_id}",
#     response_model=TaskResponse,
#     summary="Obtener tarea",
# )
# async def get_task(
#     task_id: str,
#     service: TaskService = Depends(get_task_service),
# ) -> TaskResponse:
#     """Obtener una tarea por ID."""
#     dto = await service.get_task_by_id(task_id)
#     
#     if not dto:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Task not found: {task_id}",
#         )
#     
#     return _dto_to_response(dto)
# 
# 
# @router.post(
#     "/{task_id}/assign",
#     response_model=TaskResponse,
#     summary="Asignar tarea",
# )
# async def assign_task(
#     task_id: str,
#     request: AssignTaskRequest,
#     service: TaskService = Depends(get_task_service),
# ) -> TaskResponse:
#     """Asignar una tarea a un usuario."""
#     try:
#         dto = await service.assign_task(
#             task_id=task_id,
#             user_id=request.user_id,
#         )
#         return _dto_to_response(dto)
#     
#     except TaskNotFoundError:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Task not found: {task_id}",
#         )
#     except TaskNotAssignableError as e:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail=str(e),
#         )
# 
# 
# @router.post(
#     "/{task_id}/complete",
#     response_model=TaskResponse,
#     summary="Completar tarea",
# )
# async def complete_task(
#     task_id: str,
#     service: TaskService = Depends(get_task_service),
# ) -> TaskResponse:
#     """Marcar una tarea como completada."""
#     try:
#         dto = await service.complete_task(task_id)
#         return _dto_to_response(dto)
#     
#     except TaskNotFoundError:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Task not found: {task_id}",
#         )
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail=str(e),
#         )
# 
# 
# @router.delete(
#     "/{task_id}",
#     status_code=status.HTTP_204_NO_CONTENT,
#     summary="Eliminar tarea",
# )
# async def delete_task(
#     task_id: str,
#     service: TaskService = Depends(get_task_service),
# ) -> None:
#     """Eliminar una tarea."""
#     deleted = await service.delete_task(task_id)
#     
#     if not deleted:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Task not found: {task_id}",
#         )


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Router ---")
    print("✅ Router de tareas definido correctamente")
