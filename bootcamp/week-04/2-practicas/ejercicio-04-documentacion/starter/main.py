"""
Ejercicio 04: Documentación OpenAPI
Semana 04 - Responses y Manejo de Errores

Instrucciones:
1. Lee el README.md para entender cada paso
2. Descomenta el código de cada sección
3. Ejecuta: docker compose up --build
4. Revisa: http://localhost:8000/docs y http://localhost:8000/redoc
"""

from datetime import datetime
from enum import Enum
from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Query, status
from pydantic import BaseModel, Field, EmailStr

# ============================================
# PASO 1: Metadata de la API
# ============================================
print("--- Paso 1: Metadata de la API ---")

# Descomenta para configurar metadata completa
# app = FastAPI(
#     title="Task Manager API",
#     description="""
# # Task Manager API 📋
# 
# API REST para gestión de tareas y proyectos.
# 
# ## Características
# 
# - ✅ **Tareas**: CRUD completo
# - ✅ **Usuarios**: Gestión de usuarios
# - ✅ **Proyectos**: Organización de tareas
# 
# ## Autenticación
# 
# Por implementar en v2.0 con JWT.
# 
# ## Límites
# 
# - Rate limit: 100 requests/minuto
# - Max items por página: 100
#     """,
#     version="1.0.0",
#     terms_of_service="https://example.com/terms/",
#     contact={
#         "name": "API Support Team",
#         "url": "https://example.com/support",
#         "email": "api-support@example.com"
#     },
#     license_info={
#         "name": "MIT",
#         "url": "https://opensource.org/licenses/MIT"
#     },
#     docs_url="/docs",
#     redoc_url="/redoc",
#     openapi_url="/openapi.json"
# )

# Versión simple para empezar
app = FastAPI(title="Documentación OpenAPI Practice")


# ============================================
# PASO 2: Tags para Agrupar Endpoints
# ============================================
print("--- Paso 2: Tags ---")

# Descomenta para agregar tags con descripción
# tags_metadata = [
#     {
#         "name": "tasks",
#         "description": "Gestión de tareas - **CRUD completo**",
#     },
#     {
#         "name": "users",
#         "description": "Gestión de usuarios y perfiles",
#         "externalDocs": {
#             "description": "Documentación externa",
#             "url": "https://example.com/docs/users"
#         }
#     },
#     {
#         "name": "projects",
#         "description": "Organización de tareas en proyectos",
#     },
#     {
#         "name": "health",
#         "description": "Endpoints de monitoreo y salud del servicio",
#     }
# ]

# # Recrea la app con tags
# app = FastAPI(
#     title="Task Manager API",
#     version="1.0.0",
#     openapi_tags=tags_metadata
# )

# # Endpoints con tags
# @app.get("/tasks", tags=["tasks"])
# async def list_tasks():
#     """Lista todas las tareas."""
#     return []

# @app.get("/users", tags=["users"])
# async def list_users():
#     """Lista todos los usuarios."""
#     return []

# @app.get("/projects", tags=["projects"])
# async def list_projects():
#     """Lista todos los proyectos."""
#     return []


# ============================================
# PASO 3: Documentar Endpoints
# ============================================
print("--- Paso 3: Documentar Endpoints ---")

# class TaskStatus(str, Enum):
#     pending = "pending"
#     in_progress = "in_progress"
#     completed = "completed"

# class Task(BaseModel):
#     id: int
#     title: str
#     status: TaskStatus
#     created_at: datetime

# tasks_db = {
#     1: {"id": 1, "title": "Learn FastAPI", "status": "pending", "created_at": datetime.now()}
# }

# @app.get(
#     "/tasks/{task_id}",
#     tags=["tasks"],
#     summary="Obtener tarea por ID",
#     description="""
#     Recupera una tarea específica usando su ID único.
#     
#     - **task_id**: ID numérico de la tarea (debe ser positivo)
#     
#     Si la tarea no existe, retorna un error 404.
#     """,
#     response_description="La tarea solicitada con todos sus campos",
#     response_model=Task
# )
# async def get_task(
#     task_id: Annotated[
#         int,
#         Path(
#             title="Task ID",
#             description="El ID único de la tarea a obtener",
#             ge=1,
#             example=1
#         )
#     ]
# ):
#     """
#     Este es el docstring de la función.
#     
#     Si no se especifica `description` en el decorador,
#     este texto aparece en la documentación.
#     """
#     if task_id not in tasks_db:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return tasks_db[task_id]

# @app.get(
#     "/tasks",
#     tags=["tasks"],
#     summary="Listar tareas con filtros",
#     response_model=list[Task]
# )
# async def list_tasks_filtered(
#     status_filter: Annotated[
#         TaskStatus | None,
#         Query(
#             alias="status",
#             title="Status Filter",
#             description="Filtrar tareas por estado",
#             example="pending"
#         )
#     ] = None,
#     limit: Annotated[
#         int,
#         Query(
#             title="Limit",
#             description="Máximo número de resultados (1-100)",
#             ge=1,
#             le=100,
#             example=10
#         )
#     ] = 10
# ):
#     """
#     Lista tareas con filtrado opcional por estado.
#     
#     - **status**: Filtrar por estado (pending, in_progress, completed)
#     - **limit**: Máximo número de resultados
#     """
#     tasks = list(tasks_db.values())
#     if status_filter:
#         tasks = [t for t in tasks if t["status"] == status_filter.value]
#     return tasks[:limit]


# ============================================
# PASO 4: Ejemplos en Schemas
# ============================================
print("--- Paso 4: Ejemplos en Schemas ---")

# class UserCreate(BaseModel):
#     """Schema para crear un usuario"""
#     email: EmailStr = Field(
#         ...,
#         description="Email único del usuario",
#         examples=["john@example.com", "jane@example.com"]
#     )
#     name: str = Field(
#         ...,
#         min_length=2,
#         max_length=100,
#         description="Nombre completo del usuario",
#         examples=["John Doe", "Jane Smith"]
#     )
#     age: int | None = Field(
#         None,
#         ge=0,
#         le=150,
#         description="Edad del usuario (opcional)",
#         examples=[25, 30, None]
#     )
#     
#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "email": "john.doe@example.com",
#                     "name": "John Doe",
#                     "age": 28
#                 },
#                 {
#                     "email": "jane.smith@example.com",
#                     "name": "Jane Smith",
#                     "age": None
#                 }
#             ]
#         }
#     }

# class UserResponse(BaseModel):
#     """Schema de respuesta de usuario"""
#     id: int = Field(..., description="ID único del usuario")
#     email: EmailStr
#     name: str
#     age: int | None
#     created_at: datetime = Field(..., description="Fecha de creación")
#     
#     model_config = {
#         "json_schema_extra": {
#             "example": {
#                 "id": 1,
#                 "email": "john.doe@example.com",
#                 "name": "John Doe",
#                 "age": 28,
#                 "created_at": "2024-01-15T10:30:00"
#             }
#         }
#     }

# users_db: dict[int, dict] = {}
# user_counter = 0

# @app.post(
#     "/users",
#     tags=["users"],
#     response_model=UserResponse,
#     status_code=status.HTTP_201_CREATED,
#     summary="Crear nuevo usuario"
# )
# async def create_user(user: UserCreate):
#     """
#     Crea un nuevo usuario en el sistema.
#     
#     Los ejemplos del schema aparecen en "Try it out".
#     """
#     global user_counter
#     user_counter += 1
#     
#     new_user = {
#         "id": user_counter,
#         "email": user.email,
#         "name": user.name,
#         "age": user.age,
#         "created_at": datetime.now()
#     }
#     users_db[user_counter] = new_user
#     return new_user


# ============================================
# PASO 5: Documentar Múltiples Responses
# ============================================
print("--- Paso 5: Múltiples Responses ---")

# class ProductResponse(BaseModel):
#     id: int
#     name: str
#     price: float
#     
#     model_config = {
#         "json_schema_extra": {
#             "example": {"id": 1, "name": "Laptop", "price": 999.99}
#         }
#     }

# class ErrorResponse(BaseModel):
#     detail: str
#     
#     model_config = {
#         "json_schema_extra": {
#             "example": {"detail": "Product not found"}
#         }
#     }

# class ValidationErrorResponse(BaseModel):
#     detail: list[dict]
#     
#     model_config = {
#         "json_schema_extra": {
#             "example": {
#                 "detail": [
#                     {
#                         "loc": ["path", "product_id"],
#                         "msg": "value is not a valid integer",
#                         "type": "type_error.integer"
#                     }
#                 ]
#             }
#         }
#     }

# products_db = {
#     1: {"id": 1, "name": "Laptop", "price": 999.99},
#     2: {"id": 2, "name": "Mouse", "price": 29.99}
# }

# @app.get(
#     "/products/{product_id}",
#     tags=["products"],
#     response_model=ProductResponse,
#     summary="Obtener producto",
#     responses={
#         200: {
#             "description": "Producto encontrado exitosamente",
#             "model": ProductResponse,
#             "content": {
#                 "application/json": {
#                     "example": {"id": 1, "name": "Laptop", "price": 999.99}
#                 }
#             }
#         },
#         404: {
#             "description": "Producto no encontrado",
#             "model": ErrorResponse,
#             "content": {
#                 "application/json": {
#                     "example": {"detail": "Product with id 99 not found"}
#                 }
#             }
#         },
#         422: {
#             "description": "Error de validación",
#             "model": ValidationErrorResponse
#         }
#     }
# )
# async def get_product(
#     product_id: Annotated[int, Path(ge=1, description="ID del producto")]
# ):
#     """
#     Obtiene un producto por su ID.
#     
#     En la documentación verás todos los posibles
#     códigos de respuesta documentados.
#     """
#     if product_id not in products_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Product with id {product_id} not found"
#         )
#     return products_db[product_id]

# @app.delete(
#     "/products/{product_id}",
#     tags=["products"],
#     status_code=status.HTTP_204_NO_CONTENT,
#     summary="Eliminar producto",
#     responses={
#         204: {"description": "Producto eliminado exitosamente"},
#         404: {
#             "description": "Producto no encontrado",
#             "model": ErrorResponse
#         }
#     }
# )
# async def delete_product(product_id: int):
#     """Elimina un producto del sistema."""
#     if product_id not in products_db:
#         raise HTTPException(status_code=404, detail="Product not found")
#     del products_db[product_id]
#     return None


# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health", tags=["health"] if "health" in dir() else None)
async def health_check():
    """Verificar que el servidor está funcionando."""
    return {"status": "healthy", "exercise": "04-documentacion"}
