# 🐍 Python Moderno (3.13+)

## 🎯 Objetivos

- Conocer las características modernas de Python 3.13+
- Entender por qué FastAPI requiere Python moderno
- Aplicar sintaxis moderna en tu código

---

## 📋 Contenido

### 1. ¿Por qué Python 3.13+?

FastAPI aprovecha características modernas de Python:

| Característica | Versión | Uso en FastAPI |
|----------------|---------|----------------|
| Type hints nativos | 3.9+ | Validación automática |
| Union con `\|` | 3.10+ | Tipos opcionales |
| Match statements | 3.10+ | Pattern matching |
| Mejoras async | 3.11+ | Mejor rendimiento |
| Mensajes de error | 3.13+ | Debugging más fácil |

---

### 2. F-Strings (Formatted String Literals)

La forma moderna de formatear strings:

```python
# ✅ MODERNO - f-strings
name = "FastAPI"
version = "0.115"
message = f"Bienvenido a {name} v{version}"

# También con expresiones
items = ["a", "b", "c"]
count = f"Total: {len(items)} items"

# Formateo numérico
price = 19.99
formatted = f"Precio: ${price:.2f}"  # "Precio: $19.99"

# ❌ ANTIGUO - evitar
message = "Bienvenido a {} v{}".format(name, version)
message = "Bienvenido a %s v%s" % (name, version)
```

---

### 3. Walrus Operator `:=`

Asignar y usar una variable en la misma expresión:

```python
# ✅ CON walrus operator
if (n := len(users)) > 10:
    print(f"Muchos usuarios: {n}")

# Útil en comprensiones
results = [y for x in data if (y := process(x)) is not None]

# En while loops
while (line := file.readline()):
    process(line)

# ❌ SIN walrus operator (más verboso)
n = len(users)
if n > 10:
    print(f"Muchos usuarios: {n}")
```

---

### 4. Match Statements (Pattern Matching)

Similar a switch/case pero más poderoso:

```python
def handle_response(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:  # default
            return "Unknown"

# Con patrones más complejos
def handle_request(request: dict) -> str:
    match request:
        case {"method": "GET", "path": path}:
            return f"GET request to {path}"
        case {"method": "POST", "body": body}:
            return f"POST with body: {body}"
        case _:
            return "Unknown request"
```

---

### 5. Diccionarios: Merge y Update

```python
# Merge con | (crea nuevo dict)
defaults = {"theme": "dark", "lang": "es"}
user_prefs = {"lang": "en"}
config = defaults | user_prefs
# {"theme": "dark", "lang": "en"}

# Update in-place con |=
defaults |= user_prefs  # Modifica defaults
```

---

### 6. Genéricos Nativos

Desde Python 3.9, no necesitas importar de `typing`:

```python
# ✅ MODERNO (3.9+) - genéricos nativos
def get_first(items: list[str]) -> str | None:
    return items[0] if items else None

def get_user_ages(users: dict[str, int]) -> list[int]:
    return list(users.values())

# ❌ ANTIGUO - evitar
from typing import List, Dict, Optional

def get_first(items: List[str]) -> Optional[str]:
    return items[0] if items else None
```

---

### 7. Union Types con `|`

```python
# ✅ MODERNO (3.10+)
def process(value: int | str | None) -> str:
    if value is None:
        return "No value"
    return str(value)

# ❌ ANTIGUO
from typing import Union, Optional

def process(value: Union[int, str, None]) -> str:
    ...
```

---

### 8. Mejoras en Mensajes de Error

Python 3.13 tiene mensajes de error más claros:

```python
# Error más descriptivo
# Python 3.13:
# NameError: name 'user_nmae' is not defined. Did you mean: 'user_name'?

# Errores de sintaxis señalan el problema exacto
# SyntaxError: expected ':' after dictionary key
#     {"name" "value"}
#            ^
```

---

## 💡 Resumen: Qué Usar

| Característica | Sintaxis Moderna |
|----------------|------------------|
| Strings | `f"Hello {name}"` |
| Tipos lista | `list[str]` |
| Tipos dict | `dict[str, int]` |
| Opcional | `str \| None` |
| Union | `int \| str` |
| Asignar + usar | `:=` (walrus) |
| Switch/case | `match ... case` |
| Merge dicts | `dict1 \| dict2` |

---

## ✅ Checklist de Verificación

- [ ] Usar f-strings para formateo
- [ ] Usar genéricos nativos (`list[str]` no `List[str]`)
- [ ] Usar `|` para unions (`int | None` no `Optional[int]`)
- [ ] Conocer el walrus operator `:=`
- [ ] Entender match statements

---

## ➡️ Siguiente

[03 - Type Hints](03-type-hints.md)
