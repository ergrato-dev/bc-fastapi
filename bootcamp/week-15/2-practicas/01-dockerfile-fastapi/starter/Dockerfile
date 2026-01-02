# ============================================
# Dockerfile para FastAPI - Práctica 01
# ============================================
# Descomenta las instrucciones paso a paso
# siguiendo el README.md
# ============================================

# ============================================
# PASO 1: Imagen Base
# ============================================
# FROM especifica la imagen base desde la cual construir
# python:3.13-slim es una versión reducida de Python (~150MB)
# Descomenta la siguiente línea:

# FROM python:3.13-slim


# ============================================
# PASO 2: Directorio de Trabajo
# ============================================
# WORKDIR crea el directorio si no existe y lo establece
# como directorio de trabajo para instrucciones siguientes
# Descomenta la siguiente línea:

# WORKDIR /app


# ============================================
# PASO 3: Variables de Entorno
# ============================================
# ENV establece variables de entorno
# - PYTHONDONTWRITEBYTECODE=1: No crear archivos .pyc
# - PYTHONUNBUFFERED=1: Output directo a terminal (mejor para logs)
# Descomenta las siguientes líneas:

# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1


# ============================================
# PASO 4: Copiar e Instalar Dependencias
# ============================================
# Copiamos requirements.txt primero para aprovechar caché
# Si el código cambia pero no las deps, Docker reutiliza esta capa
# Descomenta las siguientes líneas:

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt


# ============================================
# PASO 5: Copiar Código Fuente
# ============================================
# Copiamos el código después de las dependencias
# para maximizar el uso de caché
# Descomenta la siguiente línea:

# COPY main.py .


# ============================================
# PASO 6: Exponer Puerto
# ============================================
# EXPOSE documenta el puerto que la aplicación usa
# Nota: NO publica el puerto, solo lo documenta
# Para publicar, usar -p en docker run
# Descomenta la siguiente línea:

# EXPOSE 8000


# ============================================
# PASO 7: Comando de Inicio
# ============================================
# CMD define el comando que se ejecuta al iniciar el contenedor
# Usamos formato JSON (exec form) que es más robusto
# --host 0.0.0.0 permite conexiones desde fuera del contenedor
# Descomenta la siguiente línea:

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# ============================================
# DESAFÍO EXTRA (opcional)
# ============================================
# 1. Agrega un LABEL con tu información:
# LABEL maintainer="tu-email@example.com"
#
# 2. Agrega un HEALTHCHECK:
# HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
#     CMD curl -f http://localhost:8000/health || exit 1
