# ============================================
# PRODUCTS ROUTER
# ============================================

from fastapi import APIRouter, Depends, status

from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from services.product import ProductService
from dependencies import get_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductResponse])
def list_products(service: ProductService = Depends(get_product_service)):
    """Lista todos los productos."""
    return service.get_all()


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    """Obtiene producto por ID."""
    return service.get_by_id(product_id)


@router.get("/category/{category_id}", response_model=list[ProductResponse])
def get_products_by_category(
    category_id: int,
    service: ProductService = Depends(get_product_service)
):
    """Obtiene productos de una categoría."""
    return service.get_by_category(category_id)


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    data: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    """Crea nuevo producto."""
    return service.create(data)


@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    data: ProductUpdate,
    service: ProductService = Depends(get_product_service)
):
    """Actualiza producto."""
    return service.update(product_id, data)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    """Elimina producto."""
    service.delete(product_id)
