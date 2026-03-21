# 🐳 Docker Compose: Orquestación de Servicios

## 🎯 Objetivos de Aprendizaje

- Entender qué es Docker Compose y cuándo usarlo
- Escribir archivos docker-compose.yml
- Configurar redes y volúmenes
- Gestionar variables de entorno
- Orquestar aplicaciones multi-contenedor

---

## 📋 Tabla de Contenidos

1. [¿Qué es Docker Compose?](#qué-es-docker-compose)
2. [Estructura del docker-compose.yml](#estructura-del-docker-composeyml)
3. [Servicios](#servicios)
4. [Redes](#redes)
5. [Volúmenes](#volúmenes)
6. [Variables de Entorno](#variables-de-entorno)
7. [Comandos Esenciales](#comandos-esenciales)
8. [Ejemplo Completo](#ejemplo-completo)

---

## ¿Qué es Docker Compose?

**Docker Compose** es una herramienta para definir y ejecutar aplicaciones Docker multi-contenedor usando un archivo YAML.

### El Problema

```bash
# Sin Docker Compose: múltiples comandos manuales
docker network create my-network

docker run -d --name db \
  --network my-network \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:17

docker run -d --name redis \
  --network my-network \
  redis:7

docker run -d --name api \
  --network my-network \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql://... \
  -e REDIS_URL=redis://redis:6379 \
  my-fastapi-app

# 😫 Difícil de recordar, propenso a errores
```

### La Solución

```yaml
# docker-compose.yml - Todo en un archivo
services:
  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis

  db:
    image: postgres:17
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7

volumes:
  pgdata:
```

```bash
# Un comando para todo
docker compose up
# ✅ Crea red, volúmenes, y levanta todos los servicios
```

---

## Estructura del docker-compose.yml

![Estructura Docker Compose](../0-assets/03-docker-compose-stack.svg)

### Estructura Básica

```yaml
# Versión de sintaxis (opcional en Compose V2+)
# version: "3.9"  # Ya no es necesario

# Servicios (contenedores)
services:
  nombre-servicio:
    # configuración...

# Volúmenes nombrados
volumes:
  nombre-volumen:

# Redes personalizadas
networks:
  nombre-red:

# Secretos (opcional)
secrets:
  nombre-secreto:

# Configuraciones (opcional)
configs:
  nombre-config:
```

### Ejemplo Mínimo

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
```

---

## Servicios

Un **servicio** define cómo ejecutar un contenedor.

### Usando una Imagen

```yaml
services:
  db:
    image: postgres:17-alpine
    # Usa imagen de Docker Hub
```

### Construyendo desde Dockerfile

```yaml
services:
  api:
    build: .
    # Busca Dockerfile en directorio actual

  api-custom:
    build:
      context: .
      dockerfile: Dockerfile.prod
      args:
        - APP_VERSION=1.0.0
    # Más opciones de build
```

### Puertos

```yaml
services:
  api:
    ports:
      - "8000:8000"        # HOST:CONTAINER
      - "127.0.0.1:8001:8001"  # Solo localhost
      - "8002"             # Puerto aleatorio del host
```

### Variables de Entorno

```yaml
services:
  api:
    environment:
      - DEBUG=true
      - DATABASE_URL=postgresql://user:pass@db:5432/app
    
    # O desde archivo
    env_file:
      - .env
      - .env.local
```

### Dependencias

```yaml
services:
  api:
    depends_on:
      - db
      - redis
    # api espera a que db y redis inicien (no que estén ready)

  api-with-healthcheck:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    # Espera a que db esté healthy
```

### Healthcheck

```yaml
services:
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  db:
    image: postgres:17
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
```

### Restart Policy

```yaml
services:
  api:
    restart: unless-stopped
    # Opciones:
    # - "no"           → Nunca reiniciar
    # - "always"       → Siempre reiniciar
    # - "on-failure"   → Solo si falla (exit code != 0)
    # - "unless-stopped" → Siempre, excepto si se detuvo manualmente
```

### Recursos

```yaml
services:
  api:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### Comando Personalizado

```yaml
services:
  api:
    command: uvicorn src.main:app --host 0.0.0.0 --reload
    # Sobrescribe CMD del Dockerfile

  worker:
    entrypoint: ["python", "-m"]
    command: ["celery", "worker"]
```

---

## Redes

Por defecto, Compose crea una red para todos los servicios del proyecto.

### Red por Defecto

```yaml
services:
  api:
    # ...
  db:
    # ...
# Compose crea automáticamente: proyecto_default
# api puede conectar a db usando hostname "db"
```

### Redes Personalizadas

```yaml
services:
  api:
    networks:
      - frontend
      - backend

  db:
    networks:
      - backend
    # db NO está en frontend, más seguro

  nginx:
    networks:
      - frontend

networks:
  frontend:
  backend:
```

### Configuración de Red

```yaml
networks:
  backend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
```

### Alias de Red

```yaml
services:
  db:
    networks:
      backend:
        aliases:
          - database
          - postgres
    # api puede usar "db", "database", o "postgres"
```

---

## Volúmenes

### Volúmenes Nombrados

```yaml
services:
  db:
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
    # Docker gestiona la ubicación
```

### Bind Mounts

```yaml
services:
  api:
    volumes:
      - ./src:/app/src          # Desarrollo: hot reload
      - ./logs:/app/logs        # Logs persistentes
```

### Volumen Read-Only

```yaml
services:
  api:
    volumes:
      - ./config:/app/config:ro  # Solo lectura
```

### Configuración de Volumen

```yaml
volumes:
  pgdata:
    driver: local
    driver_opts:
      type: none
      device: /data/postgres
      o: bind
```

---

## Variables de Entorno

### En docker-compose.yml

```yaml
services:
  api:
    environment:
      DEBUG: "true"
      LOG_LEVEL: info
```

### Desde Archivo .env

```bash
# .env
DATABASE_URL=postgresql://user:pass@db:5432/app
SECRET_KEY=super-secret-key
DEBUG=false
```

```yaml
services:
  api:
    env_file:
      - .env
```

### Interpolación de Variables

```yaml
# Usar variables del shell o .env
services:
  api:
    image: myapp:${APP_VERSION:-latest}
    environment:
      - DATABASE_URL=${DATABASE_URL}
```

### Archivo .env para Compose

```bash
# .env (en mismo directorio que docker-compose.yml)
COMPOSE_PROJECT_NAME=myproject
POSTGRES_VERSION=17
APP_PORT=8000
```

```yaml
services:
  db:
    image: postgres:${POSTGRES_VERSION}
  
  api:
    ports:
      - "${APP_PORT}:8000"
```

---

## Comandos Esenciales

### Ciclo de Vida

```bash
# Construir imágenes
docker compose build

# Levantar servicios (foreground)
docker compose up

# Levantar servicios (background)
docker compose up -d

# Levantar y reconstruir
docker compose up --build

# Detener servicios
docker compose stop

# Detener y eliminar contenedores
docker compose down

# Detener, eliminar contenedores Y volúmenes
docker compose down -v

# Reiniciar servicios
docker compose restart
```

### Ver Estado

```bash
# Listar contenedores del proyecto
docker compose ps

# Ver logs de todos los servicios
docker compose logs

# Ver logs de un servicio específico
docker compose logs api

# Seguir logs en tiempo real
docker compose logs -f api

# Ver últimas 100 líneas
docker compose logs --tail=100 api
```

### Ejecutar Comandos

```bash
# Ejecutar comando en servicio existente
docker compose exec api bash
docker compose exec db psql -U postgres

# Ejecutar comando en nuevo contenedor
docker compose run --rm api pytest
docker compose run --rm api python manage.py migrate
```

### Escalar Servicios

```bash
# Escalar un servicio
docker compose up -d --scale api=3

# En docker-compose.yml
services:
  api:
    deploy:
      replicas: 3
```

### Otros Comandos Útiles

```bash
# Ver configuración procesada
docker compose config

# Eliminar contenedores detenidos
docker compose rm

# Ver uso de recursos
docker compose top

# Pausar/reanudar servicios
docker compose pause
docker compose unpause
```

---

## Ejemplo Completo

### Estructura del Proyecto

```
my-fastapi-project/
├── docker-compose.yml
├── docker-compose.override.yml  # Desarrollo
├── docker-compose.prod.yml      # Producción
├── .env.example
├── .env                         # No en git
├── Dockerfile
└── src/
    └── main.py
```

### docker-compose.yml (Base)

```yaml
services:
  # ===========================================
  # API FastAPI
  # ===========================================
  api:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - backend
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  # ===========================================
  # PostgreSQL Database
  # ===========================================
  db:
    image: postgres:17-alpine
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  # ===========================================
  # Redis Cache
  # ===========================================
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redisdata:/data
    networks:
      - backend
    restart: unless-stopped

# ===========================================
# Volumes
# ===========================================
volumes:
  pgdata:
  redisdata:

# ===========================================
# Networks
# ===========================================
networks:
  backend:
    driver: bridge
```

### docker-compose.override.yml (Desarrollo)

```yaml
# Se aplica automáticamente en desarrollo
services:
  api:
    build:
      target: builder  # Usar stage de desarrollo
    ports:
      - "8000:8000"
    volumes:
      - ./src:/app/src  # Hot reload
    environment:
      - DEBUG=true
      - LOG_LEVEL=debug
    command: uvicorn src.main:app --host 0.0.0.0 --reload

  db:
    ports:
      - "5432:5432"  # Acceso directo para herramientas

  redis:
    ports:
      - "6379:6379"
```

### docker-compose.prod.yml (Producción)

```yaml
services:
  api:
    build:
      target: runtime
    ports:
      - "8000:8000"
    environment:
      - DEBUG=false
      - LOG_LEVEL=info
    command: uvicorn src.main:app --host 0.0.0.0 --workers 4
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
```

### .env.example

```bash
# Copiar a .env y completar valores

# PostgreSQL
POSTGRES_USER=appuser
POSTGRES_PASSWORD=changeme
POSTGRES_DB=appdb

# Application
SECRET_KEY=change-this-in-production
DEBUG=false
LOG_LEVEL=info

# Redis
REDIS_URL=redis://redis:6379/0
```

### Uso

```bash
# Desarrollo (usa override automáticamente)
docker compose up

# Producción
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Ver configuración resultante
docker compose -f docker-compose.yml -f docker-compose.prod.yml config
```

---

## 🧪 Verificación

```bash
# 1. Levantar todo
docker compose up -d

# 2. Verificar servicios
docker compose ps

# 3. Ver logs
docker compose logs api

# 4. Probar API
curl http://localhost:8000/health

# 5. Conectar a DB
docker compose exec db psql -U appuser -d appdb

# 6. Detener todo
docker compose down

# 7. Limpiar todo (incluye volúmenes)
docker compose down -v
```

---

## 📚 Recursos Adicionales

- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Compose Specification](https://compose-spec.io/)
- [Networking in Compose](https://docs.docker.com/compose/networking/)

---

## 🔗 Siguiente

Continúa con [04-github-actions.md](04-github-actions.md) para aprender CI/CD con GitHub Actions.
