# ============================================
# PROYECTO FINAL - Dockerfile Template
# ============================================
# 
# Dockerfile multi-stage optimizado para producción.
# Adapta según las necesidades de tu proyecto.
#
# Build: docker build -t task-api .
# Run:   docker run -p 8000:8000 task-api
# ============================================

# ============================================
# STAGE 1: Builder
# ============================================
FROM python:3.13-slim AS builder

# Evitar .pyc y buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

WORKDIR /app

# Instalar uv (gestor de paquetes rápido)
RUN pip install --no-cache-dir uv

# Copiar archivos de dependencias
COPY pyproject.toml uv.lock* ./

# Instalar dependencias (sin dev)
RUN uv sync --frozen --no-dev

# ============================================
# STAGE 2: Production
# ============================================
FROM python:3.13-slim AS production

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Crear usuario no-root para seguridad
RUN groupadd -r appgroup && \
    useradd -r -g appgroup -d /app -s /sbin/nologin appuser

WORKDIR /app

# Copiar virtual environment del builder
COPY --from=builder /app/.venv /app/.venv

# Copiar código fuente
COPY --chown=appuser:appgroup src/ ./src/
COPY --chown=appuser:appgroup alembic/ ./alembic/
COPY --chown=appuser:appgroup alembic.ini ./

# Crear directorio de logs
RUN mkdir -p /app/logs && chown appuser:appgroup /app/logs

# Cambiar a usuario no-root
USER appuser

# Puerto de la aplicación
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:8000/health')" || exit 1

# Comando de inicio
# Desarrollo: uvicorn con reload
# Producción: uvicorn sin reload, con workers
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

# ============================================
# NOTAS DE USO
# ============================================
# 
# Para desarrollo con hot-reload:
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
#
# Para producción con múltiples workers:
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
#
# O usar gunicorn:
# CMD ["gunicorn", "src.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
