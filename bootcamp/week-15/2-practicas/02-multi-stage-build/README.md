# 🚀 Práctica 02: Multi-Stage Build

## 🎯 Objetivo

Optimizar una imagen Docker usando multi-stage builds para reducir significativamente el tamaño y mejorar la seguridad.

---

## 📋 Conceptos que Aprenderás

- Multi-stage builds con múltiples `FROM`
- Separación de build y runtime
- Copiar artefactos entre stages con `COPY --from`
- Crear usuario no-root para seguridad
- Optimización de tamaño de imagen

---

## 🚀 Ejercicio

### Paso 1: Ver el Problema

Primero, construye una imagen sin multi-stage para ver el tamaño:

```bash
cd starter

# Construir imagen simple
docker build -f Dockerfile.simple -t fastapi-simple .

# Ver tamaño
docker images fastapi-simple
# Probablemente ~400-500MB
```

### Paso 2: Entender Multi-Stage

Un multi-stage build usa múltiples `FROM`:

```
┌─────────────────────────────────────┐
│  Stage 1: BUILDER                   │
│  - Imagen completa                  │
│  - Herramientas de build (gcc, etc) │
│  - Instala dependencias             │
│  - NO va a producción               │
└─────────────────┬───────────────────┘
                  │ COPY --from=builder
┌─────────────────▼───────────────────┐
│  Stage 2: RUNTIME                   │
│  - Imagen slim/minimal              │
│  - Solo lo necesario para ejecutar  │
│  - Sin herramientas de build        │
│  - VA A PRODUCCIÓN                  │
└─────────────────────────────────────┘
```

### Paso 3: Crear el Builder Stage

Abre `starter/Dockerfile` y descomenta el Stage 1:

```dockerfile
# Stage 1: Builder
FROM python:3.13-slim AS builder

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Crear virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias en el venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```

**¿Por qué virtualenv?** 
- Aísla las dependencias en un directorio conocido
- Fácil de copiar al stage de runtime
- Menor tamaño que copiar todo site-packages

### Paso 4: Crear el Runtime Stage

Descomenta el Stage 2:

```dockerfile
# Stage 2: Runtime
FROM python:3.13-slim AS runtime

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Copiar SOLO el virtualenv del builder
COPY --from=builder /opt/venv /opt/venv

# Copiar código fuente
COPY main.py .
```

**Nota**: Usamos `COPY --from=builder` para copiar artefactos del stage anterior.

### Paso 5: Agregar Usuario No-Root

```dockerfile
# Crear usuario sin privilegios (seguridad)
RUN adduser --disabled-password --gecos "" --uid 1000 appuser

# Cambiar propietario de archivos
RUN chown -R appuser:appuser /app

# Usar el usuario no-root
USER appuser
```

**¿Por qué usuario no-root?**
- Si un atacante compromete la app, no tiene acceso root
- Mejor aislamiento de procesos
- Buena práctica de seguridad

### Paso 6: Finalizar Dockerfile

```dockerfile
# Puerto y comando
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Paso 7: Construir y Comparar

```bash
# Construir imagen optimizada
docker build -t fastapi-optimized .

# Comparar tamaños
docker images | grep fastapi
# fastapi-simple     ~400-500MB
# fastapi-optimized  ~150-180MB  ← Mucho más pequeña!
```

### Paso 8: Verificar Usuario

```bash
# Ejecutar contenedor
docker run -d -p 8000:8000 --name api fastapi-optimized

# Ver con qué usuario corre
docker exec api whoami
# Debería mostrar: appuser (no root)

# Ver procesos
docker exec api ps aux
# El proceso uvicorn corre como appuser
```

---

## 🧪 Verificación

```bash
# Ejecutar tests
python test_multistage.py
```

Tests que deben pasar:
- ✅ Imagen se construye correctamente
- ✅ Tamaño < 200MB
- ✅ Contenedor corre como usuario no-root
- ✅ Health check responde

---

## 📝 Dockerfile Completo

```dockerfile
# ============================================
# Stage 1: Builder
# ============================================
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============================================
# Stage 2: Runtime
# ============================================
FROM python:3.13-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY main.py .

RUN adduser --disabled-password --gecos "" --uid 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📊 Comparación de Tamaños

| Imagen | Tamaño | Reducción |
|--------|--------|-----------|
| python:3.13 (base) | ~900MB | - |
| python:3.13-slim | ~150MB | 83% |
| fastapi-simple | ~400MB | - |
| fastapi-optimized (multi-stage) | ~170MB | 57% |

---

## 🎯 Desafío Extra

1. Agrega `HEALTHCHECK` al Dockerfile
2. Usa `--target builder` para construir solo el primer stage
3. Agrega labels con información de versión

```bash
# Construir solo hasta el stage builder
docker build --target builder -t fastapi-builder .

# Útil para debugging del build
```

---

## 🔗 Siguiente

Continúa con [03-docker-compose-stack](../03-docker-compose-stack/) para orquestar múltiples servicios.
