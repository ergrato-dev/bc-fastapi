"""
InMemoryUserRepository - Adaptador de persistencia en memoria.
"""

from uuid import UUID

from domain.entities.user import User


class InMemoryUserRepository:
    """
    Adaptador: Repositorio de usuarios en memoria.
    
    TODO: Implementar todos los métodos del protocolo UserRepository.
    """
    
    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}
        self._email_index: dict[str, UUID] = {}  # Para búsqueda por email
    
    def save(self, user: User) -> None:
        """TODO: Implementar (actualizar también _email_index)."""
        pass
    
    def find_by_id(self, user_id: UUID) -> User | None:
        """TODO: Implementar."""
        pass
    
    def find_by_email(self, email: str) -> User | None:
        """TODO: Implementar (usar _email_index)."""
        pass
    
    def find_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        """TODO: Implementar."""
        pass
    
    def delete(self, user_id: UUID) -> bool:
        """TODO: Implementar (limpiar también _email_index)."""
        pass
