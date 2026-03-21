# 🔧 pytest Básico

## 🎯 Objetivos

- Instalar y configurar pytest en un proyecto FastAPI
- Escribir y ejecutar tests básicos
- Entender assertions y su sintaxis
- Organizar la estructura de tests

---

## 📦 Instalación

### Con uv (recomendado)

```bash
# Crear proyecto
uv init my-project
cd my-project

# Añadir pytest como dependencia de desarrollo
uv add --dev pytest pytest-asyncio pytest-cov httpx

# Verificar instalación
uv run pytest --version
```

### pyproject.toml

```toml
[project]
name = "my-fastapi-project"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn>=0.32.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.4",
    "pytest-asyncio>=0.24.0",
    "pytest-cov>=6.0.0",
    "httpx>=0.28.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_functions = ["test_*"]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
```

---

## 📁 Estructura de Proyecto

```
my-project/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── services/
│       ├── __init__.py
│       └── user_service.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Fixtures compartidas
│   ├── unit/                 # Tests unitarios
│   │   ├── __init__.py
│   │   └── test_services.py
│   └── integration/          # Tests de integración
│       ├── __init__.py
│       └── test_api.py
└── htmlcov/                  # Reportes de cobertura
```

---

## ✍️ Escribiendo Tests Básicos

### Primer Test

```python
# tests/test_example.py

def test_addition():
    """Test básico de suma."""
    result = 1 + 1
    assert result == 2


def test_string_contains():
    """Test de substring."""
    message = "Hello, World!"
    assert "World" in message


def test_list_length():
    """Test de longitud de lista."""
    items = [1, 2, 3, 4, 5]
    assert len(items) == 5
```

### Ejecutar Tests

```bash
# Ejecutar todos los tests
uv run pytest

# Con output detallado
uv run pytest -v

# Solo un archivo
uv run pytest tests/test_example.py

# Solo una función
uv run pytest tests/test_example.py::test_addition

# Mostrar print statements
uv run pytest -s

# Parar en primer fallo
uv run pytest -x

# Últimos 2 que fallaron
uv run pytest --lf
```

---

## 🎯 Assertions en pytest

### Assertions Básicas

```python
def test_assertions_basicas():
    # Igualdad
    assert 1 + 1 == 2
    assert "hello" == "hello"
    
    # Desigualdad
    assert 1 != 2
    
    # Verdad/Falsedad
    assert True
    assert not False
    assert bool([1, 2, 3])  # Lista no vacía es True
    assert not bool([])      # Lista vacía es False
    
    # None
    value = None
    assert value is None
    
    other = "something"
    assert other is not None
    
    # Identidad vs Igualdad
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    assert a == b       # Igualdad de contenido
    assert a is not b   # No son el mismo objeto
    assert a is c       # Son el mismo objeto
```

### Assertions de Colecciones

```python
def test_assertions_colecciones():
    numbers = [1, 2, 3, 4, 5]
    
    # Contenido
    assert 3 in numbers
    assert 10 not in numbers
    
    # Longitud
    assert len(numbers) == 5
    
    # Subconjuntos
    assert set([1, 2]).issubset(set(numbers))
    
    # Diccionarios
    user = {"name": "John", "age": 30}
    assert "name" in user
    assert user["name"] == "John"
    assert user.get("email") is None
```

### Assertions de Strings

```python
def test_assertions_strings():
    message = "Hello, World!"
    
    # Contenido
    assert "World" in message
    assert message.startswith("Hello")
    assert message.endswith("!")
    
    # Case insensitive
    assert "HELLO" in message.upper()
    
    # Regex (con re module)
    import re
    assert re.match(r"Hello.*", message)
```

### Assertions Numéricas

```python
def test_assertions_numericas():
    # Comparaciones
    assert 5 > 3
    assert 5 >= 5
    assert 3 < 5
    assert 3 <= 3
    
    # Aproximación (para floats)
    import pytest
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 3.14159 == pytest.approx(3.14, rel=0.01)  # 1% tolerancia
    assert 100 == pytest.approx(101, abs=2)          # ±2 tolerancia
    
    # Rangos
    value = 7
    assert 5 <= value <= 10
```

---

## ⚠️ Testing de Excepciones

### pytest.raises

```python
import pytest


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_divide_by_zero_raises_error():
    """Verifica que dividir por cero lanza excepción."""
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_error_message():
    """Verifica el mensaje de la excepción."""
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    
    assert "zero" in str(exc_info.value)


def test_divide_by_zero_match_pattern():
    """Verifica con regex el mensaje."""
    with pytest.raises(ValueError, match=r".*divide.*zero.*"):
        divide(10, 0)
```

### Múltiples Tipos de Excepción

```python
def test_multiple_exception_types():
    """Captura cualquiera de varias excepciones."""
    with pytest.raises((ValueError, TypeError)):
        raise ValueError("test error")
```

---

## 🏷️ Marcadores (Markers)

### Markers Built-in

```python
import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    """Este test se salta."""
    pass


@pytest.mark.skipif(
    condition=True,
    reason="Skipped on this condition"
)
def test_conditional_skip():
    """Se salta si la condición es True."""
    pass


@pytest.mark.xfail(reason="Known bug #123")
def test_known_failure():
    """Se espera que falle."""
    assert False  # No cuenta como fallo del suite


@pytest.mark.slow
def test_slow_operation():
    """Marcador personalizado para tests lentos."""
    import time
    time.sleep(2)
    assert True
```

### Registrar Markers Personalizados

```toml
# pyproject.toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]
```

### Usar Markers al Ejecutar

```bash
# Solo tests marcados como "slow"
uv run pytest -m slow

# Excluir tests lentos
uv run pytest -m "not slow"

# Combinar markers
uv run pytest -m "unit and not slow"
```

---

## 📊 Cobertura de Código

### Ejecutar con Cobertura

```bash
# Cobertura básica
uv run pytest --cov=src

# Con reporte HTML
uv run pytest --cov=src --cov-report=html

# Con reporte en terminal
uv run pytest --cov=src --cov-report=term-missing

# Fallo si cobertura < 80%
uv run pytest --cov=src --cov-fail-under=80
```

### Interpretar el Reporte

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/__init__.py               0      0   100%
src/main.py                  25      3    88%   15-17
src/services/user.py         40     10    75%   22-31
-------------------------------------------------------
TOTAL                        65     13    80%
```

- **Stmts**: Líneas de código ejecutables
- **Miss**: Líneas no ejecutadas por tests
- **Cover**: Porcentaje de cobertura
- **Missing**: Números de línea sin cobertura

### Archivo de Configuración

```toml
# pyproject.toml
[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/__init__.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
```

---

## 🗂️ Organización de Tests

### Convención de Nombres

```python
# tests/test_user_service.py

# ✅ Buenos nombres - describen el comportamiento
def test_create_user_with_valid_email_succeeds():
    pass

def test_create_user_with_invalid_email_raises_validation_error():
    pass

def test_get_user_by_id_returns_user_when_exists():
    pass

def test_get_user_by_id_returns_none_when_not_found():
    pass


# ❌ Malos nombres - no describen el comportamiento
def test_user():
    pass

def test_1():
    pass

def test_create():
    pass
```

### Agrupar con Clases

```python
# tests/test_user_service.py

class TestCreateUser:
    """Tests para la creación de usuarios."""
    
    def test_with_valid_data_succeeds(self):
        pass
    
    def test_with_invalid_email_fails(self):
        pass
    
    def test_with_duplicate_email_fails(self):
        pass


class TestGetUser:
    """Tests para obtener usuarios."""
    
    def test_by_id_returns_user(self):
        pass
    
    def test_by_id_returns_none_when_not_found(self):
        pass
    
    def test_by_email_returns_user(self):
        pass
```

---

## 📝 Output y Debugging

### Mostrar Print Statements

```python
def test_with_debug_output():
    value = calculate_something()
    print(f"DEBUG: value = {value}")  # Solo visible con -s
    assert value > 0
```

```bash
uv run pytest -s  # Muestra stdout
uv run pytest -v  # Verbose: muestra nombres de tests
uv run pytest -sv # Ambos
```

### Usar el Debugger

```python
def test_with_breakpoint():
    value = calculate_something()
    breakpoint()  # Pausa aquí para debugging
    assert value > 0
```

```bash
uv run pytest --pdb  # Entra a debugger en fallo
uv run pytest --pdb-first  # Solo en primer fallo
```

---

## ✅ Resumen de Comandos

| Comando | Descripción |
|---------|-------------|
| `pytest` | Ejecutar todos los tests |
| `pytest -v` | Modo verbose |
| `pytest -s` | Mostrar prints |
| `pytest -x` | Parar en primer fallo |
| `pytest --lf` | Reejecutar últimos fallidos |
| `pytest -m slow` | Solo marker "slow" |
| `pytest --cov=src` | Con cobertura |
| `pytest -k "user"` | Tests que contienen "user" |
| `pytest --pdb` | Debugger en fallos |

---

## 🔗 Próximo Tema

→ [03-fixtures-y-parametrize.md](03-fixtures-y-parametrize.md) - Fixtures y parametrización
