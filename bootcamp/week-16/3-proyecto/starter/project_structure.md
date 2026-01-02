# 📁 Estructura del Proyecto

Esta es la estructura recomendada para tu proyecto final.

---

## Estructura Completa

```
tu-proyecto/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions pipeline
│
├── src/
│   ├── __init__.py
│   ├── main.py                    # Entry point de la aplicación
│   ├── config.py                  # Configuración con Pydantic Settings
│   ├── database.py                # Conexión y sesión de base de datos
│   │
│   ├── models/                    # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── base.py                # Base declarativa
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│   │
│   ├── schemas/                   # Schemas Pydantic
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── task.py
│   │   ├── auth.py
│   │   └── common.py              # Schemas comunes (paginación, etc.)
│   │
│   ├── repositories/              # Capa de acceso a datos
│   │   ├── __init__.py
│   │   ├── base.py                # Repository base genérico
│   │   ├── user_repository.py
│   │   ├── project_repository.py
│   │   └── task_repository.py
│   │
│   ├── services/                  # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── project_service.py
│   │   ├── task_service.py
│   │   └── auth_service.py
│   │
│   ├── routers/                   # Endpoints de la API
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── projects.py
│   │   ├── tasks.py
│   │   └── health.py
│   │
│   ├── dependencies/              # Dependencies de FastAPI
│   │   ├── __init__.py
│   │   ├── database.py            # get_db
│   │   └── auth.py                # get_current_user, etc.
│   │
│   ├── exceptions/                # Excepciones personalizadas
│   │   ├── __init__.py
│   │   └── http.py
│   │
│   └── utils/                     # Utilidades
│       ├── __init__.py
│       └── security.py            # Hash, JWT, etc.
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Fixtures globales
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_projects.py
│   └── test_tasks.py
│
├── alembic/                       # Migraciones
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── .env.example                   # Variables de entorno template
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── docker-compose.test.yml        # Para tests
├── pyproject.toml
├── uv.lock
├── alembic.ini
└── README.md
```

---

## Descripción de Cada Capa

### `models/` - Modelos SQLAlchemy

Define la estructura de la base de datos.

```python
# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    projects = relationship("Project", back_populates="owner")
    assigned_tasks = relationship("Task", back_populates="assignee")
```

### `schemas/` - Schemas Pydantic

Validación de entrada/salida.

```python
# schemas/user.py
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
```

### `repositories/` - Acceso a Datos

Encapsula queries a la base de datos.

```python
# repositories/user_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.user import User

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_id(self, user_id: int) -> User | None:
        return await self.db.get(User, user_id)
    
    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, user: User) -> User:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
```

### `services/` - Lógica de Negocio

Contiene reglas de negocio y orquesta repositories.

```python
# services/user_service.py
from src.repositories.user_repository import UserRepository
from src.schemas.user import UserCreate, UserResponse
from src.utils.security import hash_password
from src.exceptions.http import ConflictError

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    async def create_user(self, data: UserCreate) -> UserResponse:
        # Verificar si email existe
        existing = await self.repository.get_by_email(data.email)
        if existing:
            raise ConflictError("Email already registered")
        
        # Crear usuario
        user = User(
            email=data.email,
            hashed_password=hash_password(data.password),
            full_name=data.full_name
        )
        user = await self.repository.create(user)
        return UserResponse.model_validate(user)
```

### `routers/` - Endpoints

Define los endpoints de la API.

```python
# routers/users.py
from fastapi import APIRouter, Depends, status
from src.schemas.user import UserCreate, UserResponse
from src.services.user_service import UserService
from src.dependencies.database import get_db
from src.dependencies.auth import get_current_admin

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    service = UserService(UserRepository(db))
    return await service.create_user(data)
```

### `dependencies/` - Inyección de Dependencias

```python
# dependencies/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.utils.security import verify_token
from src.dependencies.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = await db.get(User, payload["sub"])
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user

async def get_current_admin(
    user: User = Depends(get_current_user)
) -> User:
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin required")
    return user
```

---

## Archivos de Configuración

### `pyproject.toml`

```toml
[project]
name = "task-api"
version = "1.0.0"
description = "Task Management API"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.32.0",
    "sqlalchemy[asyncio]>=2.0.0",
    "asyncpg>=0.30.0",
    "pydantic>=2.10.0",
    "pydantic-settings>=2.6.0",
    "python-jose[cryptography]>=3.3.0",
    "passlib[bcrypt]>=1.7.4",
    "python-multipart>=0.0.12",
    "alembic>=1.14.0",
    "httpx>=0.28.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.24.0",
    "pytest-cov>=6.0.0",
    "ruff>=0.8.0",
    "pyright>=1.1.390",
]

[tool.ruff]
target-version = "py312"
line-length = 88

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
```

### `.env.example`

```bash
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/taskdb

# Security
SECRET_KEY=your-secret-key-at-least-32-characters-long
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# App
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO
```

### `.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]
.venv/
.env

# IDE
.vscode/
.idea/

# Testing
.coverage
htmlcov/
.pytest_cache/

# Build
dist/
*.egg-info/

# Logs
*.log
logs/
```
