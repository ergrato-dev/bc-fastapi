# ============================================
# PASO 4: Actualizar endpoints
# ============================================
"""
Los endpoints ahora crean el repositorio y lo pasan al service.
"""

from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from pydantic import BaseModel, ConfigDict

from models import Base, Product
# from repositories import ProductRepository  # ← Descomentar
# from services import ProductService, ProductCreate, ProductUpdate, NotFoundError, BusinessError  # ← Descomentar

# ============================================
# Database setup
# ============================================
DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================
# Schemas de respuesta
# ============================================
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    stock: int
    is_active: bool
    
    model_config = ConfigDict(from_attributes=True)


# ============================================
# App
# ============================================
app = FastAPI(title="Products API - Repository Pattern")


# ============================================
# ANTES: Endpoint con acceso directo
# ============================================
@app.get("/v1/products/{product_id}", response_model=ProductResponse, tags=["v1-direct"])
def get_product_direct(product_id: int, db: Session = Depends(get_db)):
    """Endpoint SIN repository (acceso directo)"""
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(404, "Product not found")
    return product


# ============================================
# DESPUÉS: Endpoints con Repository
# Descomenta estos endpoints:
# ============================================

# @app.get("/v2/products", response_model=list[ProductResponse], tags=["v2-repository"])
# def list_products(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(10, ge=1, le=100),
#     db: Session = Depends(get_db)
# ):
#     """Lista productos usando repository"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     return service.list_all(skip=skip, limit=limit)


# @app.get("/v2/products/active", response_model=list[ProductResponse], tags=["v2-repository"])
# def list_active_products(db: Session = Depends(get_db)):
#     """Lista solo productos activos"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     return service.list_active()


# @app.get("/v2/products/{product_id}", response_model=ProductResponse, tags=["v2-repository"])
# def get_product(product_id: int, db: Session = Depends(get_db)):
#     """Obtiene producto por ID"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     try:
#         return service.get_by_id(product_id)
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))


# @app.post("/v2/products", response_model=ProductResponse, status_code=201, tags=["v2-repository"])
# def create_product(data: ProductCreate, db: Session = Depends(get_db)):
#     """Crea nuevo producto"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     product = service.create(data)
#     db.commit()
#     return product


# @app.put("/v2/products/{product_id}", response_model=ProductResponse, tags=["v2-repository"])
# def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
#     """Actualiza producto"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     try:
#         product = service.update(product_id, data)
#         db.commit()
#         return product
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))


# @app.delete("/v2/products/{product_id}", status_code=204, tags=["v2-repository"])
# def delete_product(product_id: int, db: Session = Depends(get_db)):
#     """Elimina producto"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     try:
#         service.delete(product_id)
#         db.commit()
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))


# @app.patch("/v2/products/{product_id}/stock", response_model=ProductResponse, tags=["v2-repository"])
# def update_stock(product_id: int, quantity: int, db: Session = Depends(get_db)):
#     """Actualiza stock (suma o resta)"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     try:
#         product = service.update_stock(product_id, quantity)
#         db.commit()
#         return product
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))
#     except BusinessError as e:
#         raise HTTPException(400, str(e))


# @app.get("/v2/products/search/", response_model=list[ProductResponse], tags=["v2-repository"])
# def search_products(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
#     """Busca productos por nombre"""
#     repo = ProductRepository(db)
#     service = ProductService(repo)
#     return service.search(q)
