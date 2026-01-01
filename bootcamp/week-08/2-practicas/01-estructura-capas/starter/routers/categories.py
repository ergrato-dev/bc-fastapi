# ============================================
# ROUTER CATEGORIES
# ============================================
print("--- Router: Categories Endpoints ---")

# El router define los endpoints HTTP para categorías.
# Solo maneja HTTP, delega lógica al Service.
# Pertenece a la capa de Presentation.

# Descomenta las siguientes líneas:

# from fastapi import APIRouter, Depends, HTTPException, status

# from schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
# from services.category import CategoryService
# from dependencies import get_category_service

# router = APIRouter(
#     prefix="/categories",
#     tags=["categories"]
# )


# @router.get("/", response_model=list[CategoryResponse])
# def list_categories(
#     skip: int = 0,
#     limit: int = 100,
#     service: CategoryService = Depends(get_category_service)
# ):
#     """Lista todas las categorías con paginación."""
#     return service.get_all(skip=skip, limit=limit)


# @router.get("/{category_id}", response_model=CategoryResponse)
# def get_category(
#     category_id: int,
#     service: CategoryService = Depends(get_category_service)
# ):
#     """Obtiene una categoría por ID."""
#     try:
#         return service.get_by_id(category_id)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))


# @router.post(
#     "/",
#     response_model=CategoryResponse,
#     status_code=status.HTTP_201_CREATED
# )
# def create_category(
#     data: CategoryCreate,
#     service: CategoryService = Depends(get_category_service)
# ):
#     """Crea una nueva categoría."""
#     try:
#         return service.create(data)
#     except ValueError as e:
#         raise HTTPException(status_code=409, detail=str(e))


# @router.patch("/{category_id}", response_model=CategoryResponse)
# def update_category(
#     category_id: int,
#     data: CategoryUpdate,
#     service: CategoryService = Depends(get_category_service)
# ):
#     """Actualiza una categoría existente."""
#     try:
#         return service.update(category_id, data)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))


# @router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_category(
#     category_id: int,
#     service: CategoryService = Depends(get_category_service)
# ):
#     """Elimina una categoría."""
#     try:
#         service.delete(category_id)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
