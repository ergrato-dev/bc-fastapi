"""
Router de Productos
===================

CRUD con filtrado, paginación y ordenamiento.

TODO: Implementa los endpoints siguiendo las instrucciones.
"""

from fastapi import APIRouter, Path, HTTPException, status
from datetime import datetime

from database import products_db, categories_db, get_next_product_id
from schemas import ProductCreate, ProductUpdate, ProductResponse, SortOrder
from dependencies import PaginationDep, ProductFiltersDep, SortingDep

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Product not found"}}
)


# ============================================
# GET /products - Listar con filtros
# ============================================

@router.get("/")
async def list_products(
    pagination: PaginationDep,
    filters: ProductFiltersDep,
    sorting: SortingDep
):
    """
    Listar productos con filtrado, paginación y ordenamiento.
    
    TODO:
    1. Obtener todos los productos
    2. Aplicar filtros:
       - search: buscar en name y description
       - category_id: filtrar por categoría
       - min_price/max_price: rango de precios
       - in_stock: stock > 0
       - tags: productos que tengan al menos un tag
    3. Ordenar según sorting params
    4. Paginar
    5. Retornar con metadatos de paginación
    """
    # TODO: Implementar
    # Ejemplo de estructura de respuesta:
    # return {
    #     "items": [...],
    #     "total": 100,
    #     "page": pagination.page,
    #     "per_page": pagination.per_page,
    #     "pages": 10,
    #     "has_next": True,
    #     "has_prev": False
    # }
    pass


# ============================================
# GET /products/{id} - Obtener uno
# ============================================

@router.get("/{product_id}")
async def get_product(
    product_id: int = Path(..., gt=0, description="Product ID")
):
    """
    Obtener un producto por ID.
    
    TODO:
    1. Buscar en products_db
    2. Si no existe, HTTPException 404
    3. Incluir datos de la categoría
    4. Retornar el producto
    """
    # TODO: Implementar
    pass


# ============================================
# POST /products - Crear
# ============================================

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    """
    Crear un nuevo producto.
    
    TODO:
    1. Verificar que category_id existe (400 si no)
    2. Obtener nuevo ID
    3. Crear dict con datos
    4. Guardar en products_db
    5. Retornar el producto creado
    """
    # TODO: Implementar
    pass


# ============================================
# PUT /products/{id} - Actualizar completo
# ============================================

@router.put("/{product_id}")
async def replace_product(
    product_id: int = Path(..., gt=0),
    product: ProductCreate = ...
):
    """
    Reemplazar un producto completamente.
    
    TODO:
    1. Verificar que el producto existe (404)
    2. Verificar que category_id existe (400)
    3. Reemplazar todos los campos
    4. Retornar el producto actualizado
    """
    # TODO: Implementar
    pass


# ============================================
# PATCH /products/{id} - Actualizar parcial
# ============================================

@router.patch("/{product_id}")
async def update_product(
    product_id: int = Path(..., gt=0),
    product: ProductUpdate = ...
):
    """
    Actualizar un producto parcialmente.
    
    TODO:
    1. Verificar que el producto existe (404)
    2. Si se proporciona category_id, verificar que existe (400)
    3. Actualizar solo campos proporcionados (exclude_unset=True)
    4. Retornar el producto actualizado
    """
    # TODO: Implementar
    pass


# ============================================
# DELETE /products/{id} - Eliminar
# ============================================

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int = Path(..., gt=0)
):
    """
    Eliminar un producto.
    
    TODO:
    1. Verificar que existe (404)
    2. Eliminar de products_db
    3. Retornar None
    """
    # TODO: Implementar
    pass
