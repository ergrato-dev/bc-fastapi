# 🐳 Configuración Docker para BC-FastAPI

Este documento especifica las versiones y configuración Docker para el bootcamp.

## 📦 Versiones del Stack

| Tecnología | Versión | Notas |
|------------|---------|-------|
| **Python** | 3.14+ | Última versión estable |
| **FastAPI** | 0.128+ | Última versión |
| **Pydantic** | 2.12+ | Pydantic v2 (soporte Python 3.14) |
| **SQLAlchemy** | 2.0.46+ | Async support |
| **Alembic** | 1.15+ | Migraciones |
| **uv** | 0.6+ | Gestor de paquetes |
| **Docker** | 27.5+ | Container runtime |
| **Docker Compose** | 2.32+ | Orquestación |
| **PostgreSQL** | 17+ | Producción |
| **SQLite** | 3.48+ | Desarrollo/Testing |

## 🚀 ¿Por qué Docker?

1. **Entorno consistente**: Todos los estudiantes tienen el mismo entorno
2. **Sin conflictos de versiones**: No hay problemas con múltiples Python instalados
3. **Fácil configuración**: Un comando para levantar todo
4. **Reproducible**: El mismo código funciona igual en cualquier máquina
5. **Preparación para producción**: Docker es estándar en la industria

## 📋 Requisitos Previos

### Instalar Docker

**Fedora/RHEL:**
```bash
sudo dnf install docker docker-compose-plugin
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install docker.io docker-compose-v2
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar
```

**macOS:**
```bash
# Instalar Docker Desktop desde https://docker.com
# O usando Homebrew:
brew install --cask docker
```

**Windows:**
```bash
# Instalar Docker Desktop desde https://docker.com
# Requiere WSL2 habilitado
```

### Verificar Instalación

```bash
docker --version       # Docker version 27.x.x
docker compose version # Docker Compose version v2.31.x
```

## 📁 Estructura de Archivos Docker

Cada proyecto/semana incluye:

```
proyecto/
├── Dockerfile           # Imagen de la aplicación
├── docker-compose.yml   # Orquestación de servicios
├── .env.example         # Template de variables de entorno
├── .env                 # Variables de entorno (NO commitear)
├── .dockerignore        # Archivos a ignorar en build
└── src/                 # Código fuente
```

## 🔧 Comandos Esenciales

### Desarrollo Diario

```bash
# Levantar servicios (primera vez o después de cambios en Dockerfile)
docker compose up --build

# Levantar en segundo plano
docker compose up -d

# Ver logs en tiempo real
docker compose logs -f

# Ver logs de un servicio específico
docker compose logs -f api

# Detener servicios
docker compose down

# Detener y eliminar volúmenes (reset completo)
docker compose down -v
```

### Ejecutar Comandos

```bash
# Abrir shell en el contenedor
docker compose exec api bash

# Ejecutar comando específico
docker compose exec api uv run python -c "print('Hello')"

# Ejecutar tests
docker compose exec api uv run pytest

# Ejecutar migraciones
docker compose exec api uv run alembic upgrade head
```

### Gestión de Imágenes

```bash
# Ver imágenes
docker images

# Eliminar imágenes no usadas
docker image prune

# Rebuild forzado (sin cache)
docker compose build --no-cache
```

## 🐍 Python en Docker

### ¿Por qué NO instalar Python localmente?

1. Evita conflictos entre versiones de Python
2. No necesitas pyenv, virtualenv, conda, etc.
3. El entorno es idéntico al de producción
4. Más fácil de debuggear problemas

### Imagen Base

Usamos `python:3.14-slim` porque:
- Imagen oficial de Python
- Versión slim (más pequeña, sin extras innecesarios)
- Python 3.14 con las últimas características

## 📝 Variables de Entorno

### .env.example (Template)

```env
# Application
APP_NAME=bc-fastapi
APP_ENV=development
DEBUG=true

# Server
HOST=0.0.0.0
PORT=8000

# Database
DATABASE_URL=sqlite:///./app.db

# Security (generar con: openssl rand -hex 32)
SECRET_KEY=your-secret-key-here
```

### Configuración por Entorno

| Variable | Desarrollo | Testing | Producción |
|----------|------------|---------|------------|
| `DEBUG` | `true` | `true` | `false` |
| `DATABASE_URL` | `sqlite:///./app.db` | `sqlite:///:memory:` | `postgresql://...` |
| `APP_ENV` | `development` | `testing` | `production` |

## ⚡ Hot Reload

El desarrollo con Docker incluye hot reload:
- Los cambios en código se reflejan automáticamente
- No necesitas reiniciar contenedores
- Usa volúmenes para sincronizar archivos

```yaml
# docker-compose.yml
volumes:
  - ./src:/app/src  # Sincroniza código fuente
```

## 🔍 Debugging

### VS Code + Docker

1. Instalar extensión "Dev Containers"
2. Abrir proyecto en contenedor
3. Debugger funciona normalmente

### Logs y Errores

```bash
# Ver todos los logs
docker compose logs

# Seguir logs en tiempo real
docker compose logs -f

# Ver últimas 100 líneas
docker compose logs --tail=100
```

## 📚 Recursos

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [FastAPI Docker Deployment](https://fastapi.tiangolo.com/deployment/docker/)
- [uv Documentation](https://docs.astral.sh/uv/)
