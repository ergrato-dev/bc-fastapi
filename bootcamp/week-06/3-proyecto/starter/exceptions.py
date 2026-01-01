# ============================================
# Excepciones Personalizadas
# ============================================
"""
Excepciones para la capa de servicios.
Los routers las capturan y convierten a HTTP.
"""


class ServiceError(Exception):
    """Base exception para errores de servicio"""
    pass


class NotFoundError(ServiceError):
    """Recurso no encontrado"""
    pass


class DuplicateError(ServiceError):
    """Recurso duplicado"""
    pass


class ValidationError(ServiceError):
    """Error de validación de negocio"""
    pass
