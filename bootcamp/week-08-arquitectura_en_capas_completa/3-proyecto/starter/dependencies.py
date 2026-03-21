# ============================================
# DEPENDENCY INJECTION
# ============================================

from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.user import UserRepository
from repositories.category import CategoryRepository
from repositories.product import ProductRepository
from repositories.order import OrderRepository
from services.user import UserService
from services.category import CategoryService
from services.product import ProductService
from services.order import OrderService


# ============================================
# USER
# ============================================

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_user_service(
    repo: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(repo)


# ============================================
# CATEGORY
# ============================================

def get_category_repository(db: Session = Depends(get_db)) -> CategoryRepository:
    return CategoryRepository(db)


def get_category_service(
    repo: CategoryRepository = Depends(get_category_repository)
) -> CategoryService:
    return CategoryService(repo)


# ============================================
# PRODUCT
# ============================================

def get_product_repository(db: Session = Depends(get_db)) -> ProductRepository:
    return ProductRepository(db)


def get_product_service(
    product_repo: ProductRepository = Depends(get_product_repository),
    category_repo: CategoryRepository = Depends(get_category_repository)
) -> ProductService:
    return ProductService(product_repo, category_repo)


# ============================================
# ORDER
# ============================================

def get_order_repository(db: Session = Depends(get_db)) -> OrderRepository:
    return OrderRepository(db)


def get_order_service(
    order_repo: OrderRepository = Depends(get_order_repository),
    user_repo: UserRepository = Depends(get_user_repository),
    product_repo: ProductRepository = Depends(get_product_repository)
) -> OrderService:
    return OrderService(order_repo, user_repo, product_repo)
