"""
Excepciones de la capa de aplicación.

Las excepciones de aplicación son diferentes a las de dominio.
Representan errores de orquestación, no de negocio.
"""


# ============================================
# PASO 1: Excepciones de aplicación
# ============================================

# Descomenta las siguientes líneas:

# class ApplicationError(Exception):
#     """Base para errores de aplicación."""
#     pass
# 
# 
# class ValidationError(ApplicationError):
#     """Error de validación de datos de entrada."""
#     
#     def __init__(self, field: str, message: str) -> None:
#         self.field = field
#         self.message = message
#         super().__init__(f"{field}: {message}")
# 
# 
# class NotFoundError(ApplicationError):
#     """Recurso no encontrado."""
#     
#     def __init__(self, resource: str, identifier: str) -> None:
#         self.resource = resource
#         self.identifier = identifier
#         super().__init__(f"{resource} not found: {identifier}")
# 
# 
# class ConflictError(ApplicationError):
#     """Conflicto con el estado actual."""
#     pass


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("✅ Excepciones de aplicación definidas correctamente")
