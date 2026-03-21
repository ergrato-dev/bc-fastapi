"""
Excepciones del dominio.

Las excepciones de dominio representan violaciones de reglas de negocio.
Son independientes de la infraestructura.
"""


# ============================================
# BASE
# ============================================

class DomainError(Exception):
    """Base para todas las excepciones de dominio."""
    pass


# ============================================
# TASK EXCEPTIONS
# ============================================

class TaskNotFoundError(DomainError):
    """La tarea no existe."""
    
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id
        super().__init__(f"Task not found: {task_id}")


class TaskAlreadyCompletedError(DomainError):
    """La tarea ya está completada."""
    
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id
        super().__init__(f"Task already completed: {task_id}")


class InvalidTaskTransitionError(DomainError):
    """Transición de estado inválida."""
    
    def __init__(self, from_status: str, to_status: str) -> None:
        self.from_status = from_status
        self.to_status = to_status
        super().__init__(
            f"Invalid transition from {from_status} to {to_status}"
        )


# ============================================
# PROJECT EXCEPTIONS
# ============================================

class ProjectNotFoundError(DomainError):
    """El proyecto no existe."""
    
    def __init__(self, project_id: str) -> None:
        self.project_id = project_id
        super().__init__(f"Project not found: {project_id}")


# ============================================
# USER EXCEPTIONS
# ============================================

class UserNotFoundError(DomainError):
    """El usuario no existe."""
    
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        super().__init__(f"User not found: {user_id}")


class UserAlreadyExistsError(DomainError):
    """El usuario ya existe."""
    
    def __init__(self, email: str) -> None:
        self.email = email
        super().__init__(f"User already exists: {email}")
