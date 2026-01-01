# ============================================
# Task Management System - Dockerfile
# ============================================

FROM python:3.13-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    UV_SYSTEM_PYTHON=1

# Instalar uv
RUN pip install --no-cache-dir uv

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY pyproject.toml ./

# Instalar dependencias
RUN uv sync --no-dev

# Copiar código fuente
COPY . .

# Puerto
EXPOSE 8000

# Comando de inicio
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
