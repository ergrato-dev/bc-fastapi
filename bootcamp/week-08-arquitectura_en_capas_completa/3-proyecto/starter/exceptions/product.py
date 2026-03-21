# ============================================
# EXCEPCIONES PRODUCT
# ============================================

from .base import NotFoundError, ConflictError, ValidationError


class ProductNotFoundError(NotFoundError):
    """Producto no encontrado."""
    
    def __init__(self, product_id: int):
        super().__init__(
            message=f"Product with id {product_id} not found",
            code="PRODUCT_NOT_FOUND"
        )


class ProductAlreadyExistsError(ConflictError):
    """SKU ya existe."""
    
    def __init__(self, sku: str):
        super().__init__(
            message=f"Product with SKU '{sku}' already exists",
            code="PRODUCT_SKU_DUPLICATE"
        )


class InsufficientStockError(ValidationError):
    """Stock insuficiente."""
    
    def __init__(self, product_id: int, requested: int, available: int):
        super().__init__(
            message=f"Insufficient stock for product {product_id}. Requested: {requested}, Available: {available}",
            code="INSUFFICIENT_STOCK"
        )
