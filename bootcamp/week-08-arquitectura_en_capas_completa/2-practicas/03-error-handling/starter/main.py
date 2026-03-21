# ============================================
# MAIN - CON EXCEPTION HANDLERS
# ============================================
print("--- Main: App con Exception Handlers ---")

# Registra los exception handlers globales.

# Descomenta las siguientes líneas:

# from fastapi import FastAPI
# from database import engine, Base
# from routers.products import router as products_router
# from handlers.exception_handlers import register_exception_handlers

# # Crear tablas
# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Products API - Error Handling",
#     description="API con manejo de errores centralizado",
#     version="1.0.0"
# )

# # ¡IMPORTANTE! Registrar exception handlers
# register_exception_handlers(app)

# # Incluir routers
# app.include_router(products_router)


# @app.get("/")
# def root():
#     return {
#         "message": "Products API",
#         "docs": "/docs",
#         "note": "Prueba GET /products/99999 para ver error 404 formateado"
#     }


# ============================================
# PRUEBAS SUGERIDAS
# ============================================
# 1. GET /products/99999
#    → 404 {"error": "Not Found", "code": "PRODUCT_NOT_FOUND", ...}
#
# 2. POST /products/ con SKU duplicado
#    → 409 {"error": "Conflict", "code": "PRODUCT_SKU_DUPLICATE", ...}
#
# 3. PATCH /products/{id}/reduce-stock con quantity > stock
#    → 400 {"error": "Validation Error", "code": "INSUFFICIENT_STOCK", ...}
