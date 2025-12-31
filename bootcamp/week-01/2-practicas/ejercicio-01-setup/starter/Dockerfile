# ============================================
# DOCKERFILE - Imagen para FastAPI con uv
# ============================================
# Este Dockerfile crea una imagen optimizada para
# ejecutar aplicaciones FastAPI usando uv como
# gestor de paquetes.

# --------------------------------------------
# PASO 1: Imagen base
# --------------------------------------------
# Usamos Python 3.13 slim para menor tamaño
# Descomenta las siguientes líneas:

# FROM python:3.13-slim


# --------------------------------------------
# PASO 2: Variables de entorno
# --------------------------------------------
# Configuramos Python para mejor comportamiento en Docker:
# - PYTHONDONTWRITEBYTECODE: No crear archivos .pyc
# - PYTHONUNBUFFERED: Output sin buffer (logs en tiempo real)
# - UV_SYSTEM_PYTHON: uv usa el Python del sistema
# Descomenta las siguientes líneas:

# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1 \
#     UV_SYSTEM_PYTHON=1


# --------------------------------------------
# PASO 3: Instalar uv
# --------------------------------------------
# uv es un gestor de paquetes moderno y rápido
# Descomenta la siguiente línea:

# RUN pip install --no-cache-dir uv


# --------------------------------------------
# PASO 4: Directorio de trabajo
# --------------------------------------------
# Establecemos /app como directorio principal
# Descomenta la siguiente línea:

# WORKDIR /app


# --------------------------------------------
# PASO 5: Copiar dependencias
# --------------------------------------------
# Copiamos primero los archivos de dependencias
# para aprovechar el cache de Docker
# Descomenta las siguientes líneas:

# COPY pyproject.toml uv.lock* ./
# RUN uv sync --frozen --no-dev


# --------------------------------------------
# PASO 6: Copiar código fuente
# --------------------------------------------
# Copiamos el resto del código
# Descomenta la siguiente línea:

# COPY . .


# --------------------------------------------
# PASO 7: Puerto y comando
# --------------------------------------------
# Exponemos el puerto 8000 y ejecutamos FastAPI
# en modo desarrollo con hot-reload
# Descomenta las siguientes líneas:

# EXPOSE 8000
# CMD ["uv", "run", "fastapi", "dev", "src/main.py", "--host", "0.0.0.0"]
