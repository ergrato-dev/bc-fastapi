# ============================================
# MAIN - APLICACIÓN
# ============================================
print("--- Main: Products API con DTOs ---")

# Descomenta las siguientes líneas:

# from fastapi import FastAPI
# from database import engine, Base
# from routers.products import router as products_router

# # Crear tablas
# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Products API",
#     description="API con DTOs y Mappers",
#     version="1.0.0"
# )

# app.include_router(products_router)


# @app.get("/")
# def root():
#     return {"message": "Products API", "docs": "/docs"}


# ============================================
# INSTRUCCIONES
# ============================================
# 1. Descomenta todo el código
# 2. Ejecuta: uvicorn main:app --reload
# 3. Prueba en /docs:
#    - POST /products/ con cost_price=50
#    - GET /products/{id} - NO verás cost_price en response
