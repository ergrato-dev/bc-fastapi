"""
Ejercicio 04: Parámetros Combinados
===================================

Objetivo: Combinar múltiples fuentes de parámetros y usar dependencias.

Instrucciones:
1. Lee cada sección
2. Descomenta el código
3. Prueba en http://localhost:8000/docs
"""

from fastapi import FastAPI, Path, Query, Body, Header, Cookie, Depends, HTTPException, status
from pydantic import BaseModel, Field
from typing import Annotated
from enum import Enum

app = FastAPI(
    title="Ejercicio 04 - Parámetros Combinados",
    description="Combinando path, query, body, headers y cookies",
    version="1.0.0"
)

# ============================================
# SCHEMAS
# ============================================

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    price: float = Field(..., gt=0)


class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, gt=0)


class User(BaseModel):
    id: int
    username: str
    role: str


# ============================================
# BASE DE DATOS SIMULADA
# ============================================

items_db = {
    1: {"name": "Laptop", "description": "Powerful laptop", "price": 999.99},
    2: {"name": "Mouse", "description": "Wireless mouse", "price": 29.99},
}

users_db = {
    "token123": User(id=1, username="john", role="user"),
    "admin_token": User(id=2, username="admin", role="admin"),
}

posts_db = {
    1: [
        {"id": 1, "title": "First Post", "user_id": 1},
        {"id": 2, "title": "Second Post", "user_id": 1},
        {"id": 3, "title": "Third Post", "user_id": 1},
    ],
    2: [
        {"id": 4, "title": "Admin Post", "user_id": 2},
    ]
}

# ============================================
# PASO 2: Combinar Path y Query
# ============================================
print("--- Paso 2: Path + Query ---")

# Path parameters de la URL, Query parameters después de ?
# Descomenta las siguientes líneas:

# @app.get("/users/{user_id}/posts", tags=["Paso 2"])
# async def get_user_posts(
#     user_id: int = Path(..., gt=0, description="User ID"),
#     page: int = Query(default=1, ge=1, description="Page number"),
#     per_page: int = Query(default=10, ge=1, le=50, description="Posts per page")
# ):
#     """
#     Combina path parameter (user_id) con query parameters (page, per_page).
#     
#     GET /users/1/posts?page=1&per_page=5
#     """
#     user_posts = posts_db.get(user_id, [])
#     
#     # Paginar
#     start = (page - 1) * per_page
#     end = start + per_page
#     paginated = user_posts[start:end]
#     
#     return {
#         "user_id": user_id,
#         "page": page,
#         "per_page": per_page,
#         "total": len(user_posts),
#         "posts": paginated
#     }


# @app.get("/categories/{category}/products", tags=["Paso 2"])
# async def get_category_products(
#     category: str = Path(..., min_length=2, description="Category name"),
#     min_price: float | None = Query(default=None, ge=0),
#     max_price: float | None = Query(default=None, ge=0),
#     sort_by: str = Query(default="name")
# ):
#     """Path param para categoría, query params para filtros"""
#     return {
#         "category": category,
#         "filters": {
#             "min_price": min_price,
#             "max_price": max_price
#         },
#         "sort_by": sort_by
#     }


# ============================================
# PASO 3: Path, Query y Body
# ============================================
print("--- Paso 3: Path + Query + Body ---")

# Tres fuentes de parámetros en un endpoint
# Descomenta las siguientes líneas:

# @app.put("/items/{item_id}", tags=["Paso 3"])
# async def update_item(
#     item_id: int = Path(..., gt=0, description="Item ID"),
#     notify: bool = Query(default=False, description="Send notification"),
#     priority: int = Query(default=1, ge=1, le=5, description="Update priority"),
#     item: ItemUpdate = Body(..., description="Item data to update")
# ):
#     """
#     Combina las tres fuentes:
#     - Path: item_id de la URL
#     - Query: notify, priority después de ?
#     - Body: datos JSON del item
#     
#     PUT /items/1?notify=true&priority=3
#     Body: {"name": "New Name", "price": 99.99}
#     """
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     
#     # Actualizar solo campos proporcionados
#     update_data = item.model_dump(exclude_unset=True)
#     items_db[item_id].update(update_data)
#     
#     return {
#         "item_id": item_id,
#         "notify": notify,
#         "priority": priority,
#         "updated_item": items_db[item_id]
#     }


# @app.post("/users/{user_id}/items", status_code=201, tags=["Paso 3"])
# async def create_user_item(
#     user_id: int = Path(..., gt=0),
#     send_email: bool = Query(default=True),
#     item: ItemCreate = Body(...)
# ):
#     """Crear item para un usuario específico"""
#     new_id = max(items_db.keys()) + 1
#     items_db[new_id] = item.model_dump()
#     
#     return {
#         "message": f"Item created for user {user_id}",
#         "item_id": new_id,
#         "item": items_db[new_id],
#         "email_sent": send_email
#     }


# ============================================
# PASO 4: Headers
# ============================================
print("--- Paso 4: Headers ---")

# Leer encabezados HTTP de la request
# Descomenta las siguientes líneas:

# @app.get("/headers/info", tags=["Paso 4"])
# async def get_header_info(
#     user_agent: str | None = Header(default=None),
#     accept_language: str | None = Header(default=None),
#     x_request_id: str | None = Header(default=None),
#     x_api_key: str | None = Header(default=None)
# ):
#     """
#     Leer headers de la request.
#     
#     FastAPI convierte automáticamente:
#     - user_agent → User-Agent
#     - accept_language → Accept-Language
#     - x_request_id → X-Request-Id
#     """
#     return {
#         "user_agent": user_agent,
#         "accept_language": accept_language,
#         "x_request_id": x_request_id,
#         "x_api_key": x_api_key
#     }


# @app.get("/items", tags=["Paso 4"])
# async def list_items_with_headers(
#     x_token: str = Header(..., description="API Token required"),
#     x_client_version: str | None = Header(default=None)
# ):
#     """Endpoint que requiere header X-Token"""
#     if x_token != "secret-token":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid X-Token header"
#         )
#     
#     return {
#         "items": list(items_db.values()),
#         "client_version": x_client_version
#     }


# ============================================
# PASO 5: Cookies
# ============================================
print("--- Paso 5: Cookies ---")

# Leer cookies de la request
# Descomenta las siguientes líneas:

# @app.get("/session/info", tags=["Paso 5"])
# async def get_session_info(
#     session_id: str | None = Cookie(default=None),
#     user_preferences: str | None = Cookie(default=None)
# ):
#     """
#     Leer cookies del cliente.
#     
#     Las cookies se envían automáticamente por el navegador.
#     En Swagger, puedes agregar cookies en la request.
#     """
#     return {
#         "session_id": session_id,
#         "user_preferences": user_preferences,
#         "has_session": session_id is not None
#     }


# @app.get("/dashboard", tags=["Paso 5"])
# async def get_dashboard(
#     auth_token: str = Cookie(..., description="Authentication cookie required")
# ):
#     """Endpoint que requiere cookie de autenticación"""
#     if auth_token not in users_db:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication cookie"
#         )
#     
#     user = users_db[auth_token]
#     return {
#         "message": f"Welcome {user.username}!",
#         "user": user.model_dump()
#     }


# ============================================
# PASO 6: Dependencias Reutilizables
# ============================================
print("--- Paso 6: Dependencias ---")

# Crear funciones reutilizables para parámetros comunes
# Descomenta las siguientes líneas:

# async def pagination_params(
#     page: int = Query(default=1, ge=1, description="Page number"),
#     per_page: int = Query(default=10, ge=1, le=50, description="Items per page")
# ) -> dict:
#     """Dependencia para paginación reutilizable"""
#     return {
#         "page": page,
#         "per_page": per_page,
#         "offset": (page - 1) * per_page
#     }


# # Alias con Annotated
# PaginationDep = Annotated[dict, Depends(pagination_params)]


# @app.get("/products", tags=["Paso 6"])
# async def list_products(pagination: PaginationDep):
#     """Usa la dependencia de paginación"""
#     return {
#         "pagination": pagination,
#         "products": []
#     }


# @app.get("/orders", tags=["Paso 6"])
# async def list_orders(pagination: PaginationDep):
#     """Misma dependencia en otro endpoint"""
#     return {
#         "pagination": pagination,
#         "orders": []
#     }


# # Dependencia como clase
# class FilterParams:
#     def __init__(
#         self,
#         search: str | None = Query(default=None, min_length=2),
#         category: str | None = Query(default=None),
#         min_price: float | None = Query(default=None, ge=0),
#         max_price: float | None = Query(default=None, ge=0)
#     ):
#         self.search = search
#         self.category = category
#         self.min_price = min_price
#         self.max_price = max_price


# FiltersDep = Annotated[FilterParams, Depends()]


# @app.get("/catalog", tags=["Paso 6"])
# async def get_catalog(
#     filters: FiltersDep,
#     pagination: PaginationDep
# ):
#     """Combina múltiples dependencias"""
#     return {
#         "filters": {
#             "search": filters.search,
#             "category": filters.category,
#             "min_price": filters.min_price,
#             "max_price": filters.max_price
#         },
#         "pagination": pagination
#     }


# ============================================
# PASO 7: Autenticación con Dependencias
# ============================================
print("--- Paso 7: Autenticación ---")

# Dependencias para autenticación
# Descomenta las siguientes líneas:

# async def get_token(
#     authorization: str | None = Header(default=None)
# ) -> str:
#     """Extraer token del header Authorization"""
#     if not authorization:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Authorization header missing",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
#     
#     if not authorization.startswith("Bearer "):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authorization scheme. Use 'Bearer <token>'"
#         )
#     
#     return authorization.replace("Bearer ", "")


# TokenDep = Annotated[str, Depends(get_token)]


# async def get_current_user(token: TokenDep) -> User:
#     """Obtener usuario actual desde el token"""
#     if token not in users_db:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token"
#         )
#     return users_db[token]


# CurrentUserDep = Annotated[User, Depends(get_current_user)]


# async def require_admin(user: CurrentUserDep) -> User:
#     """Verificar que el usuario es admin"""
#     if user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Admin access required"
#         )
#     return user


# AdminDep = Annotated[User, Depends(require_admin)]


# @app.get("/me", tags=["Paso 7"])
# async def get_me(user: CurrentUserDep):
#     """Obtener información del usuario actual"""
#     return user


# @app.get("/admin/stats", tags=["Paso 7"])
# async def get_admin_stats(admin: AdminDep):
#     """Solo accesible por admins"""
#     return {
#         "message": f"Welcome admin {admin.username}!",
#         "stats": {
#             "total_items": len(items_db),
#             "total_users": len(users_db)
#         }
#     }


# @app.delete("/items/{item_id}", tags=["Paso 7"])
# async def delete_item(
#     item_id: int = Path(..., gt=0),
#     admin: AdminDep = ...
# ):
#     """Eliminar item (solo admins)"""
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     
#     del items_db[item_id]
#     return {
#         "message": "Item deleted",
#         "deleted_by": admin.username
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
        "ejercicio": "04 - Parámetros Combinados"
    }


@app.get("/health", tags=["Root"])
async def health_check():
    """Health check"""
    return {"status": "healthy"}
