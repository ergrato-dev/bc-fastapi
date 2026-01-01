# ============================================
# PASO 2: BaseRepository Genérico
# ============================================
"""
BaseRepository usa Python Generics para crear métodos
CRUD reutilizables por cualquier modelo.
"""

from typing import TypeVar, Generic
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Base

# TypeVar con bound=Base asegura que T sea un modelo SQLAlchemy
T = TypeVar("T", bound=Base)


# ============================================
# Descomenta BaseRepository:
# ============================================

# class BaseRepository(Generic[T]):
#     """
#     Repositorio genérico con operaciones CRUD básicas.
#     
#     Ejemplo de uso:
#         class ProductRepository(BaseRepository[Product]):
#             def __init__(self, db: Session):
#                 super().__init__(db, Product)
#     """
#     
#     def __init__(self, db: Session, model: type[T]):
#         """
#         Args:
#             db: Sesión de SQLAlchemy
#             model: Clase del modelo (Product, Category, etc.)
#         """
#         self.db = db
#         self.model = model
#     
#     # --- Métodos de lectura ---
#     
#     def get_by_id(self, id: int) -> T | None:
#         """Obtiene entidad por ID"""
#         return self.db.get(self.model, id)
#     
#     def get_all(self, skip: int = 0, limit: int = 100) -> list[T]:
#         """Lista entidades con paginación"""
#         stmt = select(self.model).offset(skip).limit(limit)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def count(self) -> int:
#         """Cuenta total de entidades"""
#         stmt = select(func.count()).select_from(self.model)
#         return self.db.execute(stmt).scalar() or 0
#     
#     def exists(self, id: int) -> bool:
#         """Verifica si existe entidad con ID"""
#         return self.get_by_id(id) is not None
#     
#     def filter_by(self, **kwargs) -> list[T]:
#         """Filtra por atributos exactos"""
#         stmt = select(self.model).filter_by(**kwargs)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def first(self, **kwargs) -> T | None:
#         """Obtiene primera entidad que coincida"""
#         stmt = select(self.model).filter_by(**kwargs).limit(1)
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     # --- Métodos de escritura ---
#     
#     def add(self, entity: T) -> T:
#         """Agrega entidad a la sesión"""
#         self.db.add(entity)
#         self.db.flush()
#         self.db.refresh(entity)
#         return entity
#     
#     def add_many(self, entities: list[T]) -> list[T]:
#         """Agrega múltiples entidades"""
#         self.db.add_all(entities)
#         self.db.flush()
#         for entity in entities:
#             self.db.refresh(entity)
#         return entities
#     
#     def update(self, entity: T) -> T:
#         """Actualiza entidad (ya debe estar en sesión)"""
#         self.db.flush()
#         self.db.refresh(entity)
#         return entity
#     
#     def delete(self, entity: T) -> None:
#         """Elimina entidad"""
#         self.db.delete(entity)
#         self.db.flush()
#     
#     def delete_by_id(self, id: int) -> bool:
#         """Elimina por ID, retorna True si existía"""
#         entity = self.get_by_id(id)
#         if entity:
#             self.delete(entity)
#             return True
#         return False
