# 📊 Rúbrica de Evaluación - Semana 14

## Rate Limiting, Seguridad, Logging y Monitoreo

### 📋 Información General

| Aspecto | Detalle |
|---------|---------|
| **Semana** | 14 de 16 |
| **Tema** | Rate Limiting, Seguridad, Logging y Monitoreo |
| **Nivel** | Avanzado |
| **Duración** | 6 horas |

---

## 🎯 Competencias Evaluadas

### CE1: Rate Limiting (20 puntos)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 18-20 | Implementa rate limiting con múltiples estrategias (por IP, usuario, endpoint). Usa Redis como backend. Maneja límites dinámicos y respuestas 429 informativas. |
| **Bueno** | 14-17 | Implementa rate limiting básico con slowapi. Configura límites por endpoint. Retorna headers de límite correctos. |
| **Suficiente** | 10-13 | Implementa rate limiting simple. Funciona pero sin configuración avanzada. Headers básicos. |
| **Insuficiente** | 0-9 | Rate limiting no funcional o mal implementado. No protege endpoints críticos. |

### CE2: Seguridad de APIs (25 puntos)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 23-25 | Implementa todos los headers de seguridad (CSP, HSTS, X-Frame-Options, etc.). CORS configurado correctamente. Prevención de ataques documentada. |
| **Bueno** | 18-22 | Configura CORS y headers principales. Middleware de seguridad funcional. Manejo de errores seguro. |
| **Suficiente** | 13-17 | CORS básico configurado. Algunos headers de seguridad. Sin exposición de datos sensibles en errores. |
| **Insuficiente** | 0-12 | Seguridad deficiente. CORS abierto (*). Errores exponen información sensible. |

### CE3: Logging Estructurado (20 puntos)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 18-20 | Logging estructurado con structlog. Contexto de request propagado. Niveles correctos. Rotación configurada. Logs en JSON. |
| **Bueno** | 14-17 | structlog configurado correctamente. Middleware de logging funcional. Contexto básico incluido. |
| **Suficiente** | 10-13 | Logging básico implementado. Formato consistente. Sin información sensible en logs. |
| **Insuficiente** | 0-9 | Logging inconsistente o ausente. Prints en lugar de logging. Datos sensibles expuestos. |

### CE4: Monitoreo y Métricas (20 puntos)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 18-20 | Prometheus Instrumentator configurado. Métricas personalizadas (counters, histograms). Endpoint /metrics seguro. Labels útiles. |
| **Bueno** | 14-17 | Métricas básicas con Prometheus. Instrumentator integrado. Métricas HTTP estándar expuestas. |
| **Suficiente** | 10-13 | Endpoint /metrics funcional. Métricas básicas de FastAPI. Sin métricas personalizadas. |
| **Insuficiente** | 0-9 | Métricas no implementadas o no funcionales. Endpoint /metrics expone errores. |

### CE5: Health Checks (15 puntos)

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Excelente** | 14-15 | Implementa liveness y readiness separados. Verifica dependencias (DB, Redis). Respuestas con detalles de estado. |
| **Bueno** | 11-13 | Health check funcional. Verifica al menos una dependencia. Formato de respuesta correcto. |
| **Suficiente** | 8-10 | Health check básico (/health retorna OK). Sin verificación de dependencias. |
| **Insuficiente** | 0-7 | Health check no implementado o siempre retorna OK sin verificaciones. |

---

## 📝 Distribución de Puntos

| Competencia | Puntos | Porcentaje |
|-------------|--------|------------|
| CE1: Rate Limiting | 20 | 20% |
| CE2: Seguridad | 25 | 25% |
| CE3: Logging | 20 | 20% |
| CE4: Monitoreo | 20 | 20% |
| CE5: Health Checks | 15 | 15% |
| **Total** | **100** | **100%** |

---

## ✅ Criterios de Aprobación

### Requisitos Mínimos (70 puntos)

- [ ] Rate limiting funcional en al menos 2 endpoints
- [ ] CORS configurado correctamente (no wildcard en producción)
- [ ] Headers de seguridad básicos implementados
- [ ] Logging estructurado con contexto de request
- [ ] Métricas Prometheus expuestas en /metrics
- [ ] Health check básico implementado
- [ ] Tests para rate limiting y health checks
- [ ] Sin datos sensibles en logs o errores

### Para Excelencia (90+ puntos)

- [ ] Rate limiting con Redis backend
- [ ] Límites dinámicos por tipo de usuario
- [ ] Todos los headers OWASP recomendados
- [ ] Logging con correlation IDs
- [ ] Métricas personalizadas de negocio
- [ ] Liveness y readiness separados
- [ ] Cobertura de tests > 80%

---

## 📊 Rúbrica de Proyecto

### Estructura del Proyecto (10 puntos extra)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Organización | 3 | Estructura de carpetas clara y consistente |
| Configuración | 3 | Settings centralizados con pydantic-settings |
| Documentación | 2 | README con instrucciones claras |
| Docker | 2 | docker-compose funcional con Redis |

### Código (10 puntos extra)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Type hints | 3 | Tipado completo en funciones públicas |
| Clean code | 4 | Funciones pequeñas, nombres descriptivos |
| Manejo errores | 3 | Excepciones personalizadas, sin crashes |

---

## 🔍 Checklist de Entrega

### Rate Limiting
- [ ] `slowapi` instalado y configurado
- [ ] Limiter global inicializado
- [ ] Límites en endpoints sensibles (login, register, etc.)
- [ ] Headers `X-RateLimit-*` en respuestas
- [ ] Respuesta 429 con `Retry-After`
- [ ] Tests de rate limiting

### Seguridad
- [ ] CORS middleware configurado
- [ ] Orígenes específicos (no `*`)
- [ ] Headers: `X-Content-Type-Options`
- [ ] Headers: `X-Frame-Options`
- [ ] Headers: `Strict-Transport-Security`
- [ ] Errores no exponen stack traces

### Logging
- [ ] `structlog` configurado
- [ ] Formato JSON en producción
- [ ] Request ID en cada log
- [ ] Niveles apropiados (INFO, WARNING, ERROR)
- [ ] Middleware de logging de requests
- [ ] Sin passwords/tokens en logs

### Monitoreo
- [ ] `prometheus-fastapi-instrumentator`
- [ ] Endpoint `/metrics` funcional
- [ ] Métricas HTTP automáticas
- [ ] Al menos 1 métrica personalizada
- [ ] Endpoint seguro (opcional auth)

### Health Checks
- [ ] Endpoint `/health` o `/healthz`
- [ ] Verifica conexión a DB
- [ ] Retorna status code correcto
- [ ] Formato JSON con detalles

---

## 📈 Niveles de Logro

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| 🏆 Excelente | 90-100 | Dominio completo. API lista para producción. |
| ✅ Bueno | 80-89 | Buen manejo. Funcionalidades completas. |
| 📝 Suficiente | 70-79 | Cumple requisitos mínimos. Necesita mejoras. |
| ⚠️ En desarrollo | 60-69 | Funcionalidad parcial. Requiere correcciones. |
| ❌ Insuficiente | 0-59 | No cumple requisitos mínimos. |

---

## 🎯 Retroalimentación

### Fortalezas Comunes
- Configuración correcta de slowapi
- CORS bien implementado
- Uso de structlog

### Áreas de Mejora Frecuentes
- Rate limiting solo con memoria (no escalable)
- CORS con wildcard en producción
- Logs sin contexto de request
- Health checks que no verifican dependencias
- Métricas sin labels útiles

---

*Rúbrica Semana 14 - Bootcamp FastAPI*
