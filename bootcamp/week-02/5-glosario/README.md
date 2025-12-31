# 📖 Glosario - Semana 02

Términos clave de Pydantic v2 ordenados alfabéticamente.

---

## A

### Annotated
Tipo de `typing` que permite agregar metadatos a tipos. En Pydantic v2, se usa para crear tipos reutilizables con validaciones.
```python
from typing import Annotated
from pydantic import Field
PositiveInt = Annotated[int, Field(gt=0)]
```

### AfterValidator
Validador que se ejecuta después de la conversión de tipos. Recibe el valor ya convertido al tipo final.

---

## B

### BaseModel
Clase base de Pydantic para crear modelos de datos con validación automática.
```python
from pydantic import BaseModel
class User(BaseModel):
    name: str
    age: int
```

### BeforeValidator
Validador que se ejecuta antes de la conversión de tipos. Recibe el valor raw sin procesar.

---

## C

### Coerción
Conversión automática de tipos que Pydantic realiza. Por ejemplo, `"42"` se convierte a `42` si el campo es `int`.

### ConfigDict
Diccionario de configuración para modelos Pydantic v2.
```python
from pydantic import ConfigDict
model_config = ConfigDict(str_strip_whitespace=True)
```

---

## D

### default_factory
Función que genera el valor por defecto de un campo. Útil para tipos mutables.
```python
tags: list[str] = Field(default_factory=list)
```

---

## E

### EmailStr
Tipo especial de Pydantic que valida formato de email.
```python
from pydantic import EmailStr
email: EmailStr
```

### exclude_unset
Parámetro de `model_dump()` que excluye campos no establecidos explícitamente. Útil para updates parciales.

### extra
Configuración que controla campos no definidos: `"forbid"`, `"allow"`, `"ignore"`.

---

## F

### Field
Función para configurar campos con validaciones, alias, descripciones, etc.
```python
from pydantic import Field
price: float = Field(gt=0, description="Precio positivo")
```

### field_validator
Decorador para crear validadores de campos específicos.
```python
@field_validator("name")
@classmethod
def validate_name(cls, v):
    return v.title()
```

### from_attributes
Configuración que permite crear modelos desde objetos con atributos (como ORM).
```python
model_config = ConfigDict(from_attributes=True)
```

### frozen
Configuración que hace el modelo inmutable (no se pueden modificar atributos después de crear).

---

## H

### HttpUrl
Tipo especial que valida URLs con esquema http o https.

---

## L

### Literal
Tipo que restringe valores a opciones específicas.
```python
from typing import Literal
status: Literal["active", "inactive"]
```

---

## M

### model_config
Atributo de clase para configurar el comportamiento del modelo.

### model_dump
Método que convierte el modelo a diccionario.
```python
user.model_dump()  # {'name': 'Alice', 'age': 30}
```

### model_dump_json
Método que convierte el modelo a string JSON.

### model_validate
Método de clase para crear instancia desde dict u objeto.
```python
User.model_validate({"name": "Alice", "age": 30})
```

### model_validator
Decorador para validar el modelo completo (múltiples campos).
```python
@model_validator(mode="after")
def validate_model(self):
    # Validar campos relacionados
    return self
```

---

## P

### pattern
Parámetro de Field para validar strings con expresiones regulares.
```python
phone: str = Field(pattern=r"^\d{10}$")
```

### populate_by_name
Configuración que permite usar tanto el nombre del campo como su alias.

---

## R

### response_model
Parámetro de FastAPI que define el schema de respuesta.
```python
@app.get("/users", response_model=UserResponse)
```

---

## S

### SecretStr
Tipo para datos sensibles que no se muestran en logs.
```python
from pydantic import SecretStr
password: SecretStr
```

### StringConstraints
Clase para definir restricciones de strings con Annotated.
```python
from pydantic import StringConstraints
Username = Annotated[str, StringConstraints(min_length=3)]
```

### str_strip_whitespace
Configuración que elimina espacios al inicio/final de strings automáticamente.

---

## V

### ValidationError
Excepción que Pydantic lanza cuando los datos no pasan la validación.

### Validator
Función que valida y/o transforma datos de un campo o modelo.

---

[← Volver a Recursos](../4-recursos/) | [Semana 03 →](../../week-03/)
