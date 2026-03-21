# ============================================
# PASO 3: Repositorios Específicos
# ============================================
"""
Los repositorios específicos heredan de BaseRepository
y agregan métodos particulares.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from models import Product, Category
# from base_repository import BaseRepository  # ← Descomentar


# ============================================
# Descomenta ProductRepository:
# ============================================

# class ProductRepository(BaseRepository[Product]):
#     """Repositorio para Product con métodos específicos"""
#     
#     def __init__(self, db: Session):
#         super().__init__(db, Product)
#     
#     def get_by_category(self, category_id: int) -> list[Product]:
#         """Obtiene productos de una categoría"""
#         return self.filter_by(category_id=category_id)
#     
#     def get_with_category(self, product_id: int) -> Product | None:
#         """Obtiene producto con categoría cargada"""
#         stmt = (
#             select(Product)
#             .options(selectinload(Product.category))
#             .where(Product.id == product_id)
#         )
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     def get_in_stock(self) -> list[Product]:
#         """Obtiene productos con stock > 0"""
#         stmt = select(Product).where(Product.stock > 0)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def search_by_name(self, query: str) -> list[Product]:
#         """Busca por nombre (case-insensitive)"""
#         stmt = select(Product).where(Product.name.ilike(f"%{query}%"))
#         return list(self.db.execute(stmt).scalars().all())


# ============================================
# Descomenta CategoryRepository:
# ============================================

# class CategoryRepository(BaseRepository[Category]):
#     """Repositorio para Category con métodos específicos"""
#     
#     def __init__(self, db: Session):
#         super().__init__(db, Category)
#     
#     def get_by_name(self, name: str) -> Category | None:
#         """Obtiene categoría por nombre"""
#         return self.first(name=name)
#     
#     def get_with_products(self, category_id: int) -> Category | None:
#         """Obtiene categoría con sus productos"""
#         stmt = (
#             select(Category)
#             .options(selectinload(Category.products))
#             .where(Category.id == category_id)
#         )
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     def name_exists(self, name: str) -> bool:
#         """Verifica si nombre ya existe"""
#         return self.get_by_name(name) is not None
