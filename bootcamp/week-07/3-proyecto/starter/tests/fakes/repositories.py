# ============================================
# Fake Repositories para Testing
# ============================================
"""
Fake Repositories permiten testear Services
sin necesidad de base de datos real.

TODO: Implementar:
- FakeUserRepository
- FakeTaskRepository
- FakeUnitOfWork
"""

from typing import TypeVar, Generic
from datetime import datetime

from src.models.base import Base
from src.models.user import User
from src.models.task import Task, Priority

T = TypeVar("T", bound=Base)


class FakeBaseRepository(Generic[T]):
    """
    Fake repository que almacena datos en memoria.
    
    TODO: Implementar métodos:
    - get_by_id(id) -> T | None
    - get_all(skip, limit) -> list[T]
    - add(entity) -> T
    - update(entity) -> T
    - delete(entity) -> None
    - count() -> int
    """
    
    def __init__(self):
        self._data: dict[int, T] = {}
        self._next_id = 1
    
    def get_by_id(self, id: int) -> T | None:
        # TODO: Implementar
        pass
    
    def get_all(self, skip: int = 0, limit: int = 100) -> list[T]:
        # TODO: Implementar
        pass
    
    def add(self, entity: T) -> T:
        # TODO: Implementar
        # Asignar ID si no tiene
        pass
    
    def update(self, entity: T) -> T:
        # TODO: Implementar
        pass
    
    def delete(self, entity: T) -> None:
        # TODO: Implementar
        pass
    
    def count(self) -> int:
        # TODO: Implementar
        pass


class FakeUserRepository(FakeBaseRepository[User]):
    """
    Fake UserRepository para testing.
    
    TODO: Implementar métodos específicos:
    - get_by_username(username) -> User | None
    - get_by_email(email) -> User | None
    - exists_by_username(username) -> bool
    - exists_by_email(email) -> bool
    """
    
    def get_by_username(self, username: str) -> User | None:
        # TODO: Implementar
        pass
    
    def get_by_email(self, email: str) -> User | None:
        # TODO: Implementar
        pass
    
    def exists_by_username(self, username: str) -> bool:
        # TODO: Implementar
        pass
    
    def exists_by_email(self, email: str) -> bool:
        # TODO: Implementar
        pass


class FakeTaskRepository(FakeBaseRepository[Task]):
    """
    Fake TaskRepository para testing.
    
    TODO: Implementar métodos específicos:
    - get_by_user(user_id) -> list[Task]
    - get_completed(user_id?) -> list[Task]
    - get_pending(user_id?) -> list[Task]
    """
    
    def get_by_user(self, user_id: int) -> list[Task]:
        # TODO: Implementar
        pass
    
    def get_completed(self, user_id: int | None = None) -> list[Task]:
        # TODO: Implementar
        pass
    
    def get_pending(self, user_id: int | None = None) -> list[Task]:
        # TODO: Implementar
        pass


class FakeUnitOfWork:
    """
    Fake UnitOfWork para testing.
    
    No necesita base de datos.
    Usa FakeRepositories internamente.
    """
    
    def __init__(self):
        self.users = FakeUserRepository()
        self.tasks = FakeTaskRepository()
        self._committed = False
        self._rolled_back = False
    
    def __enter__(self) -> "FakeUnitOfWork":
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
    
    def commit(self) -> None:
        self._committed = True
    
    def rollback(self) -> None:
        self._rolled_back = True
    
    @property
    def committed(self) -> bool:
        """Útil para verificar en tests"""
        return self._committed
    
    @property
    def rolled_back(self) -> bool:
        """Útil para verificar en tests"""
        return self._rolled_back
