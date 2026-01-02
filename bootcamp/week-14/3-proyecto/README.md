# 🛡️ Proyecto Semana 14: API Segura con Observabilidad

## 📋 Descripción

En este proyecto construirás una **API de gestión de tareas** con todas las capas de seguridad y observabilidad necesarias para producción:

- **Rate Limiting** con slowapi y Redis
- **Seguridad** con headers y CORS configurados
- **Logging estructurado** con structlog
- **Métricas Prometheus** con instrumentación automática y custom
- **Health Checks** para Kubernetes/Docker

---

## 🎯 Objetivos de Aprendizaje

Al completar este proyecto serás capaz de:

- ✅ Implementar rate limiting por usuario y endpoint
- ✅ Configurar headers de seguridad (CSP, HSTS, etc.)
- ✅ Crear logging estructurado con contexto de request
- ✅ Exponer métricas de negocio en formato Prometheus
- ✅ Implementar health checks completos
- ✅ Integrar todos los componentes en una aplicación cohesiva

---

## 📁 Estructura del Proyecto

```
3-proyecto/
├── README.md                 # Este archivo
├── starter/                  # Código inicial (completa los TODOs)
│   ├── pyproject.toml
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── .env.example
│   ├── src/
│   │   ├── main.py           # Aplicación principal
│   │   ├── config.py         # Configuración centralizada
│   │   ├── database.py       # Conexión a SQLite
│   │   ├── models.py         # Modelos SQLAlchemy
│   │   ├── schemas.py        # Schemas Pydantic
│   │   ├── security/
│   │   │   ├── __init__.py
│   │   │   ├── rate_limit.py # Rate limiting config
│   │   │   └── headers.py    # Security headers middleware
│   │   ├── observability/
│   │   │   ├── __init__.py
│   │   │   ├── logging.py    # Logging estructurado
│   │   │   ├── metrics.py    # Métricas Prometheus
│   │   │   └── health.py     # Health checks
│   │   └── routers/
│   │       ├── __init__.py
│   │       ├── tasks.py      # CRUD de tareas
│   │       └── auth.py       # Autenticación simple
│   └── tests/
│       ├── __init__.py
│       ├── test_rate_limit.py
│       ├── test_security.py
│       ├── test_logging.py
│       └── test_health.py
└── solution/                 # Solución completa (referencia)
```

---

## 🚀 Requisitos Funcionales

### 1. Rate Limiting (20 puntos)

| Endpoint | Límite | Ventana |
|----------|--------|---------|
| `POST /auth/login` | 5 requests | 1 minuto |
| `POST /tasks` | 20 requests | 1 minuto |
| `GET /tasks` | 60 requests | 1 minuto |
| `PUT/DELETE /tasks/{id}` | 30 requests | 1 minuto |

**Requisitos:**
- [ ] Configurar slowapi con límites por endpoint
- [ ] Retornar headers `X-RateLimit-*` en respuestas
- [ ] Responder 429 cuando se excede el límite
- [ ] (Bonus) Usar Redis como backend

### 2. Seguridad (20 puntos)

**Headers requeridos:**
- [ ] `X-Content-Type-Options: nosniff`
- [ ] `X-Frame-Options: DENY`
- [ ] `X-XSS-Protection: 1; mode=block`
- [ ] `Strict-Transport-Security` (HSTS)
- [ ] `Content-Security-Policy` básico

**CORS:**
- [ ] Configurar orígenes permitidos desde `.env`
- [ ] Permitir métodos GET, POST, PUT, DELETE
- [ ] Permitir headers Authorization y Content-Type

### 3. Logging Estructurado (20 puntos)

**Requisitos:**
- [ ] Usar structlog con formato JSON
- [ ] Request ID único por request (header o generado)
- [ ] Loggear: method, path, status_code, duration_ms
- [ ] Enmascarar datos sensibles (password, token)
- [ ] Niveles apropiados (INFO para requests, ERROR para excepciones)

### 4. Métricas Prometheus (20 puntos)

**Métricas automáticas:**
- [ ] `http_requests_total` (counter)
- [ ] `http_request_duration_seconds` (histogram)

**Métricas de negocio:**
- [ ] `tasks_created_total` - Tareas creadas
- [ ] `tasks_completed_total` - Tareas completadas
- [ ] `active_tasks_gauge` - Tareas activas (pendientes)

### 5. Health Checks (20 puntos)

| Endpoint | Tipo | Verificaciones |
|----------|------|----------------|
| `/health/live` | Liveness | Aplicación corriendo |
| `/health/ready` | Readiness | DB conectada, Redis (si aplica) |

**Formato de respuesta:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "service": "task-api",
  "version": "1.0.0",
  "checks": {
    "database": {"healthy": true, "latency_ms": 5},
    "redis": {"healthy": true, "latency_ms": 2}
  }
}
```

---

## 🔧 Instrucciones de Implementación

### Paso 1: Configurar Entorno

```bash
cd starter

# Copiar variables de entorno
cp .env.example .env

# Opción A: Con Docker (recomendado)
docker compose up --build

# Opción B: Local con uv
uv sync
uv run uvicorn src.main:app --reload
```

### Paso 2: Implementar TODOs

Abre cada archivo en `starter/src/` y completa los TODOs:

1. **`security/rate_limit.py`** - Configurar slowapi
2. **`security/headers.py`** - Middleware de headers
3. **`observability/logging.py`** - Configurar structlog
4. **`observability/metrics.py`** - Métricas Prometheus
5. **`observability/health.py`** - Health checks
6. **`main.py`** - Integrar todos los componentes

### Paso 3: Verificar Funcionamiento

```bash
# Rate limiting
for i in {1..10}; do curl -X POST http://localhost:8000/auth/login; done

# Security headers
curl -I http://localhost:8000/

# Métricas
curl http://localhost:8000/metrics

# Health checks
curl http://localhost:8000/health/live
curl http://localhost:8000/health/ready

# Logs (ver output del servidor)
```

### Paso 4: Ejecutar Tests

```bash
uv run pytest tests/ -v
```

---

## 📊 Criterios de Evaluación

| Componente | Puntos | Criterios |
|------------|--------|-----------|
| Rate Limiting | 20 | Límites correctos, headers, 429 |
| Seguridad | 20 | Headers presentes, CORS funcional |
| Logging | 20 | JSON, request_id, sensible masked |
| Métricas | 20 | /metrics expone todas las métricas |
| Health Checks | 20 | Liveness simple, readiness con checks |
| **Total** | **100** | |

### Niveles de Logro

- **Excelente (90-100)**: Todos los requisitos + bonus
- **Bueno (70-89)**: Requisitos principales funcionando
- **Suficiente (50-69)**: Funcionalidad básica
- **Insuficiente (<50)**: No cumple requisitos mínimos

---

## 🎁 Bonus (10 puntos extra)

- [ ] Rate limiting con Redis (persistente entre reinicios)
- [ ] Métricas de latencia de base de datos
- [ ] Dashboard Grafana básico (archivo JSON)
- [ ] Startup probe adicional
- [ ] Documentación OpenAPI con ejemplos de errores 429

---

## 📚 Recursos

- [slowapi Documentation](https://slowapi.readthedocs.io/)
- [structlog Documentation](https://www.structlog.org/)
- [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)
- [OWASP Secure Headers](https://owasp.org/www-project-secure-headers/)

---

## ⏱️ Tiempo Estimado

- **Implementación**: 2-3 horas
- **Testing**: 30 minutos
- **Documentación**: 30 minutos

**Total**: ~3-4 horas
