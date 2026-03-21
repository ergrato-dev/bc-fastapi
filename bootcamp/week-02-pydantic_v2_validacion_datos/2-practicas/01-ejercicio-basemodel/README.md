# 🏗️ Ejercicio 01: BaseModel Básico

## 🎯 Objetivo

Aprender a crear modelos Pydantic con `BaseModel`, configurar campos requeridos y opcionales, y usar `model_config`.

---

## 📚 Conceptos Clave

- `BaseModel`: Clase base para todos los modelos Pydantic
- Campos requeridos vs opcionales
- `model_config`: Configuración del modelo
- Métodos `model_dump()` y `model_dump_json()`

---

## 📝 Instrucciones

### Paso 1: Crear un BaseModel Simple

Abre `starter/main.py` y descomenta el código del **Paso 1**.

Un BaseModel básico define campos con sus tipos:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str       # Campo requerido
    email: str      # Campo requerido
    age: int        # Campo requerido
```

**Descomenta y ejecuta** para ver cómo Pydantic valida los datos.

---

### Paso 2: Campos Opcionales

Los campos con valor por defecto son opcionales:

```python
class Product(BaseModel):
    name: str                          # Requerido
    price: float                       # Requerido
    description: str | None = None     # Opcional (default: None)
    quantity: int = 0                  # Opcional (default: 0)
    active: bool = True                # Opcional (default: True)
```

**Descomenta y ejecuta** el Paso 2.

---

### Paso 3: Configuración con model_config

`model_config` permite configurar el comportamiento del modelo:

```python
from pydantic import BaseModel, ConfigDict

class StrictUser(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,  # Quitar espacios
        extra="forbid",              # No permitir campos extra
    )
    
    name: str
    email: str
```

**Descomenta y ejecuta** el Paso 3 para ver el efecto.

---

### Paso 4: Serialización

Los modelos tienen métodos para convertir a dict/JSON:

```python
user = User(name="Alice", email="alice@example.com", age=30)

# Convertir a diccionario
print(user.model_dump())

# Convertir a JSON string
print(user.model_dump_json(indent=2))
```

**Descomenta y ejecuta** el Paso 4.

---

### Paso 5: Modelos Anidados

Los modelos pueden contener otros modelos:

```python
class Address(BaseModel):
    street: str
    city: str
    country: str = "México"

class Person(BaseModel):
    name: str
    address: Address  # Modelo anidado
```

**Descomenta y ejecuta** el Paso 5.

---

## 🧪 Verificación

Ejecuta el archivo completo:

```bash
# Con Docker
docker compose up --build

# Sin Docker
uv run python main.py
```

Deberías ver la salida de cada paso sin errores.

---

## 🎯 Reto Extra

Intenta crear un modelo `Order` que tenga:
- `id`: entero requerido
- `customer_name`: string requerido
- `items`: lista de strings (default: lista vacía)
- `total`: float opcional
- `paid`: booleano (default: False)

---

[← Volver a Prácticas](../README.md) | [Siguiente: Field y Restricciones →](../02-ejercicio-field/)
