# ============================================
# Multi-Stage Dockerfile - Práctica 02
# ============================================
# Este Dockerfile usa multi-stage builds para
# crear una imagen optimizada y segura.
# Descomenta las secciones paso a paso.
# ============================================


# ============================================
# STAGE 1: BUILDER
# ============================================
# Este stage instala todas las dependencias.
# Las herramientas de build NO van a la imagen final.

# Descomenta las siguientes líneas:

# FROM python:3.13-slim AS builder

# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# WORKDIR /app

# # Crear virtualenv para aislar dependencias
# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# # Instalar dependencias en el virtualenv
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt


# ============================================
# STAGE 2: RUNTIME
# ============================================
# Este stage crea la imagen final, copiando
# solo lo necesario del stage builder.

# Descomenta las siguientes líneas:

# FROM python:3.13-slim AS runtime

# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1 \
#     PATH="/opt/venv/bin:$PATH"

# WORKDIR /app

# # Copiar virtualenv del builder (SOLO las deps instaladas)
# COPY --from=builder /opt/venv /opt/venv

# # Copiar código fuente
# COPY main.py .


# ============================================
# SEGURIDAD: Usuario No-Root
# ============================================
# Crear y usar un usuario sin privilegios.
# Si la app es comprometida, el atacante no tiene root.

# Descomenta las siguientes líneas:

# RUN adduser --disabled-password --gecos "" --uid 1000 appuser && \
#     chown -R appuser:appuser /app

# USER appuser


# ============================================
# CONFIGURACIÓN FINAL
# ============================================
# Puerto y comando de inicio.

# Descomenta las siguientes líneas:

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# ============================================
# DESAFÍO EXTRA (opcional)
# ============================================
# Agrega un HEALTHCHECK para que Docker
# pueda verificar si el contenedor está sano:
#
# HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
#     CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1
