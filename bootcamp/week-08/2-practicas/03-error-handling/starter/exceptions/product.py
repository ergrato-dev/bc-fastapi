# ============================================
# EXCEPCIONES DE PRODUCT
# ============================================
print("--- Exceptions: Product Exceptions ---")

# Excepciones específicas del dominio Product.
# Heredan de las excepciones base y añaden contexto.

# Descomenta las siguientes líneas:

# from .base import NotFoundError, ConflictError, ValidationError


# class ProductNotFoundError(NotFoundError):
#     """
#     Producto no encontrado.
#     
#     Se lanza cuando se busca un producto que no existe.
#     """
#     
#     def __init__(self, product_id: int):
#         super().__init__(
#             message=f"Product with id {product_id} not found",
#             code="PRODUCT_NOT_FOUND"
#         )
#         self.product_id = product_id


# class ProductAlreadyExistsError(ConflictError):
#     """
#     Producto ya existe (SKU duplicado).
#     
#     Se lanza cuando se intenta crear con SKU existente.
#     """
#     
#     def __init__(self, sku: str):
#         super().__init__(
#             message=f"Product with SKU '{sku}' already exists",
#             code="PRODUCT_SKU_DUPLICATE"
#         )
#         self.sku = sku


# class InsufficientStockError(ValidationError):
#     """
#     Stock insuficiente.
#     
#     Se lanza cuando no hay suficiente stock para una operación.
#     """
#     
#     def __init__(self, product_id: int, requested: int, available: int):
#         super().__init__(
#             message=(
#                 f"Insufficient stock for product {product_id}. "
#                 f"Requested: {requested}, Available: {available}"
#             ),
#             code="INSUFFICIENT_STOCK"
#         )
#         self.product_id = product_id
#         self.requested = requested
#         self.available = available
