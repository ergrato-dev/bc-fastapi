"""
============================================
PRÁCTICA 02: Optimización de API
Archivo: query_logging.py
============================================

Aprende a monitorear las queries de SQLAlchemy
para identificar problemas de rendimiento.
"""

import logging
import time
from contextlib import asynccontextmanager
from functools import wraps
from typing import Any, Callable

from sqlalchemy import event
from sqlalchemy.engine import Engine

# ============================================
# PASO 1: Logging básico de SQLAlchemy
# ============================================
print("--- Paso 1: Logging básico ---")

BASIC_LOGGING = """
# En tu database.py, habilita echo para ver todas las queries:

from sqlalchemy.ext.asyncio import create_async_engine

# Desarrollo - ver todas las queries
engine = create_async_engine(
    DATABASE_URL,
    echo=True,      # Imprime queries a stdout
    echo_pool=True  # También pool de conexiones
)

# Producción - solo queries lentas
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    # Configurar logging separado para producción
)
"""
print(BASIC_LOGGING)


# ============================================
# PASO 2: Logging estructurado
# ============================================
print("\n--- Paso 2: Logging estructurado ---")

# Descomenta para usar:
# logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

STRUCTURED_LOGGING = """
# Configura logging más detallado en tu config.py:

import logging

# Configurar logger de SQLAlchemy
def setup_db_logging(level: str = "INFO"):
    # Logger principal de engine
    engine_logger = logging.getLogger("sqlalchemy.engine")
    engine_logger.setLevel(getattr(logging, level))
    
    # Handler personalizado
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s [SQL] %(message)s",
        datefmt="%H:%M:%S"
    ))
    engine_logger.addHandler(handler)
    
    # Para ver el pool de conexiones
    pool_logger = logging.getLogger("sqlalchemy.pool")
    pool_logger.setLevel(logging.DEBUG)

# Llamar al inicio de la app
# setup_db_logging("DEBUG")  # Desarrollo
# setup_db_logging("WARNING")  # Producción
"""
print(STRUCTURED_LOGGING)


# ============================================
# PASO 3: Medir tiempo de queries
# ============================================
print("\n--- Paso 3: Medir tiempo de queries ---")

QUERY_TIMING = """
# Middleware para medir tiempo de queries

from sqlalchemy import event
from sqlalchemy.engine import Engine
import time
import logging

logger = logging.getLogger("query_timer")

@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault("query_start_time", []).append(time.perf_counter())

@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total = time.perf_counter() - conn.info["query_start_time"].pop()
    
    # Log solo queries lentas (> 100ms)
    if total > 0.1:
        logger.warning(
            f"Query lenta ({total:.3f}s): {statement[:100]}..."
        )

# Para async engine, usa este approach:
class QueryTimer:
    def __init__(self):
        self.queries = []
        self.start_time = None
    
    def start(self):
        self.start_time = time.perf_counter()
        self.queries = []
    
    def log_query(self, query: str, duration: float):
        self.queries.append({
            "query": query[:200],
            "duration": duration
        })
    
    def get_summary(self) -> dict:
        total_time = time.perf_counter() - self.start_time
        return {
            "total_queries": len(self.queries),
            "total_time": total_time,
            "slow_queries": [q for q in self.queries if q["duration"] > 0.1]
        }
"""
print(QUERY_TIMING)


# ============================================
# PASO 4: Contador de queries por request
# ============================================
print("\n--- Paso 4: Contador de queries por request ---")

QUERY_COUNTER = """
# Middleware para contar queries por request

from contextvars import ContextVar
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

# Context variable para tracking
query_count: ContextVar[int] = ContextVar("query_count", default=0)

class QueryCounterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Reset counter
        query_count.set(0)
        
        # Process request
        response = await call_next(request)
        
        # Add header with query count
        count = query_count.get()
        response.headers["X-Query-Count"] = str(count)
        
        # Log si hay muchas queries
        if count > 10:
            logger.warning(
                f"Alto número de queries ({count}) en {request.url.path}"
            )
        
        return response

# Hook para incrementar contador
def increment_query_count():
    current = query_count.get()
    query_count.set(current + 1)

# Usar en eventos de SQLAlchemy
@event.listens_for(Engine, "after_cursor_execute")
def after_execute(conn, cursor, statement, parameters, context, executemany):
    try:
        increment_query_count()
    except LookupError:
        pass  # Fuera de contexto de request

# Agregar middleware
# app.add_middleware(QueryCounterMiddleware)
"""
print(QUERY_COUNTER)


# ============================================
# PASO 5: Logging por endpoint
# ============================================
print("\n--- Paso 5: Decorador para endpoints ---")

ENDPOINT_DECORATOR = """
# Decorador para medir performance de endpoints

import time
from functools import wraps
from typing import Callable

def measure_endpoint(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        query_count.set(0)
        
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            duration = time.perf_counter() - start
            queries = query_count.get()
            
            logger.info(
                f"Endpoint: {func.__name__} | "
                f"Duration: {duration:.3f}s | "
                f"Queries: {queries}"
            )
    
    return wrapper

# Uso en router:
@router.get("/users")
@measure_endpoint
async def list_users(db: AsyncSession = Depends(get_db)):
    # ... tu código
    pass
"""
print(ENDPOINT_DECORATOR)


# ============================================
# PASO 6: Dashboard simple de métricas
# ============================================
print("\n--- Paso 6: Endpoint de métricas ---")

METRICS_ENDPOINT = """
# Endpoint para ver métricas de queries

from collections import defaultdict
from datetime import datetime, timedelta

# Storage simple en memoria (usar Redis en producción)
query_metrics = defaultdict(lambda: {
    "count": 0,
    "total_time": 0,
    "slow_count": 0
})

def record_query_metric(endpoint: str, duration: float):
    query_metrics[endpoint]["count"] += 1
    query_metrics[endpoint]["total_time"] += duration
    if duration > 0.1:
        query_metrics[endpoint]["slow_count"] += 1

@router.get("/metrics/queries", tags=["monitoring"])
async def get_query_metrics():
    '''Retorna métricas de queries por endpoint.'''
    return {
        endpoint: {
            "total_queries": data["count"],
            "total_time_seconds": round(data["total_time"], 3),
            "avg_time_ms": round((data["total_time"] / data["count"]) * 1000, 2)
                if data["count"] > 0 else 0,
            "slow_queries": data["slow_count"]
        }
        for endpoint, data in query_metrics.items()
    }

# Reset diario (en producción usar scheduler)
@router.post("/metrics/queries/reset", tags=["monitoring"])
async def reset_query_metrics():
    '''Resetea métricas de queries.'''
    query_metrics.clear()
    return {"status": "reset"}
"""
print(METRICS_ENDPOINT)


# ============================================
# EJERCICIO PRÁCTICO
# ============================================
print("\n" + "="*50)
print("📝 EJERCICIO: Implementa logging en tu proyecto")
print("="*50)
print("""
1. Habilita echo=True en desarrollo

2. Implementa el middleware QueryCounterMiddleware

3. Agrega el header X-Query-Count a responses

4. Identifica endpoints con más de 5 queries

5. Optimiza los endpoints problemáticos

Resultado esperado:
- Cada response incluye X-Query-Count header
- Logs muestran queries lentas (>100ms)
- Endpoints principales usan < 5 queries
""")
