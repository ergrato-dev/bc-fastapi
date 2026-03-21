# 🚀 Pydantic con FastAPI

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Integrar modelos Pydantic en endpoints FastAPI
- ✅ Crear schemas de Request y Response separados
- ✅ Usar `response_model` para documentación automática
- ✅ Manejar errores de validación de forma elegante
- ✅ Implementar patrones CRUD con Pydantic

---

## � Diagrama de Integración

![Integración Pydantic con FastAPI](../0-assets/03-pydantic-fastapi-integration.svg)

---

## �📚 Contenido

### 1. Integración Básica

FastAPI usa Pydantic automáticamente para:

- ✅ Validar request body
- ✅ Validar query parameters
- ✅ Serializar responses
- ✅ Generar documentación OpenAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class UserCreate(BaseModel):
    """Schema para crear un usuario."""
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=0, le=150)

class UserResponse(BaseModel):
    """Schema para respuesta de usuario."""
    id: int
    name: str
    email: EmailStr

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate) -> UserResponse:
    """
    Crea un nuevo usuario.
    
    - **name**: Nombre del usuario (1-100 caracteres)
    - **email**: Email válido
    - **age**: Edad (0-150)
    """
    # FastAPI valida automáticamente el body con UserCreate
    return UserResponse(
        id=1,
        name=user.name,
        email=user.email
    )
```

---

### 2. Request Body

Pydantic valida el body JSON automáticamente:

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    price: float = Field(gt=0)
    description: str | None = None
    tags: list[str] = Field(default_factory=list, max_length=10)

@app.post("/products")
async def create_product(product: ProductCreate):
    # product ya está validado
    return {"message": f"Product {product.name} created"}
```

**Request válido:**
```json
{
    "name": "Laptop",
    "price": 999.99,
    "description": "High-performance laptop",
    "tags": ["electronics", "computers"]
}
```

**Request inválido (error automático):**
```json
{
    "name": "",
    "price": -10
}
```

**Respuesta de error (422):**
```json
{
    "detail": [
        {
            "type": "string_too_short",
            "loc": ["body", "name"],
            "msg": "String should have at least 1 character",
            "input": ""
        },
        {
            "type": "greater_than",
            "loc": ["body", "price"],
            "msg": "Input should be greater than 0",
            "input": -10
        }
    ]
}
```

---

### 3. Query Parameters con Pydantic

```python
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel, Field

app = FastAPI()

class PaginationParams(BaseModel):
    """Parámetros de paginación."""
    page: int = Field(ge=1, default=1)
    per_page: int = Field(ge=1, le=100, default=20)
    sort_by: str = "created_at"
    order: str = Field(pattern="^(asc|desc)$", default="desc")

@app.get("/users")
async def list_users(params: PaginationParams = Depends()):
    """Lista usuarios con paginación."""
    return {
        "page": params.page,
        "per_page": params.per_page,
        "sort_by": params.sort_by,
        "order": params.order
    }
```

**URL:** `/users?page=2&per_page=50&sort_by=name&order=asc`

---

### 4. Response Model

`response_model` controla qué se envía al cliente:

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

app = FastAPI()

# Schema interno (con password)
class UserInDB(BaseModel):
    id: int
    name: str
    email: EmailStr
    hashed_password: str
    created_at: datetime

# Schema de respuesta (sin password)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

# Simular base de datos
fake_db: dict[int, UserInDB] = {
    1: UserInDB(
        id=1,
        name="Alice",
        email="alice@example.com",
        hashed_password="$2b$12$...",
        created_at=datetime.now()
    )
}

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """
    Retorna un usuario SIN el password.
    
    Aunque internamente tenemos hashed_password,
    response_model=UserResponse lo excluye automáticamente.
    """
    return fake_db[user_id]  # FastAPI filtra los campos
```

**Respuesta (password excluido automáticamente):**
```json
{
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
}
```

---

### 5. Patrón de Schemas CRUD

El patrón recomendado para APIs REST:

```python
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime

# ============================================
# SCHEMAS BASE Y CRUD
# ============================================

class UserBase(BaseModel):
    """Campos comunes para usuarios."""
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr

class UserCreate(UserBase):
    """Schema para crear usuario (POST)."""
    password: str = Field(min_length=8)

class UserUpdate(BaseModel):
    """Schema para actualizar usuario (PATCH) - todos opcionales."""
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)

class UserResponse(UserBase):
    """Schema para respuesta (sin password)."""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
    updated_at: datetime | None = None

class UserList(BaseModel):
    """Schema para lista paginada."""
    items: list[UserResponse]
    total: int
    page: int
    per_page: int
```

#### Uso en Endpoints

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> UserResponse:
    """Crear un nuevo usuario."""
    # user.password disponible para hashear
    # ...crear usuario en DB...
    pass

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    """Obtener usuario por ID."""
    # ...buscar en DB...
    pass

@app.get("/users", response_model=UserList)
async def list_users(page: int = 1, per_page: int = 20) -> UserList:
    """Listar usuarios con paginación."""
    pass

@app.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate) -> UserResponse:
    """Actualizar usuario parcialmente."""
    # Solo actualizar campos que no son None
    update_data = user.model_dump(exclude_unset=True)
    pass

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int) -> None:
    """Eliminar usuario."""
    pass
```

---

### 6. Exclude Unset vs Exclude None

Diferencia importante para updates parciales:

```python
from pydantic import BaseModel

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    bio: str | None = None

# Usuario quiere actualizar solo el email
update = UserUpdate(email="new@example.com")

# exclude_unset=True: Solo campos que el usuario envió
print(update.model_dump(exclude_unset=True))
# {'email': 'new@example.com'}

# exclude_none=True: Excluye todos los None
print(update.model_dump(exclude_none=True))
# {'email': 'new@example.com'}

# Si el usuario QUIERE poner bio=None explícitamente
update2 = UserUpdate(email="new@example.com", bio=None)

print(update2.model_dump(exclude_unset=True))
# {'email': 'new@example.com', 'bio': None}  # bio incluido!

print(update2.model_dump(exclude_none=True))
# {'email': 'new@example.com'}  # bio excluido
```

**Regla:** Usa `exclude_unset=True` para updates parciales.

---

### 7. from_attributes (ORM Mode)

Para convertir modelos SQLAlchemy a Pydantic:

```python
from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Modelo SQLAlchemy (simulado)
class UserORM:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = datetime.now()

# Schema Pydantic con from_attributes
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    email: str
    created_at: datetime

# Conversión automática
user_orm = UserORM(id=1, name="Alice", email="alice@example.com")
user_response = UserResponse.model_validate(user_orm)

print(user_response)
# id=1 name='Alice' email='alice@example.com' created_at=...
```

---

### 8. Manejo de Errores de Validación

#### Error Handler Personalizado

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    """Personalizar respuesta de errores de validación."""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"][1:]),
            "message": error["msg"],
            "type": error["type"]
        })
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation Error",
            "details": errors
        }
    )
```

**Respuesta personalizada:**
```json
{
    "error": "Validation Error",
    "details": [
        {
            "field": "email",
            "message": "value is not a valid email address",
            "type": "value_error.email"
        }
    ]
}
```

---

### 9. Schemas con Ejemplos para Documentación

```python
from pydantic import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    """Schema para crear usuario."""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "secretpass123"
            }
        }
    )
    
    name: str = Field(min_length=1, max_length=100)
    email: str
    password: str = Field(min_length=8)

# O con Field() por campo
class ProductCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=200,
        examples=["Laptop Pro 15"]
    )
    price: float = Field(
        gt=0,
        examples=[999.99]
    )
    description: str | None = Field(
        default=None,
        examples=["High-performance laptop for professionals"]
    )
```

Los ejemplos aparecen en la documentación Swagger/OpenAPI.

---

### 10. Nested Models en Requests

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    country: str = "México"
    zip_code: str = Field(pattern=r"^\d{5}$")

class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)
    unit_price: float = Field(gt=0)

class OrderCreate(BaseModel):
    customer_email: str
    shipping_address: Address
    items: list[OrderItem] = Field(min_length=1)
    notes: str | None = None

@app.post("/orders")
async def create_order(order: OrderCreate):
    """Crear orden con dirección y productos anidados."""
    total = sum(item.quantity * item.unit_price for item in order.items)
    return {
        "message": "Order created",
        "total": total,
        "items_count": len(order.items),
        "ship_to": order.shipping_address.city
    }
```

**Request:**
```json
{
    "customer_email": "cliente@example.com",
    "shipping_address": {
        "street": "Av. Reforma 123",
        "city": "CDMX",
        "zip_code": "06600"
    },
    "items": [
        {"product_id": 1, "quantity": 2, "unit_price": 99.99},
        {"product_id": 2, "quantity": 1, "unit_price": 49.99}
    ],
    "notes": "Entregar por la tarde"
}
```

---

## 📝 Resumen

| Componente | Uso |
|------------|-----|
| Request Body | `async def endpoint(data: Schema)` |
| Response Model | `@app.get("/", response_model=Schema)` |
| Query Params | `Depends(SchemaParams)` |
| ORM → Pydantic | `ConfigDict(from_attributes=True)` |
| Updates Parciales | `model_dump(exclude_unset=True)` |

### Patrón CRUD de Schemas

| Schema | Uso |
|--------|-----|
| `BaseModel` | Campos comunes |
| `Create` | POST - incluye password |
| `Update` | PATCH - todos opcionales |
| `Response` | GET - sin datos sensibles |
| `List` | Colección paginada |

---

## ✅ Checklist de Verificación

Antes de continuar, asegúrate de poder:

- [ ] Crear endpoints con validación automática de body
- [ ] Usar `response_model` para filtrar respuestas
- [ ] Implementar schemas CRUD (Create, Update, Response)
- [ ] Usar `model_dump(exclude_unset=True)` para updates
- [ ] Configurar `from_attributes=True` para ORM

---

## 🔗 Recursos Adicionales

- [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Pydantic with FastAPI](https://docs.pydantic.dev/latest/integrations/fastapi/)

---

[← Anterior: Tipos de Campo](04-field-types.md) | [Siguiente: Ejercicios Prácticos →](../2-practicas/README.md)
