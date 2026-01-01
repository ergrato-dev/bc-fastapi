# 📤 Response Models (Modelos de Respuesta)

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Definir modelos de respuesta tipados
- ✅ Usar `response_model` para validar salidas
- ✅ Excluir campos sensibles de respuestas
- ✅ Crear modelos diferentes para entrada y salida

---

## 📚 Contenido

![Flujo de Response Models](../0-assets/01-response-flow.svg)

### 1. ¿Por Qué Response Models?

Los response models garantizan que tus respuestas:

1. **Sean consistentes**: Siempre el mismo formato
2. **Sean seguras**: No exponen datos sensibles
3. **Estén documentadas**: OpenAPI genera automáticamente
4. **Sean validadas**: FastAPI verifica la estructura

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# ❌ SIN response_model - puede exponer datos sensibles
class User(BaseModel):
    id: int
    email: EmailStr
    password: str  # ¡Peligro! Esto NO debe salir en la respuesta
    
@app.get("/users/{user_id}")
async def get_user_bad(user_id: int):
    return {
        "id": user_id,
        "email": "user@example.com",
        "password": "secret123"  # ¡Se envía al cliente!
    }

# ✅ CON response_model - filtra automáticamente
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    # password NO está aquí - no se enviará

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user_good(user_id: int):
    # Aunque retornemos password, NO se enviará
    return {
        "id": user_id,
        "email": "user@example.com",
        "password": "secret123"  # Será filtrado
    }
```

---

### 2. Patrones de Modelos

#### Modelos Separados para Input/Output

```python
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

# Base con campos comunes
class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=100)

# Para crear usuario (input)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

# Para actualizar usuario (input)
class UserUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: str | None = Field(None, min_length=2, max_length=100)
    password: str | None = Field(None, min_length=8)

# Para respuestas (output)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_active: bool = True
    
    model_config = {"from_attributes": True}
```

#### Uso en Endpoints

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simulación de base de datos
fake_users_db: dict[int, dict] = {}
user_id_counter = 0

@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    global user_id_counter
    user_id_counter += 1
    
    # Simular guardado en DB
    db_user = {
        "id": user_id_counter,
        "email": user.email,
        "full_name": user.full_name,
        "password": user.password,  # En realidad hashear
        "created_at": datetime.now(),
        "is_active": True
    }
    fake_users_db[user_id_counter] = db_user
    
    return db_user  # password será filtrado por response_model

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users_db[user_id]

@app.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    stored = fake_users_db[user_id]
    update_data = user.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        stored[field] = value
    
    return stored
```

---

### 3. Opciones de Response Model

#### `response_model_exclude_unset`

No incluye campos que no fueron establecidos explícitamente:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items_db = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "Bar item", "price": 35.0, "tax": 15.0}
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def get_item(item_id: str):
    return items_db[item_id]

# GET /items/foo retorna:
# {"name": "Foo", "price": 50.2}
# (sin description, tax, tags porque no fueron establecidos)

# GET /items/bar retorna:
# {"name": "Bar", "description": "Bar item", "price": 35.0, "tax": 15.0}
```

#### `response_model_exclude` y `response_model_include`

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    internal_code: str

# Excluir campos específicos
@app.get(
    "/users/{user_id}",
    response_model=User,
    response_model_exclude={"password", "internal_code"}
)
async def get_user_excluded(user_id: int):
    return {
        "id": user_id,
        "username": "john",
        "email": "john@example.com",
        "password": "secret",
        "internal_code": "ABC123"
    }
# Retorna: {"id": 1, "username": "john", "email": "john@example.com"}

# Incluir solo campos específicos
@app.get(
    "/users/{user_id}/public",
    response_model=User,
    response_model_include={"id", "username"}
)
async def get_user_public(user_id: int):
    return {
        "id": user_id,
        "username": "john",
        "email": "john@example.com",
        "password": "secret",
        "internal_code": "ABC123"
    }
# Retorna: {"id": 1, "username": "john"}
```

> ⚠️ **Nota**: Es mejor crear modelos separados en lugar de usar `exclude`/`include`. Son más claros y más fáciles de mantener.

---

### 4. Listas y Respuestas Múltiples

```python
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float

# Lista de items
@app.get("/items", response_model=list[Item])
async def list_items():
    return [
        {"id": 1, "name": "Item 1", "price": 10.0},
        {"id": 2, "name": "Item 2", "price": 20.0}
    ]

# Respuesta con metadata (paginación)
class PaginatedResponse(BaseModel):
    items: list[Item]
    total: int
    page: int
    per_page: int
    pages: int

@app.get("/items/paginated", response_model=PaginatedResponse)
async def list_items_paginated(page: int = 1, per_page: int = 10):
    all_items = [...]  # Todos los items
    total = len(all_items)
    
    start = (page - 1) * per_page
    end = start + per_page
    
    return {
        "items": all_items[start:end],
        "total": total,
        "page": page,
        "per_page": per_page,
        "pages": (total + per_page - 1) // per_page
    }
```

---

### 5. Modelos con Alias

Para nombres de campo diferentes en JSON:

```python
from pydantic import BaseModel, Field

class UserResponse(BaseModel):
    id: int
    full_name: str = Field(..., alias="fullName")
    email_address: str = Field(..., alias="emailAddress")
    created_at: datetime = Field(..., alias="createdAt")
    
    model_config = {
        "populate_by_name": True,  # Permite usar nombre o alias
        "json_schema_extra": {
            "example": {
                "id": 1,
                "fullName": "John Doe",
                "emailAddress": "john@example.com",
                "createdAt": "2024-01-01T00:00:00"
            }
        }
    }

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    return {
        "id": user_id,
        "full_name": "John Doe",  # Puedes usar el nombre interno
        "email_address": "john@example.com",
        "created_at": datetime.now()
    }
# JSON de respuesta usa los alias:
# {"id": 1, "fullName": "John Doe", "emailAddress": "john@example.com", ...}
```

---

### 6. Union Types en Responses

```python
from pydantic import BaseModel
from typing import Union

class Dog(BaseModel):
    type: str = "dog"
    name: str
    breed: str

class Cat(BaseModel):
    type: str = "cat"
    name: str
    indoor: bool

# Puede retornar Dog o Cat
@app.get("/pets/{pet_id}", response_model=Dog | Cat)
async def get_pet(pet_id: int):
    pets = {
        1: {"type": "dog", "name": "Buddy", "breed": "Golden"},
        2: {"type": "cat", "name": "Whiskers", "indoor": True}
    }
    return pets.get(pet_id, pets[1])
```

---

### 7. Modelo de Ejemplo Completo

```python
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, EmailStr

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# ============================================
# MODELOS DE ENTRADA
# ============================================

class TaskCreate(BaseModel):
    """Datos para crear una tarea"""
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(None, max_length=1000)
    priority: TaskPriority = TaskPriority.medium
    due_date: datetime | None = None

class TaskUpdate(BaseModel):
    """Datos para actualizar una tarea (todos opcionales)"""
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=1000)
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    due_date: datetime | None = None

# ============================================
# MODELOS DE SALIDA
# ============================================

class TaskResponse(BaseModel):
    """Respuesta de una tarea individual"""
    id: int
    title: str
    description: str | None
    status: TaskStatus
    priority: TaskPriority
    due_date: datetime | None
    created_at: datetime
    updated_at: datetime | None
    
    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Complete project",
                "description": "Finish the FastAPI bootcamp project",
                "status": "pending",
                "priority": "high",
                "due_date": "2024-12-31T23:59:59",
                "created_at": "2024-01-01T10:00:00",
                "updated_at": None
            }
        }
    }

class TaskListResponse(BaseModel):
    """Respuesta paginada de lista de tareas"""
    tasks: list[TaskResponse]
    total: int
    page: int
    per_page: int
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "tasks": [
                    {
                        "id": 1,
                        "title": "Task 1",
                        "description": None,
                        "status": "pending",
                        "priority": "medium",
                        "due_date": None,
                        "created_at": "2024-01-01T10:00:00",
                        "updated_at": None
                    }
                ],
                "total": 1,
                "page": 1,
                "per_page": 10
            }
        }
    }
```

---

## 🎯 Resumen

| Concepto | Uso |
|----------|-----|
| `response_model` | Define estructura de respuesta |
| `response_model_exclude_unset` | Omite campos no establecidos |
| `response_model_exclude` | Excluye campos específicos |
| `response_model_include` | Incluye solo campos específicos |
| `from_attributes` | Permite crear desde objetos ORM |
| `alias` | Nombre diferente en JSON |

### Mejores Prácticas

1. ✅ **Siempre** usa `response_model` en endpoints
2. ✅ Crea modelos separados para entrada y salida
3. ✅ Nunca expongas campos sensibles (passwords, tokens)
4. ✅ Usa herencia para reducir duplicación
5. ✅ Incluye ejemplos en `json_schema_extra`

---

## 📚 Recursos Adicionales

- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)

---

[← Volver a Teoría](../README.md) | [Siguiente: Status Codes →](02-status-codes.md)
