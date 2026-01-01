"""
Error handlers - Mapeo de excepciones de dominio a HTTP.
"""

from fastapi import Request
from fastapi.responses import JSONResponse


class DomainError(Exception):
    """Base para errores de dominio."""
    pass


async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
    """Handler genérico para errores de dominio."""
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )
