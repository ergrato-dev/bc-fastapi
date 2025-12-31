"""
Router de Categorías
====================

CRUD completo para categorías.

TODO: Implementa los endpoints siguiendo las instrucciones.
"""

from fastapi import APIRouter, Path, HTTPException, status
from datetime import datetime

from database import categories_db, get_next_category_id
from schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    responses={404: {"description": "Category not found"}}
)


# ============================================
# GET /categories - Listar todas
# ============================================

@router.get("/", response_model=list[CategoryResponse])
async def list_categories():
    """
    Listar todas las categorías.
    
    TODO: Retorna todas las categorías de categories_db
    """
    # TODO: Implementar
    # return list(categories_db.values())
    pass


# ============================================
# GET /categories/{id} - Obtener una
# ============================================

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(
    category_id: int = Path(..., gt=0, description="Category ID")
):
    """
    Obtener una categoría por ID.
    
    TODO: 
    1. Buscar en categories_db
    2. Si no existe, HTTPException 404
    3. Retornar la categoría
    """
    # TODO: Implementar
    pass


# ============================================
# POST /categories - Crear
# ============================================

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate):
    """
    Crear una nueva categoría.
    
    TODO:
    1. Obtener nuevo ID con get_next_category_id()
    2. Crear dict con id, datos del schema, created_at
    3. Guardar en categories_db
    4. Retornar la categoría creada
    """
    # TODO: Implementar
    pass


# ============================================
# PUT /categories/{id} - Actualizar completo
# ============================================

@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: int = Path(..., gt=0),
    category: CategoryCreate = ...
):
    """
    Actualizar una categoría completamente.
    
    TODO:
    1. Verificar que existe (404 si no)
    2. Actualizar todos los campos
    3. Retornar la categoría actualizada
    """
    # TODO: Implementar
    pass


# ============================================
# DELETE /categories/{id} - Eliminar
# ============================================

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int = Path(..., gt=0)
):
    """
    Eliminar una categoría.
    
    TODO:
    1. Verificar que existe (404 si no)
    2. Eliminar de categories_db
    3. Retornar None (204 No Content)
    """
    # TODO: Implementar
    pass
