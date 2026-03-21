# ============================================
# EXCEPCIONES PRODUCT
# ============================================

from .base import NotFoundError, ValidationError


class ProductNotFoundError(NotFoundError):
    def __init__(self, product_id: int):
        super().__init__(
            message=f"Product with id {product_id} not found",
            code="PRODUCT_NOT_FOUND"
        )


class InsufficientStockError(ValidationError):
    def __init__(self, product_id: int, requested: int, available: int):
        super().__init__(
            message=(
                f"Insufficient stock for product {product_id}. "
                f"Requested: {requested}, Available: {available}"
            ),
            code="INSUFFICIENT_STOCK"
        )
