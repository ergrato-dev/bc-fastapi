# ============================================
# Dockerfile - API Production Ready
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para crear un Dockerfile
# multi-stage optimizado para producción.
# ============================================

# ============================================
# TODO 1: Stage Builder
# ============================================
# Crea el stage builder que:
# - Use python:3.13-slim como base
# - Configure variables de entorno (PYTHONDONTWRITEBYTECODE, PYTHONUNBUFFERED)
# - Instale dependencias en un virtualenv
#
# FROM python:3.13-slim AS builder
#
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1
#
# WORKDIR /app
#
# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
#
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt


# ============================================
# TODO 2: Stage Runtime
# ============================================
# Crea el stage runtime que:
# - Use python:3.13-slim como base
# - Copie el virtualenv del builder
# - Copie el código fuente
#
# FROM python:3.13-slim AS runtime
#
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1 \
#     PATH="/opt/venv/bin:$PATH"
#
# WORKDIR /app


# ============================================
# TODO 3: Usuario Non-Root
# ============================================
# Crea un usuario no-root para seguridad:
#
# RUN groupadd --gid 1000 appgroup && \
#     useradd --uid 1000 --gid appgroup --shell /bin/bash appuser


# ============================================
# TODO 4: Copiar Archivos
# ============================================
# Copia el virtualenv y el código:
#
# COPY --from=builder /opt/venv /opt/venv
# COPY --chown=appuser:appgroup src/ ./src/


# ============================================
# TODO 5: Configuración Final
# ============================================
# Configura usuario, puerto y health check:
#
# USER appuser
#
# EXPOSE 8000
#
# HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
#     CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
#
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
