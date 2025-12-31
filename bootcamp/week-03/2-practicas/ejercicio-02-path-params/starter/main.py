"""
Ejercicio 02: Path Parameters con Validación
=============================================

Objetivo: Aprender a validar path parameters con Path().

Instrucciones:
1. Lee cada sección
2. Descomenta el código
3. Prueba en http://localhost:8000/docs
"""

from fastapi import FastAPI, Path, HTTPException, status
from enum import Enum
from uuid import UUID

app = FastAPI(
    title="Ejercicio 02 - Path Parameters",
    description="Aprendiendo validación de path parameters",
    version="1.0.0"
)

# ============================================
# BASE DE DATOS SIMULADA
# ============================================

products_db = {
    1: {"name": "Laptop", "price": 999.99, "category": "electronics"},
    2: {"name": "Mouse", "price": 29.99, "category": "electronics"},
    3: {"name": "Book", "price": 19.99, "category": "books"},
}

users_db = {
    "john_doe": {"name": "John Doe", "role": "user"},
    "admin123": {"name": "Admin", "role": "admin"},
}

# ============================================
# PASO 2: Path Parameters Tipados
# ============================================
print("--- Paso 2: Tipos automáticos ---")

# FastAPI convierte automáticamente al tipo especificado
# Si falla la conversión, retorna 422 Unprocessable Entity
# Descomenta las siguientes líneas:

# @app.get("/items/{item_id}", tags=["Paso 2"])
# async def get_item(item_id: int):
#     """
#     Path parameter con tipo int.
#     
#     - /items/42 → OK
#     - /items/abc → Error 422
#     """
#     return {"item_id": item_id, "type": type(item_id).__name__}


# @app.get("/prices/{price}", tags=["Paso 2"])
# async def get_price(price: float):
#     """Path parameter con tipo float"""
#     return {"price": price, "type": type(price).__name__}


# @app.get("/orders/{order_id}", tags=["Paso 2"])
# async def get_order(order_id: UUID):
#     """
#     Path parameter con tipo UUID.
#     
#     Ejemplo válido: 550e8400-e29b-41d4-a716-446655440000
#     """
#     return {"order_id": str(order_id), "type": "UUID"}


# ============================================
# PASO 3: Validación Numérica con Path()
# ============================================
print("--- Paso 3: Validación numérica ---")

# Path() permite agregar validaciones y metadatos
# gt = greater than, ge = greater or equal
# lt = less than, le = less or equal
# Descomenta las siguientes líneas:

# @app.get("/products/{product_id}", tags=["Paso 3"])
# async def get_product(
#     product_id: int = Path(
#         ...,  # ... significa requerido
#         gt=0,  # Mayor que 0
#         le=10000,  # Menor o igual a 10000
#         title="Product ID",
#         description="The unique identifier of the product (1-10000)",
#         examples=[1, 42, 100]
#     )
# ):
#     """
#     Path parameter con validación numérica.
#     
#     Validaciones:
#     - gt=0: Debe ser mayor que 0
#     - le=10000: Debe ser menor o igual a 10000
#     """
#     if product_id not in products_db:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Product {product_id} not found"
#         )
#     return {"id": product_id, **products_db[product_id]}


# @app.get("/quantity/{qty}", tags=["Paso 3"])
# async def check_quantity(
#     qty: int = Path(
#         ...,
#         ge=1,  # Mínimo 1
#         le=100,  # Máximo 100
#         description="Quantity between 1 and 100"
#     )
# ):
#     """Validar cantidad en rango 1-100"""
#     return {"quantity": qty, "valid": True}


# ============================================
# PASO 4: Validación de Strings
# ============================================
print("--- Paso 4: Validación de strings ---")

# Path() también valida strings con min_length, max_length, pattern
# Descomenta las siguientes líneas:

# @app.get("/users/{username}", tags=["Paso 4"])
# async def get_user(
#     username: str = Path(
#         ...,
#         min_length=3,
#         max_length=20,
#         pattern=r"^[a-zA-Z0-9_]+$",  # Solo alfanuméricos y _
#         title="Username",
#         description="Username (3-20 chars, alphanumeric and underscore)",
#         examples=["john_doe", "admin123"]
#     )
# ):
#     """
#     Path parameter string con validación.
#     
#     - min_length=3: Al menos 3 caracteres
#     - max_length=20: Máximo 20 caracteres
#     - pattern: Solo letras, números y guión bajo
#     """
#     if username not in users_db:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"username": username, **users_db[username]}


# @app.get("/codes/{code}", tags=["Paso 4"])
# async def validate_code(
#     code: str = Path(
#         ...,
#         min_length=6,
#         max_length=6,
#         pattern=r"^[A-Z]{2}\d{4}$",  # 2 letras + 4 dígitos
#         description="Code format: XX0000 (e.g., AB1234)"
#     )
# ):
#     """Código con formato específico: 2 letras + 4 números"""
#     return {"code": code, "valid": True}


# ============================================
# PASO 5: Enum para Valores Fijos
# ============================================
print("--- Paso 5: Enum ---")

# Enum restringe los valores a opciones predefinidas
# Descomenta las siguientes líneas:

# class OrderStatus(str, Enum):
#     pending = "pending"
#     processing = "processing"
#     shipped = "shipped"
#     delivered = "delivered"
#     cancelled = "cancelled"


# class Category(str, Enum):
#     electronics = "electronics"
#     clothing = "clothing"
#     books = "books"
#     home = "home"


# @app.get("/orders/status/{status}", tags=["Paso 5"])
# async def get_orders_by_status(status: OrderStatus):
#     """
#     Path parameter con Enum.
#     
#     Solo acepta valores definidos en OrderStatus.
#     Swagger muestra un dropdown con las opciones.
#     """
#     return {
#         "status": status.value,
#         "status_name": status.name,
#         "message": f"Showing orders with status: {status.value}"
#     }


# @app.get("/categories/{category}/products", tags=["Paso 5"])
# async def get_products_by_category(category: Category):
#     """Productos filtrados por categoría (Enum)"""
#     filtered = [
#         {"id": pid, **p}
#         for pid, p in products_db.items()
#         if p.get("category") == category.value
#     ]
#     return {"category": category.value, "products": filtered}


# ============================================
# PASO 6: Múltiples Path Parameters
# ============================================
print("--- Paso 6: Múltiples parámetros ---")

# Puedes tener varios path parameters en la misma ruta
# Descomenta las siguientes líneas:

# @app.get("/users/{user_id}/posts/{post_id}", tags=["Paso 6"])
# async def get_user_post(
#     user_id: int = Path(..., gt=0, description="User ID"),
#     post_id: int = Path(..., gt=0, description="Post ID")
# ):
#     """Obtener un post específico de un usuario"""
#     return {
#         "user_id": user_id,
#         "post_id": post_id,
#         "title": f"Post {post_id} by user {user_id}"
#     }


# @app.get("/stores/{store_id}/products/{product_id}/reviews/{review_id}", tags=["Paso 6"])
# async def get_product_review(
#     store_id: int = Path(..., gt=0),
#     product_id: int = Path(..., gt=0),
#     review_id: int = Path(..., gt=0)
# ):
#     """Ruta con tres path parameters"""
#     return {
#         "store_id": store_id,
#         "product_id": product_id,
#         "review_id": review_id
#     }


# ============================================
# PASO 7: Capturar Rutas con /
# ============================================
print("--- Paso 7: Rutas con / ---")

# :path permite capturar rutas que contienen /
# Útil para paths de archivos
# Descomenta las siguientes líneas:

# @app.get("/files/{file_path:path}", tags=["Paso 7"])
# async def get_file(file_path: str):
#     """
#     Captura rutas de archivos con /.
#     
#     Ejemplos:
#     - /files/document.txt
#     - /files/images/photo.png
#     - /files/docs/2024/report.pdf
#     """
#     parts = file_path.split("/")
#     filename = parts[-1] if parts else ""
#     directory = "/".join(parts[:-1]) if len(parts) > 1 else ""
#     
#     return {
#         "full_path": file_path,
#         "directory": directory,
#         "filename": filename
#     }


# @app.get("/repos/{repo_path:path}/info", tags=["Paso 7"])
# async def get_repo_info(repo_path: str):
#     """Path de repositorio: owner/repo"""
#     parts = repo_path.split("/")
#     return {
#         "repo_path": repo_path,
#         "owner": parts[0] if parts else None,
#         "repo": parts[1] if len(parts) > 1 else None
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
        "ejercicio": "02 - Path Parameters"
    }


@app.get("/health", tags=["Root"])
async def health_check():
    """Health check"""
    return {"status": "healthy"}
