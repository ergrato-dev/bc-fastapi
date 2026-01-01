# ============================================
# PRODUCT MAPPER
# ============================================
print("--- Mapper: Product Conversions ---")

# El Mapper centraliza todas las conversiones entre:
# - DTO → Entity (para crear/actualizar)
# - Entity → DTO (para respuestas)
# 
# Ventajas:
# - Lógica de conversión en un solo lugar
# - Fácil de testear
# - Fácil de mantener

# Descomenta las siguientes líneas:

# from models.product import Product
# from schemas.product import (
#     ProductCreate,
#     ProductUpdate,
#     ProductResponse,
#     ProductDetail,
#     ProductAdmin
# )


# class ProductMapper:
#     """
#     Mapper para conversiones de Product.
#     
#     Centraliza toda la lógica de conversión entre
#     DTOs y Entities.
#     """
#     
#     @staticmethod
#     def to_entity(dto: ProductCreate) -> Product:
#         """
#         Convierte ProductCreate DTO → Product Entity.
#         
#         Args:
#             dto: DTO con datos de creación
#             
#         Returns:
#             Product entity (sin ID, será generado por DB)
#         """
#         return Product(
#             name=dto.name,
#             sku=dto.sku,
#             description=dto.description,
#             price=dto.price,
#             stock=dto.stock,
#             cost_price=dto.cost_price,
#             supplier_id=dto.supplier_id
#         )
#     
#     @staticmethod
#     def to_response(entity: Product) -> ProductResponse:
#         """
#         Convierte Product Entity → ProductResponse DTO.
#         
#         Usa model_validate para conversión automática.
#         Solo incluye campos definidos en ProductResponse.
#         
#         Args:
#             entity: Product entity
#             
#         Returns:
#             ProductResponse sin campos sensibles
#         """
#         return ProductResponse.model_validate(entity)
#     
#     @staticmethod
#     def to_detail(entity: Product) -> ProductDetail:
#         """
#         Convierte Product Entity → ProductDetail DTO.
#         
#         Incluye campos adicionales como updated_at.
#         
#         Args:
#             entity: Product entity
#             
#         Returns:
#             ProductDetail con información extendida
#         """
#         return ProductDetail.model_validate(entity)
#     
#     @staticmethod
#     def to_admin(entity: Product) -> ProductAdmin:
#         """
#         Convierte Product Entity → ProductAdmin DTO.
#         
#         Incluye campos internos como cost_price.
#         SOLO usar en endpoints de administración.
#         
#         Args:
#             entity: Product entity
#             
#         Returns:
#             ProductAdmin con todos los campos
#         """
#         return ProductAdmin(
#             id=entity.id,
#             name=entity.name,
#             sku=entity.sku,
#             description=entity.description,
#             price=entity.price,
#             stock=entity.stock,
#             created_at=entity.created_at,
#             cost_price=entity.cost_price,
#             supplier_id=entity.supplier_id,
#             profit_margin=entity.profit_margin
#         )
#     
#     @staticmethod
#     def update_entity(entity: Product, dto: ProductUpdate) -> Product:
#         """
#         Aplica cambios de ProductUpdate a Entity existente.
#         
#         Solo actualiza campos que fueron enviados (exclude_unset=True).
#         
#         Args:
#             entity: Product existente
#             dto: DTO con campos a actualizar
#             
#         Returns:
#             Product actualizado
#         """
#         update_data = dto.model_dump(exclude_unset=True)
#         
#         for field, value in update_data.items():
#             setattr(entity, field, value)
#         
#         return entity
#     
#     @staticmethod
#     def to_response_list(entities: list[Product]) -> list[ProductResponse]:
#         """
#         Convierte lista de entities a lista de responses.
#         
#         Args:
#             entities: Lista de Product entities
#             
#         Returns:
#             Lista de ProductResponse DTOs
#         """
#         return [ProductMapper.to_response(e) for e in entities]
