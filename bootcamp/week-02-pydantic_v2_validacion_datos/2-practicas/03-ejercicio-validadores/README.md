# 🔍 Ejercicio 03: Validadores Personalizados

## 🎯 Objetivo

Aprender a crear validadores personalizados con `@field_validator` y `@model_validator`.

---

## 📚 Conceptos Clave

- `@field_validator`: Validar un campo específico
- `@model_validator`: Validar múltiples campos juntos
- `mode='before'` vs `mode='after'`
- Transformar datos durante la validación

---

## 📝 Instrucciones

### Paso 1: Field Validator Básico

`@field_validator` valida y transforma campos individuales:

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("Name too short")
        return v.title()  # Capitalizar
```

**Descomenta y ejecuta** el Paso 1.

---

### Paso 2: Validar Múltiples Campos

Un validador puede aplicarse a varios campos:

```python
@field_validator("first_name", "last_name")
@classmethod
def validate_names(cls, v: str) -> str:
    return v.strip().title()
```

**Descomenta y ejecuta** el Paso 2.

---

### Paso 3: mode='before' vs mode='after'

- `after` (default): Después de la conversión de tipos
- `before`: Antes de la conversión (input raw)

```python
@field_validator("tags", mode="before")
@classmethod
def parse_tags(cls, v):
    if isinstance(v, str):
        return v.split(",")
    return v
```

**Descomenta y ejecuta** el Paso 3.

---

### Paso 4: Model Validator

`@model_validator` valida el modelo completo:

```python
from pydantic import model_validator

class User(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode="after")
    def validate_passwords(self) -> "User":
        if self.password != self.confirm_password:
            raise ValueError("Passwords don't match")
        return self
```

**Descomenta y ejecuta** el Paso 4.

---

### Paso 5: Validadores Prácticos

Ejemplos del mundo real:
- Validar contraseña segura
- Normalizar teléfono
- Generar slug desde título

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

Crea un modelo `Event` con:
- `start_date`: fecha de inicio
- `end_date`: fecha de fin
- Validar que `end_date` sea posterior a `start_date`
- Si no se proporciona `end_date`, usar `start_date`

---

[← Anterior: Field](../02-ejercicio-field/) | [Siguiente: Integración FastAPI →](../04-ejercicio-integracion/)
