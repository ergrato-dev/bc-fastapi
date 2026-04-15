# 🐳 Configuración con Docker

Esta es la opción **recomendada** para el bootcamp. Docker garantiza un entorno idéntico para todos los estudiantes, sin importar el sistema operativo.

## 📋 Requisitos Previos

| Herramienta | Versión mínima | Verificar |
|-------------|---------------|-----------|
| Docker | 27.0+ | `docker --version` |
| Docker Compose | 2.31+ | `docker compose version` |
| Git | 2.40+ | `git --version` |
| VS Code | 1.95+ | (recomendado) |

---

## 1. Instalar Docker

### Fedora / RHEL

```bash
sudo dnf install docker docker-compose-plugin
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
# Cierra sesión y vuelve a entrar para que el grupo tenga efecto
```

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install docker.io docker-compose-v2
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
# Cierra sesión y vuelve a entrar
```

### macOS

```bash
# Opción 1: Docker Desktop (interfaz gráfica)
# Descargar desde https://docker.com/products/docker-desktop

# Opción 2: Homebrew (solo CLI)
brew install --cask docker
```

### Windows

Descargar e instalar **Docker Desktop** desde [docker.com](https://docker.com/products/docker-desktop).

> Requiere **WSL2** habilitado. Durante la instalación, Docker Desktop ofrece habilitarlo automáticamente.

---

## 2. Verificar la Instalación

```bash
docker --version
# Docker version 27.x.x

docker compose version
# Docker Compose version v2.31.x

# Probar que Docker funciona correctamente
docker run --rm hello-world
```

Si el último comando muestra `Hello from Docker!`, todo está bien.

---

## 3. Clonar el Repositorio

```bash
git clone https://github.com/ergrato-dev/bc-fastapi.git
cd bc-fastapi
```

---

## 4. Ejecutar una Semana

Cada semana tiene su propio `docker-compose.yml`. La estructura varía ligeramente según el contenido de la semana:

```
bootcamp/week-XX-nombre/
├── 2-practicas/
│   └── 01-ejercicio-nombre/
│       ├── starter/
│       │   ├── Dockerfile
│       │   ├── docker-compose.yml
│       │   └── main.py  (o src/)
│       └── README.md
└── 3-proyecto/
    └── starter/
        ├── Dockerfile
        ├── docker-compose.yml
        ├── .env.example
        └── src/  (o main.py en la raíz)
```

> **Nota semana 12 (Testing):** los ejercicios no tienen `starter/`, el `Dockerfile` y `docker-compose.yml` están directamente en la carpeta de cada práctica (`2-practicas/01-primeros-tests/`).

### Stack por semana

| Semanas | Stack | Servicios Docker |
|---------|-------|-----------------|
| 1–8 | FastAPI + SQLite | Solo `api` |
| 9–10 | FastAPI + SQLite (hexagonal) | Solo `api` |
| 11 | FastAPI + SQLite + JWT | Solo `api` |
| 12 | FastAPI + pytest | Solo `api` (con volumen `tests/`) |
| 13 | FastAPI + WebSockets/SSE | Solo `api` |
| 14 | FastAPI + Redis + SQLite | `api` + `redis` |
| 15–16 | FastAPI + PostgreSQL + Redis | `api` + `db` + `redis` |

### Pasos para cada ejercicio

```bash
# 1. Navegar al directorio del ejercicio
cd bootcamp/week-05-sqlalchemy_orm_introduccion/2-practicas/01-ejercicio-configuracion/starter

# 2. (Solo proyectos) Copiar variables de entorno
cp .env.example .env   # existe en todos los 3-proyecto/starter/

# 3. Construir y levantar el contenedor
docker compose up --build
```

### Acceder a la API

Con el contenedor corriendo, abre en tu navegador:

| URL | Descripción |
|-----|-------------|
| `http://localhost:8000` | Aplicación |
| `http://localhost:8000/docs` | Swagger UI (interactivo) |
| `http://localhost:8000/redoc` | ReDoc |

---

## 5. Comandos del Día a Día

```bash
# Levantar servicios en primer plano (ver logs en tiempo real)
docker compose up

# Levantar en segundo plano
docker compose up -d

# Ver logs de un servicio
docker compose logs -f api

# Detener servicios
docker compose down

# Reset completo (elimina también volúmenes/base de datos)
docker compose down -v

# Rebuild forzado (sin caché, útil si cambiaste dependencias)
docker compose build --no-cache && docker compose up
```

---

## 6. Ejecutar Comandos Dentro del Contenedor

```bash
# Abrir una shell interactiva
docker compose exec api bash

# Ejecutar tests
docker compose exec api uv run pytest

# Ejecutar migraciones
docker compose exec api uv run alembic upgrade head

# Instalar un paquete nuevo
docker compose exec api uv add nombre-paquete
```

---

## 7. Hot Reload

Los proyectos del bootcamp tienen **hot reload** activado: cada vez que guardas un archivo `.py`, FastAPI reinicia automáticamente. No necesitas detener y volver a levantar el contenedor.

Esto funciona gracias a los volúmenes en `docker-compose.yml`:

```yaml
volumes:
  - ./src:/app/src  # Sincroniza tu carpeta local con el contenedor
```

---

## 8. VS Code con Dev Containers (Opcional)

Para la mejor experiencia de desarrollo puedes abrir el proyecto **dentro** del contenedor:

1. Instalar extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Abrir la paleta de comandos (`Ctrl+Shift+P`)
3. Seleccionar `Dev Containers: Reopen in Container`

Esto habilita autocompletado, linting y debugging directamente en el entorno del contenedor.

---

## ❓ Resolución de Problemas

### `permission denied` al ejecutar docker

```bash
# Agregar tu usuario al grupo docker
sudo usermod -aG docker $USER
# Luego cierra sesión y vuelve a entrar (o ejecuta: newgrp docker)
```

### Puerto 8000 ya en uso

```bash
# Ver qué proceso usa el puerto
sudo lsof -i :8000

# O cambiar el puerto en docker-compose.yml
ports:
  - "8001:8000"  # host:contenedor
```

### Cambios en código no se reflejan

```bash
# Verificar que el volumen esté configurado en docker-compose.yml
# Si no hay volúmenes, hacer rebuild
docker compose up --build
```

### Imagen desactualizada

```bash
# Forzar descarga de la última imagen base
docker compose pull
docker compose up --build
```

---

→ Volver a [setup/README.md](README.md)
