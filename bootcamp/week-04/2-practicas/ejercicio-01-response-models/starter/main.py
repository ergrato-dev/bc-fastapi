"""
Ejercicio 01: Response Models
Semana 04 - Responses y Manejo de Errores

Instrucciones:
1. Lee el README.md para entender cada paso
2. Descomenta el código de cada sección
3. Ejecuta: docker compose up --build
4. Prueba en: http://localhost:8000/docs
"""

from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="Response Models Practice",
    description="Ejercicio para practicar response models",
    version="1.0.0"
)

# ============================================
# PASO 1: Modelo Base y Response
# ============================================
print("--- Paso 1: Response Model Básico ---")

# Modelos para usuarios
# UserCreate incluye password (input)
# UserResponse NO incluye password (output)

# class UserCreate(BaseModel):
#     email: EmailStr
#     name: str
#     password: str

# class UserResponse(BaseModel):
#     id: int
#     email: EmailStr
#     name: str
#     created_at: datetime
#     # Nota: NO incluimos password aquí

# # Base de datos simulada
# users_db: dict[int, dict] = {}
# user_counter = 0

# @app.post("/users", response_model=UserResponse, status_code=201)
# async def create_user(user: UserCreate):
#     """
#     Crea un usuario.
#     
#     Aunque retornemos password en el dict,
#     response_model=UserResponse lo filtrará automáticamente.
#     """
#     global user_counter
#     user_counter += 1
#     
#     new_user = {
#         "id": user_counter,
#         "email": user.email,
#         "name": user.name,
#         "password": user.password,  # Se guarda pero NO se retorna
#         "created_at": datetime.now()
#     }
#     users_db[user_counter] = new_user
#     
#     return new_user  # password será filtrado


# ============================================
# PASO 2: Response Model Exclude Unset
# ============================================
print("--- Paso 2: Exclude Unset ---")

# Modelo con muchos campos opcionales

# class Item(BaseModel):
#     id: int
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []

# # Items donde algunos campos no están establecidos
# items_db: dict[int, dict] = {
#     1: {"id": 1, "name": "Item básico", "price": 50.0},
#     2: {
#         "id": 2,
#         "name": "Item completo",
#         "description": "Con todos los campos",
#         "price": 100.0,
#         "tax": 15.0,
#         "tags": ["premium", "featured"]
#     }
# }

# @app.get(
#     "/items/{item_id}",
#     response_model=Item,
#     response_model_exclude_unset=True
# )
# async def get_item(item_id: int):
#     """
#     Obtiene un item.
#     
#     Con response_model_exclude_unset=True:
#     - Item 1 retorna solo: id, name, price
#     - Item 2 retorna todos los campos
#     """
#     if item_id not in items_db:
#         return {"id": 0, "name": "Not found", "price": 0}
#     return items_db[item_id]


# ============================================
# PASO 3: Lista de Modelos
# ============================================
print("--- Paso 3: Lista de Modelos ---")

# class Product(BaseModel):
#     id: int
#     name: str
#     price: float
#     in_stock: bool = True

# products_db: dict[int, dict] = {
#     1: {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
#     2: {"id": 2, "name": "Mouse", "price": 29.99, "in_stock": True},
#     3: {"id": 3, "name": "Keyboard", "price": 79.99, "in_stock": False}
# }

# @app.get("/products", response_model=list[Product])
# async def list_products():
#     """
#     Lista todos los productos.
#     
#     response_model=list[Product] garantiza que cada
#     elemento de la lista cumpla con el schema.
#     """
#     return list(products_db.values())

# @app.get("/products/available", response_model=list[Product])
# async def list_available_products():
#     """Lista solo productos en stock."""
#     return [p for p in products_db.values() if p["in_stock"]]


# ============================================
# PASO 4: Respuesta con Paginación
# ============================================
print("--- Paso 4: Respuesta Paginada ---")

# class Task(BaseModel):
#     id: int
#     title: str
#     completed: bool = False

# class PaginatedTasks(BaseModel):
#     """Respuesta paginada de tareas"""
#     tasks: list[Task]
#     total: int
#     page: int
#     per_page: int
#     pages: int
#     
#     model_config = {
#         "json_schema_extra": {
#             "example": {
#                 "tasks": [{"id": 1, "title": "Task 1", "completed": False}],
#                 "total": 50,
#                 "page": 1,
#                 "per_page": 10,
#                 "pages": 5
#             }
#         }
#     }

# # Generar tareas de ejemplo
# tasks_db = {i: {"id": i, "title": f"Task {i}", "completed": i % 3 == 0} for i in range(1, 51)}

# @app.get("/tasks", response_model=PaginatedTasks)
# async def list_tasks(page: int = 1, per_page: int = 10):
#     """
#     Lista tareas con paginación.
#     
#     - page: Número de página (default: 1)
#     - per_page: Items por página (default: 10)
#     """
#     all_tasks = list(tasks_db.values())
#     total = len(all_tasks)
#     pages = (total + per_page - 1) // per_page
#     
#     start = (page - 1) * per_page
#     end = start + per_page
#     
#     return {
#         "tasks": all_tasks[start:end],
#         "total": total,
#         "page": page,
#         "per_page": per_page,
#         "pages": pages
#     }


# ============================================
# PASO 5: Modelos con Alias
# ============================================
print("--- Paso 5: Alias en Modelos ---")

# class ProductCreate(BaseModel):
#     """Input: acepta snake_case o camelCase"""
#     product_name: str = Field(..., alias="productName")
#     unit_price: float = Field(..., alias="unitPrice")
#     
#     model_config = {"populate_by_name": True}

# class ProductResponse(BaseModel):
#     """Output: retorna en camelCase"""
#     product_id: int = Field(..., serialization_alias="productId")
#     product_name: str = Field(..., serialization_alias="productName")
#     unit_price: float = Field(..., serialization_alias="unitPrice")
#     created_at: datetime = Field(..., serialization_alias="createdAt")

# aliased_products_db: dict[int, dict] = {}
# aliased_product_counter = 0

# @app.post("/products/aliased", response_model=ProductResponse, status_code=201)
# async def create_aliased_product(product: ProductCreate):
#     """
#     Crea un producto.
#     
#     Input acepta:
#     - {"productName": "...", "unitPrice": 10.0}
#     - {"product_name": "...", "unit_price": 10.0}
#     
#     Output siempre en camelCase.
#     """
#     global aliased_product_counter
#     aliased_product_counter += 1
#     
#     new_product = {
#         "product_id": aliased_product_counter,
#         "product_name": product.product_name,
#         "unit_price": product.unit_price,
#         "created_at": datetime.now()
#     }
#     aliased_products_db[aliased_product_counter] = new_product
#     
#     return new_product

# @app.get("/products/aliased/{product_id}", response_model=ProductResponse)
# async def get_aliased_product(product_id: int):
#     """Obtiene un producto (respuesta en camelCase)."""
#     if product_id not in aliased_products_db:
#         # Retornar producto de ejemplo
#         return {
#             "product_id": product_id,
#             "product_name": "Sample Product",
#             "unit_price": 99.99,
#             "created_at": datetime.now()
#         }
#     return aliased_products_db[product_id]


# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health")
async def health_check():
    """Verificar que el servidor está funcionando."""
    return {"status": "healthy", "exercise": "01-response-models"}
