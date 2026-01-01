# ============================================
# BASE REPOSITORY
# ============================================

from typing import TypeVar, Generic, Type
from sqlalchemy import select
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """Repository base con operaciones CRUD genéricas."""
    
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model
    
    def get_by_id(self, entity_id: int) -> T | None:
        return self.db.get(self.model, entity_id)
    
    def get_all(self, skip: int = 0, limit: int = 100) -> list[T]:
        stmt = select(self.model).offset(skip).limit(limit)
        return list(self.db.execute(stmt).scalars().all())
    
    def add(self, entity: T) -> T:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity
    
    def update(self, entity: T) -> T:
        self.db.commit()
        self.db.refresh(entity)
        return entity
    
    def delete(self, entity: T) -> None:
        self.db.delete(entity)
        self.db.commit()
