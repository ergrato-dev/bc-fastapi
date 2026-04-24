# 🐍 Configuración sin Docker

Esta opción es para estudiantes que **no pueden usar Docker** en su máquina. Requiere instalar Python y `uv` localmente.

> ⚠️ **Advertencia**: La opción recomendada sigue siendo Docker. Esta guía es válida para las semanas 1–8 del bootcamp. Las semanas 9+ que requieren PostgreSQL o múltiples servicios necesitan Docker.

---

## 📋 Requisitos Previos

| Herramienta | Versión mínima | Propósito |
|-------------|---------------|-----------|
| Python | **3.13+** | Runtime |
| uv | **0.6+** | Gestor de paquetes y entornos virtuales |
| Git | 2.40+ | Control de versiones |

---

## 1. Instalar Python 3.13+

### Opción A: pyenv (Recomendado)

`pyenv` permite tener múltiples versiones de Python sin conflictos y es la forma más limpia de gestionar versiones localmente.

**Fedora / RHEL:**
```bash
# Dependencias
sudo dnf install gcc zlib-devel bzip2 bzip2-devel readline readline-devel \
    sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel

# Instalar pyenv
curl https://pyenv.run | bash

# Agregar a ~/.bashrc o ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Recargar shell
source ~/.zshrc
```

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils \
    tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

source ~/.bashrc
```

**macOS:**
```bash
brew install pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

source ~/.zshrc
```

Una vez instalado `pyenv`, instala Python 3.14:

```bash
pyenv install 3.14.0
pyenv global 3.14.0   # O: pyenv local 3.14.0 (solo para este directorio)

python --version
# Python 3.14.0
```

### Opción B: Instalador oficial

Descarga Python 3.14 desde [python.org/downloads](https://www.python.org/downloads/) e instala manualmente.

> Con esta opción puede haber conflictos si ya tienes otra versión de Python. Se recomienda `pyenv`.

---

## 2. Instalar uv

`uv` es el gestor de paquetes oficial del bootcamp. Es significativamente más rápido que `pip` y gestiona entornos virtuales automáticamente.

```bash
# Instalación universal (Linux / macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Recargar variables de entorno
source $HOME/.local/bin/env

# Verificar
uv --version
# uv 0.6.x
```

**Windows (Git Bash):**
```bash
# En Git Bash (incluido con Git para Windows)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Recargar variables de entorno
source $HOME/.local/bin/env
```

> ℹ️ Abre **Git Bash** (no PowerShell ni CMD) para ejecutar estos comandos. Git Bash viene instalado junto con Git para Windows.

---

## 3. Clonar el Repositorio

```bash
git clone https://github.com/ergrato-dev/bc-fastapi.git
cd bc-fastapi
```

---

## 4. Configurar el Proyecto de una Semana

Cada ejercicio/proyecto tiene un `pyproject.toml` con sus dependencias. El flujo es:

```bash
# 1. Navegar al directorio del ejercicio
cd bootcamp/week-01-python_moderno_y_fastapi/2-practicas/01-ejercicio-setup/starter

# 2. Instalar dependencias (uv crea el entorno virtual automáticamente)
uv sync

# 3. Copiar variables de entorno
cp .env.example .env

# 4. Levantar la aplicación
uv run fastapi dev src/main.py
```

### Acceder a la API

Con la aplicación corriendo, abre en tu navegador:

| URL | Descripción |
|-----|-------------|
| `http://localhost:8000` | Aplicación |
| `http://localhost:8000/docs` | Swagger UI (interactivo) |
| `http://localhost:8000/redoc` | ReDoc |

---

## 5. Comandos del Día a Día

```bash
# Iniciar servidor de desarrollo (con hot reload)
uv run fastapi dev src/main.py

# Ejecutar tests
uv run pytest

# Ejecutar un script específico
uv run python src/script.py

# Agregar una dependencia nueva
uv add nombre-paquete==1.2.3

# Agregar dependencia de desarrollo
uv add --dev pytest==8.3.5

# Ver entorno virtual activo
uv run python -c "import sys; print(sys.executable)"
```

---

## 6. Variables de Entorno

Sin Docker, las variables de entorno se cargan desde el archivo `.env` en la carpeta del proyecto:

```bash
# Crear .env desde el template
cp .env.example .env

# Editar .env con tus valores
# El .env NO se sube al repositorio (está en .gitignore)
```

Contenido típico de `.env` para desarrollo local:

```env
APP_NAME=bc-fastapi
APP_ENV=development
DEBUG=true

HOST=127.0.0.1
PORT=8000

# SQLite (perfecto para desarrollo local)
DATABASE_URL=sqlite:///./app.db

# Generar con: python -c "import secrets; print(secrets.token_hex(32))"
SECRET_KEY=cambia-esto-por-un-secreto-real
```

---

## 7. Diferencias Respecto a Docker

| Aspecto | Con Docker | Sin Docker |
|---------|-----------|------------|
| Base de datos | PostgreSQL disponible | Solo SQLite (semanas 1-8) |
| Aislamiento | Total (contenedor) | Depende del entorno virtual |
| Variables de entorno | `docker-compose.yml` + `.env` | Solo `.env` |
| Comandos | `docker compose exec api uv run ...` | `uv run ...` |
| Puerto | Configurable en `docker-compose.yml` | Configurable en `.env` |
| Hot reload | Automático vía volúmenes | Automático vía `fastapi dev` |

---

## 8. Limitaciones

### Semanas que requieren Docker

Las siguientes semanas del bootcamp requieren servicios que no están disponibles sin Docker:

| Semana | Requiere | Razón |
|--------|---------|-------|
| Semana 9+ | Docker | PostgreSQL como BD principal |
| Semana 11 | Docker | Servicio Redis para rate limiting |
| Semana 15 | Docker | CI/CD y deployment |
| Semana 16 | Docker | Proyecto final completo |

Para estas semanas **deberás instalar Docker**. Consulta [con-docker.md](con-docker.md).

---

## ❓ Resolución de Problemas

### `python: command not found`

```bash
# Verificar que pyenv está configurado
pyenv versions

# Si usaste instalador manual, verificar PATH
which python3
python3 --version

# Crear alias si es necesario
alias python=python3
```

### `uv: command not found`

```bash
# Agregar al PATH manualmente
export PATH="$HOME/.local/bin:$PATH"

# Para hacerlo permanente, agregar al .zshrc o .bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Error al instalar dependencias con `uv sync`

```bash
# Verificar versión de Python
python --version   # Debe ser 3.13+

# Forzar creación de entorno nuevo
uv sync --reinstall

# Ver detalle del error
uv sync --verbose
```

### Puerto 8000 ya en uso

```bash
# Ver qué proceso ocupa el puerto
sudo lsof -i :8000

# Ejecutar en otro puerto
uv run fastapi dev src/main.py --port 8001
```

### Conflicto con otra versión de Python

```bash
# Fijar versión en el directorio del proyecto
pyenv local 3.14.0

# uv usará la versión indicada en pyproject.toml
# Verificar que pyproject.toml tenga:
# requires-python = ">=3.13"
```

---

→ Volver a [setup/README.md](README.md)
