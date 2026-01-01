# ============================================
# CATEGORY REPOSITORY
# ============================================

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from .base import BaseRepository
from models.category import Category
from models.product import Product


class CategoryRepository(BaseRepository[Category]):
    """Repository para Category."""
    
    def __init__(self, db: Session):
        super().__init__(db, Category)
    
    def get_by_name(self, name: str) -> Category | None:
        """Obtiene categoría por nombre."""
        stmt = select(Category).where(Category.name == name)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_active(self) -> list[Category]:
        """Obtiene solo categorías activas."""
        stmt = select(Category).where(Category.is_active == True)
        return list(self.db.execute(stmt).scalars().all())
    
    def count_products(self, category_id: int) -> int:
        """
        Cuenta productos en una categoría.
        
        TODO: Implementar para validar antes de eliminar
        """
        stmt = select(func.count(Product.id)).where(
            Product.category_id == category_id
        )
        result = self.db.execute(stmt).scalar()
        return result or 0
