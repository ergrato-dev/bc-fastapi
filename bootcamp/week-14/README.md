# 🛡️ Semana 14: Rate Limiting, Seguridad, Logging y Monitoreo

## 📋 Descripción

Esta semana aprenderás a **proteger y observar** tus APIs FastAPI. Implementaremos rate limiting para prevenir abusos, mejores prácticas de seguridad, logging estructurado para debugging y monitoreo para mantener la salud de tu aplicación en producción.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Implementar rate limiting con slowapi y Redis
- ✅ Aplicar mejores prácticas de seguridad OWASP
- ✅ Configurar CORS, CSP y headers de seguridad
- ✅ Prevenir ataques comunes (XSS, CSRF, SQL Injection)
- ✅ Implementar logging estructurado con structlog
- ✅ Crear middleware de logging para requests/responses
- ✅ Configurar métricas con Prometheus
- ✅ Monitorear health checks y endpoints de diagnóstico
- ✅ Integrar alertas y dashboards básicos

---

## 📚 Requisitos Previos

- Semana 11: Autenticación JWT
- Semana 12: Testing con pytest
- Semana 13: WebSockets y SSE
- Conocimientos de middleware FastAPI
- Docker básico (para Redis)

---

## 🗂️ Estructura de la Semana

```
week-14/
├── README.md                      # Este archivo
├── rubrica-evaluacion.md          # Criterios de evaluación
├── 0-assets/                      # Diagramas SVG
│   ├── 01-rate-limiting-flow.svg
│   ├── 02-security-layers.svg
│   ├── 03-logging-pipeline.svg
│   ├── 04-monitoring-stack.svg
│   └── 05-observability-triad.svg
├── 1-teoria/
│   ├── 01-rate-limiting.md
│   ├── 02-seguridad-apis.md
│   ├── 03-logging-estructurado.md
│   ├── 04-monitoreo-metricas.md
│   └── 05-health-checks.md
├── 2-practicas/
│   ├── 01-rate-limiting-slowapi/
│   ├── 02-security-headers/
│   ├── 03-structured-logging/
│   └── 04-prometheus-metrics/
├── 3-proyecto/
│   ├── README.md
│   ├── starter/
│   └── solution/
├── 4-recursos/
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 📝 Contenidos

### Teoría (1-teoria/)

| # | Tema | Descripción | Tiempo |
|---|------|-------------|--------|
| 01 | Rate Limiting | Algoritmos, slowapi, Redis backend | 30 min |
| 02 | Seguridad de APIs | OWASP, headers, CORS, prevención ataques | 35 min |
| 03 | Logging Estructurado | structlog, contexto, rotación | 30 min |
| 04 | Monitoreo y Métricas | Prometheus, exporters, dashboards | 30 min |
| 05 | Health Checks | Liveness, readiness, diagnósticos | 20 min |

**Total Teoría: ~2 horas 25 min**

### Prácticas (2-practicas/)

| # | Práctica | Descripción | Tiempo |
|---|----------|-------------|--------|
| 01 | Rate Limiting con slowapi | Configurar límites por endpoint/usuario | 35 min |
| 02 | Security Headers | CORS, CSP, middleware de seguridad | 30 min |
| 03 | Structured Logging | structlog + request logging middleware | 35 min |
| 04 | Prometheus Metrics | Exportar métricas, health checks | 35 min |

**Total Prácticas: ~2 horas 15 min**

### Proyecto (3-proyecto/)

| Proyecto | Descripción | Tiempo |
|----------|-------------|--------|
| API Observable | API completa con rate limiting, seguridad y monitoreo | 90 min |

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| Teoría | 2 h 25 min |
| Prácticas | 2 h 15 min |
| Proyecto | 1 h 30 min |
| **Total** | **~6 h 10 min** |

---

## 📦 Herramientas de la Semana

```toml
[project.dependencies]
fastapi = ">=0.115.0"
uvicorn = { version = ">=0.32.0", extras = ["standard"] }
pydantic = ">=2.10.0"
pydantic-settings = ">=2.6.0"

# Rate Limiting
slowapi = ">=0.1.9"
redis = ">=5.2.0"

# Security
python-jose = { version = ">=3.3.0", extras = ["cryptography"] }
passlib = { version = ">=1.7.4", extras = ["bcrypt"] }
secure = ">=0.3.0"          # Security headers

# Logging
structlog = ">=24.4.0"
python-json-logger = ">=2.0.7"

# Monitoring
prometheus-fastapi-instrumentator = ">=7.0.0"
prometheus-client = ">=0.21.0"

# Database
sqlalchemy = ">=2.0.36"
aiosqlite = ">=0.20.0"

[project.optional-dependencies]
dev = [
    "pytest>=8.3.4",
    "pytest-asyncio>=0.24.0",
    "httpx>=0.28.0",
    "pytest-cov>=6.0.0",
]
```

---

## 🎯 Competencias a Desarrollar

| Código | Competencia | Nivel |
|--------|-------------|-------|
| CE1 | Implementa rate limiting efectivo | Avanzado |
| CE2 | Aplica prácticas de seguridad OWASP | Avanzado |
| CE3 | Configura logging estructurado | Intermedio |
| CE4 | Implementa métricas y monitoreo | Intermedio |
| CE5 | Crea health checks completos | Intermedio |

---

## 📌 Entregables

1. **Prácticas completadas** (4 ejercicios guiados)
2. **Proyecto funcional** con:
   - Rate limiting configurado (por IP y por usuario)
   - Security headers implementados
   - Logging estructurado con contexto
   - Métricas Prometheus expuestas
   - Health checks (liveness + readiness)
3. **Tests pasando** para todas las funcionalidades

---

## 🔗 Navegación

| ⬅️ Anterior | 🏠 Inicio | ➡️ Siguiente |
|-------------|-----------|--------------|
| [Semana 13: WebSockets y SSE](../week-13/README.md) | [Bootcamp](../README.md) | [Semana 15: Docker](../week-15/README.md) |

---

## 💡 Tips de la Semana

> 🛡️ **Defensa en profundidad**: No confíes en una sola capa de seguridad. Rate limiting + autenticación + validación + logging = API robusta.

> 📊 **Observabilidad**: Los tres pilares son logs, métricas y traces. Esta semana cubrimos los dos primeros.

> ⚡ **Redis para rate limiting**: En producción, usa Redis como backend para rate limiting distribuido entre múltiples instancias.

---

*Semana 14 de 16 - Nivel Avanzado*
