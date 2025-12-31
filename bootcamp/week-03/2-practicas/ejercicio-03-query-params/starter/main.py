"""
Ejercicio 03: Query Parameters - Filtrado y Paginación
======================================================

Objetivo: Implementar filtrado, paginación y ordenamiento.

Instrucciones:
1. Lee cada sección
2. Descomenta el código
3. Prueba en http://localhost:8000/docs
"""

from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum

app = FastAPI(
    title="Ejercicio 03 - Query Parameters",
    description="Aprendiendo filtrado y paginación",
    version="1.0.0"
)

# ============================================
# BASE DE DATOS SIMULADA
# ============================================

products_db = [
    {"id": 1, "name": "Laptop Pro", "price": 1299.99, "category": "electronics", "tags": ["new", "featured"]},
    {"id": 2, "name": "Wireless Mouse", "price": 29.99, "category": "electronics", "tags": ["sale"]},
    {"id": 3, "name": "USB-C Hub", "price": 49.99, "category": "electronics", "tags": ["new"]},
    {"id": 4, "name": "Python Book", "price": 39.99, "category": "books", "tags": ["bestseller"]},
    {"id": 5, "name": "FastAPI Guide", "price": 29.99, "category": "books", "tags": ["new", "featured"]},
    {"id": 6, "name": "Desk Lamp", "price": 59.99, "category": "home", "tags": ["sale"]},
    {"id": 7, "name": "Coffee Maker", "price": 89.99, "category": "home", "tags": []},
    {"id": 8, "name": "Headphones", "price": 199.99, "category": "electronics", "tags": ["featured"]},
    {"id": 9, "name": "Notebook Set", "price": 15.99, "category": "office", "tags": ["sale"]},
    {"id": 10, "name": "Monitor 27\"", "price": 349.99, "category": "electronics", "tags": ["new"]},
]

# ============================================
# PASO 2: Query Parameters Básicos
# ============================================
print("--- Paso 2: Query params básicos ---")

# Query parameters con valores por defecto
# Descomenta las siguientes líneas:

# @app.get("/items", tags=["Paso 2"])
# async def list_items(skip: int = 0, limit: int = 10):
#     """
#     Query parameters con valores por defecto.
#     
#     - /items → skip=0, limit=10
#     - /items?skip=5 → skip=5, limit=10
#     - /items?limit=20 → skip=0, limit=20
#     - /items?skip=10&limit=5 → skip=10, limit=5
#     """
#     items = products_db[skip:skip + limit]
#     return {
#         "skip": skip,
#         "limit": limit,
#         "count": len(items),
#         "items": items
#     }


# Query parameter requerido (sin default)
# Descomenta las siguientes líneas:

# @app.get("/search", tags=["Paso 2"])
# async def search(q: str):
#     """
#     Query parameter REQUERIDO (sin default).
#     
#     - /search?q=laptop ✅
#     - /search ❌ Error 422
#     """
#     results = [p for p in products_db if q.lower() in p["name"].lower()]
#     return {"query": q, "results": results}


# ============================================
# PASO 3: Validación con Query()
# ============================================
print("--- Paso 3: Validación ---")

# Query() agrega validación y documentación
# Descomenta las siguientes líneas:

# @app.get("/products/validated", tags=["Paso 3"])
# async def list_products_validated(
#     skip: int = Query(
#         default=0,
#         ge=0,
#         description="Number of items to skip"
#     ),
#     limit: int = Query(
#         default=10,
#         ge=1,
#         le=100,
#         description="Maximum items to return (1-100)"
#     ),
#     q: str | None = Query(
#         default=None,
#         min_length=2,
#         max_length=50,
#         description="Search query (2-50 chars)"
#     )
# ):
#     """
#     Query parameters con validación.
#     
#     - skip >= 0
#     - limit entre 1 y 100
#     - q entre 2 y 50 caracteres (si se proporciona)
#     """
#     items = products_db.copy()
#     
#     if q:
#         items = [p for p in items if q.lower() in p["name"].lower()]
#     
#     items = items[skip:skip + limit]
#     
#     return {
#         "skip": skip,
#         "limit": limit,
#         "search": q,
#         "items": items
#     }


# ============================================
# PASO 4: Filtrado
# ============================================
print("--- Paso 4: Filtrado ---")

# Filtros opcionales
# Descomenta las siguientes líneas:

# @app.get("/products/filter", tags=["Paso 4"])
# async def filter_products(
#     category: str | None = Query(
#         default=None,
#         description="Filter by category"
#     ),
#     min_price: float | None = Query(
#         default=None,
#         ge=0,
#         description="Minimum price"
#     ),
#     max_price: float | None = Query(
#         default=None,
#         ge=0,
#         description="Maximum price"
#     ),
#     search: str | None = Query(
#         default=None,
#         min_length=2,
#         description="Search in product name"
#     ),
#     in_stock: bool | None = Query(
#         default=None,
#         description="Filter by stock availability"
#     )
# ):
#     """
#     Filtrado con múltiples criterios opcionales.
#     
#     Los filtros se aplican solo si se proporcionan.
#     """
#     result = products_db.copy()
#     applied_filters = {}
#     
#     if category:
#         result = [p for p in result if p["category"] == category]
#         applied_filters["category"] = category
#     
#     if min_price is not None:
#         result = [p for p in result if p["price"] >= min_price]
#         applied_filters["min_price"] = min_price
#     
#     if max_price is not None:
#         result = [p for p in result if p["price"] <= max_price]
#         applied_filters["max_price"] = max_price
#     
#     if search:
#         result = [p for p in result if search.lower() in p["name"].lower()]
#         applied_filters["search"] = search
#     
#     return {
#         "applied_filters": applied_filters,
#         "count": len(result),
#         "products": result
#     }


# ============================================
# PASO 5: Paginación Completa
# ============================================
print("--- Paso 5: Paginación ---")

# Paginación con metadatos
# Descomenta las siguientes líneas:

# class PaginatedResponse(BaseModel):
#     items: list[dict]
#     total: int
#     page: int
#     per_page: int
#     pages: int
#     has_next: bool
#     has_prev: bool


# @app.get("/products/paginated", response_model=PaginatedResponse, tags=["Paso 5"])
# async def list_products_paginated(
#     page: int = Query(default=1, ge=1, description="Page number"),
#     per_page: int = Query(default=5, ge=1, le=50, description="Items per page")
# ):
#     """
#     Paginación basada en número de página.
#     
#     Retorna metadatos útiles para navegación.
#     """
#     total = len(products_db)
#     pages = (total + per_page - 1) // per_page  # Ceiling division
#     
#     start = (page - 1) * per_page
#     end = start + per_page
#     items = products_db[start:end]
#     
#     return PaginatedResponse(
#         items=items,
#         total=total,
#         page=page,
#         per_page=per_page,
#         pages=pages,
#         has_next=page < pages,
#         has_prev=page > 1
#     )


# ============================================
# PASO 6: Listas de Valores
# ============================================
print("--- Paso 6: Listas ---")

# Aceptar múltiples valores del mismo parámetro
# Descomenta las siguientes líneas:

# @app.get("/products/by-tags", tags=["Paso 6"])
# async def filter_by_tags(
#     tags: list[str] = Query(
#         default=[],
#         description="Filter by tags (can specify multiple)"
#     )
# ):
#     """
#     Filtrar por múltiples tags.
#     
#     Uso: /products/by-tags?tags=new&tags=featured
#     """
#     if not tags:
#         return {"tags": [], "products": products_db}
#     
#     # Productos que tienen AL MENOS uno de los tags
#     result = [
#         p for p in products_db
#         if any(tag in p.get("tags", []) for tag in tags)
#     ]
#     
#     return {
#         "tags": tags,
#         "count": len(result),
#         "products": result
#     }


# @app.get("/products/by-ids", tags=["Paso 6"])
# async def get_by_ids(
#     ids: list[int] = Query(
#         ...,  # Requerido
#         description="Product IDs to retrieve"
#     )
# ):
#     """
#     Obtener productos por lista de IDs.
#     
#     Uso: /products/by-ids?ids=1&ids=3&ids=5
#     """
#     result = [p for p in products_db if p["id"] in ids]
#     return {
#         "requested_ids": ids,
#         "found": len(result),
#         "products": result
#     }


# ============================================
# PASO 7: Ordenamiento
# ============================================
print("--- Paso 7: Ordenamiento ---")

# Combinar filtrado con ordenamiento
# Descomenta las siguientes líneas:

# class SortOrder(str, Enum):
#     asc = "asc"
#     desc = "desc"


# class SortField(str, Enum):
#     name = "name"
#     price = "price"
#     id = "id"


# @app.get("/products/sorted", tags=["Paso 7"])
# async def list_products_sorted(
#     sort_by: SortField = Query(
#         default=SortField.name,
#         description="Field to sort by"
#     ),
#     order: SortOrder = Query(
#         default=SortOrder.asc,
#         description="Sort order"
#     ),
#     category: str | None = Query(default=None),
#     page: int = Query(default=1, ge=1),
#     per_page: int = Query(default=10, ge=1, le=50)
# ):
#     """
#     Filtrado, ordenamiento y paginación combinados.
#     """
#     result = products_db.copy()
#     
#     # Filtrar
#     if category:
#         result = [p for p in result if p["category"] == category]
#     
#     # Ordenar
#     reverse = order == SortOrder.desc
#     result.sort(key=lambda x: x[sort_by.value], reverse=reverse)
#     
#     # Paginar
#     total = len(result)
#     start = (page - 1) * per_page
#     result = result[start:start + per_page]
#     
#     return {
#         "sort_by": sort_by.value,
#         "order": order.value,
#         "category": category,
#         "page": page,
#         "per_page": per_page,
#         "total": total,
#         "products": result
#     }


# ============================================
# ENDPOINT DE VERIFICACIÓN
# ============================================

@app.get("/", tags=["Root"])
async def root():
    """Endpoint raíz para verificar que la API funciona"""
    return {
        "message": "API funcionando correctamente",
        "docs": "/docs",
        "ejercicio": "03 - Query Parameters",
        "total_products": len(products_db)
    }


@app.get("/health", tags=["Root"])
async def health_check():
    """Health check"""
    return {"status": "healthy"}
