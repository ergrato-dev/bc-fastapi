# ============================================
# EXCEPCIONES USER
# ============================================

from .base import NotFoundError


class UserNotFoundError(NotFoundError):
    def __init__(self, user_id: int):
        super().__init__(
            message=f"User with id {user_id} not found",
            code="USER_NOT_FOUND"
        )
