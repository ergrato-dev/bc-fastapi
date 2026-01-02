"""
Security Headers y CORS - Práctica Guiada

Aprende a proteger tu API con CORS y security headers.
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import logging

# ============================================
# PASO 1: Importar middleware de CORS
# ============================================
print("--- Paso 1: Importar CORS ---")

# Descomenta la siguiente línea:
# from fastapi.middleware.cors import CORSMiddleware

# Importar nuestro middleware de seguridad
# Descomenta la siguiente línea:
# from middleware import SecurityHeadersMiddleware

app = FastAPI(
    title="Security Demo",
    description="API con security headers y CORS"
)

# Logger para errores
logger = logging.getLogger(__name__)


# ============================================
# PASO 2: Configurar CORS
# ============================================
print("--- Paso 2: Configurar CORS ---")

# Lista de orígenes permitidos
# En producción, estos serían tus dominios reales
ALLOWED_ORIGINS = [
    "https://allowed-domain.com",
    "https://admin.allowed-domain.com",
]

# En desarrollo, añadir localhost
# Descomenta para desarrollo:
# ALLOWED_ORIGINS.extend([
#     "http://localhost:3000",
#     "http://localhost:5173",
#     "http://127.0.0.1:3000",
# ])

# Configurar CORS middleware
# Descomenta las siguientes líneas:
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=ALLOWED_ORIGINS,  # Orígenes específicos, NUNCA ["*"] en producción
#     allow_credentials=True,          # Permitir cookies
#     allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
#     allow_headers=["Authorization", "Content-Type"],  # Headers permitidos
#     expose_headers=["X-Request-ID"],  # Headers visibles al cliente
#     max_age=600,  # Cache preflight por 10 minutos
# )


# ============================================
# PASO 3: Añadir Security Headers Middleware
# ============================================
print("--- Paso 3: Security Headers Middleware ---")

# Descomenta la siguiente línea:
# app.add_middleware(SecurityHeadersMiddleware)


# ============================================
# PASO 4: Manejo Seguro de Errores
# ============================================
print("--- Paso 4: Manejo Seguro de Errores ---")

# Handler para errores genéricos - NO exponer información interna
# Descomenta las siguientes líneas:
# @app.exception_handler(Exception)
# async def generic_exception_handler(request: Request, exc: Exception):
#     """
#     Handler genérico para excepciones.
#     NUNCA exponer stack traces o información interna.
#     """
#     # Log interno con detalles completos
#     logger.exception(f"Unhandled error: {exc}")
#     
#     # Respuesta genérica al cliente
#     return JSONResponse(
#         status_code=500,
#         content={
#             "error": "internal_server_error",
#             "message": "An unexpected error occurred. Please try again later.",
#         }
#     )


# Handler para HTTPException - mantener mensajes controlados
# Descomenta las siguientes líneas:
# @app.exception_handler(HTTPException)
# async def http_exception_handler(request: Request, exc: HTTPException):
#     """Handler para HTTPExceptions."""
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={
#             "error": exc.detail if isinstance(exc.detail, str) else "error",
#             "message": exc.detail,
#         }
#     )


# ============================================
# PASO 5: Endpoints de Ejemplo
# ============================================
print("--- Paso 5: Endpoints ---")


@app.get("/")
async def root():
    """Endpoint raíz."""
    return {
        "message": "Security Demo API",
        "tip": "Verifica los headers de seguridad con: curl -I http://localhost:8000/"
    }


@app.get("/api/data")
async def get_data():
    """Endpoint de datos."""
    return {
        "data": [1, 2, 3],
        "message": "Datos seguros"
    }


@app.get("/api/user")
async def get_user():
    """Endpoint de usuario."""
    return {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }


# Endpoint que simula un error (para testing)
@app.get("/api/error")
async def trigger_error():
    """Endpoint que genera un error para testing."""
    # Esto NO debería exponer el stack trace
    raise ValueError("Este es un error interno de prueba")


# Endpoint con error HTTP controlado
@app.get("/api/not-found")
async def not_found():
    """Endpoint que retorna 404."""
    raise HTTPException(status_code=404, detail="Resource not found")


# ============================================
# PASO 6: Endpoint para verificar CORS
# ============================================
print("--- Paso 6: CORS Test Endpoint ---")


@app.options("/api/data")
async def options_data():
    """
    Endpoint OPTIONS para preflight CORS.
    FastAPI/Starlette maneja esto automáticamente con CORSMiddleware.
    """
    return {}


# ============================================
# PASO 7: Información de Seguridad
# ============================================
print("--- Paso 7: Security Info ---")


@app.get("/security-info")
async def security_info():
    """
    Muestra información sobre la configuración de seguridad.
    Solo para desarrollo/debugging.
    """
    return {
        "cors": {
            "allowed_origins": ALLOWED_ORIGINS,
            "allowed_methods": ["GET", "POST", "PUT", "DELETE"],
        },
        "headers": {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        },
        "note": "Este endpoint no debería existir en producción"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
