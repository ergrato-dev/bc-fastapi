# 🏗️ BaseModel en Profundidad

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Dominar la creación de modelos con BaseModel
- ✅ Configurar modelos con `model_config`
- ✅ Implementar herencia de modelos
- ✅ Usar campos opcionales y valores por defecto
- ✅ Trabajar con modelos anidados

---

## 📚 Contenido

### 1. Anatomía de un BaseModel

Un modelo Pydantic tiene varios componentes:

```python
from pydantic import BaseModel, ConfigDict, Field

class User(BaseModel):
    """Docstring que aparece en la documentación OpenAPI."""
    
    # Configuración del modelo
    model_config = ConfigDict(
        str_strip_whitespace=True,
        str_min_length=1,
    )
    
    # Campos del modelo
    id: int
    name: str
    email: str
    age: int | None = None  # Campo opcional
    tags: list[str] = Field(default_factory=list)  # Con factory
```

---

### 2. Campos Requeridos vs Opcionales

#### Campos Requeridos

Un campo **sin valor por defecto** es requerido:

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str      # Requerido
    price: float   # Requerido
    sku: str       # Requerido
```

```python
# ❌ Error: faltan campos requeridos
Product(name="Laptop")
# ValidationError: 2 validation errors
# price: Field required
# sku: Field required

# ✅ Correcto: todos los campos requeridos
Product(name="Laptop", price=999.99, sku="LAP-001")
```

#### Campos Opcionales

Un campo con **valor por defecto** o tipo `| None` es opcional:

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    description: str | None = None      # Opcional, default None
    quantity: int = 0                    # Opcional, default 0
    active: bool = True                  # Opcional, default True
```

```python
# Solo campos requeridos
product = Product(name="Mouse", price=29.99)
print(product)
# name='Mouse' price=29.99 description=None quantity=0 active=True
```

#### ⚠️ Orden de Campos

Los campos requeridos deben ir **antes** que los opcionales:

```python
# ❌ ERROR: campo requerido después de opcional
class BadModel(BaseModel):
    name: str = "default"
    price: float  # Error: non-default after default

# ✅ CORRECTO: requeridos primero
class GoodModel(BaseModel):
    price: float      # Requerido primero
    name: str = "default"  # Opcional después
```

---

### 3. Configuración con model_config

`model_config` permite configurar el comportamiento del modelo:

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        # Strings
        str_strip_whitespace=True,   # Quitar espacios al inicio/final
        str_min_length=1,            # Mínimo 1 carácter para strings
        
        # Validación
        strict=False,                # Permitir coerción de tipos
        validate_default=True,       # Validar valores por defecto
        
        # Campos extra
        extra="forbid",              # Prohibir campos no definidos
        # extra="allow"              # Permitir campos extra
        # extra="ignore"             # Ignorar campos extra
        
        # Inmutabilidad
        frozen=False,                # True = modelo inmutable
        
        # Serialización
        populate_by_name=True,       # Permitir usar alias o nombre
        use_enum_values=True,        # Usar valores de enum, no el enum
        
        # Documentación
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "email": "john@example.com"
            }
        },
    )
    
    name: str
    email: str
```

#### Opciones Comunes de `extra`

```python
from pydantic import BaseModel, ConfigDict

# extra="forbid" - Error si hay campos extra
class StrictUser(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str

StrictUser(name="Alice", age=30)  # ❌ ValidationError: extra field 'age'

# extra="ignore" - Ignora campos extra (default)
class FlexUser(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str

user = FlexUser(name="Alice", age=30)
print(user.model_dump())  # {'name': 'Alice'} - age ignorado

# extra="allow" - Guarda campos extra
class OpenUser(BaseModel):
    model_config = ConfigDict(extra="allow")
    name: str

user = OpenUser(name="Alice", age=30)
print(user.model_dump())  # {'name': 'Alice', 'age': 30}
```

#### Modelo Inmutable (frozen)

```python
from pydantic import BaseModel, ConfigDict

class ImmutableUser(BaseModel):
    model_config = ConfigDict(frozen=True)
    name: str
    age: int

user = ImmutableUser(name="Alice", age=30)
user.name = "Bob"  # ❌ ValidationError: Instance is frozen
```

---

### 4. Field() - Configuración Avanzada de Campos

`Field()` permite configurar cada campo individualmente:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    # Validación numérica
    price: float = Field(gt=0, description="Precio del producto")
    quantity: int = Field(ge=0, le=1000, default=0)
    
    # Validación de strings
    name: str = Field(min_length=1, max_length=100)
    sku: str = Field(pattern=r"^[A-Z]{3}-\d{3}$")  # Regex
    
    # Alias para JSON
    product_id: int = Field(alias="productId")
    
    # Valor por defecto con factory
    tags: list[str] = Field(default_factory=list)
    
    # Deprecación
    old_field: str | None = Field(default=None, deprecated=True)
```

#### Parámetros de Field()

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `default` | Valor por defecto | `Field(default=0)` |
| `default_factory` | Factory para default mutable | `Field(default_factory=list)` |
| `alias` | Nombre alternativo en JSON | `Field(alias="userName")` |
| `title` | Título para documentación | `Field(title="User Name")` |
| `description` | Descripción para docs | `Field(description="...")` |
| `gt`, `ge`, `lt`, `le` | Comparaciones numéricas | `Field(gt=0, le=100)` |
| `min_length`, `max_length` | Longitud de strings | `Field(min_length=1)` |
| `pattern` | Regex para validar | `Field(pattern=r"^\d+$")` |
| `deprecated` | Marcar como obsoleto | `Field(deprecated=True)` |
| `exclude` | Excluir de serialización | `Field(exclude=True)` |

#### Validaciones Numéricas

```python
from pydantic import BaseModel, Field

class Metrics(BaseModel):
    # gt = greater than (>)
    positive: float = Field(gt=0)  # Debe ser > 0
    
    # ge = greater than or equal (>=)
    non_negative: int = Field(ge=0)  # Debe ser >= 0
    
    # lt = less than (<)
    under_hundred: int = Field(lt=100)  # Debe ser < 100
    
    # le = less than or equal (<=)
    percentage: float = Field(ge=0, le=100)  # 0-100
    
    # Múltiplo de
    even: int = Field(multiple_of=2)  # Debe ser par
```

---

### 5. Herencia de Modelos

Puedes crear modelos que hereden de otros:

```python
from pydantic import BaseModel, Field
from datetime import datetime

# Modelo base
class BaseUser(BaseModel):
    """Campos comunes para usuarios."""
    name: str = Field(min_length=1, max_length=100)
    email: str

# Modelo para crear usuarios (sin ID)
class UserCreate(BaseUser):
    """Datos necesarios para crear un usuario."""
    password: str = Field(min_length=8)

# Modelo para respuestas (con ID, sin password)
class UserResponse(BaseUser):
    """Datos que se retornan al cliente."""
    id: int
    created_at: datetime

# Modelo para actualizar (todos opcionales)
class UserUpdate(BaseModel):
    """Campos opcionales para actualizar."""
    name: str | None = None
    email: str | None = None
```

#### Uso en FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate) -> UserResponse:
    # user tiene: name, email, password
    # retorna: id, name, email, created_at (sin password)
    return UserResponse(
        id=1,
        name=user.name,
        email=user.email,
        created_at=datetime.now(),
    )
```

---

### 6. Modelos Anidados

Los modelos pueden contener otros modelos:

```python
from pydantic import BaseModel, Field

class Address(BaseModel):
    """Dirección postal."""
    street: str
    city: str
    country: str = "México"
    zip_code: str = Field(pattern=r"^\d{5}$")

class Company(BaseModel):
    """Empresa."""
    name: str
    address: Address  # Modelo anidado

class User(BaseModel):
    """Usuario con empresa y direcciones."""
    name: str
    company: Company | None = None
    addresses: list[Address] = Field(default_factory=list)
```

#### Crear Instancias Anidadas

```python
# Desde diccionarios anidados (Pydantic convierte automáticamente)
data = {
    "name": "Alice",
    "company": {
        "name": "TechCorp",
        "address": {
            "street": "Av. Reforma 123",
            "city": "CDMX",
            "zip_code": "06600"
        }
    },
    "addresses": [
        {"street": "Calle 1", "city": "CDMX", "zip_code": "06600"},
        {"street": "Calle 2", "city": "GDL", "zip_code": "44100"}
    ]
}

user = User(**data)  # o User.model_validate(data)
print(user.company.address.city)  # CDMX
print(user.addresses[0].street)   # Calle 1
```

#### Serialización de Modelos Anidados

```python
# model_dump() convierte todo a diccionarios
print(user.model_dump())
# {
#     'name': 'Alice',
#     'company': {
#         'name': 'TechCorp',
#         'address': {'street': '...', 'city': 'CDMX', ...}
#     },
#     'addresses': [...]
# }

# model_dump_json() convierte a JSON string
print(user.model_dump_json(indent=2))
```

---

### 7. Patrones Comunes

#### Modelo Base con Timestamps

```python
from pydantic import BaseModel, Field
from datetime import datetime

class TimestampMixin(BaseModel):
    """Mixin con campos de timestamp."""
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None

class User(TimestampMixin):
    name: str
    email: str

user = User(name="Alice", email="alice@example.com")
print(user.created_at)  # 2025-12-31 12:00:00.123456
```

#### Modelo con ID Autogenerado

```python
from pydantic import BaseModel, Field
from uuid import uuid4

class Entity(BaseModel):
    """Entidad base con UUID."""
    id: str = Field(default_factory=lambda: str(uuid4()))

class Product(Entity):
    name: str
    price: float

product = Product(name="Laptop", price=999.99)
print(product.id)  # 550e8400-e29b-41d4-a716-446655440000
```

---

## 📝 Resumen

| Concepto | Descripción |
|----------|-------------|
| Campos requeridos | Sin valor por defecto |
| Campos opcionales | Con default o `\| None` |
| `model_config` | Configuración global del modelo |
| `Field()` | Configuración por campo |
| `extra="forbid"` | No permitir campos extra |
| `frozen=True` | Modelo inmutable |
| Herencia | Reusar campos entre modelos |
| Modelos anidados | Modelos dentro de modelos |

---

## ✅ Checklist de Verificación

Antes de continuar, asegúrate de poder:

- [ ] Crear modelos con campos requeridos y opcionales
- [ ] Configurar `model_config` con opciones comunes
- [ ] Usar `Field()` para validaciones avanzadas
- [ ] Implementar herencia de modelos
- [ ] Trabajar con modelos anidados

---

## 🔗 Recursos Adicionales

- [Pydantic Fields](https://docs.pydantic.dev/latest/concepts/fields/)
- [Model Config](https://docs.pydantic.dev/latest/concepts/config/)
- [Nested Models](https://docs.pydantic.dev/latest/concepts/models/#nested-models)

---

[← Anterior: Introducción a Pydantic](01-intro-pydantic.md) | [Siguiente: Validadores →](03-validadores.md)
