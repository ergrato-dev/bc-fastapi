# ============================================
# EXCEPCIONES USER
# ============================================

from .base import NotFoundError, ConflictError


class UserNotFoundError(NotFoundError):
    """Usuario no encontrado."""
    
    def __init__(self, user_id: int):
        super().__init__(
            message=f"User with id {user_id} not found",
            code="USER_NOT_FOUND"
        )


class UserAlreadyExistsError(ConflictError):
    """Email ya registrado."""
    
    def __init__(self, email: str):
        super().__init__(
            message=f"User with email '{email}' already exists",
            code="USER_EMAIL_DUPLICATE"
        )
