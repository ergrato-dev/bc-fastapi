# ============================================
# PRODUCT REPOSITORY
# ============================================
print("--- Repository: Product Repository ---")

# Repository para acceso a datos de Product.
# Solo operaciones de persistencia, sin lógica de negocio.

# Descomenta las siguientes líneas:

# from sqlalchemy import select
# from sqlalchemy.orm import Session

# from models.product import Product


# class ProductRepository:
#     """Repository para operaciones con Product."""
#     
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, product_id: int) -> Product | None:
#         """Obtiene producto por ID."""
#         return self.db.get(Product, product_id)
#     
#     def get_by_sku(self, sku: str) -> Product | None:
#         """Obtiene producto por SKU."""
#         stmt = select(Product).where(Product.sku == sku)
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     def get_all(self, skip: int = 0, limit: int = 100) -> list[Product]:
#         """Lista productos con paginación."""
#         stmt = select(Product).offset(skip).limit(limit)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def exists_by_sku(self, sku: str) -> bool:
#         """Verifica si existe producto con SKU."""
#         return self.get_by_sku(sku) is not None
#     
#     def add(self, product: Product) -> Product:
#         """Agrega nuevo producto."""
#         self.db.add(product)
#         self.db.commit()
#         self.db.refresh(product)
#         return product
#     
#     def update(self, product: Product) -> Product:
#         """Actualiza producto existente."""
#         self.db.commit()
#         self.db.refresh(product)
#         return product
#     
#     def delete(self, product: Product) -> None:
#         """Elimina producto."""
#         self.db.delete(product)
#         self.db.commit()
