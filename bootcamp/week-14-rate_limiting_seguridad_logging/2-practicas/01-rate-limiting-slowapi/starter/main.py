"""
Rate Limiting con slowapi - Práctica Guiada

Aprende a implementar rate limiting en FastAPI para proteger
tu API contra abusos y garantizar disponibilidad.
"""

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse

# ============================================
# PASO 1: Importar slowapi
# ============================================
print("--- Paso 1: Importar slowapi ---")

# Descomenta las siguientes líneas:
# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded


# ============================================
# PASO 2: Configurar el Limiter
# ============================================
print("--- Paso 2: Configurar el Limiter ---")

# El limiter identifica clientes por su IP usando get_remote_address
# Descomenta las siguientes líneas:
# limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Rate Limiting Demo",
    description="API con rate limiting usando slowapi"
)

# Registrar el limiter en el estado de la app
# Descomenta las siguientes líneas:
# app.state.limiter = limiter

# Registrar el handler para errores de rate limit
# Descomenta la siguiente línea:
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# ============================================
# PASO 3: Aplicar Límites a Endpoints
# ============================================
print("--- Paso 3: Aplicar Límites a Endpoints ---")

# Endpoint público con límite moderado
# Descomenta las siguientes líneas:
# @app.get("/public")
# @limiter.limit("20/minute")
# async def public_endpoint(request: Request):
#     """
#     Endpoint público.
#     Límite: 20 requests por minuto por IP.
#     """
#     return {
#         "message": "Datos públicos",
#         "tip": "Este endpoint tiene un límite de 20 req/min"
#     }


# Endpoint de login con límite estricto (protección brute force)
# Descomenta las siguientes líneas:
# @app.post("/auth/login")
# @limiter.limit("5/minute")
# async def login(request: Request):
#     """
#     Endpoint de login.
#     Límite: 5 requests por minuto (protección brute force).
#     """
#     # Simulación de login
#     return {"message": "Login simulado", "token": "fake-jwt-token"}


# Endpoint de API con límite estándar
# Descomenta las siguientes líneas:
# @app.get("/api/users")
# @limiter.limit("30/minute")
# async def get_users(request: Request):
#     """
#     Lista de usuarios.
#     Límite: 30 requests por minuto.
#     """
#     return {
#         "users": [
#             {"id": 1, "name": "Alice"},
#             {"id": 2, "name": "Bob"},
#         ]
#     }


# ============================================
# PASO 4: Límites Dinámicos por Usuario
# ============================================
print("--- Paso 4: Límites Dinámicos por Usuario ---")

# Función que determina el límite basándose en el tipo de usuario
# Descomenta las siguientes líneas:
# def get_dynamic_limit(request: Request) -> str:
#     """
#     Retorna el límite basado en el tipo de usuario.
#     
#     - Premium users: 100/minute
#     - Regular users: 30/minute  
#     - Anonymous: 10/minute
#     """
#     # Simular obtención de usuario del token
#     # En producción esto vendría del middleware de auth
#     user_type = request.headers.get("X-User-Type", "anonymous")
#     
#     limits = {
#         "premium": "100/minute",
#         "regular": "30/minute",
#         "anonymous": "10/minute",
#     }
#     
#     return limits.get(user_type, "10/minute")


# Endpoint con límite dinámico
# Descomenta las siguientes líneas:
# @app.get("/api/data")
# @limiter.limit(get_dynamic_limit)
# async def get_data(request: Request):
#     """
#     Datos de API con límite dinámico.
#     El límite depende del tipo de usuario (header X-User-Type).
#     """
#     user_type = request.headers.get("X-User-Type", "anonymous")
#     return {
#         "data": [1, 2, 3, 4, 5],
#         "user_type": user_type,
#         "message": f"Límite según tipo: {user_type}"
#     }


# ============================================
# PASO 5: Excluir Endpoints del Rate Limiting
# ============================================
print("--- Paso 5: Excluir Endpoints ---")

# Algunos endpoints no deben tener límite
# Descomenta las siguientes líneas:
# @app.get("/health")
# @limiter.exempt
# async def health_check():
#     """
#     Health check - sin límite.
#     Los health checks nunca deben ser bloqueados.
#     """
#     return {"status": "healthy"}


# @app.get("/metrics")
# @limiter.exempt
# async def metrics():
#     """
#     Métricas de Prometheus - sin límite.
#     El scraping de métricas no debe ser limitado.
#     """
#     return {"requests_total": 12345}


# ============================================
# PASO 6: Handler Personalizado para 429
# ============================================
print("--- Paso 6: Handler Personalizado ---")

# Personalizar la respuesta cuando se excede el límite
# Descomenta las siguientes líneas:
# async def custom_rate_limit_handler(
#     request: Request,
#     exc: RateLimitExceeded
# ) -> JSONResponse:
#     """
#     Handler personalizado para errores de rate limit.
#     Retorna una respuesta JSON más informativa.
#     """
#     return JSONResponse(
#         status_code=429,
#         content={
#             "error": "rate_limit_exceeded",
#             "message": "Has excedido el límite de requests permitidos",
#             "detail": str(exc.detail),
#             "retry_after_seconds": exc.retry_after,
#         },
#         headers={
#             "Retry-After": str(exc.retry_after),
#         }
#     )

# Para usar el handler personalizado, reemplaza el handler por defecto:
# app.add_exception_handler(RateLimitExceeded, custom_rate_limit_handler)


# ============================================
# PASO 7: Múltiples Límites
# ============================================
print("--- Paso 7: Múltiples Límites ---")

# Puedes aplicar múltiples límites a un endpoint
# Descomenta las siguientes líneas:
# @app.get("/api/expensive")
# @limiter.limit("5/minute")    # Máximo 5 por minuto
# @limiter.limit("50/hour")     # Y máximo 50 por hora
# async def expensive_operation(request: Request):
#     """
#     Operación costosa con múltiples límites.
#     - 5 requests por minuto
#     - 50 requests por hora
#     Ambos límites deben cumplirse.
#     """
#     return {"result": "Operación costosa completada"}


# ============================================
# Endpoint raíz para testing
# ============================================
@app.get("/")
async def root():
    """Endpoint raíz."""
    return {
        "message": "Rate Limiting Demo API",
        "endpoints": {
            "/public": "20/minute",
            "/auth/login": "5/minute", 
            "/api/users": "30/minute",
            "/api/data": "dynamic",
            "/api/expensive": "5/minute + 50/hour",
            "/health": "exempt",
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
