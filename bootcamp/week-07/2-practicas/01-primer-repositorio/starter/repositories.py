# ============================================
# PASO 2: Crear ProductRepository
# ============================================
"""
El repositorio encapsula todas las operaciones de acceso a datos.
El service ya no necesitará conocer SQLAlchemy.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Product


# ============================================
# Descomenta la clase ProductRepository:
# ============================================

# class ProductRepository:
#     """Repositorio para operaciones de Product"""
#     
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, product_id: int) -> Product | None:
#         """Obtiene producto por ID"""
#         return self.db.get(Product, product_id)
#     
#     def get_all(self, skip: int = 0, limit: int = 100) -> list[Product]:
#         """Lista productos con paginación"""
#         stmt = select(Product).offset(skip).limit(limit)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def get_active(self) -> list[Product]:
#         """Obtiene solo productos activos"""
#         stmt = select(Product).where(Product.is_active == True)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def add(self, product: Product) -> Product:
#         """Agrega producto a la sesión"""
#         self.db.add(product)
#         self.db.flush()
#         self.db.refresh(product)
#         return product
#     
#     def update(self, product: Product) -> Product:
#         """Actualiza producto"""
#         self.db.flush()
#         self.db.refresh(product)
#         return product
#     
#     def delete(self, product: Product) -> None:
#         """Elimina producto"""
#         self.db.delete(product)
#         self.db.flush()
#     
#     def search_by_name(self, query: str) -> list[Product]:
#         """Busca productos por nombre"""
#         stmt = select(Product).where(Product.name.ilike(f"%{query}%"))
#         return list(self.db.execute(stmt).scalars().all())
