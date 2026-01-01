"""
Ejercicio 02: Status Codes
Semana 04 - Responses y Manejo de Errores

Instrucciones:
1. Lee el README.md para entender cada paso
2. Descomenta el código de cada sección
3. Ejecuta: docker compose up --build
4. Prueba en: http://localhost:8000/docs
"""

from datetime import datetime
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="Status Codes Practice",
    description="Ejercicio para practicar códigos de estado HTTP",
    version="1.0.0"
)

# ============================================
# PASO 1: Códigos de Éxito Básicos
# ============================================
print("--- Paso 1: Códigos de Éxito ---")

# class TaskCreate(BaseModel):
#     title: str = Field(..., min_length=1, max_length=200)
#     description: str | None = None

# class TaskResponse(BaseModel):
#     id: int
#     title: str
#     description: str | None
#     completed: bool
#     created_at: datetime

# tasks_db: dict[int, dict] = {}
# task_counter = 0

# # 201 Created - Para POST que crea recursos
# @app.post(
#     "/tasks",
#     response_model=TaskResponse,
#     status_code=status.HTTP_201_CREATED,
#     summary="Crear tarea"
# )
# async def create_task(task: TaskCreate):
#     """
#     Crea una nueva tarea.
#     
#     Retorna **201 Created** con la tarea creada.
#     """
#     global task_counter
#     task_counter += 1
#     
#     new_task = {
#         "id": task_counter,
#         "title": task.title,
#         "description": task.description,
#         "completed": False,
#         "created_at": datetime.now()
#     }
#     tasks_db[task_counter] = new_task
#     return new_task

# # 200 OK - Para GET exitoso (default)
# @app.get(
#     "/tasks",
#     response_model=list[TaskResponse],
#     summary="Listar tareas"
# )
# async def list_tasks():
#     """
#     Lista todas las tareas.
#     
#     Retorna **200 OK** (código por defecto).
#     """
#     return list(tasks_db.values())

# # 204 No Content - Para DELETE exitoso
# @app.delete(
#     "/tasks/{task_id}",
#     status_code=status.HTTP_204_NO_CONTENT,
#     summary="Eliminar tarea"
# )
# async def delete_task(task_id: int):
#     """
#     Elimina una tarea.
#     
#     Retorna **204 No Content** (sin body).
#     """
#     if task_id not in tasks_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Task {task_id} not found"
#         )
#     del tasks_db[task_id]
#     return None  # 204 no tiene body


# ============================================
# PASO 2: Códigos de Error del Cliente
# ============================================
print("--- Paso 2: Códigos de Error 4xx ---")

# class UserCreate(BaseModel):
#     email: EmailStr
#     name: str = Field(..., min_length=2)

# class UserResponse(BaseModel):
#     id: int
#     email: EmailStr
#     name: str

# users_db: dict[int, dict] = {}
# user_counter = 0

# # 404 Not Found - Recurso no existe
# @app.get("/tasks/{task_id}", response_model=TaskResponse)
# async def get_task(task_id: int):
#     """
#     Obtiene una tarea por ID.
#     
#     - **200 OK**: Tarea encontrada
#     - **404 Not Found**: Tarea no existe
#     """
#     if task_id not in tasks_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Task {task_id} not found"
#         )
#     return tasks_db[task_id]

# # 409 Conflict - Recurso duplicado
# @app.post(
#     "/users",
#     response_model=UserResponse,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_user(user: UserCreate):
#     """
#     Crea un nuevo usuario.
#     
#     - **201 Created**: Usuario creado
#     - **409 Conflict**: Email ya registrado
#     """
#     global user_counter
#     
#     # Verificar email duplicado
#     for existing_user in users_db.values():
#         if existing_user["email"] == user.email:
#             raise HTTPException(
#                 status_code=status.HTTP_409_CONFLICT,
#                 detail=f"Email '{user.email}' is already registered"
#             )
#     
#     user_counter += 1
#     new_user = {
#         "id": user_counter,
#         "email": user.email,
#         "name": user.name
#     }
#     users_db[user_counter] = new_user
#     return new_user

# # 400 Bad Request - Lógica de negocio
# @app.post("/tasks/{task_id}/complete")
# async def complete_task(task_id: int):
#     """
#     Marca una tarea como completada.
#     
#     - **200 OK**: Tarea completada
#     - **400 Bad Request**: Tarea ya estaba completada
#     - **404 Not Found**: Tarea no existe
#     """
#     if task_id not in tasks_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Task {task_id} not found"
#         )
#     
#     task = tasks_db[task_id]
#     
#     if task["completed"]:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Task is already completed"
#         )
#     
#     task["completed"] = True
#     return {"message": "Task marked as completed", "task": task}


# ============================================
# PASO 3: Status Code Dinámico
# ============================================
print("--- Paso 3: Status Code Dinámico ---")

# class ItemCreate(BaseModel):
#     name: str
#     price: float

# class ItemResponse(BaseModel):
#     id: int
#     name: str
#     price: float
#     action: str  # "created" o "updated"

# items_db: dict[int, dict] = {}

# # PUT puede crear o actualizar
# @app.put("/items/{item_id}", response_model=ItemResponse)
# async def upsert_item(item_id: int, item: ItemCreate, response: Response):
#     """
#     Crea o actualiza un item (upsert).
#     
#     - **200 OK**: Item actualizado
#     - **201 Created**: Item creado
#     """
#     if item_id in items_db:
#         # Actualizar existente
#         items_db[item_id].update({
#             "name": item.name,
#             "price": item.price
#         })
#         response.status_code = status.HTTP_200_OK
#         action = "updated"
#     else:
#         # Crear nuevo
#         items_db[item_id] = {
#             "id": item_id,
#             "name": item.name,
#             "price": item.price
#         }
#         response.status_code = status.HTTP_201_CREATED
#         action = "created"
#     
#     return {**items_db[item_id], "action": action}


# ============================================
# PASO 4: Documentar Responses en OpenAPI
# ============================================
print("--- Paso 4: Documentar Responses ---")

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

# products_db = {
#     1: {"id": 1, "name": "Laptop", "price": 999.99},
#     2: {"id": 2, "name": "Mouse", "price": 29.99}
# }

# @app.get(
#     "/products/{product_id}",
#     response_model=ProductResponse,
#     responses={
#         200: {
#             "description": "Producto encontrado exitosamente",
#             "model": ProductResponse
#         },
#         404: {
#             "description": "Producto no encontrado",
#             "model": ErrorResponse,
#             "content": {
#                 "application/json": {
#                     "example": {"detail": "Product 99 not found"}
#                 }
#             }
#         }
#     },
#     summary="Obtener producto",
#     description="Obtiene un producto por su ID único."
# )
# async def get_product(product_id: int):
#     """
#     Obtiene un producto por ID.
#     
#     Los posibles códigos de respuesta están documentados
#     y aparecen en Swagger UI.
#     """
#     if product_id not in products_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Product {product_id} not found"
#         )
#     return products_db[product_id]

# @app.delete(
#     "/products/{product_id}",
#     status_code=status.HTTP_204_NO_CONTENT,
#     responses={
#         204: {"description": "Producto eliminado exitosamente"},
#         404: {
#             "description": "Producto no encontrado",
#             "model": ErrorResponse
#         }
#     }
# )
# async def delete_product(product_id: int):
#     """Elimina un producto."""
#     if product_id not in products_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Product {product_id} not found"
#         )
#     del products_db[product_id]
#     return None


# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health")
async def health_check():
    """Verificar que el servidor está funcionando."""
    return {"status": "healthy", "exercise": "02-status-codes"}
