# ============================================
# EXCEPCIONES BASE
# ============================================
print("--- Exceptions: Base Exceptions ---")

# Jerarquía de excepciones de la aplicación.
# Cada tipo de error tiene su propia clase base.

# Descomenta las siguientes líneas:

# class AppException(Exception):
#     """
#     Excepción base de la aplicación.
#     
#     Todas las excepciones personalizadas heredan de esta.
#     
#     Attributes:
#         message: Mensaje descriptivo del error
#         code: Código único del error (para clientes)
#     """
#     
#     def __init__(self, message: str, code: str | None = None):
#         self.message = message
#         self.code = code or self.__class__.__name__.upper()
#         super().__init__(message)


# class NotFoundError(AppException):
#     """
#     Error 404 - Recurso no encontrado.
#     
#     Usar cuando un recurso solicitado no existe.
#     """
#     pass


# class ConflictError(AppException):
#     """
#     Error 409 - Conflicto.
#     
#     Usar para duplicados, estados inválidos, etc.
#     """
#     pass


# class ValidationError(AppException):
#     """
#     Error 400 - Validación de negocio fallida.
#     
#     Diferente de validación de Pydantic.
#     Usar para reglas de negocio que fallan.
#     """
#     pass


# class UnauthorizedError(AppException):
#     """
#     Error 401 - No autenticado.
#     
#     Usar cuando falta autenticación.
#     """
#     pass


# class ForbiddenError(AppException):
#     """
#     Error 403 - Sin permisos.
#     
#     Usar cuando el usuario no tiene permisos.
#     """
#     pass
