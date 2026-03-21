# 🧪 Fundamentos de Testing

## 🎯 Objetivos

- Entender por qué es importante testear código
- Conocer la pirámide de testing
- Diferenciar tipos de tests
- Comprender el concepto de Test-Driven Development (TDD)

---

## 📋 ¿Por Qué Testear?

### Sin Tests vs Con Tests

```
Sin Tests:
┌─────────────┐
│   Código    │ → Funciona... ¿o no? 🤷
│   nuevo     │ → Rompe algo existente? 🤷
│             │ → Refactorizar? 😰
└─────────────┘

Con Tests:
┌─────────────┐    ┌─────────────┐
│   Código    │ → │    Tests    │ → ✅ Confianza
│   nuevo     │    │  verdes     │ → ✅ Documentación
│             │    │             │ → ✅ Refactoring seguro
└─────────────┘    └─────────────┘
```

### Beneficios Concretos

1. **Confianza**: Saber que el código funciona correctamente
2. **Documentación viva**: Los tests muestran cómo usar el código
3. **Refactoring seguro**: Cambiar código sin miedo a romper funcionalidad
4. **Detección temprana**: Encontrar bugs antes de producción
5. **Diseño mejorado**: Código testeable suele ser código bien diseñado

---

## 🔺 Pirámide de Testing

![Pirámide de Testing](../0-assets/01-testing-pyramid.svg)

```
                    ┌───────┐
                   /   E2E   \        ← Pocos, lentos, costosos
                  /───────────\
                 /  Integración \     ← Cantidad media
                /─────────────────\
               /     Unitarios      \  ← Muchos, rápidos, baratos
              └─────────────────────┘
```

### Características por Nivel

| Nivel | Cantidad | Velocidad | Costo | Confianza |
|-------|----------|-----------|-------|-----------|
| **Unitarios** | Muchos (70%) | Muy rápidos | Bajo | Código aislado |
| **Integración** | Medios (20%) | Medios | Medio | Componentes juntos |
| **E2E** | Pocos (10%) | Lentos | Alto | Sistema completo |

---

## 🧩 Tipos de Tests

### 1. Tests Unitarios

Prueban una **unidad de código aislada** (función, método, clase).

```python
# Código a testear
def calculate_discount(price: float, percentage: float) -> float:
    """Calcula el precio con descuento."""
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100")
    return price * (1 - percentage / 100)


# Test unitario
def test_calculate_discount_20_percent():
    result = calculate_discount(100.0, 20.0)
    assert result == 80.0


def test_calculate_discount_invalid_percentage():
    import pytest
    with pytest.raises(ValueError):
        calculate_discount(100.0, 150.0)
```

**Características:**
- ✅ Rápidos (milisegundos)
- ✅ Sin dependencias externas (DB, red, filesystem)
- ✅ Fáciles de escribir y mantener
- ✅ Gran cantidad

### 2. Tests de Integración

Prueban la **interacción entre componentes**.

```python
# Test de integración: API + Base de datos
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.database import Base, get_db


@pytest.fixture
def client(db_session):
    """Cliente con base de datos de prueba."""
    def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_create_and_get_user(client):
    # Crear usuario
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "name": "Test"}
    )
    assert response.status_code == 201
    user_id = response.json()["id"]
    
    # Obtener usuario creado
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
```

**Características:**
- ⏱️ Más lentos que unitarios
- 🔗 Requieren setup (DB, servicios)
- 🎯 Prueban flujos reales
- 📊 Cantidad media

### 3. Tests End-to-End (E2E)

Prueban el **sistema completo** como lo usaría un usuario.

```python
# Test E2E: Flujo completo de registro y login
def test_user_registration_and_login_flow(client):
    # 1. Registrar usuario
    register_response = client.post(
        "/auth/register",
        json={
            "email": "newuser@example.com",
            "password": "securepassword123",
            "full_name": "New User"
        }
    )
    assert register_response.status_code == 201
    
    # 2. Login con credenciales
    login_response = client.post(
        "/auth/token",
        data={
            "username": "newuser@example.com",
            "password": "securepassword123"
        }
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # 3. Acceder a recurso protegido
    me_response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert me_response.status_code == 200
    assert me_response.json()["email"] == "newuser@example.com"
```

**Características:**
- 🐢 Los más lentos
- 🔧 Requieren entorno completo
- 👤 Simulan usuario real
- 📉 Pocos pero valiosos

---

## 🔄 Test-Driven Development (TDD)

### El Ciclo Red-Green-Refactor

```
    ┌─────────────────────────────────────┐
    │                                     │
    ▼                                     │
┌───────┐     ┌───────┐     ┌──────────┐  │
│  RED  │ ──▶ │ GREEN │ ──▶ │ REFACTOR │──┘
│       │     │       │     │          │
│ Test  │     │ Código│     │ Mejorar  │
│ falla │     │mínimo │     │ código   │
└───────┘     └───────┘     └──────────┘
```

### Ejemplo Práctico de TDD

**Paso 1: RED** - Escribir test que falla

```python
# tests/test_calculator.py
def test_add_two_numbers():
    from src.calculator import add
    result = add(2, 3)
    assert result == 5
```

```bash
$ pytest tests/test_calculator.py
# ❌ FAILED - ModuleNotFoundError: No module named 'src.calculator'
```

**Paso 2: GREEN** - Código mínimo para pasar

```python
# src/calculator.py
def add(a: int, b: int) -> int:
    return a + b
```

```bash
$ pytest tests/test_calculator.py
# ✅ PASSED
```

**Paso 3: REFACTOR** - Mejorar sin romper tests

```python
# src/calculator.py (mejorado con validación)
def add(a: int | float, b: int | float) -> int | float:
    """
    Suma dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        
    Returns:
        La suma de a y b
    """
    return a + b
```

```bash
$ pytest tests/test_calculator.py
# ✅ PASSED (el test sigue pasando)
```

---

## 📝 Anatomía de un Buen Test

### Patrón AAA (Arrange-Act-Assert)

```python
def test_user_can_update_their_name():
    # Arrange (Preparar)
    user = User(name="Original Name", email="user@example.com")
    db_session.add(user)
    db_session.commit()
    
    # Act (Actuar)
    user.name = "New Name"
    db_session.commit()
    
    # Assert (Verificar)
    updated_user = db_session.query(User).filter_by(email="user@example.com").first()
    assert updated_user.name == "New Name"
```

### Patrón Given-When-Then (BDD)

```python
def test_authenticated_user_can_access_profile():
    # Given: Un usuario autenticado
    token = create_access_token({"sub": "user@example.com"})
    headers = {"Authorization": f"Bearer {token}"}
    
    # When: Accede a su perfil
    response = client.get("/users/me", headers=headers)
    
    # Then: Obtiene sus datos correctamente
    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"
```

---

## ✅ Buenas Prácticas

### Naming de Tests

```python
# ❌ Mal: Nombres poco descriptivos
def test_user():
    pass

def test_1():
    pass

# ✅ Bien: Nombres que describen comportamiento
def test_user_with_valid_email_can_register():
    pass

def test_user_with_duplicate_email_gets_400_error():
    pass

def test_inactive_user_cannot_login():
    pass
```

### Un Assert por Test (idealmente)

```python
# ❌ Mal: Múltiples conceptos en un test
def test_user_crud():
    user = create_user(...)
    assert user.id is not None
    
    updated = update_user(user.id, ...)
    assert updated.name == "new name"
    
    delete_user(user.id)
    assert get_user(user.id) is None


# ✅ Bien: Tests separados y enfocados
def test_create_user_assigns_id():
    user = create_user(...)
    assert user.id is not None

def test_update_user_changes_name():
    user = create_user(...)
    updated = update_user(user.id, name="new name")
    assert updated.name == "new name"

def test_delete_user_removes_from_database():
    user = create_user(...)
    delete_user(user.id)
    assert get_user(user.id) is None
```

### Tests Independientes

```python
# ❌ Mal: Tests que dependen de otros
class TestUserWorkflow:
    created_user_id = None  # Estado compartido 😱
    
    def test_1_create_user(self):
        user = create_user(...)
        TestUserWorkflow.created_user_id = user.id
    
    def test_2_update_user(self):
        # Falla si test_1 no corrió primero
        update_user(TestUserWorkflow.created_user_id, ...)


# ✅ Bien: Cada test es independiente
def test_create_user(db_session):
    user = create_user(...)
    assert user.id is not None

def test_update_user(db_session, test_user):  # Fixture proporciona usuario
    updated = update_user(test_user.id, ...)
    assert updated.name == "new name"
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Test Unitario** | Prueba una unidad aislada, rápido |
| **Test de Integración** | Prueba componentes juntos |
| **Test E2E** | Prueba sistema completo |
| **TDD** | Escribir test antes del código |
| **AAA** | Arrange-Act-Assert |
| **Pirámide** | Muchos unitarios, pocos E2E |

---

## 🔗 Próximo Tema

→ [02-pytest-basico.md](02-pytest-basico.md) - Configuración e instalación de pytest
