"""
Port: UserRepository.

Define la interfaz para persistencia de usuarios.
"""

from typing import Protocol
from uuid import UUID

from domain.entities.user import User


class UserRepository(Protocol):
    """
    Puerto: Repositorio de usuarios.
    
    TODO: Implementar un adaptador que cumpla esta interfaz
    en infrastructure/persistence/user_repository.py
    """
    
    def save(self, user: User) -> None:
        """Guardar o actualizar un usuario."""
        ...
    
    def find_by_id(self, user_id: UUID) -> User | None:
        """Buscar usuario por ID."""
        ...
    
    def find_by_email(self, email: str) -> User | None:
        """Buscar usuario por email."""
        ...
    
    def find_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        """Listar todos los usuarios."""
        ...
    
    def delete(self, user_id: UUID) -> bool:
        """Eliminar usuario por ID."""
        ...
