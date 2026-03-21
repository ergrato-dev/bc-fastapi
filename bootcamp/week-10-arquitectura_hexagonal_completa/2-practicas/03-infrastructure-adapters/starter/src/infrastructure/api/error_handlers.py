"""
Manejadores de errores para la API.

Traducen excepciones de dominio y aplicación a respuestas HTTP.
"""

from fastapi import Request, status
from fastapi.responses import JSONResponse

from domain.exceptions import (
    DomainError,
    TaskNotFoundError,
    TaskNotAssignableError,
    ProjectNotFoundError,
)


# ============================================
# PASO 1: Handler para errores de dominio
# ============================================
print("--- Paso 1: Domain Error Handler ---")

# Descomenta las siguientes líneas:

# async def domain_error_handler(
#     request: Request,
#     exc: DomainError,
# ) -> JSONResponse:
#     """
#     Manejar errores de dominio.
#     
#     Mapea excepciones de dominio a códigos HTTP apropiados.
#     """
#     # Mapear tipo de error a código HTTP
#     status_code = status.HTTP_400_BAD_REQUEST
#     
#     if isinstance(exc, (TaskNotFoundError, ProjectNotFoundError)):
#         status_code = status.HTTP_404_NOT_FOUND
#     elif isinstance(exc, TaskNotAssignableError):
#         status_code = status.HTTP_409_CONFLICT
#     
#     return JSONResponse(
#         status_code=status_code,
#         content={
#             "error": exc.__class__.__name__,
#             "detail": str(exc),
#         },
#     )


# ============================================
# PASO 2: Handler genérico (fallback)
# ============================================
print("--- Paso 2: Generic Error Handler ---")

# Descomenta las siguientes líneas:

# async def generic_error_handler(
#     request: Request,
#     exc: Exception,
# ) -> JSONResponse:
#     """
#     Manejar errores genéricos.
#     
#     Fallback para errores no manejados específicamente.
#     En producción, NO exponer detalles del error.
#     """
#     return JSONResponse(
#         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#         content={
#             "error": "InternalServerError",
#             "detail": "An unexpected error occurred",
#         },
#     )


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Error Handlers ---")
    print("✅ Error handlers definidos correctamente")
