# ============================================
# PASO 3: Configurar FastAPI con Dependencias
# ============================================
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from pydantic import BaseModel, ConfigDict

from models import Base, User, Product, Order, OrderStatus
from repositories import UserRepository, ProductRepository, OrderRepository
# from services import OrderService, UserCreate, ProductCreate, OrderCreate, NotFoundError, BusinessError

# Database
DATABASE_URL = "sqlite:///./orders.db"
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
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    model_config = ConfigDict(from_attributes=True)


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    model_config = ConfigDict(from_attributes=True)


class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total: float
    status: OrderStatus
    model_config = ConfigDict(from_attributes=True)


# ============================================
# App
# ============================================
app = FastAPI(title="Order System - Service + Repository")


# ============================================
# PASO 3a: Dependencias para Repositorios
# Descomenta:
# ============================================

# def get_user_repo(db: Session = Depends(get_db)) -> UserRepository:
#     return UserRepository(db)

# def get_product_repo(db: Session = Depends(get_db)) -> ProductRepository:
#     return ProductRepository(db)

# def get_order_repo(db: Session = Depends(get_db)) -> OrderRepository:
#     return OrderRepository(db)


# ============================================
# PASO 3b: Dependencia para Service
# Descomenta:
# ============================================

# def get_order_service(
#     user_repo: UserRepository = Depends(get_user_repo),
#     product_repo: ProductRepository = Depends(get_product_repo),
#     order_repo: OrderRepository = Depends(get_order_repo)
# ) -> OrderService:
#     return OrderService(
#         user_repo=user_repo,
#         product_repo=product_repo,
#         order_repo=order_repo
#     )


# ============================================
# Endpoints de setup (users, products)
# ============================================
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(name: str, price: float, stock: int = 10, db: Session = Depends(get_db)):
    product = Product(name=name, price=price, stock=stock)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@app.get("/products", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


# ============================================
# PASO 3c: Endpoints de Orders
# Descomenta:
# ============================================

# @app.post("/orders", response_model=OrderResponse, status_code=201)
# def create_order(
#     data: OrderCreate,
#     service: OrderService = Depends(get_order_service),
#     db: Session = Depends(get_db)
# ):
#     """Crea nueva orden"""
#     try:
#         order = service.create_order(data)
#         db.commit()
#         return order
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))
#     except BusinessError as e:
#         raise HTTPException(400, str(e))


# @app.get("/orders/{order_id}", response_model=OrderResponse)
# def get_order(
#     order_id: int,
#     service: OrderService = Depends(get_order_service)
# ):
#     """Obtiene orden por ID"""
#     try:
#         return service.get_order(order_id)
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))


# @app.get("/users/{user_id}/orders", response_model=list[OrderResponse])
# def get_user_orders(
#     user_id: int,
#     service: OrderService = Depends(get_order_service)
# ):
#     """Obtiene órdenes de un usuario"""
#     try:
#         return service.get_user_orders(user_id)
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))


# @app.post("/orders/{order_id}/confirm", response_model=OrderResponse)
# def confirm_order(
#     order_id: int,
#     service: OrderService = Depends(get_order_service),
#     db: Session = Depends(get_db)
# ):
#     """Confirma una orden"""
#     try:
#         order = service.confirm_order(order_id)
#         db.commit()
#         return order
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))
#     except BusinessError as e:
#         raise HTTPException(400, str(e))


# @app.post("/orders/{order_id}/cancel", response_model=OrderResponse)
# def cancel_order(
#     order_id: int,
#     service: OrderService = Depends(get_order_service),
#     db: Session = Depends(get_db)
# ):
#     """Cancela una orden y restaura stock"""
#     try:
#         order = service.cancel_order(order_id)
#         db.commit()
#         return order
#     except NotFoundError as e:
#         raise HTTPException(404, str(e))
#     except BusinessError as e:
#         raise HTTPException(400, str(e))
