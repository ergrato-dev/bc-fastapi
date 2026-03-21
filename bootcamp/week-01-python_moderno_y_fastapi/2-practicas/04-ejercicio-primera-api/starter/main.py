# ============================================
# PRIMERA API FASTAPI
# ============================================
# Este ejercicio te guía en la creación de una
# API completa con diferentes tipos de endpoints.

print("=" * 50)
print("Ejercicio 04: Primera API FastAPI")
print("=" * 50)


# ============================================
# PASO 1: Importar y Crear la Aplicación
# ============================================
print("\n--- Paso 1: Crear la Aplicación ---")

# Importamos FastAPI
# Descomenta la siguiente línea:

# from fastapi import FastAPI


# Creamos la instancia con metadata para la documentación
# Descomenta el siguiente bloque:

# app = FastAPI(
#     title="Bootcamp API",
#     description="API de práctica del Bootcamp FastAPI Zero to Hero",
#     version="1.0.0",
#     contact={
#         "name": "Bootcamp Team",
#         "email": "bootcamp@example.com",
#     },
# )


# Base de datos simulada (en memoria)
# Descomenta el siguiente bloque:

# fake_users_db: list[dict] = [
#     {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30},
#     {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25},
#     {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 35},
# ]
# 
# fake_items_db: list[dict] = [
#     {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
#     {"id": 2, "name": "Mouse", "price": 29.99, "in_stock": True},
#     {"id": 3, "name": "Keyboard", "price": 79.99, "in_stock": False},
#     {"id": 4, "name": "Monitor", "price": 299.99, "in_stock": True},
#     {"id": 5, "name": "Headphones", "price": 149.99, "in_stock": True},
# ]


# ============================================
# PASO 2: Endpoint Raíz
# ============================================
print("\n--- Paso 2: Endpoint Raíz ---")

# El endpoint raíz es el punto de entrada de la API
# Descomenta el siguiente bloque:

# @app.get("/")
# async def root():
#     """
#     Endpoint raíz con información de la API.
#     
#     Returns:
#         dict: Información básica de la API
#     """
#     return {
#         "name": "Bootcamp API",
#         "version": "1.0.0",
#         "status": "running",
#         "docs": "/docs",
#     }


# ============================================
# PASO 3: Health Check
# ============================================
print("\n--- Paso 3: Health Check ---")

# Es buena práctica tener un endpoint de salud
# Descomenta el siguiente bloque:

# @app.get("/health")
# async def health_check():
#     """
#     Verifica el estado de la API.
#     
#     Returns:
#         dict: Estado de salud de la API
#     """
#     return {
#         "status": "healthy",
#         "database": "connected",
#         "cache": "connected",
#     }


# ============================================
# PASO 4: Listar Usuarios (GET con Query Params)
# ============================================
print("\n--- Paso 4: Listar Usuarios ---")

# Query parameters permiten paginación y filtrado
# Descomenta el siguiente bloque:

# @app.get("/users")
# async def list_users(
#     skip: int = 0,
#     limit: int = 10,
#     min_age: int | None = None,
# ):
#     """
#     Lista todos los usuarios con paginación opcional.
#     
#     Args:
#         skip: Número de usuarios a saltar (paginación)
#         limit: Máximo número de usuarios a retornar
#         min_age: Filtrar usuarios con edad mínima
#     
#     Returns:
#         dict: Lista de usuarios y metadata
#     """
#     # Aplicar filtro de edad si se especifica
#     users = fake_users_db
#     if min_age is not None:
#         users = [u for u in users if u["age"] >= min_age]
#     
#     # Aplicar paginación
#     paginated = users[skip : skip + limit]
#     
#     return {
#         "total": len(users),
#         "skip": skip,
#         "limit": limit,
#         "users": paginated,
#     }


# ============================================
# PASO 5: Obtener Usuario por ID (Path Param)
# ============================================
print("\n--- Paso 5: Obtener Usuario por ID ---")

# Path parameters capturan valores de la URL
# Descomenta el siguiente bloque:

# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     """
#     Obtiene un usuario por su ID.
#     
#     Args:
#         user_id: ID único del usuario
#     
#     Returns:
#         dict: Datos del usuario o mensaje de error
#     """
#     for user in fake_users_db:
#         if user["id"] == user_id:
#             return user
#     
#     # Si no se encuentra, retornar error
#     return {"error": "Usuario no encontrado", "user_id": user_id}


# ============================================
# PASO 6: Listar Items con Filtros
# ============================================
print("\n--- Paso 6: Listar Items con Filtros ---")

# Múltiples query parameters para filtrado avanzado
# Descomenta el siguiente bloque:

# @app.get("/items")
# async def list_items(
#     skip: int = 0,
#     limit: int = 10,
#     in_stock: bool | None = None,
#     min_price: float | None = None,
#     max_price: float | None = None,
# ):
#     """
#     Lista items con filtros opcionales.
#     
#     Args:
#         skip: Número de items a saltar
#         limit: Máximo de items a retornar
#         in_stock: Filtrar por disponibilidad
#         min_price: Precio mínimo
#         max_price: Precio máximo
#     
#     Returns:
#         dict: Lista de items filtrados
#     """
#     items = fake_items_db
#     
#     # Aplicar filtros
#     if in_stock is not None:
#         items = [i for i in items if i["in_stock"] == in_stock]
#     
#     if min_price is not None:
#         items = [i for i in items if i["price"] >= min_price]
#     
#     if max_price is not None:
#         items = [i for i in items if i["price"] <= max_price]
#     
#     # Paginación
#     paginated = items[skip : skip + limit]
#     
#     return {
#         "total": len(items),
#         "filters": {
#             "in_stock": in_stock,
#             "min_price": min_price,
#             "max_price": max_price,
#         },
#         "items": paginated,
#     }


# ============================================
# PASO 7: Obtener Item por ID
# ============================================
print("\n--- Paso 7: Obtener Item por ID ---")

# Descomenta el siguiente bloque:

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     """
#     Obtiene un item por su ID.
#     
#     Args:
#         item_id: ID único del item
#     
#     Returns:
#         dict: Datos del item o error
#     """
#     for item in fake_items_db:
#         if item["id"] == item_id:
#             return item
#     
#     return {"error": "Item no encontrado", "item_id": item_id}


# ============================================
# PASO 8: Búsqueda
# ============================================
print("\n--- Paso 8: Endpoint de Búsqueda ---")

# Un endpoint de búsqueda con query obligatorio
# Descomenta el siguiente bloque:

# @app.get("/search")
# async def search(
#     q: str,  # Obligatorio (sin valor por defecto)
#     category: str = "all",
# ):
#     """
#     Busca usuarios e items por nombre.
#     
#     Args:
#         q: Término de búsqueda (obligatorio)
#         category: Categoría a buscar (users, items, all)
#     
#     Returns:
#         dict: Resultados de la búsqueda
#     """
#     results = {"query": q, "category": category, "users": [], "items": []}
#     
#     query_lower = q.lower()
#     
#     if category in ("users", "all"):
#         results["users"] = [
#             u for u in fake_users_db
#             if query_lower in u["name"].lower()
#         ]
#     
#     if category in ("items", "all"):
#         results["items"] = [
#             i for i in fake_items_db
#             if query_lower in i["name"].lower()
#         ]
#     
#     results["total_results"] = len(results["users"]) + len(results["items"])
#     return results


# ============================================
# PASO 9: Posts de Usuario (Path Anidado)
# ============================================
print("\n--- Paso 9: Path Anidado ---")

# Rutas anidadas para recursos relacionados
# Descomenta el siguiente bloque:

# fake_posts_db: list[dict] = [
#     {"id": 1, "user_id": 1, "title": "Mi primer post", "likes": 10},
#     {"id": 2, "user_id": 1, "title": "Aprendiendo FastAPI", "likes": 25},
#     {"id": 3, "user_id": 2, "title": "Docker es genial", "likes": 15},
# ]


# @app.get("/users/{user_id}/posts")
# async def get_user_posts(
#     user_id: int,
#     sort_by: str = "id",
# ):
#     """
#     Obtiene los posts de un usuario específico.
#     
#     Args:
#         user_id: ID del usuario
#         sort_by: Campo para ordenar (id, likes)
#     
#     Returns:
#         dict: Posts del usuario
#     """
#     # Verificar que el usuario existe
#     user_exists = any(u["id"] == user_id for u in fake_users_db)
#     if not user_exists:
#         return {"error": "Usuario no encontrado", "user_id": user_id}
#     
#     # Filtrar posts del usuario
#     user_posts = [p for p in fake_posts_db if p["user_id"] == user_id]
#     
#     # Ordenar
#     if sort_by == "likes":
#         user_posts = sorted(user_posts, key=lambda p: p["likes"], reverse=True)
#     
#     return {
#         "user_id": user_id,
#         "total_posts": len(user_posts),
#         "posts": user_posts,
#     }


# ============================================
# VERIFICACIÓN FINAL
# ============================================
print("\n" + "=" * 50)
print("Para probar esta API:")
print("1. Descomenta todo el código")
print("2. Copia este archivo a src/main.py del ejercicio-01")
print("3. Ejecuta: docker compose up --build")
print("4. Visita: http://localhost:8000/docs")
print("=" * 50)
print("""
Endpoints disponibles:
- GET /           → Info de la API
- GET /health     → Estado de salud
- GET /users      → Lista usuarios (?skip=0&limit=10&min_age=25)
- GET /users/{id} → Usuario por ID
- GET /items      → Lista items (?in_stock=true&min_price=50)
- GET /items/{id} → Item por ID
- GET /search     → Búsqueda (?q=alice&category=users)
- GET /users/{id}/posts → Posts de un usuario
""")
