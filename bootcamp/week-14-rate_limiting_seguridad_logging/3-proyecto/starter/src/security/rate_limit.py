"""
Rate Limiting Configuration.

Este módulo configura slowapi para limitar requests por usuario/IP.

TODO: Implementar la configuración de rate limiting.
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.config import get_settings


settings = get_settings()


# ============================================
# TODO 1: Configurar función de identificación
# ============================================
# La función key_func determina cómo identificar al cliente.
# Puede ser por IP, por usuario autenticado, o combinación.

def get_identifier(request: Request) -> str:
    """
    Obtiene identificador único del cliente.
    
    TODO: Implementar lógica para:
    1. Si hay usuario autenticado, usar su ID
    2. Si no, usar IP del cliente
    
    Args:
        request: Request de FastAPI
        
    Returns:
        str: Identificador único del cliente
    """
    # TODO: Implementar
    # Hint: Verificar si hay token en headers
    # forwarded = request.headers.get("X-Forwarded-For")
    # if forwarded:
    #     return forwarded.split(",")[0]
    # 
    # auth_header = request.headers.get("Authorization")
    # if auth_header:
    #     # Extraer user_id del token (simplificado)
    #     return f"user:{auth_header[:20]}"
    # 
    # return get_remote_address(request) or "unknown"
    
    return get_remote_address(request) or "unknown"


# ============================================
# TODO 2: Crear instancia del Limiter
# ============================================
# Configura slowapi con la función de identificación
# y opcionalmente con Redis como backend.

# TODO: Descomentar y completar configuración avanzada
# limiter = Limiter(
#     key_func=get_identifier,
#     default_limits=[settings.rate_limit_default],
#     storage_uri=settings.redis_url if settings.is_production else None,
#     strategy="fixed-window",  # o "moving-window"
#     headers_enabled=True,
# )

# Versión básica (reemplazar con la de arriba)
limiter = Limiter(key_func=get_identifier)


# ============================================
# TODO 3: Handler para rate limit exceeded
# ============================================

def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded) -> JSONResponse:
    """
    Handler para cuando se excede el rate limit.
    
    TODO: Personalizar la respuesta con:
    - Mensaje claro
    - Headers de retry-after
    - Logging del evento
    
    Args:
        request: Request que excedió el límite
        exc: Excepción con detalles del límite
        
    Returns:
        JSONResponse: Respuesta 429
    """
    # TODO: Implementar respuesta personalizada
    # response = JSONResponse(
    #     status_code=429,
    #     content={
    #         "error": "rate_limit_exceeded",
    #         "message": f"Too many requests. Limit: {exc.detail}",
    #         "retry_after": 60,
    #     },
    # )
    # response.headers["Retry-After"] = "60"
    # response.headers["X-RateLimit-Limit"] = str(exc.detail)
    # return response
    
    return JSONResponse(
        status_code=429,
        content={"detail": f"Rate limit exceeded: {exc.detail}"},
    )


# ============================================
# Rate Limit Decorators (para referencia)
# ============================================
# Usa estos decoradores en los endpoints:
#
# @limiter.limit("5/minute")  # 5 requests por minuto
# @app.post("/auth/login")
# async def login(request: Request):
#     ...
#
# @limiter.limit("60/minute")
# @app.get("/tasks")
# async def list_tasks(request: Request):
#     ...
