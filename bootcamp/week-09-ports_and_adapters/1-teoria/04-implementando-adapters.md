# 🔧 Implementando Adapters

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- Crear adapters que implementan Protocols correctamente
- Manejar configuración y conexiones en adapters
- Implementar mappers entre entidades y modelos de infraestructura
- Organizar adapters en una estructura de proyecto clara

---

## 📋 Contenido

### 1. Anatomía de un Adapter

Un **Adapter** tiene tres responsabilidades principales:

```
┌─────────────────────────────────────────────────────┐
│                    ADAPTER                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. RECIBIR configuración/conexiones                │
│     └─> Constructor con dependencias externas       │
│                                                     │
│  2. IMPLEMENTAR el Protocol                         │
│     └─> Todos los métodos definidos                 │
│                                                     │
│  3. TRADUCIR entre dominio e infraestructura        │
│     └─> Mappers entidad ↔ modelo                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### 2. Adapter de Persistencia (Repository)

#### 2.1 El Protocol (Port)

```python
# domain/ports/user_repository.py
from typing import Protocol
from domain.entities import User

class UserRepository(Protocol):
    """Port para persistencia de usuarios."""
    
    async def get_by_id(self, user_id: int) -> User | None:
        ...
    
    async def get_by_email(self, email: str) -> User | None:
        ...
    
    async def save(self, user: User) -> User:
        ...
    
    async def delete(self, user_id: int) -> bool:
        ...
    
    async def list_all(
        self, 
        limit: int = 100, 
        offset: int = 0
    ) -> list[User]:
        ...
```

#### 2.2 El Adapter (Implementación SQLAlchemy)

```python
# infrastructure/adapters/sqlalchemy_user_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete as sql_delete
from sqlalchemy.exc import IntegrityError

from domain.entities import User
from infrastructure.models import UserModel


class SQLAlchemyUserRepository:
    """
    Adapter: implementación SQLAlchemy de UserRepository.
    
    Responsabilidades:
    1. Gestionar la sesión de BD
    2. Traducir entre User (entidad) y UserModel (ORM)
    3. Ejecutar queries SQLAlchemy
    """
    
    def __init__(self, session: AsyncSession):
        """
        Constructor recibe dependencias externas.
        
        Args:
            session: Sesión async de SQLAlchemy (inyectada)
        """
        self._session = session
    
    # =========================================
    # Implementación del Protocol
    # =========================================
    
    async def get_by_id(self, user_id: int) -> User | None:
        """Obtiene usuario por ID."""
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None
    
    async def get_by_email(self, email: str) -> User | None:
        """Obtiene usuario por email."""
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None
    
    async def save(self, user: User) -> User:
        """
        Guarda usuario (insert o update).
        
        Si user.id es None, crea nuevo registro.
        Si user.id existe, actualiza el registro.
        """
        if user.id is None:
            return await self._create(user)
        return await self._update(user)
    
    async def delete(self, user_id: int) -> bool:
        """Elimina usuario por ID."""
        stmt = sql_delete(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(stmt)
        return result.rowcount > 0
    
    async def list_all(
        self,
        limit: int = 100,
        offset: int = 0
    ) -> list[User]:
        """Lista usuarios con paginación."""
        stmt = (
            select(UserModel)
            .order_by(UserModel.id)
            .limit(limit)
            .offset(offset)
        )
        result = await self._session.execute(stmt)
        return [self._to_entity(m) for m in result.scalars()]
    
    # =========================================
    # Métodos privados de ayuda
    # =========================================
    
    async def _create(self, user: User) -> User:
        """Crea nuevo usuario en BD."""
        model = self._to_model(user)
        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(model)
        return self._to_entity(model)
    
    async def _update(self, user: User) -> User:
        """Actualiza usuario existente."""
        stmt = select(UserModel).where(UserModel.id == user.id)
        result = await self._session.execute(stmt)
        model = result.scalar_one()
        
        # Actualizar campos
        model.email = user.email
        model.hashed_password = user.hashed_password
        model.is_active = user.is_active
        
        await self._session.flush()
        return self._to_entity(model)
    
    # =========================================
    # Mappers: Traducción entidad ↔ modelo
    # =========================================
    
    def _to_entity(self, model: UserModel) -> User:
        """Convierte modelo ORM a entidad de dominio."""
        return User(
            id=model.id,
            email=model.email,
            hashed_password=model.hashed_password,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
    
    def _to_model(self, entity: User) -> UserModel:
        """Convierte entidad de dominio a modelo ORM."""
        return UserModel(
            id=entity.id,
            email=entity.email,
            hashed_password=entity.hashed_password,
            is_active=entity.is_active
        )
```

---

### 3. Adapter de Servicio Externo

#### 3.1 El Protocol

```python
# domain/ports/notification_sender.py
from typing import Protocol
from enum import Enum

class NotificationChannel(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"

class NotificationSender(Protocol):
    """Port para envío de notificaciones."""
    
    @property
    def channel(self) -> NotificationChannel:
        """Canal de notificación que implementa."""
        ...
    
    async def send(
        self,
        recipient: str,
        message: str,
        subject: str | None = None
    ) -> bool:
        """
        Envía una notificación.
        
        Returns:
            True si se envió correctamente
        """
        ...
```

#### 3.2 Adapter de Email

```python
# infrastructure/adapters/email_adapter.py
import aiosmtplib
from email.message import EmailMessage
import logging

from domain.ports.notification_sender import NotificationSender, NotificationChannel
from infrastructure.config import SMTPConfig

logger = logging.getLogger(__name__)


class EmailAdapter:
    """
    Adapter para envío de emails via SMTP.
    
    Implementa NotificationSender Protocol.
    """
    
    def __init__(self, config: SMTPConfig):
        """
        Args:
            config: Configuración SMTP (host, port, user, password)
        """
        self._config = config
    
    @property
    def channel(self) -> NotificationChannel:
        return NotificationChannel.EMAIL
    
    async def send(
        self,
        recipient: str,
        message: str,
        subject: str | None = None
    ) -> bool:
        """Envía email via SMTP."""
        try:
            email = self._build_message(recipient, message, subject)
            
            await aiosmtplib.send(
                email,
                hostname=self._config.host,
                port=self._config.port,
                username=self._config.username,
                password=self._config.password,
                use_tls=self._config.use_tls
            )
            
            logger.info(f"Email enviado a {recipient}")
            return True
            
        except aiosmtplib.SMTPException as e:
            logger.error(f"Error enviando email a {recipient}: {e}")
            return False
    
    def _build_message(
        self,
        recipient: str,
        body: str,
        subject: str | None
    ) -> EmailMessage:
        """Construye el mensaje de email."""
        msg = EmailMessage()
        msg["From"] = self._config.from_address
        msg["To"] = recipient
        msg["Subject"] = subject or "Notificación"
        msg.set_content(body)
        return msg
```

#### 3.3 Adapter de SMS

```python
# infrastructure/adapters/sms_adapter.py
import httpx
import logging

from domain.ports.notification_sender import NotificationSender, NotificationChannel
from infrastructure.config import TwilioConfig

logger = logging.getLogger(__name__)


class SMSAdapter:
    """
    Adapter para envío de SMS via Twilio.
    
    Implementa NotificationSender Protocol.
    """
    
    def __init__(self, config: TwilioConfig):
        self._config = config
        self._base_url = f"https://api.twilio.com/2010-04-01/Accounts/{config.account_sid}/Messages.json"
    
    @property
    def channel(self) -> NotificationChannel:
        return NotificationChannel.SMS
    
    async def send(
        self,
        recipient: str,
        message: str,
        subject: str | None = None  # SMS no usa subject
    ) -> bool:
        """Envía SMS via Twilio API."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self._base_url,
                    auth=(self._config.account_sid, self._config.auth_token),
                    data={
                        "To": recipient,
                        "From": self._config.from_number,
                        "Body": message[:160]  # SMS límite
                    }
                )
                
                if response.status_code == 201:
                    logger.info(f"SMS enviado a {recipient}")
                    return True
                else:
                    logger.error(f"Error Twilio: {response.text}")
                    return False
                    
        except httpx.HTTPError as e:
            logger.error(f"Error enviando SMS a {recipient}: {e}")
            return False
```

---

### 4. Adapter para Testing (Fake)

```python
# infrastructure/adapters/fake_notification_sender.py
from domain.ports.notification_sender import NotificationSender, NotificationChannel


class FakeNotificationSender:
    """
    Fake adapter para testing.
    
    No envía notificaciones reales, solo registra las llamadas.
    """
    
    def __init__(self, channel: NotificationChannel = NotificationChannel.EMAIL):
        self._channel = channel
        self.sent_notifications: list[dict] = []
        self.should_fail: bool = False
    
    @property
    def channel(self) -> NotificationChannel:
        return self._channel
    
    async def send(
        self,
        recipient: str,
        message: str,
        subject: str | None = None
    ) -> bool:
        """Simula envío, registra en memoria."""
        if self.should_fail:
            return False
        
        self.sent_notifications.append({
            "recipient": recipient,
            "message": message,
            "subject": subject,
            "channel": self._channel.value
        })
        return True
    
    # Métodos de ayuda para tests
    
    def reset(self) -> None:
        """Limpia historial de notificaciones."""
        self.sent_notifications.clear()
        self.should_fail = False
    
    def get_last_notification(self) -> dict | None:
        """Retorna última notificación enviada."""
        return self.sent_notifications[-1] if self.sent_notifications else None
    
    def count_sent_to(self, recipient: str) -> int:
        """Cuenta notificaciones a un destinatario."""
        return sum(
            1 for n in self.sent_notifications 
            if n["recipient"] == recipient
        )
```

---

### 5. Patrón de Configuración

#### 5.1 Configuración Tipada

```python
# infrastructure/config.py
from pydantic_settings import BaseSettings
from pydantic import Field


class SMTPConfig(BaseSettings):
    """Configuración para servidor SMTP."""
    
    host: str = Field(default="localhost")
    port: int = Field(default=587)
    username: str = Field(default="")
    password: str = Field(default="")
    from_address: str = Field(default="noreply@example.com")
    use_tls: bool = Field(default=True)
    
    model_config = {"env_prefix": "SMTP_"}


class TwilioConfig(BaseSettings):
    """Configuración para Twilio SMS."""
    
    account_sid: str = Field(default="")
    auth_token: str = Field(default="")
    from_number: str = Field(default="")
    
    model_config = {"env_prefix": "TWILIO_"}


class DatabaseConfig(BaseSettings):
    """Configuración de base de datos."""
    
    url: str = Field(default="sqlite+aiosqlite:///./app.db")
    echo: bool = Field(default=False)
    pool_size: int = Field(default=5)
    
    model_config = {"env_prefix": "DB_"}


class Settings(BaseSettings):
    """Configuración principal de la aplicación."""
    
    env: str = Field(default="development")
    debug: bool = Field(default=False)
    
    # Sub-configuraciones
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    smtp: SMTPConfig = Field(default_factory=SMTPConfig)
    twilio: TwilioConfig = Field(default_factory=TwilioConfig)


settings = Settings()
```

#### 5.2 Factory con Configuración

```python
# infrastructure/factories.py
from domain.ports.notification_sender import NotificationSender
from infrastructure.adapters.email_adapter import EmailAdapter
from infrastructure.adapters.sms_adapter import SMSAdapter
from infrastructure.adapters.fake_notification_sender import FakeNotificationSender
from infrastructure.config import settings


def create_email_sender() -> NotificationSender:
    """Factory para crear email adapter."""
    if settings.env == "test":
        return FakeNotificationSender()
    return EmailAdapter(settings.smtp)


def create_sms_sender() -> NotificationSender:
    """Factory para crear SMS adapter."""
    if settings.env == "test":
        return FakeNotificationSender()
    return SMSAdapter(settings.twilio)
```

---

### 6. Estructura de Proyecto

```
src/
├── domain/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   └── user.py              # Entidades de dominio
│   └── ports/
│       ├── __init__.py
│       ├── user_repository.py    # Protocol
│       └── notification_sender.py # Protocol
│
├── application/
│   ├── __init__.py
│   └── services/
│       ├── __init__.py
│       └── user_service.py       # Usa Protocols
│
└── infrastructure/
    ├── __init__.py
    ├── config.py                 # Configuraciones
    ├── factories.py              # Factories de adapters
    ├── models/
    │   ├── __init__.py
    │   └── user_model.py         # Modelos SQLAlchemy
    └── adapters/
        ├── __init__.py
        ├── sqlalchemy_user_repository.py
        ├── email_adapter.py
        ├── sms_adapter.py
        └── fake_notification_sender.py
```

---

### 7. Mappers Externos (Opcional)

Para adapters complejos, puedes extraer los mappers:

```python
# infrastructure/mappers/user_mapper.py
from domain.entities import User
from infrastructure.models import UserModel


class UserMapper:
    """Mapper para conversión User ↔ UserModel."""
    
    @staticmethod
    def to_entity(model: UserModel) -> User:
        """Modelo ORM → Entidad de dominio."""
        return User(
            id=model.id,
            email=model.email,
            hashed_password=model.hashed_password,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
    
    @staticmethod
    def to_model(entity: User) -> UserModel:
        """Entidad de dominio → Modelo ORM."""
        return UserModel(
            id=entity.id,
            email=entity.email,
            hashed_password=entity.hashed_password,
            is_active=entity.is_active
        )
    
    @staticmethod
    def update_model(model: UserModel, entity: User) -> None:
        """Actualiza modelo existente con datos de entidad."""
        model.email = entity.email
        model.hashed_password = entity.hashed_password
        model.is_active = entity.is_active


# Uso en el adapter
class SQLAlchemyUserRepository:
    def __init__(self, session: AsyncSession):
        self._session = session
        self._mapper = UserMapper()
    
    async def get_by_id(self, user_id: int) -> User | None:
        # ...
        return self._mapper.to_entity(model) if model else None
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Adapter** | Implementación concreta de un Protocol |
| **Constructor** | Recibe dependencias externas (session, config) |
| **Mapper** | Traduce entre entidad de dominio y modelo de infra |
| **Fake Adapter** | Implementación para testing sin I/O real |
| **Factory** | Crea adapters con configuración correcta |

---

## ✅ Checklist de Verificación

- [ ] Mis adapters no heredan del Protocol
- [ ] El constructor recibe todas las dependencias
- [ ] Tengo mappers para traducir entidad ↔ modelo
- [ ] Tengo fake adapters para testing
- [ ] La configuración está externalizada

---

## 🧭 Navegación

| Anterior | Índice | Siguiente |
|:---------|:------:|----------:|
| [03 - Dependency Inversion](03-dependency-inversion-principle.md) | [README](../README.md) | [05 - Testing Estrategias](05-testing-estrategias.md) |
