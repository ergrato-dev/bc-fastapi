# ============================================
# EXCEPCIONES BASE
# ============================================

class AppException(Exception):
    def __init__(self, message: str, code: str | None = None):
        self.message = message
        self.code = code or self.__class__.__name__.upper()
        super().__init__(message)


class NotFoundError(AppException):
    pass


class ConflictError(AppException):
    pass


class ValidationError(AppException):
    pass
