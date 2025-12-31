# 📝 Type Hints en Python

## 🎯 Objetivos

- Entender qué son los type hints y por qué usarlos
- Conocer los tipos básicos y compuestos
- Aplicar type hints en funciones y variables
- Entender cómo FastAPI los usa para validación

---

## 📋 Contenido

### 1. ¿Qué son los Type Hints?

Los type hints son **anotaciones** que indican el tipo de datos:

```python
# Sin type hints - ¿qué tipo es name? ¿qué devuelve?
def greet(name):
    return f"Hello, {name}"

# Con type hints - claro y autodocumentado
def greet(name: str) -> str:
    return f"Hello, {name}"
```

#### ¿Por qué son importantes en FastAPI?

FastAPI usa type hints para:

| Función | Ejemplo |
|---------|---------|
| **Validación** | Rechaza datos inválidos automáticamente |
| **Conversión** | Convierte `"123"` a `123` si espera `int` |
| **Documentación** | Genera Swagger/OpenAPI automáticamente |
| **Autocompletado** | Tu IDE sugiere métodos correctos |

![Type hints en FastAPI](../0-assets/type-hints-fastapi.svg)

---

### 2. Tipos Básicos

```python
# Strings
name: str = "FastAPI"

# Números
age: int = 25
price: float = 19.99

# Booleanos
is_active: bool = True

# None
result: None = None
```

---

### 3. Tipos Compuestos

```python
# Listas - lista de strings
tags: list[str] = ["python", "fastapi"]

# Diccionarios - claves string, valores int
scores: dict[str, int] = {"math": 90, "science": 85}

# Tuplas - tipos fijos por posición
point: tuple[int, int] = (10, 20)
rgb: tuple[int, int, int] = (255, 128, 0)

# Sets - conjunto de enteros
unique_ids: set[int] = {1, 2, 3}
```

---

### 4. Tipos Opcionales (pueden ser None)

```python
# Usando | None (Python 3.10+)
def find_user(user_id: int) -> dict | None:
    """Retorna usuario o None si no existe"""
    if user_id in database:
        return database[user_id]
    return None

# Variable opcional
middle_name: str | None = None
```

---

### 5. Union Types (múltiples tipos)

```python
# Puede ser int O str
def process_id(id: int | str) -> str:
    return str(id)

# Múltiples tipos posibles
value: int | float | str = get_value()
```

---

### 6. Funciones con Type Hints

```python
# Función completa con tipos
def calculate_total(
    prices: list[float],
    tax_rate: float = 0.16,
    discount: float | None = None
) -> float:
    """
    Calcula el total con impuestos y descuento opcional.
    
    Args:
        prices: Lista de precios
        tax_rate: Tasa de impuesto (default 16%)
        discount: Descuento opcional a aplicar
    
    Returns:
        Total calculado
    """
    subtotal = sum(prices)
    
    if discount:
        subtotal -= discount
    
    return subtotal * (1 + tax_rate)
```

---

### 7. Type Hints en Clases

```python
class User:
    def __init__(self, name: str, email: str, age: int | None = None):
        self.name: str = name
        self.email: str = email
        self.age: int | None = age
    
    def greet(self) -> str:
        return f"Hello, {self.name}"
    
    def is_adult(self) -> bool:
        if self.age is None:
            return False
        return self.age >= 18
```

---

### 8. Tipos Avanzados

```python
from typing import Callable, Any

# Callable - funciones como parámetros
def apply_operation(
    values: list[int],
    operation: Callable[[int], int]
) -> list[int]:
    return [operation(v) for v in values]

# Any - cualquier tipo (usar con moderación)
def log_anything(data: Any) -> None:
    print(data)

# Literal - valores específicos permitidos
from typing import Literal

def set_mode(mode: Literal["dark", "light"]) -> None:
    print(f"Mode set to {mode}")
```

---

### 9. Type Hints en FastAPI

FastAPI convierte type hints en validación automática:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(
    item_id: int,              # Path param: debe ser int
    q: str | None = None,      # Query param: string opcional
    limit: int = 10            # Query param: int con default
) -> dict:
    return {
        "item_id": item_id,
        "query": q,
        "limit": limit
    }
```

Si llamas `/items/abc` (string en vez de int), FastAPI responde:

```json
{
  "detail": [
    {
      "loc": ["path", "item_id"],
      "msg": "Input should be a valid integer",
      "type": "int_parsing"
    }
  ]
}
```

---

## 📊 Tabla Resumen

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| String | `str` | `"hello"` |
| Integer | `int` | `42` |
| Float | `float` | `3.14` |
| Boolean | `bool` | `True` |
| None | `None` | `None` |
| Lista | `list[T]` | `list[str]` |
| Dict | `dict[K, V]` | `dict[str, int]` |
| Tupla | `tuple[T, ...]` | `tuple[int, str]` |
| Set | `set[T]` | `set[int]` |
| Opcional | `T \| None` | `str \| None` |
| Union | `T1 \| T2` | `int \| str` |

---

## ✅ Checklist de Verificación

- [ ] Entender la sintaxis básica de type hints
- [ ] Conocer tipos básicos: `str`, `int`, `float`, `bool`
- [ ] Usar tipos compuestos: `list`, `dict`, `tuple`, `set`
- [ ] Manejar valores opcionales con `| None`
- [ ] Tipar funciones con parámetros y retorno
- [ ] Entender cómo FastAPI usa type hints

---

## ➡️ Siguiente

[04 - Async/Await](04-async-await.md)
