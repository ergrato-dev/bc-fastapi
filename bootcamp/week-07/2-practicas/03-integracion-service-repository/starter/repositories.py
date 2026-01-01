# ============================================
# Repositorios (ya implementados)
# ============================================
from typing import TypeVar, Generic
from sqlalchemy import select, func
from sqlalchemy.orm import Session, joinedload

from models import Base, User, Product, Order, OrderStatus

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: type[T]):
        self.db = db
        self.model = model
    
    def get_by_id(self, id: int) -> T | None:
        return self.db.get(self.model, id)
    
    def get_all(self, skip: int = 0, limit: int = 100) -> list[T]:
        stmt = select(self.model).offset(skip).limit(limit)
        return list(self.db.execute(stmt).scalars().all())
    
    def add(self, entity: T) -> T:
        self.db.add(entity)
        self.db.flush()
        self.db.refresh(entity)
        return entity
    
    def update(self, entity: T) -> T:
        self.db.flush()
        self.db.refresh(entity)
        return entity
    
    def delete(self, entity: T) -> None:
        self.db.delete(entity)
        self.db.flush()


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(db, User)
    
    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.db.execute(stmt).scalar_one_or_none()


class ProductRepository(BaseRepository[Product]):
    def __init__(self, db: Session):
        super().__init__(db, Product)
    
    def get_in_stock(self) -> list[Product]:
        stmt = select(Product).where(Product.stock > 0)
        return list(self.db.execute(stmt).scalars().all())


class OrderRepository(BaseRepository[Order]):
    def __init__(self, db: Session):
        super().__init__(db, Order)
    
    def get_with_details(self, order_id: int) -> Order | None:
        stmt = (
            select(Order)
            .options(joinedload(Order.user), joinedload(Order.product))
            .where(Order.id == order_id)
        )
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_by_user(self, user_id: int) -> list[Order]:
        stmt = select(Order).where(Order.user_id == user_id)
        return list(self.db.execute(stmt).scalars().all())
    
    def get_by_status(self, status: OrderStatus) -> list[Order]:
        stmt = select(Order).where(Order.status == status)
        return list(self.db.execute(stmt).scalars().all())
