# ⚠️ Manejo de Errores

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Usar HTTPException para errores controlados
- ✅ Crear exception handlers personalizados
- ✅ Definir formatos de error consistentes
- ✅ Manejar errores de validación de Pydantic

---

## 📚 Contenido

![Flujo de Manejo de Errores](../0-assets/03-error-handling.svg)

### 1. HTTPException Básico

La forma más común de manejar errores en FastAPI:

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items_db = {
    1: {"name": "Item 1", "price": 10.0},
    2: {"name": "Item 2", "price": 20.0}
}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in items_db:
        # Lanza excepción HTTP con código y mensaje
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return items_db[item_id]

# Respuesta de error:
# {
#     "detail": "Item with id 99 not found"
# }
```

#### Con Headers Adicionales

```python
@app.get("/protected")
async def protected_resource(api_key: str | None = None):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key required",
            headers={
                "WWW-Authenticate": "Bearer",
                "X-Error-Code": "AUTH_REQUIRED"
            }
        )
    return {"data": "secret"}
```

---

### 2. Excepciones Personalizadas

Crea tus propias excepciones para mejor organización:

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

# ============================================
# EXCEPCIONES PERSONALIZADAS
# ============================================

class AppException(Exception):
    """Excepción base de la aplicación"""
    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int = status.HTTP_400_BAD_REQUEST
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        super().__init__(message)

class NotFoundError(AppException):
    """Recurso no encontrado"""
    def __init__(self, resource: str, resource_id: int | str):
        super().__init__(
            message=f"{resource} with id {resource_id} not found",
            error_code="RESOURCE_NOT_FOUND",
            status_code=status.HTTP_404_NOT_FOUND
        )

class DuplicateError(AppException):
    """Recurso duplicado"""
    def __init__(self, resource: str, field: str, value: str):
        super().__init__(
            message=f"{resource} with {field}='{value}' already exists",
            error_code="DUPLICATE_RESOURCE",
            status_code=status.HTTP_409_CONFLICT
        )

class ValidationError(AppException):
    """Error de validación personalizada"""
    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="VALIDATION_ERROR",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

class UnauthorizedError(AppException):
    """No autenticado"""
    def __init__(self, message: str = "Authentication required"):
        super().__init__(
            message=message,
            error_code="UNAUTHORIZED",
            status_code=status.HTTP_401_UNAUTHORIZED
        )

class ForbiddenError(AppException):
    """Sin permisos"""
    def __init__(self, message: str = "Permission denied"):
        super().__init__(
            message=message,
            error_code="FORBIDDEN",
            status_code=status.HTTP_403_FORBIDDEN
        )

# ============================================
# EXCEPTION HANDLER
# ============================================

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    """Manejador global para excepciones de la aplicación"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.error_code,
                "message": exc.message,
                "path": str(request.url.path)
            }
        }
    )

# ============================================
# USO EN ENDPOINTS
# ============================================

users_db = {
    1: {"id": 1, "email": "user@example.com", "name": "John"}
}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise NotFoundError("User", user_id)
    return users_db[user_id]

@app.post("/users")
async def create_user(email: str, name: str):
    # Verificar duplicado
    for user in users_db.values():
        if user["email"] == email:
            raise DuplicateError("User", "email", email)
    
    new_id = max(users_db.keys()) + 1
    users_db[new_id] = {"id": new_id, "email": email, "name": name}
    return users_db[new_id]

# Respuesta de error personalizada:
# {
#     "error": {
#         "code": "RESOURCE_NOT_FOUND",
#         "message": "User with id 99 not found",
#         "path": "/users/99"
#     }
# }
```

---

### 3. Exception Handlers Globales

#### Manejador de Errores de Validación

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, 
    exc: RequestValidationError
):
    """
    Personaliza el formato de errores de validación de Pydantic.
    Por defecto FastAPI retorna 422 con lista de errores.
    """
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed",
                "details": errors
            }
        }
    )

class UserCreate(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=0, le=150)

@app.post("/users")
async def create_user(user: UserCreate):
    return user

# POST /users con body inválido:
# {"email": "invalid", "name": "a", "age": -5}
#
# Respuesta:
# {
#     "error": {
#         "code": "VALIDATION_ERROR",
#         "message": "Request validation failed",
#         "details": [
#             {"field": "body.email", "message": "value is not a valid email", "type": "value_error.email"},
#             {"field": "body.name", "message": "String should have at least 2 characters", "type": "string_too_short"},
#             {"field": "body.age", "message": "Input should be greater than or equal to 0", "type": "greater_than_equal"}
#         ]
#     }
# }
```

#### Manejador de Errores 500

```python
import logging
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
logger = logging.getLogger(__name__)

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """
    Captura cualquier excepción no manejada.
    Importante: Logear el error pero NO exponer detalles al cliente.
    """
    # Logear con traceback completo
    logger.error(
        f"Unhandled exception on {request.method} {request.url.path}: {exc}",
        exc_info=True
    )
    
    # Retornar error genérico al cliente
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "An unexpected error occurred. Please try again later."
            }
        }
    )

@app.get("/crash")
async def crash_endpoint():
    # Esto lanzará una excepción no manejada
    result = 1 / 0
    return result
```

---

### 4. Modelo de Error Consistente

Define un formato estándar para todos los errores:

```python
from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

# ============================================
# MODELO DE ERROR ESTÁNDAR
# ============================================

class ErrorDetail(BaseModel):
    """Detalle de un error individual"""
    field: str | None = None
    message: str
    code: str | None = None

class ErrorResponse(BaseModel):
    """Respuesta de error estándar"""
    success: bool = False
    error: str
    error_code: str
    message: str
    details: list[ErrorDetail] = []
    timestamp: datetime = Field(default_factory=datetime.now)
    path: str | None = None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "success": False,
                "error": "Not Found",
                "error_code": "RESOURCE_NOT_FOUND",
                "message": "User with id 99 not found",
                "details": [],
                "timestamp": "2024-01-01T12:00:00",
                "path": "/users/99"
            }
        }
    }

# ============================================
# FUNCIÓN HELPER PARA CREAR ERRORES
# ============================================

def create_error_response(
    request: Request,
    status_code: int,
    error_code: str,
    message: str,
    details: list[dict] | None = None
) -> JSONResponse:
    """Crea una respuesta de error consistente"""
    
    # Mapear status code a nombre de error
    error_names = {
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        409: "Conflict",
        422: "Unprocessable Entity",
        429: "Too Many Requests",
        500: "Internal Server Error",
        503: "Service Unavailable"
    }
    
    error_details = []
    if details:
        for d in details:
            error_details.append(ErrorDetail(**d))
    
    response = ErrorResponse(
        error=error_names.get(status_code, "Error"),
        error_code=error_code,
        message=message,
        details=error_details,
        path=str(request.url.path)
    )
    
    return JSONResponse(
        status_code=status_code,
        content=response.model_dump(mode="json")
    )

# ============================================
# EXCEPTION HANDLERS
# ============================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return create_error_response(
        request=request,
        status_code=exc.status_code,
        error_code="HTTP_ERROR",
        message=str(exc.detail)
    )

@app.exception_handler(RequestValidationError)
async def validation_handler(request: Request, exc: RequestValidationError):
    details = [
        {
            "field": ".".join(str(loc) for loc in err["loc"]),
            "message": err["msg"],
            "code": err["type"]
        }
        for err in exc.errors()
    ]
    
    return create_error_response(
        request=request,
        status_code=422,
        error_code="VALIDATION_ERROR",
        message="Request validation failed",
        details=details
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return create_error_response(
        request=request,
        status_code=500,
        error_code="INTERNAL_ERROR",
        message="An unexpected error occurred"
    )
```

---

### 5. Errores en Dependencias

```python
from fastapi import FastAPI, Depends, HTTPException, status, Header

app = FastAPI()

# ============================================
# DEPENDENCIA QUE PUEDE FALLAR
# ============================================

async def verify_api_key(x_api_key: str = Header(...)):
    """Verifica que se proporcione una API key válida"""
    valid_keys = ["key123", "key456"]
    
    if x_api_key not in valid_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "ApiKey"}
        )
    
    return x_api_key

async def get_current_user(api_key: str = Depends(verify_api_key)):
    """Obtiene el usuario basado en la API key"""
    users = {
        "key123": {"id": 1, "name": "Alice", "role": "admin"},
        "key456": {"id": 2, "name": "Bob", "role": "user"}
    }
    return users.get(api_key)

async def require_admin(user: dict = Depends(get_current_user)):
    """Verifica que el usuario sea admin"""
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return user

# ============================================
# ENDPOINTS
# ============================================

@app.get("/profile")
async def get_profile(user: dict = Depends(get_current_user)):
    """Cualquier usuario autenticado puede acceder"""
    return user

@app.delete("/admin/users/{user_id}")
async def delete_user(user_id: int, admin: dict = Depends(require_admin)):
    """Solo admins pueden eliminar usuarios"""
    return {"message": f"User {user_id} deleted by {admin['name']}"}
```

---

### 6. Try/Except con Errores Específicos

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import httpx

app = FastAPI()

class ExternalData(BaseModel):
    id: int
    data: dict

@app.get("/external/{resource_id}")
async def get_external_resource(resource_id: int):
    """
    Obtiene datos de un servicio externo.
    Maneja diferentes tipos de errores.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.external.com/resources/{resource_id}",
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
            
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="External service timeout"
        )
    
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Resource {resource_id} not found in external service"
            )
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"External service error: {e.response.status_code}"
        )
    
    except httpx.RequestError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="External service unavailable"
        )
```

---

### 7. Logging de Errores

```python
import logging
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Middleware para loggear requests"""
    logger.info(f"Request: {request.method} {request.url.path}")
    
    try:
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response
    except Exception as e:
        logger.exception(f"Unhandled error: {e}")
        raise

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Log de errores HTTP"""
    logger.warning(
        f"HTTP {exc.status_code} on {request.method} {request.url.path}: {exc.detail}"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """Log de errores no manejados"""
    logger.error(
        f"Unhandled error on {request.method} {request.url.path}",
        exc_info=True  # Incluye traceback
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
```

---

## 🎯 Resumen

| Tipo de Error | Herramienta | Uso |
|---------------|-------------|-----|
| Error simple | `HTTPException` | Errores controlados en endpoints |
| Formato personalizado | Exception Handler | Consistencia en respuestas |
| Validación Pydantic | `RequestValidationError` | Personalizar errores 422 |
| Errores generales | `Exception` handler | Capturar errores no manejados |
| En dependencias | `HTTPException` en `Depends` | Auth, permisos, validación |

### Mejores Prácticas

1. ✅ Nunca exponer detalles técnicos en producción
2. ✅ Siempre loggear errores con contexto
3. ✅ Usar formato de error consistente
4. ✅ Mensajes de error útiles para el cliente
5. ✅ Códigos de error únicos para debugging
6. ✅ Documentar todos los errores posibles

---

## 📚 Recursos Adicionales

- [FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [Python Logging](https://docs.python.org/3/library/logging.html)

---

[← Anterior: Status Codes](02-status-codes.md) | [Siguiente: Responses Avanzadas →](04-responses-avanzadas.md)
