# ============================================
# PRODUCT REPOSITORY CON TRADUCCIÓN DE ERRORES
# ============================================
print("--- Repository: Product con Error Translation ---")

# El repository traduce errores técnicos (IntegrityError)
# a excepciones de dominio (ProductAlreadyExistsError).

# Descomenta las siguientes líneas:

# from sqlalchemy import select
# from sqlalchemy.orm import Session
# from sqlalchemy.exc import IntegrityError

# from models.product import Product
# from exceptions.product import ProductAlreadyExistsError


# class ProductRepository:
#     """
#     Repository con traducción de errores de DB.
#     """
#     
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, product_id: int) -> Product | None:
#         return self.db.get(Product, product_id)
#     
#     def get_by_sku(self, sku: str) -> Product | None:
#         stmt = select(Product).where(Product.sku == sku)
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     def get_all(self) -> list[Product]:
#         stmt = select(Product)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def add(self, product: Product) -> Product:
#         """
#         Agrega producto traduciendo errores de DB.
#         
#         IntegrityError (unique constraint) → ProductAlreadyExistsError
#         """
#         try:
#             self.db.add(product)
#             self.db.commit()
#             self.db.refresh(product)
#             return product
#         except IntegrityError:
#             self.db.rollback()
#             # Traducir error técnico a error de dominio
#             raise ProductAlreadyExistsError(product.sku)
#     
#     def update(self, product: Product) -> Product:
#         self.db.commit()
#         self.db.refresh(product)
#         return product
#     
#     def delete(self, product: Product) -> None:
#         self.db.delete(product)
#         self.db.commit()
