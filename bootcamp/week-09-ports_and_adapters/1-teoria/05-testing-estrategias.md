# 🧪 Estrategias de Testing con Ports & Adapters

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- Testear servicios de dominio usando fake adapters
- Crear fake adapters efectivos para testing
- Aplicar el patrón Spy para verificar interacciones
- Organizar tests por tipo (unit, integration)

---

## 📋 Contenido

### 1. Ventajas de Ports & Adapters para Testing

```
┌─────────────────────────────────────────────────────────────┐
│                    TESTING TRADICIONAL                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   UserService ──────► SQLAlchemy ──────► PostgreSQL         │
│        │                                      │             │
│        │              Tests lentos            │             │
│        │              Requieren BD            │             │
│        └──────────────────────────────────────┘             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    TESTING CON PORTS                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   UserService ──────► UserRepository (Protocol)             │
│        │                     │                              │
│        │                     ├─► SQLAlchemy (Producción)    │
│        │                     │                              │
│        │                     └─► FakeRepo (Testing)         │
│        │                              │                     │
│        │              Tests rápidos   │                     │
│        │              Sin BD          │                     │
│        └──────────────────────────────┘                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Métrica | Sin Ports | Con Ports |
|---------|-----------|-----------|
| Velocidad | ~100ms/test | ~1ms/test |
| Dependencias | BD, APIs, SMTP | Ninguna |
| Paralelización | Difícil | Trivial |
| Flakiness | Alta | Mínima |

---

### 2. Fake Adapters vs Mocks

#### 2.1 Fake Adapter (Recomendado)

Un **Fake** es una implementación simplificada pero funcional:

```python
# tests/fakes/fake_user_repository.py
from domain.entities import User
from domain.ports import UserRepository


class FakeUserRepository:
    """
    Fake: implementación in-memory del repositorio.
    
    Comportamiento real pero sin persistencia.
    """
    
    def __init__(self):
        self._users: dict[int, User] = {}
        self._email_index: dict[str, int] = {}
        self._next_id = 1
    
    async def get_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)
    
    async def get_by_email(self, email: str) -> User | None:
        user_id = self._email_index.get(email)
        return self._users.get(user_id) if user_id else None
    
    async def save(self, user: User) -> User:
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        
        self._users[user.id] = user
        self._email_index[user.email] = user.id
        return user
    
    async def delete(self, user_id: int) -> bool:
        user = self._users.pop(user_id, None)
        if user:
            self._email_index.pop(user.email, None)
            return True
        return False
    
    async def list_all(self, limit: int = 100, offset: int = 0) -> list[User]:
        users = list(self._users.values())
        return users[offset:offset + limit]
    
    # Métodos de ayuda para tests
    
    def add_user(self, user: User) -> User:
        """Agrega usuario directamente (setup de tests)."""
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        self._users[user.id] = user
        self._email_index[user.email] = user.id
        return user
    
    def clear(self) -> None:
        """Limpia todos los datos."""
        self._users.clear()
        self._email_index.clear()
        self._next_id = 1
```

#### 2.2 Mock (unittest.mock)

Un **Mock** registra llamadas pero no tiene comportamiento:

```python
from unittest.mock import AsyncMock, MagicMock

# ❌ Menos recomendado: Mock genérico
mock_repo = AsyncMock(spec=UserRepository)
mock_repo.get_by_email.return_value = None
mock_repo.save.return_value = User(id=1, email="test@test.com")
```

#### 2.3 ¿Cuándo usar cada uno?

| Situación | Usar |
|-----------|------|
| Tests de lógica de negocio | Fake |
| Verificar llamadas específicas | Mock/Spy |
| Tests de integración | Real adapter |
| Comportamiento complejo | Fake |
| Setup rápido | Mock |

---

### 3. Testing de Servicios

#### 3.1 Estructura de Test

```python
# tests/unit/test_user_service.py
import pytest
from datetime import datetime

from domain.entities import User
from application.services import UserService
from application.exceptions import UserAlreadyExistsError
from tests.fakes import FakeUserRepository, FakeNotificationSender


class TestUserService:
    """Tests para UserService usando fakes."""
    
    @pytest.fixture
    def user_repo(self):
        """Fake repository para cada test."""
        return FakeUserRepository()
    
    @pytest.fixture
    def notifier(self):
        """Fake notifier para cada test."""
        return FakeNotificationSender()
    
    @pytest.fixture
    def service(self, user_repo, notifier):
        """Service con dependencias fake."""
        return UserService(
            user_repository=user_repo,
            notification_sender=notifier
        )
    
    # =========================================
    # Tests de registro de usuario
    # =========================================
    
    @pytest.mark.asyncio
    async def test_register_user_success(self, service, user_repo, notifier):
        """Usuario nuevo se registra correctamente."""
        # Act
        user = await service.register_user(
            email="new@example.com",
            password="securepassword123"
        )
        
        # Assert - Usuario creado
        assert user.id is not None
        assert user.email == "new@example.com"
        assert user.hashed_password != "securepassword123"  # Hasheado
        
        # Assert - Guardado en repo
        saved = await user_repo.get_by_id(user.id)
        assert saved is not None
        assert saved.email == "new@example.com"
        
        # Assert - Notificación enviada
        assert len(notifier.sent_notifications) == 1
        assert notifier.sent_notifications[0]["recipient"] == "new@example.com"
    
    @pytest.mark.asyncio
    async def test_register_user_duplicate_email(self, service, user_repo):
        """Error al registrar email duplicado."""
        # Arrange - Usuario existente
        existing = User(
            email="existing@example.com",
            hashed_password="xxx"
        )
        user_repo.add_user(existing)
        
        # Act & Assert
        with pytest.raises(UserAlreadyExistsError) as exc:
            await service.register_user(
                email="existing@example.com",
                password="password123"
            )
        
        assert "existing@example.com" in str(exc.value)
    
    @pytest.mark.asyncio
    async def test_register_user_notification_failure(
        self, service, user_repo, notifier
    ):
        """Usuario se crea aunque falle la notificación."""
        # Arrange - Notifier falla
        notifier.should_fail = True
        
        # Act
        user = await service.register_user(
            email="test@example.com",
            password="password123"
        )
        
        # Assert - Usuario creado de todas formas
        assert user.id is not None
        saved = await user_repo.get_by_id(user.id)
        assert saved is not None
    
    # =========================================
    # Tests de obtención de usuario
    # =========================================
    
    @pytest.mark.asyncio
    async def test_get_user_found(self, service, user_repo):
        """Obtiene usuario existente."""
        # Arrange
        existing = User(
            email="user@example.com",
            hashed_password="xxx"
        )
        user_repo.add_user(existing)
        
        # Act
        result = await service.get_user(existing.id)
        
        # Assert
        assert result is not None
        assert result.email == "user@example.com"
    
    @pytest.mark.asyncio
    async def test_get_user_not_found(self, service):
        """Retorna None para usuario inexistente."""
        result = await service.get_user(99999)
        assert result is None
```

---

### 4. Patrón Spy

Un **Spy** es un fake que además registra interacciones:

```python
# tests/fakes/spy_notification_sender.py
from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol

from domain.ports import NotificationSender, NotificationChannel


@dataclass
class NotificationCall:
    """Registro de una llamada a send()."""
    recipient: str
    message: str
    subject: str | None
    timestamp: datetime
    result: bool


class SpyNotificationSender:
    """
    Spy: fake que registra todas las interacciones.
    
    Útil para verificar:
    - Cuántas veces se llamó
    - Con qué argumentos
    - En qué orden
    """
    
    def __init__(self):
        self.calls: list[NotificationCall] = []
        self.should_fail: bool = False
        self._channel = NotificationChannel.EMAIL
    
    @property
    def channel(self) -> NotificationChannel:
        return self._channel
    
    async def send(
        self,
        recipient: str,
        message: str,
        subject: str | None = None
    ) -> bool:
        result = not self.should_fail
        
        # Registrar la llamada
        self.calls.append(NotificationCall(
            recipient=recipient,
            message=message,
            subject=subject,
            timestamp=datetime.now(),
            result=result
        ))
        
        return result
    
    # Métodos de verificación
    
    def was_called(self) -> bool:
        """Verifica si se llamó al menos una vez."""
        return len(self.calls) > 0
    
    def call_count(self) -> int:
        """Número total de llamadas."""
        return len(self.calls)
    
    def was_called_with(self, recipient: str) -> bool:
        """Verifica si se llamó con este recipient."""
        return any(c.recipient == recipient for c in self.calls)
    
    def get_calls_to(self, recipient: str) -> list[NotificationCall]:
        """Obtiene todas las llamadas a un recipient."""
        return [c for c in self.calls if c.recipient == recipient]
    
    def last_call(self) -> NotificationCall | None:
        """Última llamada realizada."""
        return self.calls[-1] if self.calls else None
    
    def reset(self) -> None:
        """Limpia historial de llamadas."""
        self.calls.clear()
```

#### 4.1 Uso del Spy en Tests

```python
@pytest.mark.asyncio
async def test_bulk_notification(service):
    """Verifica envío a múltiples usuarios."""
    # Arrange
    spy = SpyNotificationSender()
    service = NotificationService(sender=spy)
    
    users = ["user1@test.com", "user2@test.com", "user3@test.com"]
    
    # Act
    await service.notify_users(users, "Hello everyone!")
    
    # Assert con Spy
    assert spy.call_count() == 3
    assert spy.was_called_with("user1@test.com")
    assert spy.was_called_with("user2@test.com")
    assert spy.was_called_with("user3@test.com")
    
    # Verificar contenido
    for call in spy.calls:
        assert call.message == "Hello everyone!"
        assert call.result is True
```

---

### 5. Testing de Adapters (Integración)

Los adapters reales se testean con integración:

```python
# tests/integration/test_sqlalchemy_user_repository.py
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from domain.entities import User
from infrastructure.adapters import SQLAlchemyUserRepository
from infrastructure.models import Base


class TestSQLAlchemyUserRepository:
    """Tests de integración para el adapter real."""
    
    @pytest.fixture
    async def engine(self):
        """Engine SQLite in-memory."""
        engine = create_async_engine(
            "sqlite+aiosqlite:///:memory:",
            echo=False
        )
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        
        yield engine
        
        await engine.dispose()
    
    @pytest.fixture
    async def session(self, engine):
        """Sesión para cada test."""
        async_session = sessionmaker(
            engine, 
            class_=AsyncSession,
            expire_on_commit=False
        )
        async with async_session() as session:
            yield session
            await session.rollback()
    
    @pytest.fixture
    def repository(self, session):
        """Repository con sesión real."""
        return SQLAlchemyUserRepository(session)
    
    @pytest.mark.asyncio
    async def test_save_and_get_user(self, repository, session):
        """Guarda y recupera usuario de BD real."""
        # Arrange
        user = User(
            email="test@example.com",
            hashed_password="hashed123"
        )
        
        # Act - Save
        saved = await repository.save(user)
        await session.commit()
        
        # Act - Get
        retrieved = await repository.get_by_id(saved.id)
        
        # Assert
        assert retrieved is not None
        assert retrieved.id == saved.id
        assert retrieved.email == "test@example.com"
    
    @pytest.mark.asyncio
    async def test_get_by_email(self, repository, session):
        """Busca usuario por email."""
        # Arrange
        user = User(email="find@me.com", hashed_password="xxx")
        await repository.save(user)
        await session.commit()
        
        # Act
        found = await repository.get_by_email("find@me.com")
        
        # Assert
        assert found is not None
        assert found.email == "find@me.com"
```

---

### 6. Organización de Tests

```
tests/
├── conftest.py               # Fixtures globales
├── fakes/
│   ├── __init__.py
│   ├── fake_user_repository.py
│   ├── fake_notification_sender.py
│   └── spy_notification_sender.py
├── unit/
│   ├── __init__.py
│   ├── test_user_service.py
│   └── test_notification_service.py
└── integration/
    ├── __init__.py
    ├── test_sqlalchemy_user_repository.py
    └── test_api.py
```

#### conftest.py

```python
# tests/conftest.py
import pytest
from tests.fakes import FakeUserRepository, FakeNotificationSender


@pytest.fixture
def fake_user_repo():
    """Fake repository disponible globalmente."""
    return FakeUserRepository()


@pytest.fixture
def fake_notifier():
    """Fake notifier disponible globalmente."""
    return FakeNotificationSender()
```

---

### 7. Pirámide de Tests

```
          ▲
         /│\         E2E Tests
        / │ \        (Pocos, lentos)
       /  │  \
      /───┼───\
     /    │    \     Integration Tests
    /     │     \    (Adapters, API)
   /──────┼──────\
  /       │       \  Unit Tests
 /        │        \ (Services con fakes)
/─────────┴─────────\
         BASE        (Muchos, rápidos)
```

| Tipo | Qué testea | Dependencias | Cantidad |
|------|------------|--------------|----------|
| Unit | Services, Domain | Fakes | 70% |
| Integration | Adapters, API | BD, Redis | 20% |
| E2E | Sistema completo | Todo | 10% |

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Fake** | Implementación simplificada funcional |
| **Mock** | Objeto que registra llamadas |
| **Spy** | Fake + registro de interacciones |
| **Unit test** | Testea servicio con fakes |
| **Integration test** | Testea adapter con infra real |

---

## ✅ Checklist de Verificación

- [ ] Tengo fakes para todos mis Protocols
- [ ] Los tests unitarios no requieren BD
- [ ] Uso Spy cuando necesito verificar interacciones
- [ ] Los tests de integración usan BD in-memory
- [ ] Mi pirámide tiene más unit tests que integration

---

## 🧭 Navegación

| Anterior | Índice | Siguiente |
|:---------|:------:|----------:|
| [04 - Implementando Adapters](04-implementando-adapters.md) | [README](../README.md) | [Práctica 01](../2-practicas/01-definir-ports/) |
