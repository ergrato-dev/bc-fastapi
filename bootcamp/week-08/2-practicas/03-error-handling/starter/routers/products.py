# ============================================
# ROUTER PRODUCTS - SIN TRY/EXCEPT
# ============================================
print("--- Router: Products sin try/except ---")

# Observa cómo el router NO tiene try/except.
# Los exception handlers globales manejan los errores.
# Esto hace el código más limpio y consistente.

# Descomenta las siguientes líneas:

# from fastapi import APIRouter, Depends, status
# from sqlalchemy.orm import Session

# from database import get_db
# from schemas.product import (
#     ProductCreate,
#     ProductUpdate,
#     ProductResponse,
#     StockUpdate
# )
# from services.product import ProductService
# from repositories.product import ProductRepository

# router = APIRouter(prefix="/products", tags=["products"])


# def get_service(db: Session = Depends(get_db)) -> ProductService:
#     repo = ProductRepository(db)
#     return ProductService(repo)


# @router.get("/", response_model=list[ProductResponse])
# def list_products(service: ProductService = Depends(get_service)):
#     """Lista todos los productos."""
#     return service.get_all()


# @router.get("/{product_id}", response_model=ProductResponse)
# def get_product(
#     product_id: int,
#     service: ProductService = Depends(get_service)
# ):
#     """
#     Obtiene producto por ID.
#     
#     Si no existe, ProductNotFoundError → 404 automático.
#     NO necesita try/except.
#     """
#     return service.get_by_id(product_id)


# @router.post(
#     "/",
#     response_model=ProductResponse,
#     status_code=status.HTTP_201_CREATED
# )
# def create_product(
#     data: ProductCreate,
#     service: ProductService = Depends(get_service)
# ):
#     """
#     Crea nuevo producto.
#     
#     Si SKU duplicado, ProductAlreadyExistsError → 409 automático.
#     NO necesita try/except.
#     """
#     return service.create(data)


# @router.patch("/{product_id}", response_model=ProductResponse)
# def update_product(
#     product_id: int,
#     data: ProductUpdate,
#     service: ProductService = Depends(get_service)
# ):
#     """Actualiza producto."""
#     return service.update(product_id, data)


# @router.patch("/{product_id}/reduce-stock", response_model=ProductResponse)
# def reduce_stock(
#     product_id: int,
#     data: StockUpdate,
#     service: ProductService = Depends(get_service)
# ):
#     """
#     Reduce stock del producto.
#     
#     Si stock insuficiente, InsufficientStockError → 400 automático.
#     NO necesita try/except.
#     """
#     return service.reduce_stock(product_id, data.quantity)


# @router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_product(
#     product_id: int,
#     service: ProductService = Depends(get_service)
# ):
#     """Elimina producto."""
#     service.delete(product_id)
