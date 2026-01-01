"""
Task Manager API - Excepciones Personalizadas
Semana 04 - Proyecto

Define excepciones de negocio y handlers.
"""

from fastapi import Request
from fastapi.responses import JSONResponse


# ============================================
# CUSTOM EXCEPTIONS - TODO: Completar
# ============================================

class TaskManagerException(Exception):
    """
    Base exception for Task Manager.
    
    TODO: Implementar:
    - code: str (código de error)
    - message: str (mensaje descriptivo)
    - status_code: int (HTTP status)
    - details: dict | None
    """
    
    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = 400,
        details: dict | None = None
    ):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details
        super().__init__(message)


class TaskNotFoundError(TaskManagerException):
    """
    Task not found exception.
    
    TODO: Implementar constructor que:
    - Reciba task_id: int
    - Llame a super() con code="TASK_NOT_FOUND"
    - status_code=404
    """
    
    def __init__(self, task_id: int):
        # TODO: Implementar
        super().__init__(
            code="TASK_NOT_FOUND",
            message=f"Task with id {task_id} not found",
            status_code=404
        )


class InvalidStatusTransitionError(TaskManagerException):
    """
    Invalid status transition exception.
    
    TODO: Implementar constructor que:
    - Reciba current_status y target_status
    - code="INVALID_STATUS_TRANSITION"
    - status_code=400
    """
    
    def __init__(self, current_status: str, target_status: str):
        # TODO: Implementar
        pass


class DuplicateTaskError(TaskManagerException):
    """
    Duplicate task exception.
    
    TODO: Implementar constructor que:
    - Reciba title: str
    - code="DUPLICATE_TASK"
    - status_code=409
    """
    
    def __init__(self, title: str):
        # TODO: Implementar
        pass


# ============================================
# EXCEPTION HANDLERS - TODO: Completar
# ============================================

async def task_manager_exception_handler(
    request: Request,
    exc: TaskManagerException
) -> JSONResponse:
    """
    Handler para TaskManagerException.
    
    TODO: Retornar JSONResponse con formato:
    {
        "error": {
            "code": exc.code,
            "message": exc.message,
            "details": exc.details
        }
    }
    """
    # TODO: Implementar
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details
            }
        }
    )
