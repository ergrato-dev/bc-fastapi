# ============================================
# EXCEPTION HANDLERS GLOBALES
# ============================================
print("--- Handlers: Exception Handlers ---")

# Los handlers globales capturan excepciones y las convierten
# en respuestas HTTP consistentes.
# 
# Ventajas:
# - Routers sin try/except
# - Respuestas de error consistentes
# - Centralización del manejo de errores

# Descomenta las siguientes líneas:

# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

# from exceptions.base import (
#     AppException,
#     NotFoundError,
#     ConflictError,
#     ValidationError,
#     UnauthorizedError,
#     ForbiddenError
# )


# async def not_found_handler(request: Request, exc: NotFoundError):
#     """
#     Handler para NotFoundError → HTTP 404.
#     """
#     return JSONResponse(
#         status_code=404,
#         content={
#             "error": "Not Found",
#             "code": exc.code,
#             "detail": exc.message
#         }
#     )


# async def conflict_handler(request: Request, exc: ConflictError):
#     """
#     Handler para ConflictError → HTTP 409.
#     """
#     return JSONResponse(
#         status_code=409,
#         content={
#             "error": "Conflict",
#             "code": exc.code,
#             "detail": exc.message
#         }
#     )


# async def validation_handler(request: Request, exc: ValidationError):
#     """
#     Handler para ValidationError → HTTP 400.
#     """
#     return JSONResponse(
#         status_code=400,
#         content={
#             "error": "Validation Error",
#             "code": exc.code,
#             "detail": exc.message
#         }
#     )


# async def unauthorized_handler(request: Request, exc: UnauthorizedError):
#     """
#     Handler para UnauthorizedError → HTTP 401.
#     """
#     return JSONResponse(
#         status_code=401,
#         content={
#             "error": "Unauthorized",
#             "code": exc.code,
#             "detail": exc.message
#         }
#     )


# async def forbidden_handler(request: Request, exc: ForbiddenError):
#     """
#     Handler para ForbiddenError → HTTP 403.
#     """
#     return JSONResponse(
#         status_code=403,
#         content={
#             "error": "Forbidden",
#             "code": exc.code,
#             "detail": exc.message
#         }
#     )


# async def app_exception_handler(request: Request, exc: AppException):
#     """
#     Handler genérico para AppException no manejadas → HTTP 500.
#     """
#     return JSONResponse(
#         status_code=500,
#         content={
#             "error": "Internal Server Error",
#             "code": exc.code,
#             "detail": exc.message
#         }
#     )


# def register_exception_handlers(app: FastAPI) -> None:
#     """
#     Registra todos los exception handlers en la aplicación.
#     
#     Args:
#         app: Instancia de FastAPI
#     """
#     # Orden importa: más específicos primero
#     app.add_exception_handler(NotFoundError, not_found_handler)
#     app.add_exception_handler(ConflictError, conflict_handler)
#     app.add_exception_handler(ValidationError, validation_handler)
#     app.add_exception_handler(UnauthorizedError, unauthorized_handler)
#     app.add_exception_handler(ForbiddenError, forbidden_handler)
#     # Genérico al final
#     app.add_exception_handler(AppException, app_exception_handler)
