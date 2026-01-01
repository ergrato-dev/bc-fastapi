# ============================================
# PRODUCT REPOSITORY
# ============================================

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .base import BaseRepository
from models.product import Product
from exceptions.product import ProductAlreadyExistsError


class ProductRepository(BaseRepository[Product]):
    """Repository para Product."""
    
    def __init__(self, db: Session):
        super().__init__(db, Product)
    
    def get_by_sku(self, sku: str) -> Product | None:
        """Obtiene producto por SKU."""
        stmt = select(Product).where(Product.sku == sku)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_by_category(self, category_id: int) -> list[Product]:
        """
        Obtiene productos de una categoría.
        
        TODO: Implementar query
        """
        stmt = select(Product).where(Product.category_id == category_id)
        return list(self.db.execute(stmt).scalars().all())
    
    def get_active(self) -> list[Product]:
        """Obtiene solo productos activos."""
        stmt = select(Product).where(Product.is_active == True)
        return list(self.db.execute(stmt).scalars().all())
    
    def add(self, product: Product) -> Product:
        """Agrega producto con manejo de SKU duplicado."""
        try:
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError:
            self.db.rollback()
            raise ProductAlreadyExistsError(product.sku)
