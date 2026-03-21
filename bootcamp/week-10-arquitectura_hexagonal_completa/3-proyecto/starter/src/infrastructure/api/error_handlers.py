"""
Error Handlers - Mapeo de excepciones de dominio a HTTP.
"""

from fastapi import Request, status
from fastapi.responses import JSONResponse

from domain.exceptions import (
    DomainError,
    TaskNotFoundError,
    ProjectNotFoundError,
    UserNotFoundError,
    UserAlreadyExistsError,
    TaskAlreadyCompletedError,
    InvalidTaskTransitionError,
)


async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
    """Handler para errores de dominio."""
    
    # Mapeo de excepciones a códigos HTTP
    status_map = {
        TaskNotFoundError: status.HTTP_404_NOT_FOUND,
        ProjectNotFoundError: status.HTTP_404_NOT_FOUND,
        UserNotFoundError: status.HTTP_404_NOT_FOUND,
        UserAlreadyExistsError: status.HTTP_409_CONFLICT,
        TaskAlreadyCompletedError: status.HTTP_400_BAD_REQUEST,
        InvalidTaskTransitionError: status.HTTP_400_BAD_REQUEST,
    }
    
    status_code = status_map.get(type(exc), status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(
        status_code=status_code,
        content={
            "error": type(exc).__name__,
            "detail": str(exc),
        },
    )
