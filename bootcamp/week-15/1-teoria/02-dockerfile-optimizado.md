# 📝 Dockerfile Optimizado para FastAPI

## 🎯 Objetivos de Aprendizaje

- Entender la estructura y sintaxis de un Dockerfile
- Aprender a optimizar imágenes con multi-stage builds
- Configurar seguridad básica en contenedores
- Aprovechar el caché de capas de Docker
- Crear imágenes de producción eficientes

---

## 📋 Tabla de Contenidos

1. [Anatomía de un Dockerfile](#anatomía-de-un-dockerfile)
2. [Instrucciones Principales](#instrucciones-principales)
3. [Sistema de Capas](#sistema-de-capas)
4. [Multi-Stage Builds](#multi-stage-builds)
5. [Optimizaciones](#optimizaciones)
6. [Seguridad](#seguridad)
7. [.dockerignore](#dockerignore)
8. [Dockerfile Completo](#dockerfile-completo)

---

## Anatomía de un Dockerfile

Un Dockerfile es un archivo de texto que contiene instrucciones secuenciales para construir una imagen:

```dockerfile
# Comentario: Dockerfile básico
FROM python:3.13-slim          # Imagen base
WORKDIR /app                   # Directorio de trabajo
COPY requirements.txt .        # Copiar archivos
RUN pip install -r req.txt     # Ejecutar comandos
EXPOSE 8000                    # Documentar puerto
CMD ["python", "main.py"]      # Comando por defecto
```

### Convenciones

- Nombre del archivo: `Dockerfile` (sin extensión)
- Instrucciones en MAYÚSCULAS (convención, no obligatorio)
- Una instrucción por línea (se pueden dividir con `\`)
- Comentarios con `#`

---

## Instrucciones Principales

### FROM - Imagen Base

```dockerfile
# Imagen oficial de Python
FROM python:3.13-slim

# Variantes comunes:
# python:3.13        → Imagen completa (~900MB)
# python:3.13-slim   → Imagen reducida (~150MB) ← Recomendada
# python:3.13-alpine → Muy pequeña (~50MB) pero puede tener problemas

# Con tag específico (recomendado para reproducibilidad)
FROM python:3.13.1-slim-bookworm
```

### WORKDIR - Directorio de Trabajo

```dockerfile
# Establece el directorio de trabajo
WORKDIR /app

# Equivale a:
# RUN mkdir -p /app && cd /app
# Todas las instrucciones siguientes se ejecutan desde /app
```

### COPY vs ADD

```dockerfile
# COPY - Simple y predecible (preferido)
COPY requirements.txt .
COPY src/ ./src/

# ADD - Características extra (evitar si no las necesitas)
# - Puede extraer archivos .tar automáticamente
# - Puede descargar desde URLs
ADD archive.tar.gz /app/  # Extrae automáticamente
```

**Recomendación**: Usa siempre `COPY` a menos que necesites las features de `ADD`.

### RUN - Ejecutar Comandos

```dockerfile
# Ejecuta comandos durante el build
RUN pip install fastapi

# Múltiples comandos en una línea (reduce capas)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Cada RUN crea una nueva capa
RUN echo "step 1"   # Capa 1
RUN echo "step 2"   # Capa 2
# vs
RUN echo "step 1" && echo "step 2"  # Una sola capa
```

### ENV - Variables de Entorno

```dockerfile
# Variables disponibles en build y runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ENV=production

# Uso en el Dockerfile
RUN echo $APP_ENV
```

### ARG - Argumentos de Build

```dockerfile
# Solo disponibles durante el build
ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim

ARG APP_VERSION=1.0.0
ENV APP_VERSION=${APP_VERSION}

# Pasar valores en build
# docker build --build-arg PYTHON_VERSION=3.12 .
```

### EXPOSE - Documentar Puertos

```dockerfile
# Documenta qué puerto usa la app (NO lo publica)
EXPOSE 8000

# Para publicar el puerto, usar -p en docker run:
# docker run -p 8000:8000 my-app
```

### CMD vs ENTRYPOINT

```dockerfile
# CMD - Comando por defecto (puede ser sobrescrito)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
# docker run my-app                    → ejecuta CMD
# docker run my-app python --version   → sobrescribe CMD

# ENTRYPOINT - Comando fijo (argumentos se añaden)
ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
# docker run my-app                          → uvicorn main:app --host 0.0.0.0 --port 8000
# docker run my-app --workers 4              → uvicorn main:app --workers 4
```

### USER - Usuario No-Root

```dockerfile
# Crear y usar usuario no-root (seguridad)
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Ahora todo se ejecuta como 'appuser', no como root
```

### HEALTHCHECK - Verificación de Salud

```dockerfile
# Docker verificará periódicamente si el contenedor está sano
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Opciones:
# --interval: Frecuencia de chequeo
# --timeout: Tiempo máximo de espera
# --start-period: Tiempo de gracia al inicio
# --retries: Intentos antes de marcar unhealthy
```

---

## Sistema de Capas

![Diagrama de capas](../0-assets/02-dockerfile-layers.svg)

### Cómo Funcionan las Capas

```dockerfile
FROM python:3.13-slim     # Capa 1 (de la imagen base)
WORKDIR /app               # Capa 2
COPY requirements.txt .    # Capa 3
RUN pip install -r req.txt # Capa 4
COPY src/ ./src/           # Capa 5
CMD ["uvicorn", "..."]     # Metadata (no crea capa)
```

Cada instrucción `FROM`, `RUN`, `COPY`, `ADD` crea una nueva capa.

### Caché de Capas

Docker cachea cada capa. Si una instrucción no cambia, reutiliza la capa cacheada:

```dockerfile
# ❌ MAL - Invalida caché frecuentemente
COPY . .                        # Cualquier cambio invalida caché
RUN pip install -r requirements.txt

# ✅ BIEN - Maximiza uso de caché
COPY requirements.txt .         # Solo cambia si deps cambian
RUN pip install -r requirements.txt  # Cacheado si req.txt no cambió
COPY src/ ./src/                # Código cambia frecuentemente
```

### Orden de Instrucciones

```
Menos frecuente → Más frecuente (de cambios)

FROM python:3.13-slim          # Casi nunca cambia
ENV PYTHONUNBUFFERED=1          # Rara vez cambia
WORKDIR /app                    # Nunca cambia
COPY requirements.txt .         # Cambia con nuevas deps
RUN pip install ...             # Cacheado si req.txt no cambió
COPY src/ ./src/                # Cambia frecuentemente ← Al final
```

---

## Multi-Stage Builds

Los **multi-stage builds** permiten usar múltiples `FROM` para crear imágenes más pequeñas y seguras.

### El Problema

```dockerfile
# ❌ Imagen única con todo
FROM python:3.13

# Herramientas de build (gcc, etc.) quedan en imagen final
RUN apt-get update && apt-get install -y gcc
RUN pip install -r requirements.txt

# Imagen final: 900MB+ con herramientas innecesarias
```

### La Solución: Multi-Stage

```dockerfile
# ============================================
# Stage 1: Builder - Instalar dependencias
# ============================================
FROM python:3.13-slim AS builder

# Instalar herramientas de compilación (solo en builder)
RUN apt-get update && apt-get install -y --no-install-recommends gcc

WORKDIR /app

# Instalar dependencias en un virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============================================
# Stage 2: Runtime - Imagen final limpia
# ============================================
FROM python:3.13-slim AS runtime

WORKDIR /app

# Copiar SOLO el virtualenv del builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copiar código
COPY src/ ./src/

# Usuario no-root
RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Beneficios del Multi-Stage

| Aspecto | Sin Multi-Stage | Con Multi-Stage |
|---------|-----------------|-----------------|
| Tamaño imagen | ~800MB | ~150MB |
| Herramientas build | Incluidas | Excluidas |
| Seguridad | Menor | Mayor |
| Tiempo deploy | Más lento | Más rápido |

---

## Optimizaciones

### 1. Usar Imagen Base Apropiada

```dockerfile
# ❌ Imagen completa (900MB+)
FROM python:3.13

# ✅ Imagen slim (150MB)
FROM python:3.13-slim

# ⚠️ Alpine (50MB) - puede tener problemas con algunas libs
FROM python:3.13-alpine
```

### 2. Combinar Comandos RUN

```dockerfile
# ❌ Múltiples capas
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get clean

# ✅ Una sola capa, limpieza incluida
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### 3. Usar --no-cache-dir

```dockerfile
# ❌ Cache de pip ocupa espacio
RUN pip install -r requirements.txt

# ✅ Sin cache
RUN pip install --no-cache-dir -r requirements.txt
```

### 4. Copiar Solo lo Necesario

```dockerfile
# ❌ Copia todo (incluye .git, tests, docs, etc.)
COPY . .

# ✅ Copia solo lo necesario
COPY pyproject.toml uv.lock ./
COPY src/ ./src/
```

### 5. Variables de Entorno Python

```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1 \
    # No crear archivos .pyc (innecesarios en contenedor)
    PYTHONUNBUFFERED=1 \
    # Output directo a terminal (mejor para logs)
    PIP_NO_CACHE_DIR=1 \
    # pip sin cache
    PIP_DISABLE_PIP_VERSION_CHECK=1
    # No verificar versión de pip
```

---

## Seguridad

### 1. Usuario No-Root

```dockerfile
# ❌ Corre como root (peligroso)
CMD ["uvicorn", "main:app"]

# ✅ Usuario sin privilegios
RUN adduser --disabled-password --gecos "" --uid 1000 appuser
USER appuser
CMD ["uvicorn", "main:app"]
```

### 2. No Incluir Secretos

```dockerfile
# ❌ NUNCA hacer esto
ENV DATABASE_PASSWORD=supersecret
COPY .env /app/.env

# ✅ Pasar secretos en runtime
# docker run -e DATABASE_PASSWORD=xxx my-app
# O usar Docker secrets / sistemas de gestión de secretos
```

### 3. Imagen Base Confiable

```dockerfile
# ✅ Usar imágenes oficiales con tag específico
FROM python:3.13.1-slim-bookworm

# Verificar origen de la imagen
# docker pull python:3.13-slim --platform linux/amd64
```

### 4. Escanear Vulnerabilidades

```bash
# Usar Trivy para escanear imagen
docker build -t my-app .
trivy image my-app

# O integrar en CI/CD
```

---

## .dockerignore

El archivo `.dockerignore` excluye archivos del contexto de build:

```dockerignore
# .dockerignore

# Git
.git
.gitignore

# Python
__pycache__
*.py[cod]
*$py.class
*.so
.Python
.venv
venv/
ENV/

# Testing
.pytest_cache
.coverage
htmlcov/
.tox

# IDE
.idea/
.vscode/
*.swp
*.swo

# Docker
Dockerfile*
docker-compose*
.docker

# Docs
docs/
*.md
!README.md

# Local config
.env
.env.local
*.log

# Misc
.DS_Store
Thumbs.db
```

### Importancia del .dockerignore

```bash
# Sin .dockerignore, todo se copia al daemon
# Contexto grande = build lento

# Ejemplo de contexto excesivo:
# Sending build context to Docker daemon  500MB  ← Muy grande

# Con buen .dockerignore:
# Sending build context to Docker daemon  5MB    ← Rápido
```

---

## Dockerfile Completo

### Con uv (Recomendado para el Bootcamp)

```dockerfile
# ============================================
# Dockerfile para FastAPI con uv
# ============================================

# Stage 1: Builder
FROM python:3.13-slim AS builder

# Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copiar archivos de dependencias
COPY pyproject.toml uv.lock ./

# Crear virtualenv e instalar dependencias
RUN uv sync --frozen --no-dev

# ============================================
# Stage 2: Runtime
# ============================================
FROM python:3.13-slim AS runtime

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copiar virtualenv del builder
COPY --from=builder /app/.venv ./.venv

# Copiar código fuente
COPY src/ ./src/

# Crear usuario no-root
RUN adduser --disabled-password --gecos "" --uid 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Metadatos
LABEL maintainer="tu-email@example.com" \
      version="1.0.0" \
      description="FastAPI Application"

# Puerto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Con pip (Alternativa)

```dockerfile
# ============================================
# Dockerfile para FastAPI con pip
# ============================================

FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Crear virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============================================
FROM python:3.13-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY src/ ./src/

RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🧪 Verificación

### Construir y Probar

```bash
# Construir
docker build -t my-fastapi-app .

# Ver tamaño
docker images my-fastapi-app

# Ejecutar
docker run -d -p 8000:8000 --name api my-fastapi-app

# Probar
curl http://localhost:8000/health

# Ver logs
docker logs api

# Inspeccionar
docker inspect api

# Limpiar
docker stop api && docker rm api
```

### Verificar Tamaño de Imagen

```bash
# Ver capas
docker history my-fastapi-app

# Meta: imagen < 200MB para FastAPI básico
```

---

## 📚 Recursos Adicionales

- [Dockerfile Reference](https://docs.docker.com/engine/reference/dockerfile/)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Multi-stage Builds](https://docs.docker.com/build/building/multi-stage/)

---

## 🔗 Siguiente

Continúa con [03-docker-compose.md](03-docker-compose.md) para aprender a orquestar múltiples servicios.
