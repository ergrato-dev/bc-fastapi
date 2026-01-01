# ============================================
# BASE REPOSITORY
# ============================================
print("--- Repository: Base Repository ---")

# El BaseRepository implementa operaciones CRUD genéricas
# que pueden ser reutilizadas por repositories específicos.
# Pertenece a la capa de Data Access.

# Descomenta las siguientes líneas:

# from typing import TypeVar, Generic, Type
# from sqlalchemy import select
# from sqlalchemy.orm import Session

# # TypeVar para el tipo de modelo
# T = TypeVar("T")


# class BaseRepository(Generic[T]):
#     """
#     Repository base con operaciones CRUD genéricas.
#     
#     Attributes:
#         db: Sesión de SQLAlchemy
#         model: Clase del modelo
#     """
#     
#     def __init__(self, db: Session, model: Type[T]):
#         self.db = db
#         self.model = model
#     
#     def get_by_id(self, entity_id: int) -> T | None:
#         """Obtiene entidad por ID."""
#         return self.db.get(self.model, entity_id)
#     
#     def get_all(self, skip: int = 0, limit: int = 100) -> list[T]:
#         """Obtiene lista de entidades con paginación."""
#         stmt = select(self.model).offset(skip).limit(limit)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def add(self, entity: T) -> T:
#         """Agrega nueva entidad."""
#         self.db.add(entity)
#         self.db.commit()
#         self.db.refresh(entity)
#         return entity
#     
#     def update(self, entity: T) -> T:
#         """Actualiza entidad existente."""
#         self.db.commit()
#         self.db.refresh(entity)
#         return entity
#     
#     def delete(self, entity: T) -> None:
#         """Elimina entidad."""
#         self.db.delete(entity)
#         self.db.commit()
