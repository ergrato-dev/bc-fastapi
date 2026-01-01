# ============================================
# PASO 3: Refactorizar ProductService
# ============================================
"""
El service ahora recibe un repositorio en lugar de una sesión.
Ya no tiene imports de SQLAlchemy.
"""

from pydantic import BaseModel, Field

from models import Product
# from repositories import ProductRepository  # ← Descomentar


# ============================================
# Schemas
# ============================================
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    price: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)


class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    description: str | None = None
    price: float | None = Field(None, gt=0)
    stock: int | None = Field(None, ge=0)
    is_active: bool | None = None


# ============================================
# Excepciones
# ============================================
class NotFoundError(Exception):
    pass


class BusinessError(Exception):
    pass


# ============================================
# Service ANTES (acceso directo a SQLAlchemy)
# ============================================
# from sqlalchemy import select
# from sqlalchemy.orm import Session
# 
# class ProductServiceOld:
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, product_id: int) -> Product:
#         product = self.db.get(Product, product_id)
#         if not product:
#             raise NotFoundError(f"Product {product_id} not found")
#         return product
#     
#     def list_all(self) -> list[Product]:
#         stmt = select(Product)
#         return list(self.db.execute(stmt).scalars().all())


# ============================================
# Service DESPUÉS (usa repositorio)
# Descomenta esta clase:
# ============================================

# class ProductService:
#     """Service que usa repositorio para acceso a datos"""
#     
#     def __init__(self, product_repo: ProductRepository):
#         # ✅ Recibe repositorio, NO Session
#         self.repo = product_repo
#     
#     def get_by_id(self, product_id: int) -> Product:
#         """Obtiene producto o lanza error"""
#         product = self.repo.get_by_id(product_id)
#         if not product:
#             raise NotFoundError(f"Product {product_id} not found")
#         return product
#     
#     def list_all(self, skip: int = 0, limit: int = 100) -> list[Product]:
#         """Lista todos los productos"""
#         return self.repo.get_all(skip=skip, limit=limit)
#     
#     def list_active(self) -> list[Product]:
#         """Lista solo productos activos"""
#         return self.repo.get_active()
#     
#     def create(self, data: ProductCreate) -> Product:
#         """Crea nuevo producto"""
#         product = Product(
#             name=data.name,
#             description=data.description,
#             price=data.price,
#             stock=data.stock
#         )
#         return self.repo.add(product)
#     
#     def update(self, product_id: int, data: ProductUpdate) -> Product:
#         """Actualiza producto existente"""
#         product = self.get_by_id(product_id)
#         
#         update_data = data.model_dump(exclude_unset=True)
#         for key, value in update_data.items():
#             setattr(product, key, value)
#         
#         return self.repo.update(product)
#     
#     def delete(self, product_id: int) -> None:
#         """Elimina producto"""
#         product = self.get_by_id(product_id)
#         self.repo.delete(product)
#     
#     def update_stock(self, product_id: int, quantity: int) -> Product:
#         """Actualiza stock (lógica de negocio)"""
#         product = self.get_by_id(product_id)
#         
#         new_stock = product.stock + quantity
#         if new_stock < 0:
#             raise BusinessError("Insufficient stock")
#         
#         product.stock = new_stock
#         return self.repo.update(product)
#     
#     def search(self, query: str) -> list[Product]:
#         """Busca productos por nombre"""
#         return self.repo.search_by_name(query)
