# 📦 Tipos de Campo Especiales

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Usar tipos especiales de Pydantic (EmailStr, HttpUrl, etc.)
- ✅ Crear strings con restricciones usando Annotated
- ✅ Trabajar con tipos numéricos restringidos
- ✅ Manejar fechas y UUIDs
- ✅ Crear tipos personalizados reutilizables

---

## � Mapa de Tipos de Campo

![Tipos de campo en Pydantic](../0-assets/02-field-types.svg)

---

## �📚 Contenido

### 1. Tipos de String Especiales

Pydantic incluye tipos que validan formatos específicos:

```python
from pydantic import BaseModel, EmailStr, HttpUrl, AnyUrl

class Contact(BaseModel):
    email: EmailStr                    # Email válido
    website: HttpUrl                   # URL con http/https
    any_link: AnyUrl                   # Cualquier URL válida
```

```python
# Válido
contact = Contact(
    email="user@example.com",
    website="https://example.com",
    any_link="ftp://files.example.com"
)

# Inválido
Contact(email="not-an-email", ...)
# ValidationError: value is not a valid email address
```

#### Instalación de email-validator

Para usar `EmailStr`, necesitas instalar:

```bash
uv add pydantic[email]
# o
uv add email-validator
```

#### Tipos de URL Disponibles

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `HttpUrl` | Solo http/https | `https://example.com` |
| `AnyUrl` | Cualquier esquema | `ftp://`, `mailto:` |
| `AnyHttpUrl` | http/https sin restricciones | `http://localhost` |
| `FileUrl` | URLs de archivo | `file:///path/to/file` |
| `PostgresDsn` | DSN de PostgreSQL | `postgresql://user:pass@host/db` |
| `RedisDsn` | DSN de Redis | `redis://localhost:6379/0` |

```python
from pydantic import BaseModel, PostgresDsn, RedisDsn

class DatabaseConfig(BaseModel):
    postgres_url: PostgresDsn
    redis_url: RedisDsn

config = DatabaseConfig(
    postgres_url="postgresql://user:pass@localhost:5432/mydb",
    redis_url="redis://localhost:6379/0"
)
```

---

### 2. Strings con Restricciones (Annotated)

En Pydantic v2, usamos `Annotated` con `StringConstraints`:

```python
from typing import Annotated
from pydantic import BaseModel, StringConstraints

# Definir tipos personalizados
Username = Annotated[
    str,
    StringConstraints(
        min_length=3,
        max_length=20,
        pattern=r"^[a-z0-9_]+$"
    )
]

Slug = Annotated[
    str,
    StringConstraints(
        min_length=1,
        max_length=100,
        to_lower=True,
        strip_whitespace=True
    )
]

Password = Annotated[
    str,
    StringConstraints(min_length=8, max_length=128)
]

class User(BaseModel):
    username: Username
    slug: Slug
    password: Password
```

```python
# Válido
user = User(
    username="john_doe",
    slug="  My-Article  ",  # Se convierte a "my-article"
    password="secret123"
)
print(user.slug)  # my-article

# Inválido
User(username="Jo", slug="test", password="short")
# ValidationError: String should have at least 3 characters
```

#### Parámetros de StringConstraints

| Parámetro | Descripción |
|-----------|-------------|
| `min_length` | Longitud mínima |
| `max_length` | Longitud máxima |
| `pattern` | Regex que debe cumplir |
| `strip_whitespace` | Quitar espacios al inicio/final |
| `to_lower` | Convertir a minúsculas |
| `to_upper` | Convertir a mayúsculas |

---

### 3. Números con Restricciones

#### Usando Field()

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    price: float = Field(gt=0, le=1000000)
    quantity: int = Field(ge=0, le=9999)
    discount: float = Field(ge=0, le=100)
```

#### Usando Annotated (Reutilizable)

```python
from typing import Annotated
from pydantic import BaseModel, Field

# Tipos numéricos reutilizables
PositiveFloat = Annotated[float, Field(gt=0)]
PositiveInt = Annotated[int, Field(gt=0)]
NonNegativeInt = Annotated[int, Field(ge=0)]
Percentage = Annotated[float, Field(ge=0, le=100)]
Port = Annotated[int, Field(ge=1, le=65535)]

class ServerConfig(BaseModel):
    port: Port
    max_connections: PositiveInt
    timeout_seconds: PositiveFloat
    cpu_threshold: Percentage
```

```python
config = ServerConfig(
    port=8080,
    max_connections=100,
    timeout_seconds=30.5,
    cpu_threshold=80.0
)

# Inválido
ServerConfig(port=70000, ...)  # Port must be <= 65535
```

---

### 4. Fechas y Tiempos

```python
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel, Field, PastDate, FutureDate

class Event(BaseModel):
    name: str
    
    # Fechas básicas
    created_at: datetime
    event_date: date
    start_time: time
    
    # Fechas con restricciones
    birth_date: PastDate              # Debe ser en el pasado
    appointment: FutureDate           # Debe ser en el futuro
    
    # Duración
    duration: timedelta
```

```python
from datetime import date, datetime, time, timedelta

event = Event(
    name="Conference",
    created_at=datetime.now(),
    event_date=date(2025, 6, 15),
    start_time=time(9, 0),
    birth_date=date(1990, 5, 20),
    appointment=date(2026, 1, 15),
    duration=timedelta(hours=2)
)

# Pydantic parsea strings automáticamente
event2 = Event(
    name="Meeting",
    created_at="2025-12-31T10:30:00",  # ISO format string
    event_date="2025-06-15",
    start_time="09:00:00",
    birth_date="1990-05-20",
    appointment="2026-01-15",
    duration="PT2H"  # ISO 8601 duration
)
```

#### Tipos de Fecha Especiales

| Tipo | Descripción |
|------|-------------|
| `PastDate` | Fecha en el pasado |
| `FutureDate` | Fecha en el futuro |
| `PastDatetime` | Datetime en el pasado |
| `FutureDatetime` | Datetime en el futuro |
| `AwareDatetime` | Datetime con timezone |
| `NaiveDatetime` | Datetime sin timezone |

---

### 5. UUIDs

```python
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class Entity(BaseModel):
    # UUID requerido
    id: UUID
    
    # UUID con valor por defecto
    tracking_id: UUID = Field(default_factory=uuid4)

# Pydantic acepta strings UUID
entity = Entity(id="550e8400-e29b-41d4-a716-446655440000")
print(entity.id)  # UUID('550e8400-e29b-41d4-a716-446655440000')
print(type(entity.id))  # <class 'uuid.UUID'>

# También acepta UUID directamente
from uuid import uuid4
entity2 = Entity(id=uuid4())
```

---

### 6. Enumeraciones

```python
from enum import Enum
from pydantic import BaseModel, ConfigDict

class Status(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"

class Priority(int, Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    
    title: str
    status: Status = Status.PENDING
    priority: Priority = Priority.MEDIUM
```

```python
# Acepta valor de enum o string
task1 = Task(title="Review code", status=Status.ACTIVE, priority=Priority.HIGH)
task2 = Task(title="Write docs", status="pending", priority=2)

print(task1.status)    # active (string, por use_enum_values=True)
print(task2.priority)  # 2

# Sin use_enum_values, retorna el enum
# print(task1.status)  # Status.ACTIVE
```

---

### 7. Tipos de Colecciones

```python
from pydantic import BaseModel, Field
from typing import Annotated

class Article(BaseModel):
    # Lista con validación de longitud
    tags: list[str] = Field(min_length=1, max_length=10)
    
    # Set (valores únicos)
    categories: set[str] = Field(default_factory=set)
    
    # Diccionario
    metadata: dict[str, str] = Field(default_factory=dict)
    
    # Tupla con tipos específicos
    coordinates: tuple[float, float] | None = None
    
    # Lista de objetos complejos
    authors: list[str] = Field(min_length=1)
```

```python
article = Article(
    tags=["python", "fastapi", "tutorial"],
    categories={"backend", "web", "backend"},  # Set elimina duplicados
    metadata={"version": "1.0", "lang": "es"},
    coordinates=(19.4326, -99.1332),
    authors=["Alice", "Bob"]
)

print(article.categories)  # {'backend', 'web'}
```

---

### 8. Tipos Literales

Para campos que solo aceptan valores específicos:

```python
from typing import Literal
from pydantic import BaseModel

class Config(BaseModel):
    environment: Literal["development", "staging", "production"]
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    database: Literal["sqlite", "postgresql", "mysql"]
```

```python
# Válido
config = Config(
    environment="production",
    log_level="INFO",
    database="postgresql"
)

# Inválido
Config(environment="testing", ...)
# ValidationError: Input should be 'development', 'staging' or 'production'
```

---

### 9. Tipos Secretos

Para datos sensibles que no deben mostrarse en logs:

```python
from pydantic import BaseModel, SecretStr, SecretBytes

class Credentials(BaseModel):
    username: str
    password: SecretStr
    api_key: SecretStr

creds = Credentials(
    username="admin",
    password="super_secret_123",
    api_key="sk-1234567890"
)

# El valor secreto no se muestra
print(creds)
# username='admin' password=SecretStr('**********') api_key=SecretStr('**********')

# Para obtener el valor real
print(creds.password.get_secret_value())  # super_secret_123

# En JSON también se oculta
print(creds.model_dump())
# {'username': 'admin', 'password': SecretStr('**********'), ...}

# Para incluir secretos en el dump
print(creds.model_dump(mode="json", exclude={"password"}))
```

---

### 10. Crear Tipos Personalizados

#### Con Annotated (Recomendado)

```python
from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator

def validate_isbn(v: str) -> str:
    """Valida formato ISBN-13."""
    clean = v.replace("-", "").replace(" ", "")
    if len(clean) != 13 or not clean.isdigit():
        raise ValueError("Invalid ISBN-13 format")
    return clean

ISBN = Annotated[str, AfterValidator(validate_isbn)]

class Book(BaseModel):
    title: str
    isbn: ISBN

book = Book(title="Clean Code", isbn="978-0-13-235088-4")
print(book.isbn)  # 9780132350884
```

#### Con BeforeValidator

```python
from typing import Annotated, Any
from pydantic import BaseModel, BeforeValidator

def parse_bool(v: Any) -> bool:
    """Parsea valores booleanos de forma flexible."""
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        if v.lower() in ("true", "1", "yes", "on"):
            return True
        if v.lower() in ("false", "0", "no", "off"):
            return False
    raise ValueError(f"Cannot parse {v} as boolean")

FlexibleBool = Annotated[bool, BeforeValidator(parse_bool)]

class Settings(BaseModel):
    debug: FlexibleBool
    verbose: FlexibleBool

settings = Settings(debug="yes", verbose="0")
print(settings.debug)    # True
print(settings.verbose)  # False
```

---

## 📝 Resumen de Tipos

| Categoría | Tipos |
|-----------|-------|
| **Strings** | `EmailStr`, `HttpUrl`, `AnyUrl` |
| **Restricciones** | `StringConstraints`, `Field(gt=, le=)` |
| **Fechas** | `date`, `datetime`, `PastDate`, `FutureDate` |
| **Identificadores** | `UUID` |
| **Enums** | `Enum`, `Literal` |
| **Secretos** | `SecretStr`, `SecretBytes` |
| **Colecciones** | `list`, `set`, `dict`, `tuple` |

---

## ✅ Checklist de Verificación

Antes de continuar, asegúrate de poder:

- [ ] Usar `EmailStr` y `HttpUrl` para validar formatos
- [ ] Crear strings restringidos con `Annotated` y `StringConstraints`
- [ ] Definir tipos numéricos con restricciones
- [ ] Trabajar con fechas y UUIDs
- [ ] Crear tipos personalizados con `AfterValidator`

---

## 🔗 Recursos Adicionales

- [Pydantic Types](https://docs.pydantic.dev/latest/concepts/types/)
- [Standard Library Types](https://docs.pydantic.dev/latest/api/standard_library_types/)
- [Custom Types](https://docs.pydantic.dev/latest/concepts/types/#custom-types)

---

[← Anterior: Validadores](03-validadores.md) | [Siguiente: Pydantic con FastAPI →](05-pydantic-fastapi.md)
