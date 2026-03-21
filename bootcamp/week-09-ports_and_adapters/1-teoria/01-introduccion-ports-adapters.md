# 🔌 Introducción al Patrón Ports & Adapters

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- Comprender el origen y propósito del patrón Ports & Adapters
- Identificar los componentes principales: Ports, Adapters, Dominio
- Entender los beneficios de separar el dominio de la infraestructura
- Reconocer cuándo aplicar este patrón

---

## 📋 Contenido

### 1. El Problema: Acoplamiento con Infraestructura

En arquitecturas tradicionales, el código de negocio suele estar **acoplado** directamente a tecnologías específicas:

```python
# ❌ PROBLEMA: Código de negocio acoplado a SQLAlchemy
class UserService:
    def __init__(self):
        # Dependencia directa de SQLAlchemy
        self.session = SessionLocal()
    
    def create_user(self, email: str, password: str) -> User:
        # Lógica de negocio mezclada con acceso a datos
        user = UserModel(email=email, password=hash_password(password))
        self.session.add(user)
        self.session.commit()
        
        # También envía email directamente
        smtp = smtplib.SMTP("smtp.example.com")
        smtp.send_message(create_welcome_email(email))
        
        return user
```

**¿Qué problemas tiene este código?**

| Problema | Consecuencia |
|----------|--------------|
| **Acoplamiento fuerte** | No puedes cambiar SQLAlchemy sin modificar UserService |
| **Difícil de testear** | Necesitas una DB real y servidor SMTP para tests |
| **Violación de SRP** | UserService hace demasiadas cosas |
| **No reutilizable** | No puedes usar la lógica con otra BD |

---

### 2. La Solución: Ports & Adapters

El patrón **Ports & Adapters** (también conocido como **Arquitectura Hexagonal**) fue propuesto por **Alistair Cockburn** en 2005.

![Diagrama del patrón Ports & Adapters](../0-assets/01-ports-adapters-pattern.svg)

#### 2.1 Conceptos Clave

| Concepto | Descripción | Analogía |
|----------|-------------|----------|
| **Dominio** | Lógica de negocio pura, sin dependencias externas | El "cerebro" de la aplicación |
| **Port** | Interfaz que define un contrato | Un "enchufe" estándar |
| **Adapter** | Implementación concreta de un Port | Un "adaptador de corriente" |

#### 2.2 El Dominio en el Centro

```
          ┌─────────────────────────────────────────────┐
          │                                             │
          │    ┌─────────────────────────────────┐      │
          │    │                                 │      │
    ──────┼────►        DOMINIO / NEGOCIO       │◄─────┼─────
   Adapter│    │     (Lógica pura, sin I/O)     │      │Adapter
          │    │                                 │      │
          │    └─────────────────────────────────┘      │
          │          ▲                     ▲            │
          │          │ Port                │ Port       │
          │          │                     │            │
          │    ┌─────┴─────┐         ┌─────┴─────┐      │
          │    │  Adapter  │         │  Adapter  │      │
          │    │ (SQLAlch) │         │  (SMTP)   │      │
          │    └───────────┘         └───────────┘      │
          │          │                     │            │
          └──────────┼─────────────────────┼────────────┘
                     │                     │
                     ▼                     ▼
                 PostgreSQL           Mail Server
```

---

### 3. Ports: Definiendo Contratos

Un **Port** es una **interfaz** que define qué operaciones necesita el dominio, **sin especificar cómo** se implementan.

```python
from typing import Protocol

# Port para persistencia de usuarios
class UserRepository(Protocol):
    """
    Port: Define el contrato para acceso a usuarios.
    
    El dominio necesita estas operaciones, pero no le importa
    si se implementan con PostgreSQL, MongoDB o un archivo JSON.
    """
    
    async def get_by_id(self, user_id: int) -> User | None:
        """Obtiene un usuario por su ID."""
        ...
    
    async def get_by_email(self, email: str) -> User | None:
        """Obtiene un usuario por su email."""
        ...
    
    async def save(self, user: User) -> User:
        """Guarda un usuario (crear o actualizar)."""
        ...
    
    async def delete(self, user_id: int) -> bool:
        """Elimina un usuario."""
        ...


# Port para envío de notificaciones
class NotificationSender(Protocol):
    """
    Port: Define el contrato para enviar notificaciones.
    
    El dominio solo sabe que puede enviar notificaciones,
    no le importa si es por email, SMS o paloma mensajera.
    """
    
    async def send(
        self,
        recipient: str,
        subject: str,
        message: str
    ) -> bool:
        """Envía una notificación."""
        ...
```

#### 3.1 Características de un buen Port

| Característica | Descripción |
|----------------|-------------|
| **Agnóstico a tecnología** | No menciona SQLAlchemy, SMTP, etc. |
| **Centrado en dominio** | Usa lenguaje del negocio |
| **Mínimo necesario** | Solo operaciones que el dominio requiere |
| **Bien documentado** | Clarifica el contrato esperado |

---

### 4. Adapters: Implementaciones Concretas

Un **Adapter** es una **implementación concreta** de un Port que se conecta con una tecnología específica.

```python
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class SQLAlchemyUserRepository:
    """
    Adapter: Implementación de UserRepository usando SQLAlchemy.
    
    Esta clase "adapta" SQLAlchemy al contrato definido por el Port.
    """
    
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, user_id: int) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None
    
    async def get_by_email(self, email: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None
    
    async def save(self, user: User) -> User:
        model = self._to_model(user)
        self._session.add(model)
        await self._session.flush()
        return self._to_entity(model)
    
    async def delete(self, user_id: int) -> bool:
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        model = result.scalar_one_or_none()
        if model:
            await self._session.delete(model)
            return True
        return False
    
    def _to_entity(self, model: UserModel) -> User:
        """Convierte modelo SQLAlchemy a entidad de dominio."""
        return User(
            id=model.id,
            email=model.email,
            hashed_password=model.hashed_password,
            created_at=model.created_at
        )
    
    def _to_model(self, entity: User) -> UserModel:
        """Convierte entidad de dominio a modelo SQLAlchemy."""
        return UserModel(
            id=entity.id,
            email=entity.email,
            hashed_password=entity.hashed_password,
            created_at=entity.created_at
        )
```

#### 4.1 Múltiples Adapters para el mismo Port

```python
# Adapter para MongoDB
class MongoUserRepository:
    def __init__(self, database: Database):
        self._collection = database["users"]
    
    async def get_by_id(self, user_id: int) -> User | None:
        doc = await self._collection.find_one({"_id": user_id})
        return User(**doc) if doc else None
    
    # ... resto de métodos


# Adapter para testing (in-memory)
class InMemoryUserRepository:
    def __init__(self):
        self._users: dict[int, User] = {}
        self._next_id = 1
    
    async def get_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)
    
    async def save(self, user: User) -> User:
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        self._users[user.id] = user
        return user
    
    # ... resto de métodos
```

---

### 5. El Servicio de Dominio

El servicio de dominio **solo conoce los Ports**, no los Adapters:

```python
class UserService:
    """
    Servicio de dominio que orquesta la lógica de negocio.
    
    Depende SOLO de Ports (abstracciones), no de Adapters (implementaciones).
    """
    
    def __init__(
        self,
        user_repository: UserRepository,       # Port
        notification_sender: NotificationSender  # Port
    ):
        self._user_repo = user_repository
        self._notifier = notification_sender
    
    async def register_user(self, email: str, password: str) -> User:
        """
        Registra un nuevo usuario.
        
        Esta es lógica de negocio PURA:
        - No sabe qué BD se usa
        - No sabe cómo se envían emails
        - Solo orquesta las operaciones
        """
        # Validar que el email no exista
        existing = await self._user_repo.get_by_email(email)
        if existing:
            raise UserAlreadyExistsError(email)
        
        # Crear usuario
        user = User(
            email=email,
            hashed_password=hash_password(password)
        )
        
        # Guardar (¿PostgreSQL? ¿MongoDB? No importa!)
        saved_user = await self._user_repo.save(user)
        
        # Notificar (¿Email? ¿SMS? No importa!)
        await self._notifier.send(
            recipient=email,
            subject="Bienvenido",
            message=f"Tu cuenta ha sido creada exitosamente."
        )
        
        return saved_user
```

---

### 6. Beneficios del Patrón

| Beneficio | Descripción |
|-----------|-------------|
| **Testabilidad** | Puedes testear el dominio con adapters fake/mock |
| **Flexibilidad** | Cambiar de PostgreSQL a MongoDB sin tocar el dominio |
| **Mantenibilidad** | Código de negocio aislado y limpio |
| **Desarrollo paralelo** | Frontend puede usar mocks mientras backend implementa |
| **Onboarding fácil** | Nuevos devs entienden el dominio sin conocer infraestructura |

### 6.1 Testabilidad en Acción

```python
import pytest

@pytest.mark.asyncio
async def test_register_user_success():
    # Arrange - Usamos adapters fake
    user_repo = InMemoryUserRepository()
    notifier = FakeNotificationSender()
    
    service = UserService(
        user_repository=user_repo,
        notification_sender=notifier
    )
    
    # Act
    user = await service.register_user("test@example.com", "password123")
    
    # Assert
    assert user.email == "test@example.com"
    assert user.id is not None
    assert len(notifier.sent_messages) == 1
    assert notifier.sent_messages[0]["recipient"] == "test@example.com"


@pytest.mark.asyncio
async def test_register_user_already_exists():
    # Arrange
    user_repo = InMemoryUserRepository()
    existing_user = User(email="test@example.com", hashed_password="xxx")
    await user_repo.save(existing_user)
    
    service = UserService(
        user_repository=user_repo,
        notification_sender=FakeNotificationSender()
    )
    
    # Act & Assert
    with pytest.raises(UserAlreadyExistsError):
        await service.register_user("test@example.com", "password123")
```

---

### 7. Ports de Entrada vs Salida

Existen dos tipos de Ports:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   DRIVING ADAPTERS          DOMINIO         DRIVEN ADAPTERS │
│   (Entrada)                                 (Salida)        │
│                                                             │
│   ┌──────────┐          ┌──────────┐       ┌──────────┐    │
│   │ REST API │──Port──▶ │ Service  │──Port─▶│ Database │    │
│   └──────────┘          │  Layer   │        └──────────┘    │
│                         └──────────┘                         │
│   ┌──────────┐               │             ┌──────────┐    │
│   │   CLI    │───────────────┘   └────────▶│  Email   │    │
│   └──────────┘                              └──────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Tipo | Descripción | Ejemplos |
|------|-------------|----------|
| **Driving (Entrada)** | Inician acciones en el dominio | REST API, CLI, Tests, WebSockets |
| **Driven (Salida)** | El dominio los usa para efectos externos | DB, Email, APIs externas, Filesystem |

---

### 8. Cuándo Usar Ports & Adapters

#### ✅ Usar cuando:

- La aplicación tiene **múltiples puntos de entrada** (API, CLI, eventos)
- Necesitas **cambiar tecnologías** sin afectar el negocio
- Quieres **tests rápidos** sin infraestructura real
- El proyecto es de **mediano a largo plazo**
- El equipo necesita **trabajar en paralelo**

#### ❌ Evitar cuando:

- Proyecto muy pequeño o prototipo rápido
- No hay expectativa de cambio de tecnología
- El equipo no tiene experiencia con el patrón
- Time-to-market es crítico y no hay tiempo para diseño

---

## 📚 Resumen

| Concepto | Definición |
|----------|------------|
| **Ports & Adapters** | Patrón que aísla el dominio de la infraestructura |
| **Port** | Interfaz/contrato que define operaciones necesarias |
| **Adapter** | Implementación concreta que satisface un Port |
| **Dominio** | Lógica de negocio pura, sin dependencias externas |
| **Driving Port** | Punto de entrada al dominio (API, CLI) |
| **Driven Port** | Servicio que el dominio necesita (DB, Email) |

---

## ✅ Checklist de Verificación

Antes de continuar, verifica que puedes:

- [ ] Explicar qué problema resuelve Ports & Adapters
- [ ] Diferenciar entre Port y Adapter
- [ ] Identificar Driving vs Driven ports
- [ ] Entender por qué el dominio no debe conocer los adapters
- [ ] Reconocer los beneficios de testabilidad

---

## 🔗 Recursos Adicionales

- [Hexagonal Architecture - Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- [Ports and Adapters Pattern](https://herbertograca.com/2017/09/14/ports-adapters-architecture/)
- [Clean Architecture - Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

## 🧭 Navegación

| Anterior | Índice | Siguiente |
|:---------|:------:|----------:|
| - | [README](../README.md) | [02 - Protocols en Python](02-protocols-python.md) |
