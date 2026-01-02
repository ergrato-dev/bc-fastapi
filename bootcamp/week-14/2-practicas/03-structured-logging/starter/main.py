"""
Logging Estructurado con structlog - Práctica Guiada

Aprende a implementar logging estructurado para mejor
debugging y análisis en producción.
"""

from contextlib import asynccontextmanager
import time
import uuid

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

from logging_config import setup_logging, get_logger

# ============================================
# PASO 1: Inicializar Logging
# ============================================
print("--- Paso 1: Inicializar Logging ---")

# Configurar logging estructurado
# json_logs=False para desarrollo (más legible)
# json_logs=True para producción (parseable)
# Descomenta la siguiente línea:
# setup_logging(json_logs=False, log_level="DEBUG")

# Obtener logger
logger = get_logger(__name__)


# ============================================
# PASO 2: Request Logging Middleware
# ============================================
print("--- Paso 2: Request Logging Middleware ---")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware que loguea cada request y response.
    
    - Genera un request_id único para tracking
    - Loguea inicio y fin del request
    - Mide duración del request
    """
    
    async def dispatch(self, request: Request, call_next):
        # Descomenta las siguientes líneas:
        
        # # Generar ID único para este request
        # request_id = str(uuid.uuid4())[:8]
        # 
        # # Guardar en el state del request para uso posterior
        # request.state.request_id = request_id
        # 
        # # Obtener IP del cliente
        # client_ip = request.client.host if request.client else "unknown"
        # 
        # # Log de inicio
        # logger.info(
        #     "request_started",
        #     request_id=request_id,
        #     method=request.method,
        #     path=request.url.path,
        #     client_ip=client_ip,
        #     user_agent=request.headers.get("user-agent", "")[:50],
        # )
        # 
        # # Medir tiempo
        # start_time = time.perf_counter()
        # 
        # try:
        #     response = await call_next(request)
        #     
        #     # Calcular duración
        #     duration_ms = (time.perf_counter() - start_time) * 1000
        #     
        #     # Log de fin
        #     logger.info(
        #         "request_completed",
        #         request_id=request_id,
        #         status_code=response.status_code,
        #         duration_ms=round(duration_ms, 2),
        #     )
        #     
        #     # Añadir request_id al response header
        #     response.headers["X-Request-ID"] = request_id
        #     
        #     return response
        #     
        # except Exception as exc:
        #     duration_ms = (time.perf_counter() - start_time) * 1000
        #     
        #     logger.exception(
        #         "request_failed",
        #         request_id=request_id,
        #         duration_ms=round(duration_ms, 2),
        #         error_type=type(exc).__name__,
        #     )
        #     raise
        
        # Versión sin logging (remover cuando descomentas)
        return await call_next(request)


# ============================================
# PASO 3: Crear App con Middleware
# ============================================
print("--- Paso 3: Crear App ---")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle de la aplicación."""
    logger.info("application_startup")
    yield
    logger.info("application_shutdown")


app = FastAPI(
    title="Structured Logging Demo",
    lifespan=lifespan
)

# Añadir middleware de logging
# Descomenta la siguiente línea:
# app.add_middleware(RequestLoggingMiddleware)


# ============================================
# PASO 4: Endpoints con Logging
# ============================================
print("--- Paso 4: Endpoints con Logging ---")


@app.get("/")
async def root():
    """Endpoint raíz."""
    logger.debug("root_accessed")
    return {"message": "Structured Logging Demo"}


@app.get("/api/users")
async def get_users(request: Request):
    """Lista usuarios con logging."""
    # Descomenta las siguientes líneas:
    
    # # Obtener request_id del middleware
    # request_id = getattr(request.state, "request_id", "unknown")
    # 
    # # Crear logger con contexto
    # log = logger.bind(request_id=request_id)
    # 
    # # Log de operación
    # log.info("fetching_users")
    # 
    # # Simular fetch de usuarios
    # users = [
    #     {"id": 1, "name": "Alice", "email": "alice@example.com"},
    #     {"id": 2, "name": "Bob", "email": "bob@example.com"},
    # ]
    # 
    # log.info("users_fetched", count=len(users))
    # 
    # return {"users": users}
    
    return {"users": [{"id": 1, "name": "Alice"}]}


@app.get("/api/users/{user_id}")
async def get_user(user_id: int, request: Request):
    """Obtiene un usuario específico."""
    # Descomenta las siguientes líneas:
    
    # request_id = getattr(request.state, "request_id", "unknown")
    # log = logger.bind(request_id=request_id, user_id=user_id)
    # 
    # log.info("fetching_user")
    # 
    # # Simular búsqueda
    # if user_id > 100:
    #     log.warning("user_not_found")
    #     from fastapi import HTTPException
    #     raise HTTPException(status_code=404, detail="User not found")
    # 
    # user = {"id": user_id, "name": f"User {user_id}"}
    # log.info("user_fetched", user_name=user["name"])
    # 
    # return user
    
    return {"id": user_id, "name": f"User {user_id}"}


@app.post("/api/orders")
async def create_order(request: Request):
    """Crea una orden con logging detallado."""
    # Descomenta las siguientes líneas:
    
    # request_id = getattr(request.state, "request_id", "unknown")
    # log = logger.bind(request_id=request_id)
    # 
    # log.info("order_creation_started")
    # 
    # # Simular creación de orden
    # order_id = 12345
    # total = 99.99
    # 
    # log.info(
    #     "order_created",
    #     order_id=order_id,
    #     total=total,
    #     currency="USD"
    # )
    # 
    # return {"order_id": order_id, "total": total}
    
    return {"order_id": 12345, "total": 99.99}


# ============================================
# PASO 5: Endpoint que genera warning/error
# ============================================
print("--- Paso 5: Logs de Warning y Error ---")


@app.get("/api/risky")
async def risky_operation(request: Request):
    """Endpoint que puede generar warnings."""
    # Descomenta las siguientes líneas:
    
    # import random
    # request_id = getattr(request.state, "request_id", "unknown")
    # log = logger.bind(request_id=request_id)
    # 
    # log.info("risky_operation_started")
    # 
    # # Simular operación que puede fallar
    # success_rate = random.random()
    # 
    # if success_rate < 0.3:
    #     log.error(
    #         "risky_operation_failed",
    #         success_rate=round(success_rate, 2),
    #         reason="random_failure"
    #     )
    #     from fastapi import HTTPException
    #     raise HTTPException(status_code=500, detail="Operation failed")
    # 
    # elif success_rate < 0.5:
    #     log.warning(
    #         "risky_operation_degraded",
    #         success_rate=round(success_rate, 2)
    #     )
    #     return {"status": "degraded", "message": "Operation completed with warnings"}
    # 
    # log.info("risky_operation_completed")
    # return {"status": "success"}
    
    return {"status": "success"}


# ============================================
# PASO 6: Logging de datos sensibles (MASKED)
# ============================================
print("--- Paso 6: Datos Sensibles ---")


@app.post("/api/login")
async def login(request: Request):
    """
    Simula login - los passwords deben estar masked en logs.
    """
    # Descomenta las siguientes líneas:
    
    # request_id = getattr(request.state, "request_id", "unknown")
    # log = logger.bind(request_id=request_id)
    # 
    # # En producción, estos vendrían del body
    # email = "user@example.com"
    # password = "secret123"  # NUNCA debería aparecer en logs
    # 
    # # El procesador mask_sensitive_data debería enmascarar esto
    # log.info(
    #     "login_attempt",
    #     email=email,
    #     password=password,  # Será masked si el procesador está activo
    # )
    # 
    # log.info("login_successful", email=email)
    # 
    # return {"message": "Login successful", "token": "fake-jwt-token"}
    
    return {"message": "Login successful"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
