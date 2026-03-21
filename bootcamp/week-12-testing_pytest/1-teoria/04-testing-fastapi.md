# 🚀 Testing FastAPI

## 🎯 Objetivos

- Usar TestClient para tests síncronos
- Usar httpx para tests asíncronos
- Testear endpoints con diferentes métodos HTTP
- Override de dependencias para tests
- Testear autenticación y autorización

---

## 📋 TestClient vs httpx

| Característica | TestClient | httpx (AsyncClient) |
|----------------|------------|---------------------|
| Tipo | Síncrono | Asíncrono |
| Uso | Tests simples | Tests async, WebSockets |
| Velocidad | Rápido | Rápido |
| Configuración | Mínima | Requiere pytest-asyncio |

---

## 🔧 TestClient Básico

### Setup Mínimo

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

### Con Context Manager

```python
def test_with_context_manager():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
```

---

## 📡 Testear Métodos HTTP

### GET

```python
def test_get_items():
    """Test GET /items/"""
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item_by_id():
    """Test GET /items/{id}"""
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_get_item_not_found():
    """Test GET /items/{id} - 404"""
    response = client.get("/items/99999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
```

### GET con Query Parameters

```python
def test_get_items_with_pagination():
    """Test GET /items/?skip=0&limit=10"""
    response = client.get("/items/", params={"skip": 0, "limit": 10})
    assert response.status_code == 200
    assert len(response.json()) <= 10


def test_get_items_with_filter():
    """Test GET /items/?category=electronics"""
    response = client.get("/items/", params={"category": "electronics"})
    assert response.status_code == 200
    for item in response.json():
        assert item["category"] == "electronics"
```

### POST

```python
def test_create_item():
    """Test POST /items/"""
    new_item = {
        "name": "Test Item",
        "price": 29.99,
        "description": "A test item"
    }
    response = client.post("/items/", json=new_item)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == new_item["name"]
    assert data["price"] == new_item["price"]
    assert "id" in data


def test_create_item_invalid_data():
    """Test POST /items/ - Validation error"""
    invalid_item = {
        "name": "",  # Nombre vacío
        "price": -10  # Precio negativo
    }
    response = client.post("/items/", json=invalid_item)
    assert response.status_code == 422  # Validation Error
```

### PUT

```python
def test_update_item():
    """Test PUT /items/{id}"""
    update_data = {
        "name": "Updated Item",
        "price": 39.99
    }
    response = client.put("/items/1", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Item"
    assert data["price"] == 39.99


def test_update_item_partial():
    """Test PATCH /items/{id}"""
    response = client.patch("/items/1", json={"price": 49.99})
    assert response.status_code == 200
    assert response.json()["price"] == 49.99
```

### DELETE

```python
def test_delete_item():
    """Test DELETE /items/{id}"""
    # Primero crear
    response = client.post("/items/", json={"name": "To Delete", "price": 10})
    item_id = response.json()["id"]
    
    # Luego eliminar
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204  # No Content
    
    # Verificar que no existe
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404
```

---

## 🔐 Testear Autenticación

### Endpoint de Login

```python
def test_login_success():
    """Test POST /auth/token"""
    response = client.post(
        "/auth/token",
        data={
            "username": "test@example.com",
            "password": "correctpassword"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials():
    """Test POST /auth/token - Wrong password"""
    response = client.post(
        "/auth/token",
        data={
            "username": "test@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401
```

### Endpoints Protegidos

```python
def test_protected_endpoint_without_token():
    """Test acceso sin autenticación."""
    response = client.get("/users/me")
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]


def test_protected_endpoint_with_valid_token(auth_token):
    """Test acceso con token válido."""
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert "email" in response.json()


def test_protected_endpoint_with_expired_token():
    """Test con token expirado."""
    expired_token = create_test_token(expire_minutes=-1)
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {expired_token}"}
    )
    assert response.status_code == 401


def test_admin_only_endpoint_as_user(user_token):
    """Test endpoint admin con usuario normal."""
    response = client.delete(
        "/admin/users/1",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 403
```

### Fixture para Token

```python
# tests/conftest.py
import pytest
from src.auth import create_access_token


@pytest.fixture
def auth_token(test_user):
    """Token de autenticación para tests."""
    return create_access_token(
        data={"sub": test_user.email, "role": test_user.role}
    )


@pytest.fixture
def admin_token(admin_user):
    """Token de admin para tests."""
    return create_access_token(
        data={"sub": admin_user.email, "role": "admin"}
    )
```

---

## 🔄 Override de Dependencias

### Reemplazar Base de Datos

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.database import Base, get_db


# Base de datos en memoria para tests
TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="function")
def db_session():
    """Sesión de BD de prueba."""
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    
    TestingSession = sessionmaker(bind=engine)
    session = TestingSession()
    
    yield session
    
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """TestClient con BD override."""
    def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as c:
        yield c
    
    app.dependency_overrides.clear()
```

### Reemplazar Servicios Externos

```python
# src/dependencies.py
async def get_email_service():
    return RealEmailService()


# tests/conftest.py
@pytest.fixture
def client_with_mock_email(db_session):
    """Cliente con servicio de email mockeado."""
    
    class MockEmailService:
        sent_emails = []
        
        async def send(self, to: str, subject: str, body: str):
            self.sent_emails.append({"to": to, "subject": subject})
            return True
    
    mock_service = MockEmailService()
    
    app.dependency_overrides[get_db] = lambda: db_session
    app.dependency_overrides[get_email_service] = lambda: mock_service
    
    with TestClient(app) as c:
        c.mock_email_service = mock_service  # Acceso al mock
        yield c
    
    app.dependency_overrides.clear()


def test_registration_sends_email(client_with_mock_email):
    response = client_with_mock_email.post(
        "/auth/register",
        json={"email": "new@example.com", "password": "pass123"}
    )
    assert response.status_code == 201
    
    # Verificar que se envió email
    sent = client_with_mock_email.mock_email_service.sent_emails
    assert len(sent) == 1
    assert sent[0]["to"] == "new@example.com"
```

---

## ⚡ Tests Asíncronos con httpx

### Setup con pytest-asyncio

```python
# tests/test_async_api.py
import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest.fixture
async def async_client(db_session):
    """Cliente asíncrono para tests."""
    from src.database import get_db
    
    def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
    
    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_get_items_async(async_client):
    """Test asíncrono de GET /items/"""
    response = await async_client.get("/items/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_item_async(async_client):
    """Test asíncrono de POST /items/"""
    response = await async_client.post(
        "/items/",
        json={"name": "Async Item", "price": 19.99}
    )
    assert response.status_code == 201
```

### Configuración en pyproject.toml

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
```

---

## 📤 Testear File Uploads

```python
from io import BytesIO


def test_upload_file():
    """Test POST /files/upload"""
    # Crear archivo en memoria
    file_content = b"Hello, this is test content"
    files = {
        "file": ("test.txt", BytesIO(file_content), "text/plain")
    }
    
    response = client.post("/files/upload", files=files)
    assert response.status_code == 201
    assert response.json()["filename"] == "test.txt"


def test_upload_image():
    """Test upload de imagen."""
    # Crear imagen PNG mínima (1x1 pixel)
    png_header = b'\x89PNG\r\n\x1a\n'
    files = {
        "image": ("test.png", BytesIO(png_header), "image/png")
    }
    
    response = client.post("/files/upload-image", files=files)
    assert response.status_code == 201


def test_upload_invalid_file_type():
    """Test con tipo de archivo no permitido."""
    files = {
        "file": ("malware.exe", BytesIO(b"bad content"), "application/exe")
    }
    
    response = client.post("/files/upload", files=files)
    assert response.status_code == 400
```

---

## 🎭 Testear Responses

### Headers

```python
def test_response_headers():
    """Verificar headers de respuesta."""
    response = client.get("/items/")
    
    assert response.headers["content-type"] == "application/json"
    assert "x-request-id" in response.headers


def test_cors_headers():
    """Verificar CORS headers."""
    response = client.options(
        "/items/",
        headers={"Origin": "http://localhost:3000"}
    )
    
    assert "access-control-allow-origin" in response.headers
```

### Cookies

```python
def test_login_sets_cookie():
    """Verificar que login establece cookie."""
    response = client.post(
        "/auth/login",
        data={"username": "user@test.com", "password": "pass"}
    )
    
    assert "session" in response.cookies
    assert response.cookies["session"] is not None


def test_request_with_cookie():
    """Test con cookie."""
    client.cookies.set("session", "test-session-value")
    response = client.get("/users/me")
    assert response.status_code == 200
```

### Redirect

```python
def test_redirect():
    """Test de redirección."""
    response = client.get("/old-path", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/new-path"


def test_follow_redirect():
    """Test siguiendo redirección."""
    response = client.get("/old-path", follow_redirects=True)
    assert response.status_code == 200
```

---

## 📊 Fixture Completa de FastAPI

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.database import Base, get_db
from src.models import User
from src.auth import get_password_hash, create_access_token


TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="session")
def engine():
    """Engine compartido para toda la sesión."""
    return create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )


@pytest.fixture(scope="function")
def tables(engine):
    """Crear/destruir tablas para cada test."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session(engine, tables):
    """Sesión de BD para cada test."""
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope="function")
def client(db_session):
    """TestClient configurado."""
    app.dependency_overrides[get_db] = lambda: db_session
    
    with TestClient(app) as c:
        yield c
    
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(db_session):
    """Usuario de prueba en BD."""
    user = User(
        email="test@example.com",
        hashed_password=get_password_hash("testpassword"),
        is_active=True,
        role="user"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def auth_headers(test_user):
    """Headers con token de autenticación."""
    token = create_access_token({"sub": test_user.email})
    return {"Authorization": f"Bearer {token}"}
```

---

## ✅ Checklist de Tests de API

- [ ] Tests para cada método HTTP (GET, POST, PUT, DELETE)
- [ ] Tests de casos exitosos (happy path)
- [ ] Tests de errores de validación (422)
- [ ] Tests de recursos no encontrados (404)
- [ ] Tests de autenticación (401)
- [ ] Tests de autorización (403)
- [ ] Tests con diferentes roles de usuario
- [ ] Tests de paginación y filtros

---

## 🔗 Próximo Tema

→ [05-mocking-y-patching.md](05-mocking-y-patching.md) - Mocking y patching de dependencias
