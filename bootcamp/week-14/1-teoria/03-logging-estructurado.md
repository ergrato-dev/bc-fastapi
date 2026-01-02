# 📝 Logging Estructurado con structlog

## 📋 Contenido

1. [¿Por qué Logging Estructurado?](#por-qué-logging-estructurado)
2. [Problemas del Logging Tradicional](#problemas-del-logging-tradicional)
3. [Introducción a structlog](#introducción-a-structlog)
4. [Configuración en FastAPI](#configuración-en-fastapi)
5. [Contexto y Procesadores](#contexto-y-procesadores)
6. [Request Logging Middleware](#request-logging-middleware)
7. [Mejores Prácticas](#mejores-prácticas)

---

## ¿Por qué Logging Estructurado?

El logging es esencial para **debugging**, **auditoría** y **monitoreo** en producción.

![Logging Pipeline](../0-assets/03-logging-pipeline.svg)

### Logging Tradicional vs Estructurado

```python
# Logging tradicional (texto plano)
logger.info(f"User {user_id} logged in from {ip_address}")
# Output: "2024-01-15 10:30:45 INFO User 123 logged in from 192.168.1.1"

# Logging estructurado (JSON)
logger.info("user_login", user_id=user_id, ip_address=ip_address)
# Output: {"event": "user_login", "user_id": 123, "ip_address": "192.168.1.1", "timestamp": "2024-01-15T10:30:45Z"}
```

### Ventajas del Logging Estructurado

| Aspecto | Tradicional | Estructurado |
|---------|-------------|--------------|
| Parseo | Regex complicados | JSON nativo |
| Búsqueda | Texto libre | Campos específicos |
| Agregación | Difícil | Fácil (por campo) |
| Herramientas | grep | Elasticsearch, Loki |
| Alertas | Patrones de texto | Queries precisas |

---

## Problemas del Logging Tradicional

### 1. Inconsistencia en Formato

```python
# Cada desarrollador escribe diferente
logger.info(f"User {user_id} logged in")
logger.info(f"Login successful for user: {user_id}")
logger.info(f"AUTH: user={user_id} action=login")
```

### 2. Difícil de Parsear

```python
# ¿Cómo extraer user_id de estos logs?
"User 123 logged in from 192.168.1.1"
"Login attempt: user_id=456, status=success"
"[AUTH] Login: 789"
```

### 3. Información Sensible

```python
# ❌ Fácil cometer errores
logger.info(f"Login: user={email}, password={password}")  # 💥 Password en logs!
```

### 4. Sin Contexto

```python
# ¿De qué request viene este log?
logger.info("Database query completed")  # Sin request_id, user, endpoint...
```

---

## Introducción a structlog

**structlog** es la librería estándar para logging estructurado en Python.

### Instalación

```bash
uv add structlog
```

### Uso Básico

```python
import structlog

# Obtener logger
logger = structlog.get_logger()

# Logging con campos estructurados
logger.info("user_created", user_id=123, email="user@example.com")

# Output JSON:
# {
#   "event": "user_created",
#   "user_id": 123,
#   "email": "user@example.com",
#   "timestamp": "2024-01-15T10:30:45.123456Z",
#   "level": "info"
# }
```

### Niveles de Log

```python
logger.debug("debug_info", data="...")      # Desarrollo
logger.info("operation_completed", ...)      # Operaciones normales
logger.warning("deprecated_usage", ...)      # Alertas
logger.error("operation_failed", ...)        # Errores recuperables
logger.critical("system_failure", ...)       # Errores críticos
logger.exception("unhandled_error", ...)     # Con traceback
```

---

## Configuración en FastAPI

### Configuración Completa

```python
# src/logging_config.py
import logging
import sys
from typing import Any

import structlog
from structlog.types import Processor


def setup_logging(
    json_logs: bool = True,
    log_level: str = "INFO"
) -> None:
    """Configura structlog para la aplicación."""
    
    # Procesadores compartidos
    shared_processors: list[Processor] = [
        # Añade nivel de log
        structlog.stdlib.add_log_level,
        # Añade nombre del logger
        structlog.stdlib.add_logger_name,
        # Añade timestamp ISO
        structlog.processors.TimeStamper(fmt="iso"),
        # Añade información de caller (archivo, línea)
        structlog.processors.CallsiteParameterAdder(
            parameters=[
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.LINENO,
            ]
        ),
        # Procesa excepciones
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
    ]
    
    if json_logs:
        # Producción: JSON
        renderer = structlog.processors.JSONRenderer()
    else:
        # Desarrollo: Consola legible
        renderer = structlog.dev.ConsoleRenderer(colors=True)
    
    structlog.configure(
        processors=shared_processors + [
            # Prepara para el renderer final
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    # Configurar formatter para stdlib logging
    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=shared_processors,
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer,
        ],
    )
    
    # Handler para stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    
    # Configurar root logger
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.addHandler(handler)
    root_logger.setLevel(log_level)
    
    # Configurar loggers de librerías (menos verbose)
    for logger_name in ["uvicorn", "uvicorn.access", "sqlalchemy"]:
        logging.getLogger(logger_name).setLevel(logging.WARNING)
```

### Integración en main.py

```python
# src/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
import structlog

from src.logging_config import setup_logging
from src.config import settings

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    setup_logging(
        json_logs=settings.environment == "production",
        log_level=settings.log_level
    )
    logger.info("application_startup", environment=settings.environment)
    
    yield
    
    # Shutdown
    logger.info("application_shutdown")


app = FastAPI(lifespan=lifespan)
```

---

## Contexto y Procesadores

### Bind: Añadir Contexto Persistente

```python
import structlog

logger = structlog.get_logger()

# Logger base
logger.info("base_log")
# {"event": "base_log", ...}

# Bind añade contexto que persiste
logger = logger.bind(request_id="abc-123", user_id=456)
logger.info("with_context")
# {"event": "with_context", "request_id": "abc-123", "user_id": 456, ...}

logger.info("another_log")
# {"event": "another_log", "request_id": "abc-123", "user_id": 456, ...}

# Unbind remueve contexto
logger = logger.unbind("user_id")
logger.info("partial_context")
# {"event": "partial_context", "request_id": "abc-123", ...}
```

### Context Variables (Thread-Safe)

Para contexto que debe propagarse a través de async calls:

```python
# src/logging_context.py
import structlog
from contextvars import ContextVar
from typing import Any

# Context variable para request info
request_context: ContextVar[dict[str, Any]] = ContextVar(
    "request_context", 
    default={}
)


def bind_contextvars(**kwargs: Any) -> None:
    """Añade valores al contexto."""
    ctx = request_context.get().copy()
    ctx.update(kwargs)
    request_context.set(ctx)


def clear_contextvars() -> None:
    """Limpia el contexto."""
    request_context.set({})


def get_logger() -> structlog.stdlib.BoundLogger:
    """Obtiene logger con contexto actual."""
    return structlog.get_logger().bind(**request_context.get())
```

### Procesador Personalizado

```python
# src/processors.py
from typing import Any

def mask_sensitive_data(
    logger: Any, 
    method_name: str, 
    event_dict: dict[str, Any]
) -> dict[str, Any]:
    """Enmascara datos sensibles en logs."""
    
    sensitive_keys = {"password", "token", "secret", "api_key", "authorization"}
    
    for key in event_dict:
        if key.lower() in sensitive_keys:
            event_dict[key] = "***MASKED***"
        elif key.lower() == "email" and isinstance(event_dict[key], str):
            # Mostrar solo dominio del email
            email = event_dict[key]
            if "@" in email:
                event_dict[key] = f"***@{email.split('@')[1]}"
    
    return event_dict


# Añadir a la configuración
shared_processors = [
    # ... otros procesadores
    mask_sensitive_data,  # Añadir antes del renderer
    # ...
]
```

---

## Request Logging Middleware

### Middleware Completo

```python
# src/middleware/logging.py
import time
import uuid
from typing import Callable

import structlog
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.logging_context import bind_contextvars, clear_contextvars

logger = structlog.get_logger()


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware que loggea cada request/response."""
    
    async def dispatch(
        self, 
        request: Request, 
        call_next: Callable
    ) -> Response:
        # Generar ID único para el request
        request_id = str(uuid.uuid4())[:8]
        
        # Bind context para todos los logs de este request
        clear_contextvars()
        bind_contextvars(
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            client_ip=self._get_client_ip(request),
        )
        
        # Añadir request_id al state para uso en endpoints
        request.state.request_id = request_id
        
        # Log inicio
        logger.info(
            "request_started",
            query_params=dict(request.query_params),
            user_agent=request.headers.get("user-agent", ""),
        )
        
        # Medir tiempo
        start_time = time.perf_counter()
        
        try:
            response = await call_next(request)
            
            # Calcular duración
            duration_ms = (time.perf_counter() - start_time) * 1000
            
            # Log fin
            logger.info(
                "request_completed",
                status_code=response.status_code,
                duration_ms=round(duration_ms, 2),
            )
            
            # Añadir request_id al response header
            response.headers["X-Request-ID"] = request_id
            
            return response
            
        except Exception as exc:
            duration_ms = (time.perf_counter() - start_time) * 1000
            
            logger.exception(
                "request_failed",
                duration_ms=round(duration_ms, 2),
                error=str(exc),
            )
            raise
        
        finally:
            clear_contextvars()
    
    def _get_client_ip(self, request: Request) -> str:
        """Obtiene IP del cliente considerando proxies."""
        # X-Forwarded-For puede tener múltiples IPs
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            return forwarded.split(",")[0].strip()
        
        # X-Real-IP (nginx)
        real_ip = request.headers.get("x-real-ip")
        if real_ip:
            return real_ip
        
        # IP directa
        if request.client:
            return request.client.host
        
        return "unknown"


# Aplicar en main.py
app.add_middleware(RequestLoggingMiddleware)
```

### Output de Ejemplo

```json
{
  "event": "request_started",
  "request_id": "a1b2c3d4",
  "method": "POST",
  "path": "/api/users",
  "client_ip": "192.168.1.100",
  "query_params": {},
  "user_agent": "Mozilla/5.0...",
  "timestamp": "2024-01-15T10:30:45.123456Z",
  "level": "info"
}

{
  "event": "user_created",
  "request_id": "a1b2c3d4",
  "method": "POST",
  "path": "/api/users",
  "client_ip": "192.168.1.100",
  "user_id": 789,
  "email": "***@example.com",
  "timestamp": "2024-01-15T10:30:45.234567Z",
  "level": "info"
}

{
  "event": "request_completed",
  "request_id": "a1b2c3d4",
  "method": "POST",
  "path": "/api/users",
  "client_ip": "192.168.1.100",
  "status_code": 201,
  "duration_ms": 45.23,
  "timestamp": "2024-01-15T10:30:45.345678Z",
  "level": "info"
}
```

---

## Mejores Prácticas

### 1. Usar Eventos Descriptivos

```python
# ❌ MAL: Mensajes vagos
logger.info("Done")
logger.info("Error occurred")
logger.info(f"Processing {item}")

# ✅ BIEN: Eventos específicos con contexto
logger.info("payment_processed", amount=100, currency="USD", order_id=123)
logger.error("payment_failed", reason="insufficient_funds", order_id=123)
logger.info("order_shipped", order_id=123, carrier="fedex", tracking="ABC123")
```

### 2. Niveles Apropiados

```python
# DEBUG: Información detallada para desarrollo
logger.debug("cache_lookup", key="user:123", hit=True)

# INFO: Operaciones normales de negocio
logger.info("user_registered", user_id=123)
logger.info("order_created", order_id=456, total=99.99)

# WARNING: Situaciones inusuales pero manejadas
logger.warning("rate_limit_approaching", user_id=123, current=95, limit=100)
logger.warning("deprecated_endpoint_used", endpoint="/v1/old-api")

# ERROR: Errores que necesitan atención
logger.error("payment_failed", order_id=456, reason="gateway_timeout")
logger.error("external_api_error", service="stripe", status=500)

# CRITICAL: El sistema no puede continuar
logger.critical("database_connection_lost", retry_count=5)
```

### 3. No Loggear Datos Sensibles

```python
# ❌ NUNCA loggear
logger.info("login", password="secret123")  # Passwords
logger.info("payment", card_number="4111...")  # Tarjetas
logger.info("request", authorization="Bearer eyJ...")  # Tokens completos

# ✅ Loggear de forma segura
logger.info("login_attempt", email="***@example.com")
logger.info("payment_processed", card_last_four="1234")
logger.info("authenticated_request", token_prefix="eyJ...[truncated]")
```

### 4. Usar Correlation IDs

```python
# Propagar request_id a través de servicios
async def call_external_service(request_id: str, data: dict):
    headers = {"X-Request-ID": request_id}
    
    logger.info("external_call_started", service="inventory")
    response = await client.post(url, json=data, headers=headers)
    logger.info("external_call_completed", service="inventory", status=response.status_code)
```

### 5. Logging en Excepciones

```python
# ❌ MAL: Solo re-raise
try:
    result = await process_order(order)
except Exception:
    raise

# ✅ BIEN: Log con contexto, luego re-raise
try:
    result = await process_order(order)
except ValidationError as e:
    logger.warning("order_validation_failed", order_id=order.id, errors=e.errors())
    raise
except Exception as e:
    logger.exception("order_processing_failed", order_id=order.id)
    raise
```

### 6. Configuración por Entorno

```python
# src/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str = "development"
    log_level: str = "INFO"
    log_format: str = "json"  # "json" o "console"
    
    @property
    def json_logs(self) -> bool:
        return self.log_format == "json" or self.environment == "production"


# Desarrollo: logs legibles en consola
# LOG_FORMAT=console LOG_LEVEL=DEBUG

# Producción: JSON para agregación
# LOG_FORMAT=json LOG_LEVEL=INFO
```

---

## Ejemplo Completo

```python
# src/services/order_service.py
import structlog
from src.logging_context import get_logger

logger = structlog.get_logger()


async def create_order(user_id: int, items: list[dict]) -> Order:
    """Crea una orden con logging completo."""
    
    # Logger con contexto del request (request_id, etc.)
    log = get_logger().bind(user_id=user_id)
    
    log.info("order_creation_started", item_count=len(items))
    
    try:
        # Validar stock
        log.debug("validating_stock")
        await validate_stock(items)
        
        # Calcular total
        total = calculate_total(items)
        log.debug("total_calculated", total=total)
        
        # Crear en DB
        order = await db.create_order(user_id=user_id, items=items, total=total)
        log.info("order_created", order_id=order.id, total=total)
        
        # Procesar pago
        log.info("payment_processing", order_id=order.id)
        payment = await process_payment(order)
        log.info("payment_completed", order_id=order.id, payment_id=payment.id)
        
        return order
        
    except InsufficientStockError as e:
        log.warning("order_failed_stock", missing_items=e.missing_items)
        raise
        
    except PaymentError as e:
        log.error("order_failed_payment", reason=e.reason, order_id=order.id)
        await rollback_order(order.id)
        raise
        
    except Exception:
        log.exception("order_failed_unexpected")
        raise
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **structlog** | Librería para logging estructurado |
| **JSON Logs** | Formato ideal para producción |
| **Context Binding** | Añadir info persistente al logger |
| **Request ID** | Identificador único por request |
| **Procesadores** | Transforman/enriquecen logs |
| **Middleware** | Logging automático de requests |

---

## 🔗 Recursos

- [structlog Documentation](https://www.structlog.org/)
- [Python Logging Best Practices](https://docs.python.org/3/howto/logging.html)
- [12 Factor App - Logs](https://12factor.net/logs)

---

*Siguiente: [04 - Monitoreo y Métricas](04-monitoreo-metricas.md)*
