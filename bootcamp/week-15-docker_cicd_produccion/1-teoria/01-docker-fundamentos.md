# 🐳 Docker: Fundamentos de Containerización

## 🎯 Objetivos de Aprendizaje

- Entender qué es Docker y por qué usarlo
- Conocer la diferencia entre contenedores y máquinas virtuales
- Comprender los componentes principales de Docker
- Aprender comandos básicos de Docker
- Entender el flujo de trabajo con contenedores

---

## 📋 Tabla de Contenidos

1. [¿Qué es Docker?](#qué-es-docker)
2. [Contenedores vs Máquinas Virtuales](#contenedores-vs-máquinas-virtuales)
3. [Arquitectura de Docker](#arquitectura-de-docker)
4. [Componentes Principales](#componentes-principales)
5. [Comandos Esenciales](#comandos-esenciales)
6. [Flujo de Trabajo](#flujo-de-trabajo)
7. [Por qué Docker para FastAPI](#por-qué-docker-para-fastapi)

---

## ¿Qué es Docker?

Docker es una plataforma de **containerización** que permite empaquetar aplicaciones junto con todas sus dependencias en unidades estandarizadas llamadas **contenedores**.

### El Problema que Resuelve

```
❌ Sin Docker:
"Funciona en mi máquina" → No funciona en producción
- Diferentes versiones de Python
- Dependencias faltantes
- Configuraciones distintas
- Sistemas operativos diferentes

✅ Con Docker:
"Funciona en mi contenedor" → Funciona en CUALQUIER lugar
- Mismo Python siempre
- Todas las dependencias incluidas
- Configuración idéntica
- Aislamiento del sistema host
```

### Analogía del Contenedor de Envío

Piensa en Docker como los **contenedores de envío marítimo**:

- **Antes**: Cada producto se cargaba de forma diferente
- **Después**: Todo va en contenedores estándar que cualquier barco puede transportar

```
📦 Contenedor Docker = Tu app + Python + Dependencias + Config
    ↓
🚢 Puede ejecutarse en cualquier máquina con Docker
    - Tu laptop (Windows/Mac/Linux)
    - Servidor de staging
    - Servidor de producción
    - AWS, Google Cloud, Azure...
```

---

## Contenedores vs Máquinas Virtuales

![Diagrama comparativo](../0-assets/01-docker-architecture.svg)

### Máquinas Virtuales (VMs)

```
┌─────────────────────────────────────────────────┐
│              Máquina Virtual                     │
├─────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐         │
│  │  App A  │  │  App B  │  │  App C  │         │
│  ├─────────┤  ├─────────┤  ├─────────┤         │
│  │ Libs/   │  │ Libs/   │  │ Libs/   │         │
│  │ Bins    │  │ Bins    │  │ Bins    │         │
│  ├─────────┤  ├─────────┤  ├─────────┤         │
│  │Guest OS │  │Guest OS │  │Guest OS │  ← Cada VM
│  │(Ubuntu) │  │(Debian) │  │(CentOS) │    tiene
│  └─────────┘  └─────────┘  └─────────┘    su propio
├─────────────────────────────────────────────────┤    OS
│              Hypervisor (VMware, VirtualBox)    │
├─────────────────────────────────────────────────┤
│              Host Operating System               │
├─────────────────────────────────────────────────┤
│              Hardware (CPU, RAM, Disco)          │
└─────────────────────────────────────────────────┘
```

### Contenedores Docker

```
┌─────────────────────────────────────────────────┐
│              Docker Containers                   │
├─────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐         │
│  │  App A  │  │  App B  │  │  App C  │         │
│  ├─────────┤  ├─────────┤  ├─────────┤         │
│  │ Libs/   │  │ Libs/   │  │ Libs/   │         │
│  │ Bins    │  │ Bins    │  │ Bins    │         │
│  └─────────┘  └─────────┘  └─────────┘         │
├─────────────────────────────────────────────────┤
│              Docker Engine                       │ ← Comparte
├─────────────────────────────────────────────────┤   el kernel
│              Host Operating System               │   del host
├─────────────────────────────────────────────────┤
│              Hardware (CPU, RAM, Disco)          │
└─────────────────────────────────────────────────┘
```

### Comparación

| Característica | VMs | Contenedores |
|----------------|-----|--------------|
| **Tamaño** | GBs (incluye OS completo) | MBs (solo app + deps) |
| **Inicio** | Minutos | Segundos |
| **Aislamiento** | Completo (hardware virtual) | A nivel de proceso |
| **Rendimiento** | Overhead del hypervisor | Casi nativo |
| **Densidad** | ~10-20 por servidor | ~100s por servidor |
| **Portabilidad** | Menos portable | Muy portable |

---

## Arquitectura de Docker

### Componentes del Ecosistema

```
┌──────────────────────────────────────────────────────────────┐
│                        Docker CLI                             │
│                   (docker build, run, ...)                   │
└──────────────────────────┬───────────────────────────────────┘
                           │ REST API
┌──────────────────────────▼───────────────────────────────────┐
│                     Docker Daemon                             │
│                      (dockerd)                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Images    │  │ Containers  │  │     Networks        │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│  ┌─────────────┐  ┌─────────────────────────────────────┐   │
│  │   Volumes   │  │           Registry Client           │   │
│  └─────────────┘  └─────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│                    Docker Registry                            │
│              (Docker Hub, ghcr.io, ECR...)                   │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  python:3.13  │  postgres:17  │  redis:7  │  ...    │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

### Docker Client (CLI)

El **Docker CLI** es la interfaz de línea de comandos que usamos para interactuar con Docker:

```bash
# Ejemplos de comandos del CLI
docker build -t my-app .      # Construir imagen
docker run my-app             # Ejecutar contenedor
docker ps                     # Listar contenedores
docker images                 # Listar imágenes
docker logs container_id      # Ver logs
```

### Docker Daemon (dockerd)

El **daemon** es el servicio que corre en background y hace el trabajo real:

- Construye imágenes
- Ejecuta contenedores
- Gestiona redes y volúmenes
- Se comunica con registries

### Docker Registry

Un **registry** es un repositorio de imágenes Docker:

- **Docker Hub** (hub.docker.com) - Registry público por defecto
- **GitHub Container Registry** (ghcr.io)
- **Amazon ECR**, **Google GCR**, **Azure ACR**
- Registries privados

---

## Componentes Principales

### 1. Imagen (Image)

Una **imagen** es una plantilla de solo lectura con instrucciones para crear un contenedor:

```
📦 Imagen = Snapshot de tu aplicación
├── Sistema base (e.g., Debian slim)
├── Python 3.13
├── Dependencias (FastAPI, SQLAlchemy, etc.)
├── Tu código fuente
└── Configuración de inicio
```

Las imágenes se construyen en **capas** (layers):

```dockerfile
# Cada instrucción crea una capa
FROM python:3.13-slim        # Capa 1: Imagen base
WORKDIR /app                  # Capa 2: Crear directorio
COPY requirements.txt .       # Capa 3: Copiar archivo
RUN pip install -r req.txt    # Capa 4: Instalar deps
COPY . .                      # Capa 5: Copiar código
```

### 2. Contenedor (Container)

Un **contenedor** es una instancia ejecutable de una imagen:

```
🏃 Contenedor = Imagen + Capa de escritura
├── Todo lo de la imagen (read-only)
└── Capa de escritura para cambios en runtime
```

```bash
# Una imagen, múltiples contenedores
docker run -d --name api-1 my-fastapi-app
docker run -d --name api-2 my-fastapi-app
docker run -d --name api-3 my-fastapi-app
# 3 contenedores independientes de la misma imagen
```

### 3. Dockerfile

Un **Dockerfile** es un archivo de texto con instrucciones para construir una imagen:

```dockerfile
# Dockerfile básico para FastAPI
FROM python:3.13-slim

WORKDIR /app

# Instalar dependencias primero (mejor caché)
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

# Copiar código
COPY src/ ./src/

# Puerto y comando
EXPOSE 8000
CMD ["uv", "run", "fastapi", "run", "src/main.py", "--host", "0.0.0.0"]
```

### 4. Volumen (Volume)

Un **volumen** persiste datos más allá del ciclo de vida del contenedor:

```bash
# Sin volumen: datos se pierden al eliminar contenedor
docker run postgres

# Con volumen: datos persisten
docker run -v postgres_data:/var/lib/postgresql/data postgres
```

### 5. Red (Network)

Las **redes** permiten comunicación entre contenedores:

```bash
# Crear red
docker network create my-network

# Conectar contenedores a la red
docker run --network my-network --name api my-app
docker run --network my-network --name db postgres

# 'api' puede conectarse a 'db' usando el nombre como hostname
# postgresql://user:pass@db:5432/mydb
```

---

## Comandos Esenciales

### Gestión de Imágenes

```bash
# Construir imagen desde Dockerfile
docker build -t my-app:v1 .

# Listar imágenes locales
docker images

# Descargar imagen de registry
docker pull python:3.13-slim

# Subir imagen a registry
docker push myuser/my-app:v1

# Eliminar imagen
docker rmi my-app:v1

# Eliminar imágenes no usadas
docker image prune
```

### Gestión de Contenedores

```bash
# Ejecutar contenedor (modo interactivo)
docker run -it python:3.13 bash

# Ejecutar contenedor (modo detached/background)
docker run -d --name api -p 8000:8000 my-app

# Listar contenedores en ejecución
docker ps

# Listar todos los contenedores (incluidos detenidos)
docker ps -a

# Ver logs de un contenedor
docker logs api
docker logs -f api  # Follow (tiempo real)

# Ejecutar comando en contenedor existente
docker exec -it api bash

# Detener contenedor
docker stop api

# Iniciar contenedor detenido
docker start api

# Eliminar contenedor
docker rm api

# Eliminar contenedores detenidos
docker container prune
```

### Mapeo de Puertos

```bash
# Sintaxis: -p HOST_PORT:CONTAINER_PORT
docker run -p 8000:8000 my-app    # localhost:8000 → container:8000
docker run -p 3000:8000 my-app    # localhost:3000 → container:8000
docker run -p 8000:8000 -p 5432:5432 my-app  # Múltiples puertos
```

### Variables de Entorno

```bash
# Pasar variable individual
docker run -e DATABASE_URL="postgresql://..." my-app

# Pasar múltiples variables
docker run -e DB_HOST=localhost -e DB_PORT=5432 my-app

# Usar archivo .env
docker run --env-file .env my-app
```

### Volúmenes

```bash
# Volumen nombrado (Docker lo gestiona)
docker run -v app_data:/app/data my-app

# Bind mount (carpeta local)
docker run -v $(pwd)/src:/app/src my-app

# Montar como solo lectura
docker run -v $(pwd)/config:/app/config:ro my-app
```

---

## Flujo de Trabajo

### Desarrollo Local con Docker

```
1. Escribir código → 2. Crear Dockerfile → 3. Build → 4. Run → 5. Test
     ↑                                                              │
     └──────────────────────────────────────────────────────────────┘
                        (iterar)
```

```bash
# 1. Escribir tu aplicación FastAPI
# src/main.py, etc.

# 2. Crear Dockerfile
# (ver siguiente sección)

# 3. Construir imagen
docker build -t my-fastapi-app .

# 4. Ejecutar contenedor
docker run -d -p 8000:8000 --name api my-fastapi-app

# 5. Probar
curl http://localhost:8000/health

# 6. Ver logs si hay problemas
docker logs api

# 7. Detener y eliminar para reconstruir
docker stop api && docker rm api
docker build -t my-fastapi-app . && docker run -d -p 8000:8000 --name api my-fastapi-app
```

### Desarrollo con Hot Reload

Para desarrollo, monta tu código como volumen:

```bash
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/src:/app/src \
  --name api-dev \
  my-fastapi-app \
  fastapi dev src/main.py --host 0.0.0.0
```

Cambios en `src/` se reflejan inmediatamente sin reconstruir.

---

## Por qué Docker para FastAPI

### 1. Consistencia de Entornos

```python
# requirements.txt local vs producción
# LOCAL: Python 3.11, uvicorn 0.25
# PROD:  Python 3.9,  uvicorn 0.20  ← Bugs!

# Con Docker: SIEMPRE igual
FROM python:3.13-slim
# Mismo Python, mismas dependencias, mismo comportamiento
```

### 2. Dependencias Aisladas

```bash
# Sin Docker: conflictos entre proyectos
proyecto-a/  → necesita sqlalchemy 1.4
proyecto-b/  → necesita sqlalchemy 2.0
# 😱 Conflicto en tu sistema

# Con Docker: cada proyecto aislado
docker run proyecto-a  # sqlalchemy 1.4
docker run proyecto-b  # sqlalchemy 2.0
# ✅ Sin conflictos
```

### 3. Fácil Onboarding

```bash
# Sin Docker (nuevo desarrollador):
1. Instalar Python 3.13
2. Instalar PostgreSQL 17
3. Instalar Redis
4. Crear virtualenv
5. Instalar dependencias
6. Configurar variables de entorno
7. Crear base de datos
8. Ejecutar migraciones
# 😫 2 horas después...

# Con Docker:
docker compose up
# ✅ 2 minutos
```

### 4. Deploy Simplificado

```bash
# Local → Staging → Producción
# Misma imagen, misma configuración base
docker build -t my-app:v1.2.3 .
docker push my-app:v1.2.3

# En producción
docker pull my-app:v1.2.3
docker run my-app:v1.2.3
```

### 5. Escalabilidad

```bash
# Escalar horizontalmente es trivial
docker run -d --name api-1 my-app
docker run -d --name api-2 my-app
docker run -d --name api-3 my-app
# 3 instancias balanceadas con un load balancer
```

---

## 🧪 Verificación de Conocimientos

### Conceptos Clave

1. ¿Cuál es la diferencia principal entre un contenedor y una VM?
2. ¿Qué es una imagen Docker?
3. ¿Qué hace el Docker daemon?
4. ¿Cómo persisten datos los contenedores?

### Comandos Prácticos

```bash
# 1. Ejecuta un contenedor de Python interactivo
docker run -it python:3.13 python

# 2. Lista todas las imágenes locales
docker images

# 3. Ejecuta nginx en background, puerto 8080
docker run -d -p 8080:80 nginx

# 4. Ve los logs del contenedor nginx
docker logs <container_id>

# 5. Detén y elimina todos los contenedores
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```

---

## 📚 Recursos Adicionales

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub - Official Images](https://hub.docker.com/search?image_filter=official)
- [Play with Docker](https://labs.play-with-docker.com/) - Sandbox gratuito

---

## 🔗 Siguiente

Continúa con [02-dockerfile-optimizado.md](02-dockerfile-optimizado.md) para aprender a crear Dockerfiles eficientes para FastAPI.
