# ============================================
# SCHEMAS CATEGORY (DTOs)
# ============================================
print("--- Schemas: Category DTOs ---")

# Los schemas son DTOs (Data Transfer Objects) que definen
# la estructura de datos para entrada y salida de la API.
# Pertenecen a la capa de Presentación.

# Descomenta las siguientes líneas:

# from datetime import datetime
# from pydantic import BaseModel, Field, ConfigDict


# class CategoryCreate(BaseModel):
#     """
#     DTO para crear una categoría.
#     
#     Todos los campos requeridos para creación.
#     """
#     name: str = Field(
#         ...,
#         min_length=2,
#         max_length=100,
#         description="Nombre de la categoría"
#     )
#     description: str | None = Field(
#         None,
#         max_length=500,
#         description="Descripción opcional"
#     )


# class CategoryUpdate(BaseModel):
#     """
#     DTO para actualizar una categoría.
#     
#     Todos los campos son opcionales (PATCH).
#     """
#     name: str | None = Field(
#         None,
#         min_length=2,
#         max_length=100
#     )
#     description: str | None = Field(
#         None,
#         max_length=500
#     )
#     is_active: bool | None = None


# class CategoryResponse(BaseModel):
#     """
#     DTO de respuesta para categoría.
#     
#     Define exactamente qué campos se exponen al cliente.
#     """
#     model_config = ConfigDict(from_attributes=True)
#     
#     id: int
#     name: str
#     description: str | None
#     is_active: bool
#     created_at: datetime
