# ============================================
# ROUTER PRODUCTS (auxiliar)
# ============================================

# Descomenta para crear productos de prueba:

# from fastapi import APIRouter, Depends, status
# from sqlalchemy.orm import Session

# from database import get_db
# from models.product import Product
# from schemas.product import ProductCreate, ProductResponse
# from repositories.product import ProductRepository

# router = APIRouter(prefix="/products", tags=["products"])


# @router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
# def create_product(data: ProductCreate, db: Session = Depends(get_db)):
#     repo = ProductRepository(db)
#     product = Product(
#         name=data.name,
#         sku=data.sku,
#         price=data.price,
#         stock=data.stock
#     )
#     return repo.add(product)


# @router.get("/", response_model=list[ProductResponse])
# def list_products(db: Session = Depends(get_db)):
#     repo = ProductRepository(db)
#     return repo.get_all()
