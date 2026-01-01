# ============================================
# EXCEPCIONES CATEGORY
# ============================================

from .base import NotFoundError, ValidationError


class CategoryNotFoundError(NotFoundError):
    """Categoría no encontrada."""
    
    def __init__(self, category_id: int):
        super().__init__(
            message=f"Category with id {category_id} not found",
            code="CATEGORY_NOT_FOUND"
        )


class CategoryHasProductsError(ValidationError):
    """No se puede eliminar categoría con productos."""
    
    def __init__(self, category_id: int, product_count: int):
        super().__init__(
            message=f"Category {category_id} has {product_count} products and cannot be deleted",
            code="CATEGORY_HAS_PRODUCTS"
        )
