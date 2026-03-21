# ============================================
# EXCEPCIONES BASE
# ============================================


class AppException(Exception):
    """Excepción base de la aplicación."""
    
    def __init__(self, message: str, code: str | None = None):
        self.message = message
        self.code = code or self.__class__.__name__.upper()
        super().__init__(message)


class NotFoundError(AppException):
    """Recurso no encontrado - 404."""
    pass


class ConflictError(AppException):
    """Conflicto (duplicado) - 409."""
    pass


class ValidationError(AppException):
    """Error de validación de negocio - 400."""
    pass
