# ============================================
# EXCEPTION HANDLERS
# ============================================

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions.base import (
    AppException,
    NotFoundError,
    ConflictError,
    ValidationError
)


async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": "Not Found", "code": exc.code, "detail": exc.message}
    )


async def conflict_handler(request: Request, exc: ConflictError):
    return JSONResponse(
        status_code=409,
        content={"error": "Conflict", "code": exc.code, "detail": exc.message}
    )


async def validation_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={"error": "Validation Error", "code": exc.code, "detail": exc.message}
    )


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Error", "code": exc.code, "detail": exc.message}
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(NotFoundError, not_found_handler)
    app.add_exception_handler(ConflictError, conflict_handler)
    app.add_exception_handler(ValidationError, validation_handler)
    app.add_exception_handler(AppException, app_exception_handler)
