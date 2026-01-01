# 📖 Documentación OpenAPI

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Entender la especificación OpenAPI
- ✅ Personalizar la documentación automática
- ✅ Usar Swagger UI y ReDoc
- ✅ Documentar endpoints con ejemplos
- ✅ Agrupar endpoints con tags

---

## 📚 Contenido

### 1. ¿Qué es OpenAPI?

**OpenAPI** (antes Swagger) es una especificación estándar para describir APIs REST. FastAPI genera automáticamente documentación OpenAPI 3.1.

#### Acceso a la Documentación

```python
from fastapi import FastAPI

app = FastAPI()

# Documentación disponible automáticamente:
# - Swagger UI: http://localhost:8000/docs
# - ReDoc: http://localhost:8000/redoc
# - OpenAPI JSON: http://localhost:8000/openapi.json
```

---

### 2. Configurar Metadata de la API

```python
from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="""
## Task Manager API 🚀

Esta API permite gestionar tareas y proyectos.

### Características

* **Tareas**: CRUD completo de tareas
* **Proyectos**: Organización de tareas
* **Usuarios**: Autenticación y permisos

### Autenticación

Usa Bearer Token en el header `Authorization`.
    """,
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "API Support",
        "url": "https://example.com/contact/",
        "email": "support@example.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    # URLs de documentación personalizadas
    docs_url="/docs",           # Swagger UI (None para deshabilitar)
    redoc_url="/redoc",         # ReDoc (None para deshabilitar)
    openapi_url="/openapi.json" # Schema JSON
)
```

---

### 3. Tags para Agrupar Endpoints

```python
from fastapi import FastAPI, APIRouter
from enum import Enum

# Definir tags con descripción
tags_metadata = [
    {
        "name": "tasks",
        "description": "Operaciones con tareas. **CRUD completo**.",
    },
    {
        "name": "users",
        "description": "Gestión de usuarios y autenticación.",
        "externalDocs": {
            "description": "Documentación externa",
            "url": "https://example.com/docs/users"
        }
    },
    {
        "name": "admin",
        "description": "Operaciones administrativas. _Requiere permisos especiales_.",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Usar tags en endpoints
@app.get("/tasks", tags=["tasks"])
async def list_tasks():
    """Lista todas las tareas."""
    return []

@app.post("/tasks", tags=["tasks"])
async def create_task(title: str):
    """Crea una nueva tarea."""
    return {"title": title}

@app.get("/users/me", tags=["users"])
async def get_current_user():
    """Obtiene el usuario actual."""
    return {"id": 1, "name": "John"}

# Router con tag por defecto
admin_router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

@admin_router.get("/stats")
async def admin_stats():
    """Estadísticas del sistema (admin only)."""
    return {"users": 100, "tasks": 500}

app.include_router(admin_router)
```

---

### 4. Documentar Endpoints

#### Docstrings y Summary

```python
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get(
    "/tasks/{task_id}",
    summary="Obtener tarea por ID",
    description="""
    Recupera una tarea específica usando su ID único.
    
    - **task_id**: ID numérico de la tarea
    
    Si la tarea no existe, retorna 404.
    """,
    response_description="La tarea solicitada",
    tags=["tasks"]
)
async def get_task(task_id: int):
    """
    Esta es la documentación del docstring.
    
    Aparece si no se especifica description en el decorador.
    """
    return {"id": task_id, "title": "Task", "completed": False}

# Usando solo docstring (más común)
@app.post("/tasks", tags=["tasks"], status_code=201)
async def create_task(task: Task):
    """
    Crea una nueva tarea.
    
    - **title**: Título de la tarea (requerido)
    - **completed**: Estado inicial (default: false)
    
    Retorna la tarea creada con su ID asignado.
    """
    return task
```

#### Documentar Parámetros

```python
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(
    item_id: Annotated[
        int,
        Path(
            title="Item ID",
            description="ID único del item a buscar",
            ge=1,
            example=123
        )
    ],
    q: Annotated[
        str | None,
        Query(
            title="Search Query",
            description="Término de búsqueda opcional",
            min_length=1,
            max_length=50,
            example="laptop"
        )
    ] = None,
    skip: Annotated[
        int,
        Query(
            title="Skip",
            description="Número de resultados a saltar",
            ge=0,
            example=0
        )
    ] = 0,
    limit: Annotated[
        int,
        Query(
            title="Limit",
            description="Máximo número de resultados",
            ge=1,
            le=100,
            example=10
        )
    ] = 10
):
    """Obtiene un item con búsqueda y paginación."""
    return {
        "item_id": item_id,
        "q": q,
        "skip": skip,
        "limit": limit
    }
```

---

### 5. Ejemplos en Schemas

```python
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, EmailStr

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Título de la tarea",
        examples=["Completar informe", "Revisar código"]
    )
    description: str | None = Field(
        None,
        max_length=1000,
        description="Descripción detallada (opcional)",
        examples=["Informe mensual de ventas", None]
    )
    priority: Priority = Field(
        Priority.medium,
        description="Nivel de prioridad"
    )
    due_date: datetime | None = Field(
        None,
        description="Fecha límite",
        examples=["2024-12-31T23:59:59"]
    )
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Completar proyecto FastAPI",
                    "description": "Terminar el bootcamp de FastAPI",
                    "priority": "high",
                    "due_date": "2024-06-30T18:00:00"
                },
                {
                    "title": "Revisar emails",
                    "description": None,
                    "priority": "low",
                    "due_date": None
                }
            ]
        }
    }

class TaskResponse(BaseModel):
    id: int = Field(..., description="ID único de la tarea")
    title: str
    description: str | None
    priority: Priority
    due_date: datetime | None
    completed: bool = Field(False, description="Estado de completitud")
    created_at: datetime = Field(..., description="Fecha de creación")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Completar proyecto FastAPI",
                "description": "Terminar el bootcamp",
                "priority": "high",
                "due_date": "2024-06-30T18:00:00",
                "completed": False,
                "created_at": "2024-01-01T10:00:00"
            }
        }
    }
```

---

### 6. Documentar Múltiples Responses

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

class ErrorResponse(BaseModel):
    detail: str

class ValidationErrorResponse(BaseModel):
    detail: list[dict]

@app.get(
    "/items/{item_id}",
    response_model=Item,
    responses={
        200: {
            "description": "Item encontrado exitosamente",
            "model": Item,
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Laptop",
                        "price": 999.99
                    }
                }
            }
        },
        404: {
            "description": "Item no encontrado",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {"detail": "Item with id 99 not found"}
                }
            }
        },
        422: {
            "description": "Error de validación",
            "model": ValidationErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["path", "item_id"],
                                "msg": "value is not a valid integer",
                                "type": "type_error.integer"
                            }
                        ]
                    }
                }
            }
        }
    }
)
async def get_item(item_id: int):
    """
    Obtiene un item por su ID.
    
    Retorna el item completo si existe, o error 404 si no.
    """
    items_db = {1: {"id": 1, "name": "Laptop", "price": 999.99}}
    
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return items_db[item_id]
```

---

### 7. Deprecar Endpoints

```python
from fastapi import FastAPI

app = FastAPI()

# Endpoint deprecado
@app.get(
    "/items-old",
    deprecated=True,
    summary="[DEPRECATED] Lista items",
    description="⚠️ Este endpoint está deprecado. Usa `/items` en su lugar."
)
async def list_items_old():
    """Este endpoint será removido en v2.0"""
    return []

# Nuevo endpoint
@app.get("/items", summary="Lista items")
async def list_items():
    """Endpoint actual para listar items."""
    return []
```

---

### 8. Ocultar Endpoints de la Documentación

```python
from fastapi import FastAPI

app = FastAPI()

# Endpoint visible en docs
@app.get("/public")
async def public_endpoint():
    return {"message": "Visible in docs"}

# Endpoint oculto de docs
@app.get("/internal", include_in_schema=False)
async def internal_endpoint():
    """Este endpoint no aparece en la documentación."""
    return {"message": "Hidden from docs"}

# Health check oculto
@app.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "ok"}
```

---

### 9. Personalizar OpenAPI Schema

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

@app.get("/items")
async def list_items():
    return []

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Custom API",
        version="2.0.0",
        description="API con schema personalizado",
        routes=app.routes,
    )
    
    # Agregar logo
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png"
    }
    
    # Agregar servers
    openapi_schema["servers"] = [
        {"url": "https://api.example.com", "description": "Production"},
        {"url": "https://staging.example.com", "description": "Staging"},
        {"url": "http://localhost:8000", "description": "Development"}
    ]
    
    # Agregar seguridad global
    openapi_schema["security"] = [{"bearerAuth": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

---

### 10. Ejemplo Completo: API Documentada

```python
from datetime import datetime
from enum import Enum
from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Query, status
from pydantic import BaseModel, Field

# ============================================
# CONFIGURACIÓN DE LA API
# ============================================

tags_metadata = [
    {
        "name": "tasks",
        "description": "Gestión de tareas - CRUD completo",
    },
    {
        "name": "health",
        "description": "Estado del servicio",
    }
]

app = FastAPI(
    title="Task Manager API",
    description="""
# Task Manager API 📋

API REST para gestión de tareas.

## Características

- ✅ CRUD completo de tareas
- ✅ Filtrado y paginación
- ✅ Validación de datos
- ✅ Manejo de errores

## Autenticación

Por implementar en versión 2.0
    """,
    version="1.0.0",
    openapi_tags=tags_metadata,
    contact={
        "name": "Dev Team",
        "email": "dev@example.com"
    }
)

# ============================================
# MODELOS
# ============================================

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskCreate(BaseModel):
    """Schema para crear una tarea"""
    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Título de la tarea"
    )
    description: str | None = Field(
        None,
        max_length=1000,
        description="Descripción opcional"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Aprender FastAPI",
                "description": "Completar el bootcamp de FastAPI"
            }
        }
    }

class TaskResponse(BaseModel):
    """Schema de respuesta de tarea"""
    id: int = Field(..., description="ID único")
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Aprender FastAPI",
                "description": "Completar el bootcamp",
                "status": "pending",
                "created_at": "2024-01-01T10:00:00"
            }
        }
    }

class TaskList(BaseModel):
    """Lista paginada de tareas"""
    tasks: list[TaskResponse]
    total: int
    page: int
    per_page: int

class ErrorResponse(BaseModel):
    """Respuesta de error estándar"""
    detail: str
    
    model_config = {
        "json_schema_extra": {
            "example": {"detail": "Task not found"}
        }
    }

# ============================================
# BASE DE DATOS SIMULADA
# ============================================

tasks_db: dict[int, dict] = {
    1: {
        "id": 1,
        "title": "Tarea de ejemplo",
        "description": "Esta es una tarea de ejemplo",
        "status": TaskStatus.pending,
        "created_at": datetime.now()
    }
}
task_counter = 1

# ============================================
# ENDPOINTS
# ============================================

@app.get(
    "/health",
    tags=["health"],
    summary="Health check",
    response_description="Estado del servicio"
)
async def health_check():
    """
    Verifica que el servicio está funcionando.
    
    Útil para load balancers y monitoreo.
    """
    return {"status": "healthy", "timestamp": datetime.now()}

@app.get(
    "/tasks",
    tags=["tasks"],
    response_model=TaskList,
    summary="Listar tareas",
    response_description="Lista paginada de tareas"
)
async def list_tasks(
    status_filter: Annotated[
        TaskStatus | None,
        Query(
            alias="status",
            description="Filtrar por estado"
        )
    ] = None,
    page: Annotated[
        int,
        Query(ge=1, description="Número de página")
    ] = 1,
    per_page: Annotated[
        int,
        Query(ge=1, le=100, description="Items por página")
    ] = 10
):
    """
    Lista todas las tareas con paginación opcional.
    
    - **status**: Filtrar por estado (pending, in_progress, completed)
    - **page**: Página a obtener (default: 1)
    - **per_page**: Resultados por página (default: 10, max: 100)
    """
    tasks = list(tasks_db.values())
    
    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter]
    
    total = len(tasks)
    start = (page - 1) * per_page
    end = start + per_page
    
    return {
        "tasks": tasks[start:end],
        "total": total,
        "page": page,
        "per_page": per_page
    }

@app.get(
    "/tasks/{task_id}",
    tags=["tasks"],
    response_model=TaskResponse,
    summary="Obtener tarea",
    responses={
        200: {"description": "Tarea encontrada"},
        404: {"description": "Tarea no encontrada", "model": ErrorResponse}
    }
)
async def get_task(
    task_id: Annotated[
        int,
        Path(
            description="ID de la tarea",
            ge=1,
            example=1
        )
    ]
):
    """
    Obtiene una tarea específica por su ID.
    
    Retorna 404 si la tarea no existe.
    """
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
    return tasks_db[task_id]

@app.post(
    "/tasks",
    tags=["tasks"],
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear tarea",
    response_description="Tarea creada exitosamente"
)
async def create_task(task: TaskCreate):
    """
    Crea una nueva tarea.
    
    - **title**: Título (requerido, 1-200 caracteres)
    - **description**: Descripción (opcional, max 1000 caracteres)
    
    Retorna la tarea creada con su ID asignado.
    """
    global task_counter
    task_counter += 1
    
    new_task = {
        "id": task_counter,
        "title": task.title,
        "description": task.description,
        "status": TaskStatus.pending,
        "created_at": datetime.now()
    }
    tasks_db[task_counter] = new_task
    return new_task

@app.delete(
    "/tasks/{task_id}",
    tags=["tasks"],
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar tarea",
    responses={
        204: {"description": "Tarea eliminada"},
        404: {"description": "Tarea no encontrada", "model": ErrorResponse}
    }
)
async def delete_task(
    task_id: Annotated[int, Path(description="ID de la tarea", ge=1)]
):
    """
    Elimina una tarea por su ID.
    
    Retorna 204 si se elimina exitosamente, 404 si no existe.
    """
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
    del tasks_db[task_id]
    return None
```

---

## 🎯 Resumen

| Elemento | Uso |
|----------|-----|
| `title`, `description` | Metadata de la API |
| `tags` | Agrupar endpoints |
| `summary` | Título corto del endpoint |
| `description` / docstring | Descripción detallada |
| `responses` | Documentar códigos de respuesta |
| `deprecated` | Marcar endpoints obsoletos |
| `include_in_schema` | Ocultar de docs |
| `Field(description=...)` | Documentar campos |
| `json_schema_extra` | Ejemplos en schemas |

### Mejores Prácticas

1. ✅ Siempre documenta con docstrings descriptivos
2. ✅ Usa tags para organizar endpoints
3. ✅ Incluye ejemplos realistas
4. ✅ Documenta todos los códigos de respuesta posibles
5. ✅ Usa `Field(description=...)` en todos los campos
6. ✅ Depreca antes de eliminar endpoints

---

## 📚 Recursos Adicionales

- [FastAPI OpenAPI](https://fastapi.tiangolo.com/tutorial/metadata/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [ReDoc](https://github.com/Redocly/redoc)

---

[← Anterior: Responses Avanzadas](04-responses-avanzadas.md) | [Volver a Teoría →](../README.md)
