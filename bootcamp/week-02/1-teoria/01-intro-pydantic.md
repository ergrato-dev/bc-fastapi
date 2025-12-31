# 🎯 Introducción a Pydantic v2

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Entender qué es Pydantic y por qué es esencial en FastAPI
- ✅ Conocer las diferencias entre Pydantic v1 y v2
- ✅ Crear tu primer modelo de datos
- ✅ Entender el flujo de validación automática

---

## 📚 Contenido

### 1. ¿Qué es Pydantic?

**Pydantic** es una librería de Python para **validación de datos** usando type hints. Convierte y valida datos automáticamente basándose en los tipos que defines.

![Flujo de validación Pydantic](../0-assets/01-pydantic-validation-flow.svg)

#### ¿Por qué es importante?

| Sin Pydantic | Con Pydantic |
|--------------|--------------|
| Validación manual | Validación automática |
| Código repetitivo | Modelos declarativos |
| Errores difíciles de rastrear | Mensajes de error claros |
| Sin documentación | OpenAPI automático |

#### Ejemplo: El Problema sin Pydantic

```python
# ❌ SIN PYDANTIC - Validación manual, tedioso y propenso a errores
def create_user(data: dict) -> dict:
    # Validar que existan los campos
    if "name" not in data:
        raise ValueError("name is required")
    if "email" not in data:
        raise ValueError("email is required")
    if "age" not in data:
        raise ValueError("age is required")
    
    # Validar tipos
    if not isinstance(data["name"], str):
        raise TypeError("name must be a string")
    if not isinstance(data["email"], str):
        raise TypeError("email must be a string")
    if not isinstance(data["age"], int):
        raise TypeError("age must be an integer")
    
    # Validar formato de email
    if "@" not in data["email"]:
        raise ValueError("invalid email format")
    
    # Validar rango de edad
    if data["age"] < 0 or data["age"] > 150:
        raise ValueError("age must be between 0 and 150")
    
    return data

# Llamar la función
try:
    user = create_user({"name": "Alice", "email": "alice@example.com", "age": 30})
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```

#### Ejemplo: La Solución con Pydantic

```python
# ✅ CON PYDANTIC - Declarativo, limpio y automático
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(ge=0, le=150)

# Pydantic valida automáticamente
user = User(name="Alice", email="alice@example.com", age=30)
print(user)  # name='Alice' email='alice@example.com' age=30

# Si los datos son inválidos, lanza ValidationError con detalles
try:
    invalid_user = User(name="Bob", email="not-an-email", age=200)
except Exception as e:
    print(e)
    # 2 validation errors for User
    # email: value is not a valid email address
    # age: Input should be less than or equal to 150
```

---

### 2. Pydantic v2 vs v1

Pydantic v2 (lanzado en 2023) es una **reescritura completa** con mejoras significativas:

| Característica | v1 | v2 |
|----------------|----|----|
| **Rendimiento** | Base | 5-50x más rápido |
| **Core** | Python puro | Rust (pydantic-core) |
| **Configuración** | `class Config` | `model_config = ConfigDict(...)` |
| **Validadores** | `@validator` | `@field_validator` |
| **Serialización** | `.dict()`, `.json()` | `.model_dump()`, `.model_dump_json()` |

#### Sintaxis v1 vs v2

```python
# ❌ PYDANTIC V1 (obsoleto)
from pydantic import BaseModel, validator

class UserV1(BaseModel):
    name: str
    
    class Config:
        str_strip_whitespace = True
    
    @validator("name")
    def validate_name(cls, v):
        return v.title()
    
    def to_dict(self):
        return self.dict()


# ✅ PYDANTIC V2 (actual)
from pydantic import BaseModel, ConfigDict, field_validator

class UserV2(BaseModel):
    name: str
    
    model_config = ConfigDict(str_strip_whitespace=True)
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        return v.title()
    
    def to_dict(self):
        return self.model_dump()
```

> ⚠️ **Importante**: En este bootcamp usamos **Pydantic v2.10+**. Si encuentras tutoriales con sintaxis v1, adáptalos.

---

### 3. Tu Primer Modelo Pydantic

Un modelo Pydantic es una clase que hereda de `BaseModel`:

```python
from pydantic import BaseModel

class Product(BaseModel):
    """Modelo para representar un producto."""
    name: str
    price: float
    quantity: int = 0  # Valor por defecto
    description: str | None = None  # Campo opcional
```

#### Crear Instancias

```python
# Desde argumentos
product1 = Product(name="Laptop", price=999.99, quantity=10)

# Desde diccionario
data = {"name": "Mouse", "price": 29.99}
product2 = Product(**data)

# Desde JSON string
import json
json_data = '{"name": "Keyboard", "price": 79.99, "quantity": 5}'
product3 = Product.model_validate_json(json_data)

print(product1)
# name='Laptop' price=999.99 quantity=10 description=None

print(product2.model_dump())
# {'name': 'Mouse', 'price': 29.99, 'quantity': 0, 'description': None}
```

#### Conversión Automática de Tipos

Pydantic intenta convertir los tipos automáticamente (coerción):

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    active: bool

# Pydantic convierte los tipos automáticamente
item = Item(name=123, price="49.99", active="yes")
print(item)
# name='123' price=49.99 active=True

print(type(item.name))   # <class 'str'>
print(type(item.price))  # <class 'float'>
print(type(item.active)) # <class 'bool'>
```

> 💡 **Nota**: El nombre `123` se convierte a `"123"`, el precio `"49.99"` a `49.99`, y `"yes"` a `True`.

---

### 4. Validación Automática

Cuando los datos no son válidos, Pydantic lanza `ValidationError`:

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int
    email: str

# Datos inválidos
try:
    user = User(name="Alice", age="not a number", email=12345)
except ValidationError as e:
    print(e)
```

**Salida:**
```
2 validation errors for User
age
  Input should be a valid integer, unable to parse string as an integer
  [type=int_parsing, input_value='not a number', input_type=str]
email
  Input should be a valid string
  [type=string_type, input_value=12345, input_type=int]
```

#### Acceder a los Errores Programáticamente

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    user = User(name="Alice", age="invalid")
except ValidationError as e:
    # Lista de errores
    print(e.errors())
    # [{'type': 'int_parsing', 'loc': ('age',), 'msg': '...', 'input': 'invalid'}]
    
    # JSON de errores
    print(e.json())
    
    # Número de errores
    print(e.error_count())  # 1
```

---

### 5. Métodos Principales de BaseModel

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `model_dump()` | Convierte a diccionario | `user.model_dump()` |
| `model_dump_json()` | Convierte a JSON string | `user.model_dump_json()` |
| `model_validate()` | Crea desde dict con validación | `User.model_validate(data)` |
| `model_validate_json()` | Crea desde JSON string | `User.model_validate_json(json_str)` |
| `model_copy()` | Crea una copia | `user.model_copy(update={"name": "Bob"})` |
| `model_json_schema()` | Genera JSON Schema | `User.model_json_schema()` |

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=30)

# Convertir a dict
print(user.model_dump())
# {'name': 'Alice', 'age': 30}

# Convertir a JSON
print(user.model_dump_json())
# '{"name":"Alice","age":30}'

# Crear copia con cambios
user2 = user.model_copy(update={"name": "Bob"})
print(user2)
# name='Bob' age=30

# Generar JSON Schema
print(User.model_json_schema())
# {'properties': {'name': {'type': 'string'}, 'age': {'type': 'integer'}}, ...}
```

---

### 6. Pydantic en FastAPI

FastAPI usa Pydantic **automáticamente** para:

1. **Validar request bodies**
2. **Serializar responses**
3. **Generar documentación OpenAPI**

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Modelo para request
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

# Modelo para response
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate) -> UserResponse:
    """
    FastAPI automáticamente:
    1. Valida el body con UserCreate
    2. Retorna error 422 si es inválido
    3. Serializa la respuesta con UserResponse
    4. Documenta en /docs
    """
    # user ya está validado aquí
    return UserResponse(id=1, name=user.name, email=user.email)
```

**Request inválido → Respuesta 422:**
```json
{
    "detail": [
        {
            "type": "value_error",
            "loc": ["body", "email"],
            "msg": "value is not a valid email address",
            "input": "not-an-email"
        }
    ]
}
```

---

## 📝 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Pydantic** | Librería de validación basada en type hints |
| **BaseModel** | Clase base para crear modelos |
| **ValidationError** | Excepción cuando la validación falla |
| **Coerción** | Conversión automática de tipos |
| **model_dump()** | Convertir modelo a diccionario |
| **model_validate()** | Crear modelo desde diccionario |

---

## ✅ Checklist de Verificación

Antes de continuar, asegúrate de poder:

- [ ] Explicar qué problema resuelve Pydantic
- [ ] Crear un modelo básico con `BaseModel`
- [ ] Entender la diferencia entre v1 y v2
- [ ] Manejar `ValidationError`
- [ ] Usar `model_dump()` y `model_validate()`

---

## 🔗 Recursos Adicionales

- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [Migration Guide v1 to v2](https://docs.pydantic.dev/latest/migration/)
- [FastAPI - Request Body](https://fastapi.tiangolo.com/tutorial/body/)

---

[← Volver a Semana 02](../README.md) | [Siguiente: BaseModel en Profundidad →](02-basemodel.md)
