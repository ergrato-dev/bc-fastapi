# ============================================
# CATEGORIES ROUTER
# ============================================

from fastapi import APIRouter, Depends, status

from schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from services.category import CategoryService
from dependencies import get_category_service

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=list[CategoryResponse])
def list_categories(service: CategoryService = Depends(get_category_service)):
    """Lista todas las categorías."""
    return service.get_all()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service)
):
    """Obtiene categoría por ID."""
    return service.get_by_id(category_id)


@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_category(
    data: CategoryCreate,
    service: CategoryService = Depends(get_category_service)
):
    """Crea nueva categoría."""
    return service.create(data)


@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    data: CategoryUpdate,
    service: CategoryService = Depends(get_category_service)
):
    """Actualiza categoría."""
    return service.update(category_id, data)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service)
):
    """Elimina categoría (si no tiene productos)."""
    service.delete(category_id)
