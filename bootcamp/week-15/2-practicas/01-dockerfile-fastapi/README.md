# 🐳 Práctica 01: Dockerfile para FastAPI

## 🎯 Objetivo

Crear un Dockerfile básico y funcional para una aplicación FastAPI, aprendiendo las instrucciones fundamentales de Docker.

---

## 📋 Conceptos que Aprenderás

- Instrucciones básicas de Dockerfile (FROM, WORKDIR, COPY, RUN, CMD)
- Configuración de variables de entorno para Python
- Exposición de puertos
- Ejecución de contenedores

---

## 🚀 Ejercicio

### Paso 1: Explorar la Aplicación

Primero, revisa la aplicación FastAPI que vamos a containerizar:

```bash
cd starter
cat main.py
```

La aplicación tiene:
- Un endpoint de health check (`/health`)
- Un endpoint de información (`/info`)
- Un endpoint de items (`/items`)

### Paso 2: Crear el Dockerfile Base

Abre `starter/Dockerfile` y descomenta las instrucciones paso a paso.

**Instrucción FROM:**
```dockerfile
# FROM especifica la imagen base
# python:3.13-slim es una versión reducida (~150MB vs ~900MB)
FROM python:3.13-slim
```

**Instrucción WORKDIR:**
```dockerfile
# WORKDIR crea y establece el directorio de trabajo
# Todas las instrucciones siguientes se ejecutan desde aquí
WORKDIR /app
```

### Paso 3: Configurar Variables de Entorno

```dockerfile
# ENV establece variables de entorno disponibles en build y runtime
# PYTHONDONTWRITEBYTECODE=1 → No crear archivos .pyc
# PYTHONUNBUFFERED=1 → Output directo (mejor para logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
```

### Paso 4: Instalar Dependencias

```dockerfile
# COPY copia archivos del contexto al contenedor
COPY requirements.txt .

# RUN ejecuta comandos durante el build
# --no-cache-dir evita guardar cache de pip (reduce tamaño)
RUN pip install --no-cache-dir -r requirements.txt
```

### Paso 5: Copiar Código Fuente

```dockerfile
# Copiamos el código después de las dependencias
# Esto aprovecha el caché de Docker (si el código cambia,
# no se reinstalan las dependencias)
COPY main.py .
```

### Paso 6: Exponer Puerto y Comando

```dockerfile
# EXPOSE documenta el puerto que usa la aplicación
# NO publica el puerto, solo documenta
EXPOSE 8000

# CMD define el comando por defecto al ejecutar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Paso 7: Construir la Imagen

```bash
# Construir imagen con tag 'fastapi-basic'
docker build -t fastapi-basic .

# Ver la imagen creada
docker images fastapi-basic
```

### Paso 8: Ejecutar el Contenedor

```bash
# Ejecutar en modo interactivo (ver logs)
docker run -p 8000:8000 fastapi-basic

# O en modo detached (background)
docker run -d -p 8000:8000 --name api fastapi-basic
```

### Paso 9: Verificar

```bash
# Probar health check
curl http://localhost:8000/health

# Probar info endpoint
curl http://localhost:8000/info

# Ver logs (si está en background)
docker logs api
```

---

## 🧪 Verificación

Ejecuta los tests para verificar tu Dockerfile:

```bash
# Desde el directorio starter/
python test_dockerfile.py
```

Tests que deben pasar:
- ✅ Imagen se construye correctamente
- ✅ Contenedor inicia sin errores
- ✅ Health check responde 200
- ✅ Tamaño de imagen < 300MB

---

## 📝 Dockerfile Completo

Al final, tu `Dockerfile` debería verse así:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🔍 Comandos Útiles

```bash
# Ver capas de la imagen
docker history fastapi-basic

# Inspeccionar imagen
docker inspect fastapi-basic

# Eliminar contenedor
docker stop api && docker rm api

# Eliminar imagen
docker rmi fastapi-basic

# Limpiar recursos no usados
docker system prune
```

---

## 🎯 Desafío Extra

1. Agrega un `LABEL` con tu nombre como maintainer
2. Agrega un `HEALTHCHECK` en el Dockerfile
3. Intenta reducir el tamaño de la imagen

---

## 🔗 Siguiente

Continúa con [02-multi-stage-build](../02-multi-stage-build/) para optimizar tu imagen.
