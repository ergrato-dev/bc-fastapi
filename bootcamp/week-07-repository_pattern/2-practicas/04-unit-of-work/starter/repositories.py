# ============================================
# Repositorios
# ============================================
from typing import TypeVar, Generic
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Base, Account, Transfer

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: type[T]):
        self.db = db
        self.model = model
    
    def get_by_id(self, id: int) -> T | None:
        return self.db.get(self.model, id)
    
    def add(self, entity: T) -> T:
        self.db.add(entity)
        self.db.flush()
        self.db.refresh(entity)
        return entity
    
    def update(self, entity: T) -> T:
        self.db.flush()
        self.db.refresh(entity)
        return entity


class AccountRepository(BaseRepository[Account]):
    def __init__(self, db: Session):
        super().__init__(db, Account)
    
    def get_by_owner(self, owner: str) -> Account | None:
        stmt = select(Account).where(Account.owner == owner)
        return self.db.execute(stmt).scalar_one_or_none()


class TransferRepository(BaseRepository[Transfer]):
    def __init__(self, db: Session):
        super().__init__(db, Transfer)
    
    def get_by_account(self, account_id: int) -> list[Transfer]:
        stmt = select(Transfer).where(
            (Transfer.from_account_id == account_id) |
            (Transfer.to_account_id == account_id)
        )
        return list(self.db.execute(stmt).scalars().all())
