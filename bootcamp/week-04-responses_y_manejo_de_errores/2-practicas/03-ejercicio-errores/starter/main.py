"""
Ejercicio 03: Manejo de Errores
Semana 04 - Responses y Manejo de Errores

Instrucciones:
1. Lee el README.md para entender cada paso
2. Descomenta el código de cada sección
3. Ejecuta: docker compose up --build
4. Prueba en: http://localhost:8000/docs
"""

from datetime import datetime
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="Error Handling Practice",
    description="Ejercicio para practicar manejo de errores",
    version="1.0.0"
)

# ============================================
# PASO 1: HTTPException Básico
# ============================================
print("--- Paso 1: HTTPException Básico ---")

# class Item(BaseModel):
#     id: int
#     name: str
#     price: float

# items_db: dict[int, dict] = {
#     1: {"id": 1, "name": "Laptop", "price": 999.99},
#     2: {"id": 2, "name": "Mouse", "price": 29.99}
# }

# @app.get("/items/{item_id}", response_model=Item)
# async def get_item(item_id: int):
#     """
#     Obtiene un item por ID.
#     
#     Usa HTTPException para errores controlados.
#     """
#     if item_id not in items_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Item with id {item_id} not found"
#         )
#     return items_db[item_id]

# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     """Elimina un item."""
#     if item_id not in items_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Item {item_id} not found"
#         )
#     
#     # Simular que algunos items no se pueden eliminar
#     if items_db[item_id]["price"] > 500:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Cannot delete items with price > $500"
#         )
#     
#     del items_db[item_id]
#     return {"message": f"Item {item_id} deleted"}


# ============================================
# PASO 2: Excepciones Personalizadas
# ============================================
print("--- Paso 2: Excepciones Personalizadas ---")

# # Definir excepciones personalizadas
# class AppError(Exception):
#     """Base exception for application errors"""
#     def __init__(self, message: str, error_code: str):
#         self.message = message
#         self.error_code = error_code
#         super().__init__(message)

# class NotFoundError(AppError):
#     """Resource not found"""
#     def __init__(self, resource: str, resource_id: int | str):
#         super().__init__(
#             message=f"{resource} with id '{resource_id}' not found",
#             error_code="RESOURCE_NOT_FOUND"
#         )
#         self.resource = resource
#         self.resource_id = resource_id

# class DuplicateError(AppError):
#     """Resource already exists"""
#     def __init__(self, resource: str, field: str, value: str):
#         super().__init__(
#             message=f"{resource} with {field}='{value}' already exists",
#             error_code="DUPLICATE_RESOURCE"
#         )

# class BusinessRuleError(AppError):
#     """Business rule violation"""
#     def __init__(self, message: str):
#         super().__init__(
#             message=message,
#             error_code="BUSINESS_RULE_VIOLATION"
#         )

# # Exception handlers
# @app.exception_handler(NotFoundError)
# async def not_found_handler(request: Request, exc: NotFoundError):
#     return JSONResponse(
#         status_code=status.HTTP_404_NOT_FOUND,
#         content={
#             "error": exc.error_code,
#             "message": exc.message,
#             "resource": exc.resource,
#             "resource_id": exc.resource_id
#         }
#     )

# @app.exception_handler(DuplicateError)
# async def duplicate_handler(request: Request, exc: DuplicateError):
#     return JSONResponse(
#         status_code=status.HTTP_409_CONFLICT,
#         content={
#             "error": exc.error_code,
#             "message": exc.message
#         }
#     )

# @app.exception_handler(BusinessRuleError)
# async def business_rule_handler(request: Request, exc: BusinessRuleError):
#     return JSONResponse(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         content={
#             "error": exc.error_code,
#             "message": exc.message
#         }
#     )

# # Uso de excepciones personalizadas
# class UserCreate(BaseModel):
#     email: EmailStr
#     name: str

# class UserResponse(BaseModel):
#     id: int
#     email: str
#     name: str

# users_db: dict[int, dict] = {
#     1: {"id": 1, "email": "alice@example.com", "name": "Alice"}
# }
# user_counter = 1

# @app.get("/users/{user_id}", response_model=UserResponse)
# async def get_user(user_id: int):
#     """Obtiene un usuario usando excepción personalizada."""
#     if user_id not in users_db:
#         raise NotFoundError("User", user_id)
#     return users_db[user_id]

# @app.post("/users", response_model=UserResponse, status_code=201)
# async def create_user(user: UserCreate):
#     """Crea un usuario verificando duplicados."""
#     global user_counter
#     
#     # Verificar email duplicado
#     for existing in users_db.values():
#         if existing["email"] == user.email:
#             raise DuplicateError("User", "email", user.email)
#     
#     user_counter += 1
#     new_user = {"id": user_counter, "email": user.email, "name": user.name}
#     users_db[user_counter] = new_user
#     return new_user


# ============================================
# PASO 3: Formato de Error Consistente
# ============================================
print("--- Paso 3: Formato Consistente ---")

# class StandardErrorResponse(BaseModel):
#     """Modelo estándar para todas las respuestas de error"""
#     success: bool = False
#     error_code: str
#     message: str
#     details: list[dict] | None = None
#     timestamp: datetime
#     path: str

# def create_error_response(
#     request: Request,
#     status_code: int,
#     error_code: str,
#     message: str,
#     details: list[dict] | None = None
# ) -> JSONResponse:
#     """Helper para crear respuestas de error consistentes."""
#     return JSONResponse(
#         status_code=status_code,
#         content={
#             "success": False,
#             "error_code": error_code,
#             "message": message,
#             "details": details,
#             "timestamp": datetime.now().isoformat(),
#             "path": str(request.url.path)
#         }
#     )

# # Override del handler de HTTPException para formato consistente
# @app.exception_handler(HTTPException)
# async def http_exception_handler(request: Request, exc: HTTPException):
#     return create_error_response(
#         request=request,
#         status_code=exc.status_code,
#         error_code=f"HTTP_{exc.status_code}",
#         message=str(exc.detail)
#     )

# # Handler para errores no capturados (500)
# @app.exception_handler(Exception)
# async def unhandled_exception_handler(request: Request, exc: Exception):
#     # En producción: loggear el error real pero no exponerlo
#     # logger.error(f"Unhandled error: {exc}", exc_info=True)
#     return create_error_response(
#         request=request,
#         status_code=500,
#         error_code="INTERNAL_ERROR",
#         message="An unexpected error occurred. Please try again later."
#     )

# @app.get("/crash")
# async def crash_endpoint():
#     """Endpoint que causa un error 500 para probar el handler."""
#     raise ValueError("This is a test error")


# ============================================
# PASO 4: Errores de Validación Personalizados
# ============================================
print("--- Paso 4: Errores de Validación ---")

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(
#     request: Request, 
#     exc: RequestValidationError
# ):
#     """
#     Personaliza el formato de errores de validación.
#     
#     Pydantic genera errores con mucha información.
#     Este handler los formatea de forma más amigable.
#     """
#     errors = []
#     for error in exc.errors():
#         field_path = " -> ".join(str(loc) for loc in error["loc"])
#         errors.append({
#             "field": field_path,
#             "message": error["msg"],
#             "type": error["type"]
#         })
#     
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content={
#             "success": False,
#             "error_code": "VALIDATION_ERROR",
#             "message": "Request validation failed",
#             "details": errors,
#             "timestamp": datetime.now().isoformat(),
#             "path": str(request.url.path)
#         }
#     )

# # Modelo con muchas validaciones para probar
# class ProductCreate(BaseModel):
#     name: str = Field(..., min_length=2, max_length=100)
#     description: str | None = Field(None, max_length=500)
#     price: float = Field(..., gt=0, description="Price must be positive")
#     quantity: int = Field(..., ge=0, le=10000)
#     category: str = Field(..., pattern="^[a-z]+$")

# @app.post("/products")
# async def create_product(product: ProductCreate):
#     """
#     Crea un producto.
#     
#     Prueba enviando datos inválidos para ver
#     el formato personalizado de errores.
#     """
#     return {"message": "Product created", "product": product.model_dump()}


# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health")
async def health_check():
    """Verificar que el servidor está funcionando."""
    return {"status": "healthy", "exercise": "03-errores"}
