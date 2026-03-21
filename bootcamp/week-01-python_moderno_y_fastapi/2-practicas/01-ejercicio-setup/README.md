# 🐳 Ejercicio 01: Setup del Entorno Docker

## 🎯 Objetivo

Configurar el entorno de desarrollo con Docker y crear tu primer proyecto FastAPI.

**Duración estimada:** 30 minutos

---

## 📋 Requisitos Previos

- Docker Desktop instalado ([Guía de instalación](../../../_docs/docker-setup.md))
- VS Code con extensión Docker
- Terminal disponible

---

## 📝 Instrucciones

### Paso 1: Crear la Estructura del Proyecto

Crea una carpeta para tu proyecto y los archivos necesarios:

```bash
mkdir mi-primera-api
cd mi-primera-api
```

Tu estructura debe verse así:

```
mi-primera-api/
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── src/
    └── main.py
```

---

### Paso 2: Crear el Dockerfile

El Dockerfile define cómo construir la imagen de tu aplicación.

**Abre `starter/Dockerfile`** y descomenta cada sección siguiendo las instrucciones.

```dockerfile
# El Dockerfile usa Python 3.13 slim como base
# e instala uv como gestor de paquetes
```

---

### Paso 3: Crear docker-compose.yml

Docker Compose orquesta los servicios de tu aplicación.

**Abre `starter/docker-compose.yml`** y descomenta el contenido.

```yaml
# docker-compose.yml define el servicio 'api'
# con el puerto 8000 expuesto
```

---

### Paso 4: Crear pyproject.toml

Este archivo define las dependencias del proyecto.

**Abre `starter/pyproject.toml`** y descomenta el contenido.

```toml
# pyproject.toml especifica Python 3.13+ y FastAPI como dependencia
```

---

### Paso 5: Crear la Aplicación FastAPI

**Abre `starter/src/main.py`** y descomenta el código paso a paso.

---

### Paso 6: Ejecutar el Proyecto

Una vez descomentado todo:

```bash
# Construir y ejecutar
docker compose up --build

# Deberías ver:
# api-1  | INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

### Paso 7: Verificar

1. Abre `http://localhost:8000` en tu navegador
2. Abre `http://localhost:8000/docs` para ver la documentación

---

## ✅ Checklist de Verificación

- [ ] Docker Compose ejecuta sin errores
- [ ] La API responde en `http://localhost:8000`
- [ ] La documentación está disponible en `/docs`
- [ ] Entiendes cada línea del Dockerfile

---

## 🔗 Navegación

[← Volver a Prácticas](../README.md) | [Siguiente: Type Hints →](../02-ejercicio-type-hints/)
