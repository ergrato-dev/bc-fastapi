# 🧪 Proyecto Semana 12: API con Testing Completo

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplo Genérico de Referencia

> Los ejemplos usan **"Warehouse"** (Almacén) que NO está en el pool.
> **Debes adaptar TODO a tu dominio asignado.**

| Concepto | Ejemplo Genérico | Adapta a tu Dominio |
|----------|-----------------|---------------------|
| Entity Under Test | `Item` | `{YourEntity}` |
| Service Under Test | `ItemService` | `{YourEntity}Service` |
| Fixtures | `sample_item`, `item_factory` | `sample_{entity}`, `{entity}_factory` |

---

## 🎯 Objetivo

Implementar **Testing completo**:

- Unit tests para servicios
- Integration tests para endpoints
- Fixtures y factories
- Cobertura mínima del 80%

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Configuración de Pytest

```python
# Ejemplo genérico - conftest.py
import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from main import app
from database import Base, get_session

# Base de datos de testing (SQLite en memoria)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest.fixture
async def test_engine():
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest.fixture
async def test_session(test_engine):
    async with AsyncSession(test_engine) as session:
        yield session

@pytest.fixture
async def client(test_session):
    async def override_get_session():
        yield test_session
    
    app.dependency_overrides[get_session] = override_get_session
    
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client
    
    app.dependency_overrides.clear()
```

### Factories para Datos de Prueba

```python
# Ejemplo genérico - tests/factories.py
from dataclasses import dataclass, field
from typing import Callable
import random
import string

@dataclass
class ItemFactory:
    """Factory para crear Items de prueba"""
    sku: str = field(default_factory=lambda: f"WH-{random.randint(1000, 9999)}")
    name: str = field(default_factory=lambda: f"Item {random.choice(['Alpha', 'Beta', 'Gamma'])}")
    quantity: int = field(default_factory=lambda: random.randint(1, 100))
    zone_id: int = 1
    
    def build(self) -> dict:
        """Retorna dict para crear via API"""
        return {
            "sku": self.sku,
            "name": self.name,
            "quantity": self.quantity,
            "zone_id": self.zone_id
        }
    
    def build_model(self) -> Item:
        """Retorna modelo para insertar en DB"""
        return Item(**self.build())

# Fixtures usando factories
@pytest.fixture
def item_factory():
    return ItemFactory

@pytest.fixture
async def sample_item(test_session, item_factory):
    item = item_factory().build_model()
    test_session.add(item)
    await test_session.commit()
    await test_session.refresh(item)
    return item
```

### Unit Tests para Services

```python
# Ejemplo genérico - tests/unit/test_item_service.py
import pytest
from unittest.mock import AsyncMock, MagicMock
from services.item_service import ItemService
from domain.entities import Item

class TestItemService:
    """Tests unitarios para ItemService"""
    
    @pytest.fixture
    def mock_repository(self):
        return AsyncMock()
    
    @pytest.fixture
    def service(self, mock_repository):
        return ItemService(repository=mock_repository)
    
    @pytest.mark.asyncio
    async def test_get_by_sku_returns_item(self, service, mock_repository):
        # Arrange
        expected_item = Item(id=1, sku="WH-1234", name="Test", quantity=10, zone_id=1)
        mock_repository.find_by_sku.return_value = expected_item
        
        # Act
        result = await service.get_by_sku("WH-1234")
        
        # Assert
        assert result == expected_item
        mock_repository.find_by_sku.assert_called_once_with("WH-1234")
    
    @pytest.mark.asyncio
    async def test_get_by_sku_returns_none_when_not_found(self, service, mock_repository):
        # Arrange
        mock_repository.find_by_sku.return_value = None
        
        # Act
        result = await service.get_by_sku("INVALID")
        
        # Assert
        assert result is None
    
    @pytest.mark.asyncio
    async def test_create_item_validates_sku_unique(self, service, mock_repository):
        # Arrange
        mock_repository.find_by_sku.return_value = Item(id=1, sku="WH-1234", ...)
        
        # Act & Assert
        with pytest.raises(DuplicateSKUError):
            await service.create(ItemCreate(sku="WH-1234", ...))
    
    @pytest.mark.asyncio
    async def test_transfer_reduces_source_quantity(self, service, mock_repository):
        # Arrange
        source = Item(id=1, sku="WH-1234", quantity=50, zone_id=1)
        mock_repository.find_by_id.return_value = source
        
        # Act
        await service.transfer(item_id=1, target_zone_id=2, quantity=20)
        
        # Assert
        assert source.quantity == 30
```

### Integration Tests para Endpoints

```python
# Ejemplo genérico - tests/integration/test_items_api.py
import pytest
from httpx import AsyncClient

class TestItemsAPI:
    """Tests de integración para endpoints de Items"""
    
    @pytest.mark.asyncio
    async def test_create_item_returns_201(self, client: AsyncClient, auth_headers):
        # Arrange
        payload = {
            "sku": "WH-9999",
            "name": "New Item",
            "quantity": 50,
            "zone_id": 1
        }
        
        # Act
        response = await client.post("/items/", json=payload, headers=auth_headers)
        
        # Assert
        assert response.status_code == 201
        data = response.json()
        assert data["sku"] == "WH-9999"
        assert "id" in data
    
    @pytest.mark.asyncio
    async def test_create_item_duplicate_sku_returns_409(
        self, client: AsyncClient, sample_item, auth_headers
    ):
        # Arrange
        payload = {"sku": sample_item.sku, "name": "Dup", "quantity": 1, "zone_id": 1}
        
        # Act
        response = await client.post("/items/", json=payload, headers=auth_headers)
        
        # Assert
        assert response.status_code == 409
    
    @pytest.mark.asyncio
    async def test_get_items_returns_paginated_list(
        self, client: AsyncClient, sample_item, auth_headers
    ):
        # Act
        response = await client.get("/items/", headers=auth_headers)
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert "total" in data
        assert "page" in data
    
    @pytest.mark.asyncio
    async def test_get_item_not_found_returns_404(self, client: AsyncClient, auth_headers):
        # Act
        response = await client.get("/items/99999", headers=auth_headers)
        
        # Assert
        assert response.status_code == 404
    
    @pytest.mark.asyncio
    async def test_unauthorized_request_returns_401(self, client: AsyncClient):
        # Act (sin headers de auth)
        response = await client.get("/items/")
        
        # Assert
        assert response.status_code == 401
```

### Fixtures de Autenticación

```python
# Ejemplo genérico - tests/conftest.py (continuación)
@pytest.fixture
async def test_user(test_session):
    user = User(
        email="test@warehouse.com",
        hashed_password=hash_password("testpass"),
        role=Role.OPERATOR
    )
    test_session.add(user)
    await test_session.commit()
    return user

@pytest.fixture
async def auth_headers(test_user, jwt_service):
    token = jwt_service.create_access_token(test_user.id, test_user.role)
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
async def admin_headers(test_session, jwt_service):
    admin = User(email="admin@warehouse.com", ..., role=Role.ADMIN)
    test_session.add(admin)
    await test_session.commit()
    token = jwt_service.create_access_token(admin.id, admin.role)
    return {"Authorization": f"Bearer {token}"}
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── services/
├── routers/
├── tests/
│   ├── conftest.py          # Fixtures globales
│   ├── factories.py         # Factories de datos
│   ├── unit/
│   │   ├── test_item_service.py
│   │   └── test_validators.py
│   └── integration/
│       ├── test_items_api.py
│       └── test_auth_api.py
├── pytest.ini
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Unit tests funcionan | 15 |
| Integration tests funcionan | 15 |
| Cobertura >= 80% | 10 |
| **Adaptación al Dominio** (35%) | |
| Tests relevantes al negocio | 12 |
| Factories específicas | 13 |
| Originalidad (no copia ejemplo) | 10 |
| **Calidad del Código** (25%) | |
| Tests bien organizados | 10 |
| Fixtures reutilizables | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No copies** los tests de "Item/ItemService"
- ✅ **Diseña** tests específicos de tu dominio
- ✅ **Crea** factories para tus entidades

---

## 📚 Recursos

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/)
- [HTTPX Testing](https://www.python-httpx.org/async/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
