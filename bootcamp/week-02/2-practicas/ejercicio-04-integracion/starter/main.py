"""
Ejercicio 04: Integración con FastAPI
=====================================

Este ejercicio te enseña a integrar Pydantic con FastAPI.
Descomenta cada sección y ejecuta para ver los resultados.

Ejecutar:
    docker compose up --build
    
Luego visita: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator
from datetime import datetime

app = FastAPI(
    title="Ejercicio 04: Integración Pydantic + FastAPI",
    description="Aprende a usar Pydantic con FastAPI",
    version="1.0.0",
)

print("=" * 60)
print("EJERCICIO 04: Integración con FastAPI")
print("=" * 60)
print("\nVisita http://localhost:8000/docs para probar los endpoints\n")


# ============================================
# PASO 1: Request Body Básico
# ============================================

# FastAPI valida automáticamente el body con Pydantic.

# Descomenta las siguientes líneas:
# class ItemCreate(BaseModel):
#     """Schema para crear un item."""
#     name: str = Field(min_length=1, max_length=100)
#     price: float = Field(gt=0)
#     quantity: int = Field(ge=0, default=0)
#     description: str | None = None
#
# @app.post("/items", tags=["Paso 1"])
# async def create_item(item: ItemCreate):
#     """
#     Crear un nuevo item.
#     
#     FastAPI valida automáticamente el body usando ItemCreate.
#     Si los datos son inválidos, retorna error 422.
#     """
#     return {
#         "message": "Item created",
#         "item": item.model_dump()
#     }


# ============================================
# PASO 2: Response Model
# ============================================

# response_model controla qué se envía al cliente.

# Descomenta las siguientes líneas:
# class UserInDB(BaseModel):
#     """Modelo interno (con password)."""
#     id: int
#     name: str
#     email: str
#     hashed_password: str  # No queremos exponer esto
#     created_at: datetime
#
# class UserResponse(BaseModel):
#     """Schema de respuesta (sin password)."""
#     id: int
#     name: str
#     email: str
#
# # Simular base de datos
# fake_users_db: dict[int, UserInDB] = {
#     1: UserInDB(
#         id=1,
#         name="Alice",
#         email="alice@example.com",
#         hashed_password="$2b$12$hashedpassword",
#         created_at=datetime.now()
#     ),
#     2: UserInDB(
#         id=2,
#         name="Bob",
#         email="bob@example.com",
#         hashed_password="$2b$12$anotherhashedpassword",
#         created_at=datetime.now()
#     ),
# }
#
# @app.get("/users/{user_id}", response_model=UserResponse, tags=["Paso 2"])
# async def get_user(user_id: int):
#     """
#     Obtener usuario por ID.
#     
#     response_model=UserResponse filtra automáticamente
#     los campos sensibles como hashed_password.
#     """
#     if user_id not in fake_users_db:
#         raise HTTPException(status_code=404, detail="User not found")
#     
#     # Aunque retornamos UserInDB completo,
#     # FastAPI filtra usando response_model
#     return fake_users_db[user_id]
#
# @app.get("/users", response_model=list[UserResponse], tags=["Paso 2"])
# async def list_users():
#     """Listar todos los usuarios (sin passwords)."""
#     return list(fake_users_db.values())


# ============================================
# PASO 3: Schemas CRUD
# ============================================

# Patrón de schemas para APIs REST.

# Descomenta las siguientes líneas:
# class ProductBase(BaseModel):
#     """Campos comunes para productos."""
#     name: str = Field(min_length=1, max_length=200)
#     price: float = Field(gt=0)
#     description: str | None = None
#
# class ProductCreate(ProductBase):
#     """Schema para crear producto (POST)."""
#     sku: str = Field(pattern=r"^[A-Z]{3}-\d{3}$")
#
# class ProductUpdate(BaseModel):
#     """Schema para actualizar producto (PATCH) - todos opcionales."""
#     name: str | None = Field(default=None, min_length=1, max_length=200)
#     price: float | None = Field(default=None, gt=0)
#     description: str | None = None
#
# class ProductResponse(ProductBase):
#     """Schema de respuesta."""
#     model_config = ConfigDict(from_attributes=True)
#     
#     id: int
#     sku: str
#     created_at: datetime
#
# # Simular base de datos
# fake_products_db: dict[int, dict] = {}
# product_counter = 0
#
# @app.post(
#     "/products",
#     response_model=ProductResponse,
#     status_code=status.HTTP_201_CREATED,
#     tags=["Paso 3"]
# )
# async def create_product(product: ProductCreate):
#     """Crear un nuevo producto."""
#     global product_counter
#     product_counter += 1
#     
#     new_product = {
#         "id": product_counter,
#         **product.model_dump(),
#         "created_at": datetime.now()
#     }
#     fake_products_db[product_counter] = new_product
#     
#     return new_product
#
# @app.get("/products/{product_id}", response_model=ProductResponse, tags=["Paso 3"])
# async def get_product(product_id: int):
#     """Obtener producto por ID."""
#     if product_id not in fake_products_db:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return fake_products_db[product_id]


# ============================================
# PASO 4: Updates Parciales
# ============================================

# Usa exclude_unset=True para solo actualizar campos enviados.

# Descomenta las siguientes líneas:
# @app.patch("/products/{product_id}", response_model=ProductResponse, tags=["Paso 4"])
# async def update_product(product_id: int, product: ProductUpdate):
#     """
#     Actualizar producto parcialmente.
#     
#     Solo actualiza los campos que el cliente envía.
#     """
#     if product_id not in fake_products_db:
#         raise HTTPException(status_code=404, detail="Product not found")
#     
#     # exclude_unset=True: solo incluye campos que el cliente envió
#     update_data = product.model_dump(exclude_unset=True)
#     
#     if not update_data:
#         raise HTTPException(status_code=400, detail="No fields to update")
#     
#     # Actualizar solo los campos enviados
#     stored_product = fake_products_db[product_id]
#     for key, value in update_data.items():
#         stored_product[key] = value
#     
#     return stored_product
#
# @app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Paso 4"])
# async def delete_product(product_id: int):
#     """Eliminar producto."""
#     if product_id not in fake_products_db:
#         raise HTTPException(status_code=404, detail="Product not found")
#     
#     del fake_products_db[product_id]
#     return None


# ============================================
# PASO 5: Manejo de Errores Personalizado
# ============================================

# Personalizar respuestas de error de validación.

# Descomenta las siguientes líneas:
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     """Personalizar errores de validación."""
#     errors = []
#     for error in exc.errors():
#         field = ".".join(str(loc) for loc in error["loc"][1:])  # Saltar 'body'
#         errors.append({
#             "field": field,
#             "message": error["msg"],
#             "type": error["type"]
#         })
#     
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content={
#             "error": "Validation Error",
#             "message": "The request data is invalid",
#             "details": errors
#         }
#     )
#
# # Modelo con validaciones estrictas para probar
# class StrictUser(BaseModel):
#     """Usuario con validaciones estrictas."""
#     username: str = Field(min_length=3, max_length=20, pattern=r"^[a-z0-9_]+$")
#     email: EmailStr
#     age: int = Field(ge=18, le=120)
#     
#     @field_validator("username")
#     @classmethod
#     def validate_username(cls, v: str) -> str:
#         if v.startswith("_") or v.endswith("_"):
#             raise ValueError("Username cannot start or end with underscore")
#         return v
#
# @app.post("/strict-users", tags=["Paso 5"])
# async def create_strict_user(user: StrictUser):
#     """
#     Crear usuario con validaciones estrictas.
#     
#     Prueba con datos inválidos para ver el error personalizado.
#     """
#     return {"message": "User created", "username": user.username}


# ============================================
# ENDPOINT DE SALUD
# ============================================

@app.get("/", tags=["Health"])
async def root():
    """Endpoint de salud."""
    return {
        "status": "ok",
        "message": "API running",
        "docs": "Visit /docs for Swagger UI"
    }


# ============================================
# RESUMEN
# ============================================

@app.get("/resumen", tags=["Info"])
async def resumen():
    """Resumen del ejercicio."""
    return {
        "paso_1": "Request body con Pydantic (POST /items)",
        "paso_2": "Response model para filtrar (GET /users/{id})",
        "paso_3": "Schemas CRUD (POST/GET /products)",
        "paso_4": "Updates parciales con exclude_unset (PATCH /products/{id})",
        "paso_5": "Manejo de errores personalizado (POST /strict-users)",
    }
