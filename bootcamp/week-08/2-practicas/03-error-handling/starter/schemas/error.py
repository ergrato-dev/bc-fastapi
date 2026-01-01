# ============================================
# SCHEMA ERROR RESPONSE
# ============================================
print("--- Schema: Error Response ---")

# Schema para respuestas de error consistentes.
# Todos los errores siguen el mismo formato.

# Descomenta las siguientes líneas:

# from pydantic import BaseModel


# class ErrorResponse(BaseModel):
#     """
#     Schema para respuestas de error.
#     
#     Todos los errores de la API siguen este formato.
#     
#     Attributes:
#         error: Tipo de error (Not Found, Conflict, etc.)
#         code: Código único del error (PRODUCT_NOT_FOUND, etc.)
#         detail: Mensaje descriptivo
#     """
#     error: str
#     code: str
#     detail: str
#     
#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "error": "Not Found",
#                 "code": "PRODUCT_NOT_FOUND",
#                 "detail": "Product with id 123 not found"
#             }
#         }
