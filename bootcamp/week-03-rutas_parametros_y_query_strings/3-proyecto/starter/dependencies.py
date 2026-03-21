"""
Dependencias Reutilizables
==========================

Define dependencias para paginación, filtros y ordenamiento.

TODO: Completa las dependencias siguiendo las instrucciones.
"""

from fastapi import Query, Depends
from typing import Annotated
from schemas import SortOrder, ProductSortField


# ============================================
# PAGINACIÓN
# ============================================

class PaginationParams:
    """
    Dependencia para parámetros de paginación.
    
    TODO: Implementa los parámetros:
    - page: int (default 1, >= 1)
    - per_page: int (default 10, >= 1, <= 50)
    - offset: int (calculado)
    """
    
    def __init__(
        self,
        page: int = Query(default=1, ge=1, description="Page number"),
        per_page: int = Query(default=10, ge=1, le=50, description="Items per page")
    ):
        self.page = page
        self.per_page = per_page
        self.offset = (page - 1) * per_page


# Alias para usar con Annotated
PaginationDep = Annotated[PaginationParams, Depends()]


# ============================================
# FILTROS DE PRODUCTOS
# ============================================

class ProductFilters:
    """
    Dependencia para filtros de productos.
    
    TODO: Implementa los filtros:
    - search: str | None (min 2 chars)
    - category_id: int | None (> 0)
    - min_price: float | None (>= 0)
    - max_price: float | None (>= 0)
    - in_stock: bool | None
    - tags: list[str] (default [])
    """
    
    def __init__(
        self,
        # TODO: Añade los parámetros con Query()
        search: str | None = Query(default=None, min_length=2, description="Search in name and description"),
        category_id: int | None = Query(default=None, gt=0, description="Filter by category ID"),
        # TODO: Completa el resto de filtros
    ):
        self.search = search
        self.category_id = category_id
        # TODO: Inicializa el resto de atributos


# Alias
ProductFiltersDep = Annotated[ProductFilters, Depends()]


# ============================================
# ORDENAMIENTO
# ============================================

class SortingParams:
    """
    Dependencia para ordenamiento.
    
    TODO: Implementa los parámetros:
    - sort_by: ProductSortField (default name)
    - order: SortOrder (default asc)
    """
    
    def __init__(
        self,
        sort_by: ProductSortField = Query(default=ProductSortField.name, description="Field to sort by"),
        order: SortOrder = Query(default=SortOrder.asc, description="Sort order")
    ):
        self.sort_by = sort_by
        self.order = order


# Alias
SortingDep = Annotated[SortingParams, Depends()]
