# ============================================
# MAIN - APLICACIÓN COMPLETA
# ============================================
print("--- Main: Orders API - Flujo Completo ---")

# Descomenta las siguientes líneas:

# from fastapi import FastAPI
# from database import engine, Base
# from routers.users import router as users_router
# from routers.products import router as products_router
# from routers.orders import router as orders_router
# from handlers.exception_handlers import register_exception_handlers

# # Crear tablas
# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Orders API",
#     description="API con flujo completo de pedidos",
#     version="1.0.0"
# )

# # Registrar exception handlers
# register_exception_handlers(app)

# # Incluir routers
# app.include_router(users_router)
# app.include_router(products_router)
# app.include_router(orders_router)


# @app.get("/")
# def root():
#     return {
#         "message": "Orders API",
#         "docs": "/docs",
#         "flujo": [
#             "1. POST /users/ - Crear usuario",
#             "2. POST /products/ - Crear productos",
#             "3. POST /orders/ - Crear pedido"
#         ]
#     }


# ============================================
# INSTRUCCIONES
# ============================================
# 1. Descomentar TODO el código en todos los archivos
# 2. Ejecutar: uvicorn main:app --reload
# 3. Crear datos:
#    POST /users/ {"name": "John", "email": "john@test.com"}
#    POST /products/ {"name": "Widget", "sku": "WDG-001", "price": 29.99, "stock": 10}
#    POST /products/ {"name": "Gadget", "sku": "GDG-001", "price": 49.99, "stock": 5}
# 4. Crear pedido:
#    POST /orders/ {"user_id": 1, "items": [{"product_id": 1, "quantity": 2}], "shipping_address": "123 Main St"}
