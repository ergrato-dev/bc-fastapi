# ============================================
# PRODUCT REPOSITORY
# ============================================

# Descomenta las siguientes líneas:

# from sqlalchemy import select
# from sqlalchemy.orm import Session
# from models.product import Product


# class ProductRepository:
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, product_id: int) -> Product | None:
#         return self.db.get(Product, product_id)
#     
#     def get_all(self) -> list[Product]:
#         stmt = select(Product)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def add(self, product: Product) -> Product:
#         self.db.add(product)
#         self.db.commit()
#         self.db.refresh(product)
#         return product
#     
#     def update(self, product: Product) -> Product:
#         """Actualiza producto (para reducir stock)."""
#         self.db.commit()
#         self.db.refresh(product)
#         return product
