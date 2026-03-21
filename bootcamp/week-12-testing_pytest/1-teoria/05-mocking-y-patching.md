# 🎭 Mocking y Patching

## 🎯 Objetivos

- Entender cuándo y por qué usar mocks
- Dominar unittest.mock (Mock, MagicMock, patch)
- Mockear servicios externos y dependencias
- Usar pytest-mock para simplificar mocking

---

## 📋 ¿Por Qué Mockear?

### El Problema

```python
# Sin mock - problemas reales
def test_send_welcome_email():
    user = create_user("new@example.com")
    send_welcome_email(user)  # 😱 ¡Envía email real!
    # - Lento (conexión SMTP)
    # - Requiere servidor de email
    # - Envía spam a usuarios
    # - Falla sin internet
```

### La Solución

```python
# Con mock - aislado y rápido
def test_send_welcome_email(mocker):
    mock_smtp = mocker.patch("src.email.smtplib.SMTP")
    
    user = create_user("new@example.com")
    send_welcome_email(user)
    
    # Verificar que se llamó correctamente
    mock_smtp.return_value.send_message.assert_called_once()
```

---

## 🎯 Cuándo Mockear

| Mockear ✅ | No Mockear ❌ |
|-----------|---------------|
| APIs externas | Lógica de negocio propia |
| Base de datos (en unit tests) | Funciones puras |
| Servicios de email | Validaciones |
| Sistemas de archivos | Cálculos |
| Time/datetime | Código que estás testeando |
| Servicios de pago | Pydantic models |

---

## 🔧 unittest.mock Básico

### Mock

```python
from unittest.mock import Mock


def test_mock_basic():
    # Crear mock
    mock_service = Mock()
    
    # Configurar retorno
    mock_service.get_user.return_value = {"id": 1, "name": "John"}
    
    # Usar el mock
    result = mock_service.get_user(user_id=1)
    
    # Verificar llamada
    mock_service.get_user.assert_called_once_with(user_id=1)
    
    # Verificar resultado
    assert result["name"] == "John"
```

### MagicMock

```python
from unittest.mock import MagicMock


def test_magic_mock():
    # MagicMock soporta métodos mágicos
    mock_list = MagicMock()
    
    # Configurar __len__
    mock_list.__len__.return_value = 5
    assert len(mock_list) == 5
    
    # Configurar __getitem__
    mock_list.__getitem__.return_value = "item"
    assert mock_list[0] == "item"
    
    # Context manager
    mock_file = MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.read.return_value = "file content"
    
    with mock_file as f:
        content = f.read()
    
    assert content == "file content"
```

### Configurar Retornos

```python
from unittest.mock import Mock


def test_return_value():
    mock = Mock()
    
    # Retorno simple
    mock.get_name.return_value = "Alice"
    assert mock.get_name() == "Alice"
    
    # Retorno diferente por llamada
    mock.get_number.side_effect = [1, 2, 3]
    assert mock.get_number() == 1
    assert mock.get_number() == 2
    assert mock.get_number() == 3
    
    # Lanzar excepción
    mock.dangerous.side_effect = ValueError("Error!")
    with pytest.raises(ValueError):
        mock.dangerous()
    
    # Función personalizada
    def custom_response(x):
        return x * 2
    
    mock.double.side_effect = custom_response
    assert mock.double(5) == 10
```

---

## 🔄 patch()

### Patch como Decorador

```python
from unittest.mock import patch


# src/services.py
import requests

def get_external_data():
    response = requests.get("https://api.example.com/data")
    return response.json()


# tests/test_services.py
@patch("src.services.requests.get")
def test_get_external_data(mock_get):
    # Configurar mock
    mock_response = Mock()
    mock_response.json.return_value = {"key": "value"}
    mock_get.return_value = mock_response
    
    # Ejecutar
    result = get_external_data()
    
    # Verificar
    assert result == {"key": "value"}
    mock_get.assert_called_once_with("https://api.example.com/data")
```

### Patch como Context Manager

```python
def test_with_context_manager():
    with patch("src.services.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"data": [1, 2, 3]}
        
        result = get_external_data()
        
        assert result["data"] == [1, 2, 3]
```

### Múltiples Patches

```python
@patch("src.services.requests.get")
@patch("src.services.cache.set")
@patch("src.services.logger.info")
def test_multiple_patches(mock_logger, mock_cache, mock_get):
    # ⚠️ Orden inverso: el más cercano al def es el primero
    mock_get.return_value.json.return_value = {"id": 1}
    
    result = fetch_and_cache_data()
    
    mock_get.assert_called_once()
    mock_cache.assert_called_once()
    mock_logger.assert_called()
```

---

## 🎯 patch.object()

Mockear un método específico de un objeto:

```python
from unittest.mock import patch


class UserService:
    def get_user(self, user_id: int):
        # Llamada real a la BD
        return db.query(User).get(user_id)
    
    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        if user:
            db.delete(user)


def test_delete_user():
    service = UserService()
    
    with patch.object(service, "get_user") as mock_get:
        mock_get.return_value = User(id=1, name="Test")
        
        service.delete_user(1)
        
        mock_get.assert_called_once_with(1)
```

---

## ⏰ Mockear Tiempo

### datetime

```python
from unittest.mock import patch
from datetime import datetime


def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    return "Good evening"


@patch("src.greetings.datetime")
def test_morning_greeting(mock_datetime):
    mock_datetime.now.return_value = datetime(2024, 1, 1, 9, 0, 0)
    
    assert get_greeting() == "Good morning"


@patch("src.greetings.datetime")
def test_evening_greeting(mock_datetime):
    mock_datetime.now.return_value = datetime(2024, 1, 1, 20, 0, 0)
    
    assert get_greeting() == "Good evening"
```

### freezegun (Librería recomendada)

```python
from freezegun import freeze_time


@freeze_time("2024-01-15 09:30:00")
def test_morning_with_freezegun():
    assert get_greeting() == "Good morning"


@freeze_time("2024-01-15 20:00:00")
def test_evening_with_freezegun():
    assert get_greeting() == "Good evening"
```

---

## 📧 Mockear Servicios Externos

### Servicio de Email

```python
# src/notifications.py
import smtplib
from email.mime.text import MIMEText


class EmailService:
    def __init__(self, smtp_host: str, smtp_port: int):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
    
    def send(self, to: str, subject: str, body: str) -> bool:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["To"] = to
        
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
            server.send_message(msg)
        
        return True


# tests/test_notifications.py
@patch("src.notifications.smtplib.SMTP")
def test_send_email(mock_smtp):
    # Configurar mock
    mock_server = MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_server
    
    # Ejecutar
    service = EmailService("smtp.test.com", 587)
    result = service.send("user@test.com", "Test", "Body")
    
    # Verificar
    assert result is True
    mock_smtp.assert_called_once_with("smtp.test.com", 587)
    mock_server.send_message.assert_called_once()
```

### API Externa con httpx

```python
# src/weather.py
import httpx


async def get_weather(city: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.weather.com/v1/current",
            params={"city": city}
        )
        return response.json()


# tests/test_weather.py
import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
@patch("src.weather.httpx.AsyncClient")
async def test_get_weather(mock_client_class):
    # Configurar mock async
    mock_response = AsyncMock()
    mock_response.json.return_value = {"temp": 25, "city": "Madrid"}
    
    mock_client = AsyncMock()
    mock_client.get.return_value = mock_response
    mock_client_class.return_value.__aenter__.return_value = mock_client
    
    # Ejecutar
    result = await get_weather("Madrid")
    
    # Verificar
    assert result["temp"] == 25
    mock_client.get.assert_called_once()
```

### Con respx (Recomendado para httpx)

```python
import respx
import httpx
import pytest


@pytest.mark.asyncio
@respx.mock
async def test_get_weather_with_respx():
    # Configurar mock de URL
    respx.get("https://api.weather.com/v1/current").mock(
        return_value=httpx.Response(
            200,
            json={"temp": 25, "city": "Madrid"}
        )
    )
    
    result = await get_weather("Madrid")
    
    assert result["temp"] == 25
```

---

## 🧪 pytest-mock

Simplifica el mocking con fixtures:

```python
# Con pytest-mock
def test_with_mocker(mocker):
    # Más limpio que @patch
    mock_get = mocker.patch("src.services.requests.get")
    mock_get.return_value.json.return_value = {"data": "test"}
    
    result = get_external_data()
    
    assert result["data"] == "test"


def test_spy(mocker):
    # Spy: llama al real pero permite verificar llamadas
    spy_print = mocker.spy(builtins, "print")
    
    print("Hello")
    print("World")
    
    assert spy_print.call_count == 2


def test_stub(mocker):
    # Stub: reemplaza sin verificar
    mocker.patch("os.remove")  # No hace nada
    
    import os
    os.remove("fake_file.txt")  # No falla
```

---

## 🎯 Assertions de Mock

### Verificar Llamadas

```python
def test_mock_assertions():
    mock = Mock()
    
    # Hacer llamadas
    mock.method("arg1", key="value")
    mock.method("arg2")
    
    # Verificar que se llamó
    mock.method.assert_called()
    
    # Verificar última llamada
    mock.method.assert_called_with("arg2")
    
    # Verificar alguna llamada específica
    mock.method.assert_any_call("arg1", key="value")
    
    # Verificar número de llamadas
    assert mock.method.call_count == 2
    
    # Verificar todas las llamadas
    from unittest.mock import call
    mock.method.assert_has_calls([
        call("arg1", key="value"),
        call("arg2")
    ])
```

### Verificar No Llamado

```python
def test_not_called():
    mock = Mock()
    
    # No llamar el método
    result = some_function_that_might_call_mock(condition=False)
    
    mock.dangerous_method.assert_not_called()
```

---

## 🗄️ Mockear Base de Datos

### Override de Dependencia FastAPI

```python
# tests/conftest.py
import pytest
from unittest.mock import MagicMock

from src.database import get_db


@pytest.fixture
def mock_db():
    """Mock de sesión de BD."""
    db = MagicMock()
    
    # Configurar comportamientos
    db.query.return_value.filter.return_value.first.return_value = None
    db.add = MagicMock()
    db.commit = MagicMock()
    db.refresh = MagicMock()
    
    return db


@pytest.fixture
def client(mock_db):
    from src.main import app
    from fastapi.testclient import TestClient
    
    app.dependency_overrides[get_db] = lambda: mock_db
    
    with TestClient(app) as c:
        yield c
    
    app.dependency_overrides.clear()
```

### Configurar Retornos de Query

```python
def test_get_user_not_found(client, mock_db):
    # Configurar: usuario no existe
    mock_db.query.return_value.filter.return_value.first.return_value = None
    
    response = client.get("/users/999")
    
    assert response.status_code == 404


def test_get_user_found(client, mock_db):
    # Configurar: usuario existe
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.email = "test@example.com"
    mock_db.query.return_value.filter.return_value.first.return_value = mock_user
    
    response = client.get("/users/1")
    
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
```

---

## ⚡ AsyncMock

Para código asíncrono:

```python
from unittest.mock import AsyncMock
import pytest


@pytest.mark.asyncio
async def test_async_service():
    # Crear mock asíncrono
    mock_service = AsyncMock()
    mock_service.fetch_data.return_value = {"result": "success"}
    
    # Usar await
    result = await mock_service.fetch_data()
    
    assert result["result"] == "success"
    mock_service.fetch_data.assert_awaited_once()


@pytest.mark.asyncio
async def test_async_side_effect():
    mock = AsyncMock()
    
    # Side effects para async
    mock.get_items.side_effect = [
        [{"id": 1}],
        [{"id": 2}],
    ]
    
    first = await mock.get_items()
    second = await mock.get_items()
    
    assert first[0]["id"] == 1
    assert second[0]["id"] == 2
```

---

## ✅ Buenas Prácticas

### ✅ Hacer

```python
# Mock solo lo externo
@patch("src.service.external_api.call")
def test_service(mock_api):
    mock_api.return_value = {"data": "test"}
    result = my_service.process()  # Testea la lógica real
    assert result == expected

# Verificar interacciones importantes
def test_user_creation(mocker):
    mock_email = mocker.patch("src.email.send")
    
    create_user("test@example.com")
    
    mock_email.assert_called_once_with(
        to="test@example.com",
        subject="Welcome!"
    )
```

### ❌ Evitar

```python
# No mockear lo que estás testeando
@patch("src.calculator.add")  # ❌ ¡Estás testeando add!
def test_add(mock_add):
    mock_add.return_value = 5
    assert add(2, 3) == 5  # No testea nada real

# No sobre-mockear
def test_over_mocked(mocker):
    mocker.patch("src.module.function1")
    mocker.patch("src.module.function2")
    mocker.patch("src.module.function3")
    mocker.patch("src.module.function4")
    # Si mockeas todo, no testeas nada
```

---

## 📚 Resumen

| Herramienta | Uso |
|-------------|-----|
| `Mock()` | Mock básico |
| `MagicMock()` | Mock con métodos mágicos |
| `AsyncMock()` | Mock para async/await |
| `patch()` | Reemplazar imports |
| `patch.object()` | Reemplazar atributo de objeto |
| `mocker` (pytest-mock) | Fixture para mocking |
| `respx` | Mock de httpx |

---

## 🔗 Recursos Adicionales

- [unittest.mock docs](https://docs.python.org/3/library/unittest.mock.html)
- [pytest-mock](https://pytest-mock.readthedocs.io/)
- [respx](https://lundberg.github.io/respx/)
