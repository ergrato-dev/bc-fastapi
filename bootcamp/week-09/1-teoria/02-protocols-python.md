# 🐍 Protocols en Python: Interfaces sin Herencia

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- Entender qué son los Protocols y cuándo usarlos
- Diferenciar Protocol de ABC (Abstract Base Class)
- Implementar interfaces usando Protocol
- Usar `runtime_checkable` para validaciones en tiempo de ejecución

---

## 📋 Contenido

### 1. ¿Qué es un Protocol?

Un **Protocol** es una forma de definir **interfaces estructurales** en Python, introducido en Python 3.8 (PEP 544).

```python
from typing import Protocol

class Drawable(Protocol):
    """Cualquier objeto que tenga un método draw()."""
    
    def draw(self) -> None:
        ...
```

La magia de Protocol es el **duck typing estructural**:

> "Si camina como pato y grazna como pato, es un pato"

```python
# Esta clase NO hereda de Drawable
class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

# Pero ES compatible con Drawable porque tiene draw()
def render(shape: Drawable) -> None:
    shape.draw()

# ✅ Funciona! Circle tiene draw()
render(Circle())
```

---

### 2. Protocol vs ABC (Abstract Base Class)

| Característica | Protocol | ABC |
|----------------|----------|-----|
| **Herencia requerida** | ❌ No | ✅ Sí |
| **Tipo de typing** | Estructural | Nominal |
| **Modificar clases existentes** | ✅ Compatible | ❌ Requiere herencia |
| **Runtime checking** | Con `@runtime_checkable` | Con `isinstance()` |
| **Uso principal** | Interfaces/Ports | Clases base abstractas |

### 2.1 Ejemplo Comparativo

```python
from abc import ABC, abstractmethod
from typing import Protocol

# ========================================
# OPCIÓN 1: ABC (requiere herencia)
# ========================================
class RepositoryABC(ABC):
    @abstractmethod
    async def save(self, entity) -> None:
        pass

# ❌ DEBE heredar explícitamente
class UserRepository(RepositoryABC):
    async def save(self, entity) -> None:
        print("Saving user")


# ========================================
# OPCIÓN 2: Protocol (no requiere herencia)
# ========================================
class RepositoryProtocol(Protocol):
    async def save(self, entity) -> None:
        ...

# ✅ NO necesita heredar, solo implementar el método
class ProductRepository:
    async def save(self, entity) -> None:
        print("Saving product")

# ProductRepository ES compatible con RepositoryProtocol
# aunque no herede de él
```

---

### 3. Definiendo Protocols para Ports

En Ports & Adapters, usamos Protocols para definir los **contratos** que el dominio necesita:

```python
from typing import Protocol
from dataclasses import dataclass
from datetime import datetime

# ========================================
# Entidad de Dominio
# ========================================
@dataclass
class User:
    id: int | None
    email: str
    hashed_password: str
    created_at: datetime | None = None


# ========================================
# Port: Repositorio de Usuarios
# ========================================
class UserRepository(Protocol):
    """
    Port para persistencia de usuarios.
    
    Define las operaciones que el dominio necesita,
    sin especificar la implementación.
    """
    
    async def get_by_id(self, user_id: int) -> User | None:
        """Obtiene usuario por ID."""
        ...
    
    async def get_by_email(self, email: str) -> User | None:
        """Obtiene usuario por email."""
        ...
    
    async def save(self, user: User) -> User:
        """Guarda usuario (crear o actualizar)."""
        ...
    
    async def delete(self, user_id: int) -> bool:
        """Elimina usuario por ID."""
        ...
    
    async def list_all(self, limit: int = 100, offset: int = 0) -> list[User]:
        """Lista usuarios con paginación."""
        ...
```

### 3.1 Port para Servicios Externos

```python
class EmailSender(Protocol):
    """Port para envío de emails."""
    
    async def send(
        self,
        to: str,
        subject: str,
        body: str,
        html: bool = False
    ) -> bool:
        """
        Envía un email.
        
        Args:
            to: Dirección del destinatario
            subject: Asunto del email
            body: Contenido del mensaje
            html: Si el body es HTML
            
        Returns:
            True si se envió correctamente
        """
        ...


class PasswordHasher(Protocol):
    """Port para hashing de contraseñas."""
    
    def hash(self, password: str) -> str:
        """Genera hash de una contraseña."""
        ...
    
    def verify(self, password: str, hashed: str) -> bool:
        """Verifica una contraseña contra su hash."""
        ...
```

---

### 4. Implementando un Adapter

El Adapter implementa los métodos del Protocol **sin heredar**:

```python
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class SQLAlchemyUserRepository:
    """
    Adapter: implementación SQLAlchemy del UserRepository Protocol.
    
    Nota: NO hereda de UserRepository, solo implementa sus métodos.
    """
    
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, user_id: int) -> User | None:
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None
    
    async def get_by_email(self, email: str) -> User | None:
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None
    
    async def save(self, user: User) -> User:
        if user.id is None:
            # Create
            model = UserModel(
                email=user.email,
                hashed_password=user.hashed_password
            )
            self._session.add(model)
        else:
            # Update
            stmt = select(UserModel).where(UserModel.id == user.id)
            result = await self._session.execute(stmt)
            model = result.scalar_one()
            model.email = user.email
            model.hashed_password = user.hashed_password
        
        await self._session.flush()
        return self._to_entity(model)
    
    async def delete(self, user_id: int) -> bool:
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        if model:
            await self._session.delete(model)
            return True
        return False
    
    async def list_all(self, limit: int = 100, offset: int = 0) -> list[User]:
        stmt = select(UserModel).limit(limit).offset(offset)
        result = await self._session.execute(stmt)
        return [self._to_entity(m) for m in result.scalars()]
    
    def _to_entity(self, model: UserModel) -> User:
        return User(
            id=model.id,
            email=model.email,
            hashed_password=model.hashed_password,
            created_at=model.created_at
        )
```

---

### 5. Type Checking con Protocols

El type checker (mypy, pyright) verifica compatibilidad estructural:

```python
def create_user_service(repo: UserRepository) -> UserService:
    """El type checker verifica que repo cumpla el Protocol."""
    return UserService(repo)

# ✅ OK - SQLAlchemyUserRepository tiene todos los métodos
sql_repo = SQLAlchemyUserRepository(session)
service = create_user_service(sql_repo)

# ❌ ERROR - InCompleteRepo no tiene todos los métodos
class IncompleteRepo:
    async def get_by_id(self, user_id: int) -> User | None:
        ...
    # Falta: get_by_email, save, delete, list_all

incomplete = IncompleteRepo()
service = create_user_service(incomplete)  # Type error!
```

---

### 6. Runtime Checkable Protocols

Por defecto, Protocol solo funciona para type checking estático. Para verificar en runtime, usa `@runtime_checkable`:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None:
        ...

# Ahora puedes usar isinstance()
class FileHandler:
    def close(self) -> None:
        print("Closing file")

handler = FileHandler()

if isinstance(handler, Closeable):
    print("Handler es Closeable")  # ✅ Se imprime
    handler.close()
```

### 6.1 Limitaciones de runtime_checkable

```python
@runtime_checkable
class Repository(Protocol):
    async def save(self, entity) -> None:
        ...

class FakeRepo:
    async def save(self, entity) -> None:
        pass

# isinstance() solo verifica que el método EXISTE
# NO verifica la firma completa (parámetros, return type)
print(isinstance(FakeRepo(), Repository))  # True

class BadRepo:
    def save(self):  # Firma diferente!
        pass

# ⚠️ También da True! Solo verifica nombre del método
print(isinstance(BadRepo(), Repository))  # True
```

> **Nota**: Para validación completa de firma, confía en el type checker estático (mypy/pyright).

---

### 7. Protocols Genéricos

Puedes crear Protocols con genéricos para mayor flexibilidad:

```python
from typing import Protocol, TypeVar, Generic

T = TypeVar("T")
ID = TypeVar("ID")

class Repository(Protocol[T, ID]):
    """Protocol genérico para cualquier repositorio."""
    
    async def get_by_id(self, entity_id: ID) -> T | None:
        ...
    
    async def save(self, entity: T) -> T:
        ...
    
    async def delete(self, entity_id: ID) -> bool:
        ...


# Uso específico
class UserRepository(Repository[User, int], Protocol):
    """Especialización para User con ID entero."""
    
    async def get_by_email(self, email: str) -> User | None:
        ...


class ProductRepository(Repository[Product, str], Protocol):
    """Especialización para Product con ID string (SKU)."""
    
    async def get_by_category(self, category: str) -> list[Product]:
        ...
```

---

### 8. Buenas Prácticas con Protocols

#### ✅ DO: Protocols pequeños y enfocados

```python
# ✅ BIEN: Interfaces pequeñas (Interface Segregation)
class Readable(Protocol):
    def read(self) -> bytes:
        ...

class Writable(Protocol):
    def write(self, data: bytes) -> None:
        ...

class ReadWritable(Readable, Writable, Protocol):
    """Combina ambos protocols."""
    pass
```

#### ❌ DON'T: Protocols enormes

```python
# ❌ MAL: Protocol demasiado grande
class GodRepository(Protocol):
    async def get_user(self, id: int) -> User: ...
    async def get_product(self, id: int) -> Product: ...
    async def get_order(self, id: int) -> Order: ...
    async def save_user(self, user: User) -> User: ...
    async def save_product(self, product: Product) -> Product: ...
    # ... 50 métodos más
```

#### ✅ DO: Documentar el contrato

```python
class NotificationSender(Protocol):
    """
    Port para envío de notificaciones.
    
    Implementaciones deben:
    - Ser idempotentes (enviar 2 veces = 1 notificación)
    - Manejar errores internamente (no propagar excepciones de red)
    - Retornar False si el envío falla definitivamente
    """
    
    async def send(self, recipient: str, message: str) -> bool:
        """
        Envía una notificación.
        
        Args:
            recipient: Identificador del destinatario (email, phone, etc.)
            message: Contenido de la notificación
            
        Returns:
            True si se envió/encoló correctamente, False si falló
        """
        ...
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Protocol** | Interface estructural sin herencia obligatoria |
| **Duck Typing** | Compatible si tiene los métodos requeridos |
| **@runtime_checkable** | Permite `isinstance()` en runtime |
| **Protocol genérico** | `Protocol[T]` para tipos parametrizados |
| **ISP** | Protocols pequeños y enfocados |

---

## ✅ Checklist de Verificación

- [ ] Puedo definir un Protocol con métodos tipados
- [ ] Entiendo la diferencia entre Protocol y ABC
- [ ] Sé cuándo usar `@runtime_checkable`
- [ ] Puedo crear Protocols genéricos
- [ ] Aplico Interface Segregation Principle

---

## 🧭 Navegación

| Anterior | Índice | Siguiente |
|:---------|:------:|----------:|
| [01 - Introducción Ports & Adapters](01-introduccion-ports-adapters.md) | [README](../README.md) | [03 - Dependency Inversion Principle](03-dependency-inversion-principle.md) |
