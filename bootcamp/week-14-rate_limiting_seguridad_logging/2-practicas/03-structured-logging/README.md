# 📝 Práctica 03: Logging Estructurado con structlog

## 🎯 Objetivos

- Configurar structlog para logging estructurado
- Implementar middleware de logging de requests
- Añadir contexto a los logs (request_id, user_id)
- Configurar diferentes formatos para dev/prod

---

## 📋 Descripción

En esta práctica implementaremos logging estructurado usando structlog. Crearemos un sistema de logging que capture información contextual de cada request y produzca logs en formato JSON para facilitar el análisis.

---

## ⏱️ Duración

**35 minutos**

---

## 📁 Estructura

```
03-structured-logging/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py
    ├── logging_config.py
    └── test_logging.py
```

---

## 🚀 Pasos

### Paso 1: Configurar structlog

**Abre `starter/logging_config.py`** y descomenta la sección del Paso 1.

La configuración incluye:
- Timestamp ISO
- Nivel de log
- Nombre del logger
- Información de archivo y línea

---

### Paso 2: Formato Según Entorno

Descomenta la sección del Paso 2.

- **Desarrollo**: Formato colorido y legible
- **Producción**: JSON para herramientas de análisis

---

### Paso 3: Request Logging Middleware

**Abre `starter/main.py`** y descomenta la sección del Paso 3.

El middleware:
1. Genera un request_id único
2. Loguea inicio del request
3. Mide el tiempo de respuesta
4. Loguea fin del request con duración

---

### Paso 4: Contexto de Request

Descomenta la sección del Paso 4.

Usa `bind()` para añadir contexto persistente al logger:

```python
logger = logger.bind(user_id=123)
logger.info("action")  # Incluirá user_id automáticamente
```

---

### Paso 5: Logging en Servicios

Descomenta la sección del Paso 5.

Aplica logging estructurado en la lógica de negocio con eventos descriptivos.

---

### Paso 6: Ejecutar y Probar

1. Inicia el servidor:
```bash
cd starter
uv sync
uv run uvicorn main:app --reload
```

2. Haz requests y observa los logs:
```bash
curl http://localhost:8000/api/users
curl http://localhost:8000/api/orders
```

3. Ejecuta tests:
```bash
uv run pytest test_logging.py -v
```

---

## ✅ Verificación

Tu implementación está correcta si:

- [ ] Los logs aparecen en formato JSON
- [ ] Cada request tiene un `request_id` único
- [ ] Los logs incluyen `timestamp`, `level`, `event`
- [ ] La duración del request se loguea
- [ ] No hay passwords/tokens en los logs
- [ ] Los tests pasan

---

## 🔍 Output Esperado

```json
{"event": "request_started", "request_id": "a1b2c3d4", "method": "GET", "path": "/api/users", "timestamp": "2024-01-15T10:30:45.123456Z", "level": "info"}
{"event": "user_fetched", "request_id": "a1b2c3d4", "user_id": 1, "timestamp": "2024-01-15T10:30:45.234567Z", "level": "info"}
{"event": "request_completed", "request_id": "a1b2c3d4", "status_code": 200, "duration_ms": 12.34, "timestamp": "2024-01-15T10:30:45.345678Z", "level": "info"}
```

---

## 📚 Recursos

- [structlog Documentation](https://www.structlog.org/)
- [Python Logging Best Practices](https://docs.python.org/3/howto/logging.html)
