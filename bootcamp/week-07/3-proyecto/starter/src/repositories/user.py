# ============================================
# User Repository
# ============================================
from sqlalchemy import select
from sqlalchemy.orm import Session

from .base import BaseRepository
from ..models.user import User


class UserRepository(BaseRepository[User]):
    """
    Repositorio específico para usuarios.
    
    Hereda operaciones CRUD de BaseRepository
    y añade métodos específicos.
    
    TODO: Implementar métodos:
    - get_by_username(username) -> User | None
    - get_by_email(email) -> User | None
    - get_active_users() -> list[User]
    - exists_by_username(username) -> bool
    - exists_by_email(email) -> bool
    """
    
    def __init__(self, db: Session):
        super().__init__(db, User)
    
    def get_by_username(self, username: str) -> User | None:
        """Obtiene usuario por username"""
        # TODO: Implementar
        pass
    
    def get_by_email(self, email: str) -> User | None:
        """Obtiene usuario por email"""
        # TODO: Implementar
        pass
    
    def get_active_users(self) -> list[User]:
        """Obtiene todos los usuarios activos"""
        # TODO: Implementar filtrando is_active=True
        pass
    
    def exists_by_username(self, username: str) -> bool:
        """Verifica si existe un usuario con ese username"""
        # TODO: Implementar usando get_by_username
        pass
    
    def exists_by_email(self, email: str) -> bool:
        """Verifica si existe un usuario con ese email"""
        # TODO: Implementar usando get_by_email
        pass
