# 📦 Versiones del Stack - BC FastAPI Bootcamp

Este documento define las versiones oficiales de todas las tecnologías usadas en el bootcamp.

> ⚠️ **IMPORTANTE**: Siempre usar las versiones especificadas para evitar incompatibilidades.

## 🐍 Lenguaje y Runtime

| Tecnología | Versión Mínima | Versión Recomendada | Notas |
|------------|----------------|---------------------|-------|
| Python | 3.12 | **3.13** | Última estable |
| Docker | 27.0 | **27.4+** | Container runtime |
| Docker Compose | 2.30 | **2.31+** | Plugin v2 |

## 🚀 Framework y Librerías Core

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| `fastapi` | **0.115+** | Framework web |
| `uvicorn[standard]` | **0.34+** | Servidor ASGI |
| `pydantic` | **2.10+** | Validación de datos |
| `pydantic-settings` | **2.7+** | Configuración |

## 🗄️ Base de Datos

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| `sqlalchemy` | **2.0+** | ORM (sync y async) |
| `alembic` | **1.14+** | Migraciones |
| `aiosqlite` | **0.20+** | SQLite async |
| `asyncpg` | **0.30+** | PostgreSQL async |

### Motores de BD

| Motor | Versión | Uso |
|-------|---------|-----|
| SQLite | 3.47+ | Desarrollo y testing |
| PostgreSQL | **17+** | Producción |

## 🔐 Seguridad

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| `python-jose[cryptography]` | **3.3+** | JWT tokens |
| `passlib[bcrypt]` | **1.7+** | Hash de contraseñas |
| `python-multipart` | **0.0.18+** | Form data |

## 🧪 Testing

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| `pytest` | **8.3+** | Framework de testing |
| `pytest-asyncio` | **0.24+** | Tests async |
| `httpx` | **0.28+** | Cliente HTTP para tests |
| `pytest-cov` | **6.0+** | Coverage |

## 🛠️ Herramientas de Desarrollo

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| `uv` | **0.5+** | Gestor de paquetes |
| `ruff` | **0.8+** | Linter + Formatter |
| `mypy` | **1.13+** | Type checking |
| `pre-commit` | **4.0+** | Git hooks |

## 📋 pyproject.toml Base

```toml
[project]
name = "bc-fastapi-weekXX"
version = "0.1.0"
description = "FastAPI Bootcamp - Week XX"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.34.0",
    "pydantic>=2.10.0",
    "pydantic-settings>=2.7.0",
    "sqlalchemy>=2.0.0",
    "alembic>=1.14.0",
    "aiosqlite>=0.20.0",
    "python-jose[cryptography]>=3.3.0",
    "passlib[bcrypt]>=1.7.4",
    "python-multipart>=0.0.18",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.24.0",
    "httpx>=0.28.0",
    "pytest-cov>=6.0.0",
    "ruff>=0.8.0",
    "mypy>=1.13.0",
    "pre-commit>=4.0.0",
]

[tool.ruff]
target-version = "py312"
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]

[tool.mypy]
python_version = "3.12"
strict = true
```

## 🐳 Dockerfile Base

```dockerfile
FROM python:3.13-slim

# Metadata
LABEL maintainer="EPTI Dev"
LABEL version="1.0"

# Environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

# Install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Install dependencies
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev

# Copy source
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uv", "run", "fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
```

## 📦 docker-compose.yml Base

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./src:/app/src
    env_file:
      - .env
    environment:
      - APP_ENV=development
    command: uv run fastapi dev src/main.py --host 0.0.0.0 --port 8000

  # PostgreSQL para producción (opcional)
  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: ${DB_USER:-postgres}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-postgres}
      POSTGRES_DB: ${DB_NAME:-app}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

## 🔄 Actualización de Versiones

Las versiones se actualizan:
- **Mensualmente**: Revisión de parches de seguridad
- **Por release mayor**: Evaluación de breaking changes
- **Fecha última actualización**: Diciembre 2025

## ✅ Verificación de Versiones

```bash
# Python
docker compose exec api python --version

# FastAPI
docker compose exec api uv run python -c "import fastapi; print(fastapi.__version__)"

# Pydantic
docker compose exec api uv run python -c "import pydantic; print(pydantic.__version__)"

# SQLAlchemy
docker compose exec api uv run python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```
