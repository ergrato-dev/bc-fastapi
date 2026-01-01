# ============================================
# PRODUCT SERVICE CON EXCEPCIONES DE DOMINIO
# ============================================
print("--- Service: Product con Domain Exceptions ---")

# El service lanza excepciones de dominio específicas.
# Los handlers globales las convertirán en HTTP responses.

# Descomenta las siguientes líneas:

# from models.product import Product
# from schemas.product import ProductCreate, ProductUpdate
# from repositories.product import ProductRepository
# from exceptions.product import (
#     ProductNotFoundError,
#     InsufficientStockError
# )


# class ProductService:
#     """
#     Service que lanza excepciones de dominio.
#     """
#     
#     def __init__(self, repo: ProductRepository):
#         self.repo = repo
#     
#     def get_all(self) -> list[Product]:
#         return self.repo.get_all()
#     
#     def get_by_id(self, product_id: int) -> Product:
#         """
#         Obtiene producto o lanza ProductNotFoundError.
#         """
#         product = self.repo.get_by_id(product_id)
#         if not product:
#             raise ProductNotFoundError(product_id)
#         return product
#     
#     def create(self, data: ProductCreate) -> Product:
#         """
#         Crea producto.
#         
#         ProductAlreadyExistsError viene del repository si SKU duplicado.
#         """
#         product = Product(
#             name=data.name,
#             sku=data.sku,
#             price=data.price,
#             stock=data.stock
#         )
#         return self.repo.add(product)
#     
#     def update(self, product_id: int, data: ProductUpdate) -> Product:
#         """
#         Actualiza producto existente.
#         """
#         product = self.get_by_id(product_id)  # Lanza NotFound si no existe
#         
#         update_data = data.model_dump(exclude_unset=True)
#         for field, value in update_data.items():
#             setattr(product, field, value)
#         
#         return self.repo.update(product)
#     
#     def reduce_stock(self, product_id: int, quantity: int) -> Product:
#         """
#         Reduce stock del producto.
#         
#         Lanza InsufficientStockError si no hay suficiente.
#         """
#         product = self.get_by_id(product_id)
#         
#         if product.stock < quantity:
#             raise InsufficientStockError(
#                 product_id=product_id,
#                 requested=quantity,
#                 available=product.stock
#             )
#         
#         product.stock -= quantity
#         return self.repo.update(product)
#     
#     def delete(self, product_id: int) -> None:
#         """Elimina producto."""
#         product = self.get_by_id(product_id)
#         self.repo.delete(product)
