# 🐳 Práctica 03: Docker Compose Stack

## 🎯 Objetivo

Crear un stack completo con Docker Compose: API FastAPI + PostgreSQL + Redis, aprendiendo a orquestar múltiples servicios.

---

## 📋 Conceptos que Aprenderás

- Definir múltiples servicios en docker-compose.yml
- Configurar redes para comunicación entre contenedores
- Usar volúmenes para persistencia de datos
- Gestionar variables de entorno con archivos .env
- Implementar healthchecks y dependencias

---

## 🚀 Ejercicio

### Paso 1: Estructura del Proyecto

```
starter/
├── docker-compose.yml    # Orquestación (lo crearás)
├── Dockerfile            # Ya creado
├── .env.example          # Template de variables
├── .env                  # Tus variables (lo crearás)
├── src/
│   ├── main.py           # Aplicación FastAPI
│   ├── config.py         # Configuración
│   └── database.py       # Conexión a DB
└── requirements.txt
```

### Paso 2: Configurar Variables de Entorno

```bash
cd starter

# Copiar template
cp .env.example .env

# Editar con tus valores (o usar los defaults)
cat .env
```

### Paso 3: Crear docker-compose.yml

Abre `starter/docker-compose.yml` y descomenta paso a paso.

#### Servicio API

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
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
```

**Puntos clave:**
- `depends_on` con `condition: service_healthy` espera a que DB esté lista
- `@db:5432` usa el nombre del servicio como hostname
- Variables interpoladas desde `.env`

#### Servicio PostgreSQL

```yaml
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
```

**Puntos clave:**
- `postgres:17-alpine` es imagen oficial y ligera
- `volumes: pgdata:/...` persiste datos
- `healthcheck` verifica que PostgreSQL está listo

#### Servicio Redis

```yaml
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redisdata:/data
    networks:
      - backend
```

**Puntos clave:**
- `--appendonly yes` persiste datos
- Sin healthcheck (Redis inicia muy rápido)

#### Volúmenes y Redes

```yaml
volumes:
  pgdata:
  redisdata:

networks:
  backend:
    driver: bridge
```

### Paso 4: Levantar el Stack

```bash
# Construir y levantar todo
docker compose up --build

# O en background
docker compose up -d --build

# Ver estado de servicios
docker compose ps

# Ver logs de un servicio específico
docker compose logs api
docker compose logs db
```

### Paso 5: Verificar Conexiones

```bash
# Probar API
curl http://localhost:8000/health

# Verificar conexión a DB
curl http://localhost:8000/db-check

# Verificar conexión a Redis
curl http://localhost:8000/redis-check
```

### Paso 6: Interactuar con Servicios

```bash
# Conectar a PostgreSQL
docker compose exec db psql -U appuser -d appdb

# Conectar a Redis
docker compose exec redis redis-cli

# Ejecutar comando en API
docker compose exec api python -c "print('Hello from container!')"
```

### Paso 7: Gestionar el Stack

```bash
# Detener servicios
docker compose stop

# Iniciar servicios detenidos
docker compose start

# Reiniciar un servicio
docker compose restart api

# Detener y eliminar contenedores
docker compose down

# Detener, eliminar contenedores Y volúmenes (¡cuidado!)
docker compose down -v
```

---

## 🧪 Verificación

```bash
python test_compose.py
```

Tests que deben pasar:
- ✅ Todos los servicios inician
- ✅ API conecta a PostgreSQL
- ✅ API conecta a Redis
- ✅ Datos persisten después de restart

---

## 📝 docker-compose.yml Completo

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
      - REDIS_URL=redis://redis:6379/0
      - DEBUG=true
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - backend
    restart: unless-stopped

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

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redisdata:/data
    networks:
      - backend
    restart: unless-stopped

volumes:
  pgdata:
  redisdata:

networks:
  backend:
    driver: bridge
```

---

## 🎯 Desafío Extra

1. Agrega un servicio `adminer` para administrar PostgreSQL vía web
2. Agrega healthcheck al servicio Redis
3. Crea un archivo `docker-compose.override.yml` para desarrollo

```yaml
# docker-compose.override.yml (desarrollo)
services:
  api:
    volumes:
      - ./src:/app/src  # Hot reload
    command: uvicorn src.main:app --host 0.0.0.0 --reload

  db:
    ports:
      - "5432:5432"  # Acceso directo
```

---

## 🔗 Siguiente

Continúa con [04-github-actions-cicd](../04-github-actions-cicd/) para automatizar CI/CD.
