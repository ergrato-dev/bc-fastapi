# ============================================
# Base Repository Genérico
# ============================================
from typing import TypeVar, Generic
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models.base import Base

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    """
    Repositorio base genérico con operaciones CRUD.
    
    TODO: Implementar métodos:
    - get_by_id(id) -> T | None
    - get_all(skip, limit) -> list[T]
    - add(entity) -> T
    - update(entity) -> T
    - delete(entity) -> None
    - count() -> int
    """
    
    def __init__(self, db: Session, model: type[T]):
        """
        Inicializa el repositorio.
        
        Args:
            db: Sesión de SQLAlchemy
            model: Clase del modelo
        """
        self.db = db
        self.model = model
    
    def get_by_id(self, id: int) -> T | None:
        """Obtiene entidad por ID"""
        # TODO: Implementar usando db.get()
        pass
    
    def get_all(self, skip: int = 0, limit: int = 100) -> list[T]:
        """Obtiene todas las entidades con paginación"""
        # TODO: Implementar usando select() con offset/limit
        pass
    
    def add(self, entity: T) -> T:
        """
        Agrega nueva entidad.
        
        IMPORTANTE: Usa flush() para obtener el ID,
        pero NO hace commit (eso lo maneja el UoW)
        """
        # TODO: Implementar usando db.add(), db.flush(), db.refresh()
        pass
    
    def update(self, entity: T) -> T:
        """
        Actualiza entidad existente.
        
        IMPORTANTE: Usa flush(), no commit()
        """
        # TODO: Implementar
        pass
    
    def delete(self, entity: T) -> None:
        """Elimina entidad"""
        # TODO: Implementar usando db.delete(), db.flush()
        pass
    
    def count(self) -> int:
        """Cuenta total de entidades"""
        # TODO: Implementar
        pass
