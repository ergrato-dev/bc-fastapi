# ============================================
# ROUTER PRODUCTS
# ============================================
print("--- Router: Products Endpoints ---")

# Router con endpoints que usan DTOs específicos.
# Observa cómo response_model define lo que se expone.

# Descomenta las siguientes líneas:

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from database import get_db
# from schemas.product import ProductCreate, ProductUpdate, ProductResponse
# from services.product import ProductService
# from repositories.product import ProductRepository

# router = APIRouter(prefix="/products", tags=["products"])


# def get_service(db: Session = Depends(get_db)) -> ProductService:
#     """Factory de ProductService."""
#     repo = ProductRepository(db)
#     return ProductService(repo)


# @router.get("/", response_model=list[ProductResponse])
# def list_products(service: ProductService = Depends(get_service)):
#     """
#     Lista todos los productos.
#     
#     Response: Lista de ProductResponse (sin campos internos)
#     """
#     return service.get_all()


# @router.get("/{product_id}", response_model=ProductResponse)
# def get_product(
#     product_id: int,
#     service: ProductService = Depends(get_service)
# ):
#     """
#     Obtiene producto por ID.
#     
#     Response: ProductResponse (sin cost_price, internal_notes)
#     """
#     try:
#         return service.get_by_id(product_id)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))


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
#     Input: ProductCreate (puede incluir cost_price)
#     Response: ProductResponse (SIN cost_price)
#     """
#     try:
#         return service.create(data)
#     except ValueError as e:
#         raise HTTPException(status_code=409, detail=str(e))


# @router.patch("/{product_id}", response_model=ProductResponse)
# def update_product(
#     product_id: int,
#     data: ProductUpdate,
#     service: ProductService = Depends(get_service)
# ):
#     """
#     Actualiza producto (PATCH - campos parciales).
#     
#     Input: ProductUpdate (solo campos a cambiar)
#     Response: ProductResponse
#     """
#     try:
#         return service.update(product_id, data)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))


# @router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_product(
#     product_id: int,
#     service: ProductService = Depends(get_service)
# ):
#     """Elimina producto."""
#     try:
#         service.delete(product_id)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
