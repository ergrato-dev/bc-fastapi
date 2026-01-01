# ============================================
# PRODUCT SERVICE
# ============================================
print("--- Service: Product Service con Mapper ---")

# Service con lógica de negocio que usa Mapper
# para todas las conversiones DTO ↔ Entity.

# Descomenta las siguientes líneas:

# from models.product import Product
# from schemas.product import ProductCreate, ProductUpdate, ProductResponse
# from repositories.product import ProductRepository
# from mappers.product import ProductMapper


# class ProductService:
#     """
#     Service para lógica de negocio de Product.
#     
#     Usa ProductMapper para todas las conversiones.
#     """
#     
#     def __init__(self, repo: ProductRepository):
#         self.repo = repo
#     
#     def get_all(self) -> list[ProductResponse]:
#         """
#         Lista todos los productos.
#         
#         Returns:
#             Lista de ProductResponse (sin campos internos)
#         """
#         entities = self.repo.get_all()
#         # Mapper convierte lista de entities
#         return ProductMapper.to_response_list(entities)
#     
#     def get_by_id(self, product_id: int) -> ProductResponse:
#         """
#         Obtiene producto por ID.
#         
#         Returns:
#             ProductResponse
#             
#         Raises:
#             ValueError: Si no existe
#         """
#         entity = self.repo.get_by_id(product_id)
#         if not entity:
#             raise ValueError(f"Product {product_id} not found")
#         
#         # Mapper convierte entity → response
#         return ProductMapper.to_response(entity)
#     
#     def create(self, data: ProductCreate) -> ProductResponse:
#         """
#         Crea nuevo producto.
#         
#         Args:
#             data: ProductCreate DTO
#             
#         Returns:
#             ProductResponse creado
#             
#         Raises:
#             ValueError: Si SKU duplicado
#         """
#         # Validación de negocio
#         if self.repo.exists_by_sku(data.sku):
#             raise ValueError(f"SKU '{data.sku}' already exists")
#         
#         # Mapper convierte DTO → Entity
#         entity = ProductMapper.to_entity(data)
#         
#         # Persistir
#         saved = self.repo.add(entity)
#         
#         # Mapper convierte Entity → Response
#         return ProductMapper.to_response(saved)
#     
#     def update(self, product_id: int, data: ProductUpdate) -> ProductResponse:
#         """
#         Actualiza producto existente.
#         
#         Args:
#             product_id: ID del producto
#             data: ProductUpdate DTO con campos a actualizar
#             
#         Returns:
#             ProductResponse actualizado
#         """
#         entity = self.repo.get_by_id(product_id)
#         if not entity:
#             raise ValueError(f"Product {product_id} not found")
#         
#         # Mapper aplica cambios del DTO a la entidad
#         updated = ProductMapper.update_entity(entity, data)
#         
#         # Persistir
#         saved = self.repo.update(updated)
#         
#         # Mapper convierte Entity → Response
#         return ProductMapper.to_response(saved)
#     
#     def delete(self, product_id: int) -> None:
#         """Elimina producto."""
#         entity = self.repo.get_by_id(product_id)
#         if not entity:
#             raise ValueError(f"Product {product_id} not found")
#         
#         self.repo.delete(entity)
