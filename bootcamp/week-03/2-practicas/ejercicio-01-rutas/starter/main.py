"""
Ejercicio 01: Rutas CRUD Básicas
================================

Objetivo: Aprender a crear rutas con diferentes métodos HTTP.

Instrucciones:
1. Lee cada sección
2. Descomenta el código
3. Prueba en http://localhost:8000/docs
"""

from fastapi import FastAPI, APIRouter, status

app = FastAPI(
    title="Ejercicio 01 - Rutas CRUD",
    description="Aprendiendo rutas básicas en FastAPI",
    version="1.0.0"
)

# ============================================
# BASE DE DATOS SIMULADA
# ============================================

items_db: dict[int, dict] = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Mouse", "price": 29.99},
    3: {"name": "Keyboard", "price": 79.99},
}
next_id = 4

# ============================================
# PASO 2: Rutas GET
# ============================================
print("--- Paso 2: Rutas GET ---")

# GET para obtener recursos
# Descomenta las siguientes líneas:

# @app.get("/items", tags=["Items"])
# async def list_items():
#     """Listar todos los items"""
#     return list(items_db.values())


# @app.get("/items/{item_id}", tags=["Items"])
# async def get_item(item_id: int):
#     """Obtener un item por ID"""
#     if item_id not in items_db:
#         return {"error": "Item not found"}
#     return {"id": item_id, **items_db[item_id]}


# ============================================
# PASO 3: Ruta POST
# ============================================
print("--- Paso 3: Ruta POST ---")

# POST para crear recursos
# status_code=201 indica "Created"
# Descomenta las siguientes líneas:

# @app.post("/items", status_code=status.HTTP_201_CREATED, tags=["Items"])
# async def create_item(item: dict):
#     """Crear un nuevo item"""
#     global next_id
#     items_db[next_id] = item
#     result = {"id": next_id, **item}
#     next_id += 1
#     return result


# ============================================
# PASO 4: Rutas PUT y PATCH
# ============================================
print("--- Paso 4: PUT y PATCH ---")

# PUT reemplaza el recurso completo
# PATCH actualiza parcialmente
# Descomenta las siguientes líneas:

# @app.put("/items/{item_id}", tags=["Items"])
# async def replace_item(item_id: int, item: dict):
#     """Reemplazar un item completamente"""
#     if item_id not in items_db:
#         return {"error": "Item not found"}
#     items_db[item_id] = item
#     return {"id": item_id, **item}


# @app.patch("/items/{item_id}", tags=["Items"])
# async def update_item(item_id: int, item: dict):
#     """Actualizar un item parcialmente"""
#     if item_id not in items_db:
#         return {"error": "Item not found"}
#     items_db[item_id].update(item)
#     return {"id": item_id, **items_db[item_id]}


# ============================================
# PASO 5: Ruta DELETE
# ============================================
print("--- Paso 5: DELETE ---")

# DELETE elimina recursos
# 204 No Content - no retorna body
# Descomenta las siguientes líneas:

# @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
# async def delete_item(item_id: int):
#     """Eliminar un item"""
#     if item_id in items_db:
#         del items_db[item_id]
#     return None


# ============================================
# PASO 6: Orden de Rutas
# ============================================
print("--- Paso 6: Orden de Rutas ---")

# Las rutas fijas deben ir ANTES de las dinámicas
# Si no, "me" se interpretaría como un user_id
# Descomenta las siguientes líneas:

# @app.get("/users/me", tags=["Users"])
# async def get_current_user():
#     """Obtener usuario actual (ruta fija)"""
#     return {"id": 0, "username": "current_user", "role": "admin"}


# @app.get("/users/admin", tags=["Users"])
# async def get_admin_user():
#     """Obtener usuario admin (ruta fija)"""
#     return {"id": 1, "username": "admin", "role": "superadmin"}


# @app.get("/users/{user_id}", tags=["Users"])
# async def get_user(user_id: str):
#     """Obtener usuario por ID (ruta dinámica)"""
#     return {"user_id": user_id, "username": f"user_{user_id}"}


# ============================================
# PASO 7: APIRouter
# ============================================
print("--- Paso 7: APIRouter ---")

# APIRouter permite organizar rutas en módulos
# Descomenta las siguientes líneas:

# products_router = APIRouter(
#     prefix="/products",
#     tags=["Products"],
#     responses={404: {"description": "Not found"}}
# )

# products_db = {
#     1: {"name": "iPhone", "category": "electronics"},
#     2: {"name": "T-Shirt", "category": "clothing"},
# }


# @products_router.get("/")
# async def list_products():
#     """Listar todos los productos"""
#     return list(products_db.values())


# @products_router.get("/{product_id}")
# async def get_product(product_id: int):
#     """Obtener producto por ID"""
#     if product_id not in products_db:
#         return {"error": "Product not found"}
#     return {"id": product_id, **products_db[product_id]}


# @products_router.post("/", status_code=201)
# async def create_product(product: dict):
#     """Crear producto"""
#     new_id = max(products_db.keys()) + 1
#     products_db[new_id] = product
#     return {"id": new_id, **product}


# # Incluir el router en la app
# app.include_router(products_router)


# ============================================
# ENDPOINT DE VERIFICACIÓN
# ============================================

@app.get("/", tags=["Root"])
async def root():
    """Endpoint raíz para verificar que la API funciona"""
    return {
        "message": "API funcionando correctamente",
        "docs": "/docs",
        "ejercicio": "01 - Rutas CRUD Básicas"
    }


@app.get("/health", tags=["Root"])
async def health_check():
    """Health check"""
    return {"status": "healthy"}
