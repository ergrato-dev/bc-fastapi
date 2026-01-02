# 🚀 Proyecto Semana 15: API Production-Ready

## 📋 Descripción

En este proyecto integrador crearás una **API lista para producción** con:

- 🐳 **Dockerfile** multi-stage optimizado
- 🎼 **Docker Compose** para desarrollo local
- 🔄 **GitHub Actions** para CI/CD
- 🔒 **Configuración de seguridad** (non-root, healthchecks)
- 📊 **Monitoreo básico** (health endpoints, métricas)

---

## 🎯 Objetivos de Aprendizaje

Al completar este proyecto serás capaz de:

1. ✅ Crear Dockerfiles optimizados para producción
2. ✅ Orquestar servicios con Docker Compose
3. ✅ Implementar pipelines CI/CD con GitHub Actions
4. ✅ Configurar health checks y monitoreo
5. ✅ Aplicar mejores prácticas de seguridad en contenedores

---

## 📁 Estructura del Proyecto

```
starter/
├── .github/
│   └── workflows/
│       └── ci.yml              # TODO: Pipeline CI/CD
├── src/
│   ├── __init__.py
│   ├── main.py                 # TODO: FastAPI app
│   ├── config.py               # TODO: Configuración
│   ├── database.py             # TODO: Conexión DB
│   ├── models.py               # TODO: Modelos SQLAlchemy
│   ├── schemas.py              # TODO: Schemas Pydantic
│   └── routers/
│       ├── __init__.py
│       ├── health.py           # TODO: Health endpoints
│       └── tasks.py            # TODO: CRUD de tareas
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # TODO: Fixtures
│   └── test_api.py             # TODO: Tests
├── Dockerfile                  # TODO: Multi-stage build
├── docker-compose.yml          # TODO: Stack completo
├── docker-compose.prod.yml     # TODO: Override producción
├── .env.example
├── requirements.txt
└── pyproject.toml
```

---

## 🛠️ Requisitos Funcionales

### 1. API de Gestión de Tareas

La API debe permitir:

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/health` | GET | Health check básico |
| `/health/ready` | GET | Readiness check (incluye DB) |
| `/health/live` | GET | Liveness check |
| `/api/v1/tasks` | GET | Listar tareas (paginación) |
| `/api/v1/tasks` | POST | Crear tarea |
| `/api/v1/tasks/{id}` | GET | Obtener tarea |
| `/api/v1/tasks/{id}` | PUT | Actualizar tarea |
| `/api/v1/tasks/{id}` | DELETE | Eliminar tarea |

### 2. Modelo de Datos

```python
class Task:
    id: int
    title: str
    description: str | None
    completed: bool = False
    priority: str = "medium"  # low, medium, high
    created_at: datetime
    updated_at: datetime
```

### 3. Docker Compose Stack

Servicios requeridos:
- **api**: Aplicación FastAPI
- **db**: PostgreSQL 17
- **redis**: Cache (opcional)

---

## 📝 Tareas a Completar

### Nivel Básico (70 puntos)

- [ ] **T1** (15 pts): Dockerfile multi-stage funcional
- [ ] **T2** (15 pts): Docker Compose con API + PostgreSQL
- [ ] **T3** (15 pts): Health endpoints funcionando
- [ ] **T4** (15 pts): CRUD de tareas completo
- [ ] **T5** (10 pts): Tests pasando

### Nivel Intermedio (+20 puntos)

- [ ] **T6** (10 pts): GitHub Actions CI pipeline
- [ ] **T7** (10 pts): Usuario non-root en contenedor

### Nivel Avanzado (+10 puntos)

- [ ] **T8** (5 pts): Docker Compose para producción
- [ ] **T9** (5 pts): Caché con Redis

---

## 🚀 Instrucciones

### Paso 1: Configuración Inicial

```bash
cd starter

# Copiar variables de entorno
cp .env.example .env

# Revisar la estructura
tree -a
```

### Paso 2: Completar el Dockerfile

Abre `Dockerfile` y completa los TODOs:

1. Stage builder con dependencias
2. Stage runtime optimizado
3. Usuario non-root
4. Health check

### Paso 3: Completar Docker Compose

Abre `docker-compose.yml` y configura:

1. Servicio `api` con build context
2. Servicio `db` PostgreSQL
3. Networks y volumes
4. Health checks

### Paso 4: Implementar la API

Completa los archivos en `src/`:

1. `config.py` - Pydantic Settings
2. `database.py` - SQLAlchemy async
3. `models.py` - Modelo Task
4. `schemas.py` - Schemas Pydantic
5. `routers/health.py` - Health endpoints
6. `routers/tasks.py` - CRUD endpoints
7. `main.py` - FastAPI app

### Paso 5: Escribir Tests

Completa `tests/test_api.py` con:

1. Tests de health endpoints
2. Tests CRUD de tareas
3. Tests de validación

### Paso 6: Pipeline CI/CD

Completa `.github/workflows/ci.yml`:

1. Job de lint
2. Job de tests
3. Job de build Docker

### Paso 7: Verificar Todo

```bash
# Construir y levantar
docker compose up --build

# En otra terminal, probar
curl http://localhost:8000/health
curl http://localhost:8000/docs

# Ejecutar tests
docker compose exec api pytest -v

# Verificar logs
docker compose logs -f api
```

---

## ✅ Criterios de Evaluación

### Dockerfile (30 puntos)

| Criterio | Puntos |
|----------|--------|
| Multi-stage build funcional | 10 |
| Imagen < 200MB | 5 |
| Usuario non-root | 5 |
| Health check configurado | 5 |
| No vulnerabilidades críticas | 5 |

### Docker Compose (25 puntos)

| Criterio | Puntos |
|----------|--------|
| Servicios levantando correctamente | 10 |
| Variables de entorno externalizadas | 5 |
| Volúmenes persistentes | 5 |
| Health checks en servicios | 5 |

### API (25 puntos)

| Criterio | Puntos |
|----------|--------|
| Health endpoints funcionales | 5 |
| CRUD completo | 10 |
| Validación con Pydantic | 5 |
| Manejo de errores | 5 |

### CI/CD (10 puntos)

| Criterio | Puntos |
|----------|--------|
| Workflow ejecutándose | 5 |
| Jobs de lint/test/build | 5 |

### Tests (10 puntos)

| Criterio | Puntos |
|----------|--------|
| Cobertura > 70% | 5 |
| Tests significativos | 5 |

---

## 📚 Recursos de Apoyo

- [Teoría: Docker Fundamentos](../1-teoria/01-docker-fundamentos.md)
- [Teoría: Dockerfile Optimizado](../1-teoria/02-dockerfile-optimizado.md)
- [Teoría: Docker Compose](../1-teoria/03-docker-compose.md)
- [Teoría: GitHub Actions](../1-teoria/04-github-actions.md)
- [Práctica: Multi-stage Build](../2-practicas/02-multi-stage-build/)
- [Práctica: Compose Stack](../2-practicas/03-docker-compose-stack/)

---

## 🎯 Entregables

1. **Código fuente** en repositorio Git
2. **Screenshot** del workflow de GitHub Actions pasando
3. **Screenshot** de `docker compose ps` con servicios healthy
4. **Respuestas** a las preguntas de reflexión

### Preguntas de Reflexión

1. ¿Cuánto redujo el tamaño de la imagen usando multi-stage build?
2. ¿Qué beneficios tiene usar un usuario non-root?
3. ¿Cómo manejarías secrets en producción real?
4. ¿Qué agregarías para mejorar el monitoreo?

---

## ⏱️ Tiempo Estimado

- Dockerfile + Compose: 1.5 horas
- API + Models: 1.5 horas  
- Tests: 30 minutos
- CI/CD: 30 minutos
- **Total**: ~4 horas

---

## 🔗 Navegación

- ⬅️ [Prácticas](../2-practicas/)
- ➡️ [Semana 16: Proyecto Final](../../week-16/)
- 🏠 [Inicio del Bootcamp](../../)
