# 📦 Ejercicio 02: Field y Restricciones

## 🎯 Objetivo

Aprender a usar `Field()` para agregar validaciones avanzadas y tipos especiales de Pydantic.

---

## 📚 Conceptos Clave

- `Field()`: Configuración avanzada de campos
- Validaciones numéricas: `gt`, `ge`, `lt`, `le`
- Validaciones de strings: `min_length`, `max_length`, `pattern`
- Tipos especiales: `EmailStr`, `HttpUrl`
- `Annotated` para tipos reutilizables

---

## 📝 Instrucciones

### Paso 1: Validaciones Numéricas con Field

`Field()` permite agregar restricciones a los campos:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    price: float = Field(gt=0)           # Mayor que 0
    quantity: int = Field(ge=0, le=1000) # 0-1000
    discount: float = Field(ge=0, le=100) # Porcentaje
```

**Descomenta y ejecuta** el Paso 1.

---

### Paso 2: Validaciones de Strings

```python
class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    bio: str = Field(max_length=500, default="")
    phone: str = Field(pattern=r"^\d{10}$")  # Regex
```

**Descomenta y ejecuta** el Paso 2.

---

### Paso 3: Tipos Especiales de Pydantic

Pydantic incluye tipos que validan formatos específicos:

```python
from pydantic import EmailStr, HttpUrl

class Contact(BaseModel):
    email: EmailStr
    website: HttpUrl
```

**Descomenta y ejecuta** el Paso 3.

---

### Paso 4: Tipos Reutilizables con Annotated

Crea tipos personalizados reutilizables:

```python
from typing import Annotated
from pydantic import Field, StringConstraints

Username = Annotated[str, StringConstraints(min_length=3, max_length=20)]
PositiveFloat = Annotated[float, Field(gt=0)]
```

**Descomenta y ejecuta** el Paso 4.

---

### Paso 5: Alias y Documentación

```python
class APIResponse(BaseModel):
    user_id: int = Field(alias="userId")  # JSON usa camelCase
    full_name: str = Field(
        alias="fullName",
        description="Nombre completo del usuario",
        examples=["John Doe"]
    )
```

**Descomenta y ejecuta** el Paso 5.

---

## 🧪 Verificación

```bash
docker compose up --build
# o
uv run python main.py
```

---

## 🎯 Reto Extra

Crea un modelo `CreditCard` con:
- `number`: string de exactamente 16 dígitos
- `holder`: string de 2-100 caracteres
- `expiry_month`: entero 1-12
- `expiry_year`: entero >= año actual
- `cvv`: string de 3-4 dígitos

---

[← Anterior: BaseModel](../ejercicio-01-basemodel/) | [Siguiente: Validadores →](../ejercicio-03-validadores/)
