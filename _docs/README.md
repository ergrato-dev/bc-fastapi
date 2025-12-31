# 📚 Documentación del Bootcamp

Esta carpeta contiene documentación general que aplica a todo el bootcamp.

## 📋 Índice

| Documento | Descripción |
|-----------|-------------|
| [docker-setup.md](docker-setup.md) | Configuración de Docker y docker compose |
| [stack-versions.md](stack-versions.md) | Versiones oficiales de todas las tecnologías |

## 🐳 Entorno de Desarrollo

Este bootcamp utiliza **Docker** como entorno de desarrollo para:

- ✅ Evitar problemas con múltiples versiones de Python
- ✅ Garantizar entorno consistente para todos los estudiantes
- ✅ Preparar para deployment en producción
- ✅ Simplificar la configuración inicial

### Requisitos

- Docker 27+
- Docker Compose 2.31+
- VS Code (recomendado)

### Inicio Rápido

```bash
# Clonar repositorio
git clone https://github.com/ergrato-dev/bc-fastapi.git
cd bc-fastapi

# Ir a una semana específica
cd bootcamp/week-01

# Levantar entorno
docker compose up --build
```

## 📦 Stack Tecnológico

| Categoría | Tecnologías |
|-----------|-------------|
| **Runtime** | Python 3.13, Docker 27+ |
| **Framework** | FastAPI 0.115+, Pydantic 2.10+ |
| **Base de Datos** | SQLAlchemy 2.0+, SQLite/PostgreSQL 17+ |
| **Testing** | pytest 8+, httpx 0.28+ |
| **Herramientas** | uv 0.5+, ruff 0.8+ |

Ver [stack-versions.md](stack-versions.md) para versiones detalladas.

## 🔗 Enlaces Útiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)
- [uv Documentation](https://docs.astral.sh/uv/)
