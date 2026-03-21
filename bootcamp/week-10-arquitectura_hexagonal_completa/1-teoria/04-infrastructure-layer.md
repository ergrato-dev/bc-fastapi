# 🔧 Infrastructure Layer - Conectando con el Mundo Exterior

## 🎯 Objetivos de Aprendizaje

- Implementar Driving Adapters (API REST con FastAPI)
- Crear Driven Adapters (Repositories, servicios externos)
- Mapear entre modelos de infraestructura y dominio
- Configurar la aplicación de forma centralizada
- Manejar errores y traducirlos a respuestas HTTP

---

## 📚 Contenido

### 1. ¿Qué es el Infrastructure Layer?

El **Infrastructure Layer** es la capa más externa que:
- **Conecta** la aplicación con el mundo exterior
- **Implementa** los Ports definidos en el dominio
- **Contiene** frameworks y bibliotecas externas
- **Adapta** formatos externos al dominio y viceversa

![Infrastructure Layer](../0-assets/04-infrastructure-layer.svg)

### 2. Tipos de Adapters

#### Driving Adapters (Primarios)

**Invocan** la aplicación desde el exterior:
- REST API (FastAPI)
- GraphQL
- CLI
- Message Queue Consumers
- Scheduled Jobs

#### Driven Adapters (Secundarios)

**Son invocados** por la aplicación:
- Repositories (bases de datos)
- External API clients
- Message publishers
- Email/SMS services
- File storage

### 3. Estructura del Infrastructure Layer

```
infrastructure/
├── __init__.py
├── api/                    # Driving Adapter: REST API
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── tasks.py
│   │   └── projects.py
│   ├── schemas/            # Pydantic models para API
│   │   ├── __init__.py
│   │   ├── task_schemas.py
│   │   └── project_schemas.py
│   ├── dependencies.py     # FastAPI dependencies
│   └── error_handlers.py   # Exception handlers
├── persistence/            # Driven Adapter: Database
│   ├── __init__.py
│   ├── in_memory/
│   │   ├── __init__.py
│   │   ├── task_repository.py
│   │   └── project_repository.py
│   └── sqlalchemy/         # (futuro)
│       ├── __init__.py
│       └── ...
├── external/               # Driven Adapters: APIs externas
│   ├── __init__.py
│   └── notification_service.py
└── config.py               # Configuración
```

### 4. Driving Adapter: REST API

#### 4.1 Schemas (Pydantic Models)

```python
# infrastructure/api/schemas/task_schemas.py
"""Schemas Pydantic para la API de tareas."""

from pydantic import BaseModel, Field
from enum import Enum


class PriorityEnum(str, Enum):
    """Enum para validación de prioridad en API."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class TaskStatusEnum(str, Enum):
    """Enum para validación de estado en API."""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELLED = "cancelled"


# ============================================
# Request Schemas (Input)
# ============================================

class CreateTaskRequest(BaseModel):
    """Request body para crear tarea."""
    
    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Título de la tarea",
        examples=["Implementar login"],
    )
    description: str = Field(
        default="",
        max_length=2000,
        description="Descripción detallada",
    )
    priority: PriorityEnum = Field(
        default=PriorityEnum.MEDIUM,
        description="Prioridad de la tarea",
    )
    project_id: str | None = Field(
        default=None,
        description="ID del proyecto (opcional)",
    )


class AssignTaskRequest(BaseModel):
    """Request body para asignar tarea."""
    
    user_id: str = Field(
        ...,
        description="ID del usuario a asignar",
    )


class UpdateTaskRequest(BaseModel):
    """Request body para actualizar tarea."""
    
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    priority: PriorityEnum | None = None


# ============================================
# Response Schemas (Output)
# ============================================

class TaskResponse(BaseModel):
    """Response body para una tarea."""
    
    id: str
    title: str
    description: str
    status: TaskStatusEnum
    priority: PriorityEnum
    project_id: str | None
    assignee_id: str | None
    created_at: str
    updated_at: str
    
    model_config = {"from_attributes": True}


class TaskListResponse(BaseModel):
    """Response body para lista de tareas."""
    
    items: list[TaskResponse]
    total: int
    limit: int
    offset: int
    has_more: bool


class ErrorResponse(BaseModel):
    """Response body para errores."""
    
    error: str
    detail: str | None = None
    field: str | None = None
```

#### 4.2 Router (Endpoints)

```python
# infrastructure/api/routers/tasks.py
"""Router de tareas - Driving Adapter."""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from uuid import UUID

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
    UpdateTaskRequest,
    TaskResponse,
    TaskListResponse,
)
from infrastructure.api.dependencies import get_task_service


router = APIRouter(prefix="/tasks", tags=["Tasks"])


def _dto_to_response(dto: TaskDTO) -> TaskResponse:
    """Convertir DTO de aplicación a response de API."""
    return TaskResponse(
        id=dto.id,
        title=dto.title,
        description=dto.description,
        status=dto.status,
        priority=dto.priority,
        project_id=dto.project_id,
        assignee_id=dto.assignee_id,
        created_at=dto.created_at,
        updated_at=dto.updated_at,
    )


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear tarea",
    description="Crea una nueva tarea en el sistema.",
)
async def create_task(
    request: CreateTaskRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """
    Crear una nueva tarea.
    
    - **title**: Título de la tarea (requerido)
    - **description**: Descripción detallada
    - **priority**: LOW, MEDIUM, HIGH, CRITICAL
    - **project_id**: ID del proyecto (opcional)
    """
    try:
        dto = await service.create_task(
            title=request.title,
            description=request.description,
            priority=request.priority.value,
            project_id=request.project_id,
        )
        return _dto_to_response(dto)
    
    except ProjectNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project not found: {e.project_id}",
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=TaskListResponse,
    summary="Listar tareas",
)
async def list_tasks(
    project_id: str | None = Query(None, description="Filtrar por proyecto"),
    assignee_id: str | None = Query(None, description="Filtrar por asignado"),
    status: str | None = Query(None, description="Filtrar por estado"),
    limit: int = Query(20, ge=1, le=100, description="Límite de resultados"),
    offset: int = Query(0, ge=0, description="Offset para paginación"),
    service: TaskService = Depends(get_task_service),
) -> TaskListResponse:
    """Obtener lista de tareas con filtros opcionales."""
    result = await service.get_tasks(
        project_id=project_id,
        assignee_id=assignee_id,
        status=status,
        limit=limit,
        offset=offset,
    )
    
    return TaskListResponse(
        items=[_dto_to_response(dto) for dto in result.items],
        total=result.total,
        limit=result.limit,
        offset=result.offset,
        has_more=result.has_more,
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Obtener tarea",
)
async def get_task(
    task_id: str,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """Obtener una tarea por su ID."""
    dto = await service.get_task_by_id(task_id)
    
    if not dto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task not found: {task_id}",
        )
    
    return _dto_to_response(dto)


@router.post(
    "/{task_id}/assign",
    response_model=TaskResponse,
    summary="Asignar tarea",
)
async def assign_task(
    task_id: str,
    request: AssignTaskRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """Asignar una tarea a un usuario."""
    try:
        dto = await service.assign_task(
            task_id=task_id,
            user_id=request.user_id,
        )
        return _dto_to_response(dto)
    
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task not found: {task_id}",
        )
    except TaskNotAssignableError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.post(
    "/{task_id}/complete",
    response_model=TaskResponse,
    summary="Completar tarea",
)
async def complete_task(
    task_id: str,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """Marcar una tarea como completada."""
    try:
        dto = await service.complete_task(task_id)
        return _dto_to_response(dto)
    
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task not found: {task_id}",
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar tarea",
)
async def delete_task(
    task_id: str,
    service: TaskService = Depends(get_task_service),
) -> None:
    """Eliminar una tarea."""
    deleted = await service.delete_task(task_id)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task not found: {task_id}",
        )
```

### 5. Driven Adapter: Repository

```python
# infrastructure/persistence/in_memory/task_repository.py
"""Driven Adapter: Repository en memoria para tareas."""

from uuid import UUID
from typing import Dict

from domain.entities.task import Task
from domain.value_objects.task_status import TaskStatus
from domain.ports.task_repository import TaskRepository


class InMemoryTaskRepository:
    """
    Implementación en memoria del TaskRepository.
    
    Esta clase implementa el Port TaskRepository definido
    en el dominio. Es un Driven Adapter.
    """
    
    def __init__(self) -> None:
        self._tasks: Dict[UUID, Task] = {}
    
    async def save(self, task: Task) -> None:
        """Guardar o actualizar una tarea."""
        self._tasks[task.id] = task
    
    async def get_by_id(self, task_id: UUID) -> Task | None:
        """Obtener tarea por ID."""
        return self._tasks.get(task_id)
    
    async def get_all(self) -> list[Task]:
        """Obtener todas las tareas."""
        return list(self._tasks.values())
    
    async def get_by_project(self, project_id: UUID) -> list[Task]:
        """Obtener tareas de un proyecto."""
        return [
            task for task in self._tasks.values()
            if task.project_id == project_id
        ]
    
    async def get_by_assignee(self, user_id: UUID) -> list[Task]:
        """Obtener tareas asignadas a un usuario."""
        return [
            task for task in self._tasks.values()
            if task.assignee_id == user_id
        ]
    
    async def get_by_status(self, status: TaskStatus) -> list[Task]:
        """Obtener tareas por estado."""
        return [
            task for task in self._tasks.values()
            if task.status == status
        ]
    
    async def delete(self, task_id: UUID) -> bool:
        """Eliminar una tarea."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
    
    async def exists(self, task_id: UUID) -> bool:
        """Verificar si una tarea existe."""
        return task_id in self._tasks
    
    # Métodos adicionales para testing
    def clear(self) -> None:
        """Limpiar todos los datos (útil para tests)."""
        self._tasks.clear()
    
    def count(self) -> int:
        """Contar tareas (útil para tests)."""
        return len(self._tasks)
```

### 6. Error Handlers

```python
# infrastructure/api/error_handlers.py
"""Manejadores de errores para la API."""

from fastapi import Request, status
from fastapi.responses import JSONResponse

from domain.exceptions import (
    DomainError,
    TaskNotFoundError,
    TaskNotAssignableError,
    ProjectNotFoundError,
)
from application.exceptions import (
    ApplicationError,
    ValidationError,
    NotFoundError,
)


async def domain_error_handler(
    request: Request,
    exc: DomainError,
) -> JSONResponse:
    """Manejar errores de dominio."""
    
    # Mapear errores de dominio a códigos HTTP
    status_code = status.HTTP_400_BAD_REQUEST
    
    if isinstance(exc, (TaskNotFoundError, ProjectNotFoundError)):
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, TaskNotAssignableError):
        status_code = status.HTTP_409_CONFLICT
    
    return JSONResponse(
        status_code=status_code,
        content={
            "error": exc.__class__.__name__,
            "detail": str(exc),
        },
    )


async def application_error_handler(
    request: Request,
    exc: ApplicationError,
) -> JSONResponse:
    """Manejar errores de aplicación."""
    
    status_code = status.HTTP_400_BAD_REQUEST
    
    if isinstance(exc, NotFoundError):
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, ValidationError):
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    
    content = {"error": exc.__class__.__name__, "detail": str(exc)}
    
    if isinstance(exc, ValidationError):
        content["field"] = exc.field
    
    return JSONResponse(status_code=status_code, content=content)


async def generic_error_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Manejar errores genéricos (fallback)."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "InternalServerError",
            "detail": "An unexpected error occurred",
        },
    )
```

### 7. Configuración

```python
# infrastructure/config.py
"""Configuración de la aplicación."""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Configuración usando Pydantic Settings.
    
    Lee variables de entorno automáticamente.
    """
    
    # API
    app_name: str = "Task Management API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Database (futuro)
    database_url: str = "sqlite:///./tasks.db"
    
    # Persistence type
    persistence_type: str = "memory"  # "memory" | "sqlite"
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


@lru_cache
def get_settings() -> Settings:
    """
    Obtener configuración (cacheada).
    
    Usa lru_cache para que solo se lea una vez.
    """
    return Settings()
```

---

## 🧪 Ejercicio de Comprensión

¿Por qué el Router usa `TaskService` en lugar de `CreateTaskUseCase` directamente?

```python
# Opción A: Usar Service
@router.post("/")
async def create_task(
    request: CreateTaskRequest,
    service: TaskService = Depends(get_task_service),
):
    return await service.create_task(...)

# Opción B: Usar Use Case directamente
@router.post("/")
async def create_task(
    request: CreateTaskRequest,
    use_case: CreateTaskUseCase = Depends(get_create_task_use_case),
):
    return await use_case.execute(...)
```

<details>
<summary>Ver respuesta</summary>

**Ambas opciones son válidas**, pero tienen diferentes trade-offs:

**Opción A (Service)**:
- ✅ Simplifica el router (una sola dependencia)
- ✅ Fácil de mockear en tests
- ❌ Añade una capa de indirección

**Opción B (Use Case directo)**:
- ✅ Más explícito sobre qué se usa
- ✅ Menos código (sin service intermedio)
- ❌ Más dependencias en el router

La elección depende del tamaño del proyecto. Para proyectos pequeños, Use Cases directos están bien. Para proyectos grandes, Services como fachada simplifican.

</details>

---

## ✅ Checklist de Verificación

- [ ] Driving Adapters (API) no contienen lógica de negocio
- [ ] Driven Adapters implementan los Ports del dominio
- [ ] Schemas de API son diferentes de DTOs de aplicación
- [ ] Errores de dominio se traducen a respuestas HTTP
- [ ] Configuración está centralizada

---

_Siguiente: [05 - Composition Root](05-composition-root.md)_
