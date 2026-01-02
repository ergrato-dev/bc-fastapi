# 📖 Glosario - Semana 12: Testing con pytest

## A

### AAA Pattern (Arrange-Act-Assert)
Patrón de estructuración de tests en tres fases: preparar datos (Arrange), ejecutar acción (Act), verificar resultado (Assert).

```python
def test_suma():
    # Arrange
    a, b = 2, 3
    # Act
    resultado = suma(a, b)
    # Assert
    assert resultado == 5
```

### Assertion
Declaración que verifica una condición. Si es falsa, el test falla.

```python
assert resultado == esperado
assert usuario.is_active is True
```

### AsyncMock
Versión asíncrona de Mock para mockear coroutines.

```python
from unittest.mock import AsyncMock

mock_fetch = AsyncMock(return_value={"data": "test"})
result = await mock_fetch()
```

### Autouse
Opción de fixture que la aplica automáticamente a todos los tests sin necesidad de declararla como parámetro.

```python
@pytest.fixture(autouse=True)
def setup_logging():
    logging.disable(logging.CRITICAL)
```

---

## C

### Code Coverage
Métrica que indica qué porcentaje del código es ejecutado por los tests.

```bash
pytest --cov=src --cov-report=html
```

### conftest.py
Archivo especial de pytest donde se definen fixtures compartidas entre múltiples archivos de test.

---

## D

### Dependency Override
Técnica de FastAPI para reemplazar dependencias durante testing.

```python
app.dependency_overrides[get_db] = lambda: test_db
```

---

## F

### Fixture
Función que proporciona datos o configuración reutilizable para tests.

```python
@pytest.fixture
def client():
    return TestClient(app)
```

### Fixture Scope
Determina cuándo se crea y destruye una fixture:
- `function`: Una vez por test (default)
- `class`: Una vez por clase
- `module`: Una vez por módulo
- `session`: Una vez por sesión

---

## I

### Integration Test
Test que verifica la interacción entre múltiples componentes o sistemas.

---

## M

### Marker
Decorador que categoriza tests para ejecutarlos selectivamente.

```python
@pytest.mark.slow
def test_proceso_largo():
    ...

# Ejecutar: pytest -m slow
```

### Mock
Objeto simulado que reemplaza dependencias reales durante testing.

```python
from unittest.mock import Mock
mock_service = Mock()
mock_service.get_user.return_value = User(id=1)
```

### MagicMock
Mock avanzado que implementa métodos mágicos automáticamente (`__len__`, `__iter__`, etc.).

### Monkey Patching
Técnica de reemplazar atributos o funciones en tiempo de ejecución.

```python
def test_api(monkeypatch):
    monkeypatch.setattr("module.API_KEY", "test-key")
```

---

## P

### Parametrize
Decorador para ejecutar el mismo test con diferentes datos de entrada.

```python
@pytest.mark.parametrize("a,b,expected", [(1,2,3), (0,0,0)])
def test_suma(a, b, expected):
    assert suma(a, b) == expected
```

### Patch
Decorador/context manager que reemplaza temporalmente objetos.

```python
with patch("module.function") as mock:
    mock.return_value = "test"
    resultado = mi_funcion()
```

---

## R

### Red-Green-Refactor
Ciclo de TDD: escribir test que falla (Red), implementar código mínimo para pasar (Green), mejorar código (Refactor).

---

## S

### Side Effect
Comportamiento personalizado de un mock, puede ser una excepción o una secuencia de valores.

```python
mock.side_effect = [1, 2, 3]  # Retorna 1, luego 2, luego 3
mock.side_effect = ValueError("Error")  # Lanza excepción
```

### Stub
Objeto simple que retorna respuestas predefinidas sin lógica.

---

## T

### TDD (Test-Driven Development)
Metodología donde los tests se escriben antes que el código de producción.

### Test Client
Cliente HTTP para hacer peticiones a la API durante testing sin servidor real.

```python
from fastapi.testclient import TestClient
client = TestClient(app)
response = client.get("/users/1")
```

### Test Double
Término genérico para objetos que reemplazan dependencias reales (Mock, Stub, Fake, Spy).

### Test Isolation
Principio de que cada test debe ser independiente y no afectar a otros.

---

## U

### Unit Test
Test que verifica una unidad aislada de código (función, método, clase).

---

## Y

### Yield Fixture
Fixture que usa `yield` para ejecutar código de limpieza después del test.

```python
@pytest.fixture
def db_session():
    session = create_session()
    yield session
    session.rollback()
    session.close()
```
