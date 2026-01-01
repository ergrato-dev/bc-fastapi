# ============================================
# Unit of Work
# ============================================
from sqlalchemy.orm import Session

from .repositories import UserRepository, TaskRepository


class UnitOfWork:
    """
    Unit of Work coordina transacciones entre repositorios.
    
    Todos los repositorios comparten la MISMA sesión.
    Permite commit/rollback de múltiples operaciones como una unidad.
    
    TODO: Implementar:
    - __enter__: crear repositorios
    - __exit__: rollback si hay excepción
    - commit(): confirmar cambios
    - rollback(): revertir cambios
    
    Uso:
        with UnitOfWork(session) as uow:
            user = uow.users.get_by_id(1)
            task = Task(title="Nueva", user_id=user.id)
            uow.tasks.add(task)
            uow.commit()
    """
    
    def __init__(self, session: Session):
        self._session = session
    
    def __enter__(self) -> "UnitOfWork":
        """
        Crea los repositorios con la sesión compartida.
        """
        # TODO: Crear self.users y self.tasks
        # self.users = UserRepository(self._session)
        # self.tasks = TaskRepository(self._session)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Si hay excepción, hace rollback automático.
        """
        # TODO: Implementar rollback condicional
        pass
    
    def commit(self) -> None:
        """Confirma todos los cambios en la transacción"""
        # TODO: Implementar
        pass
    
    def rollback(self) -> None:
        """Revierte todos los cambios en la transacción"""
        # TODO: Implementar
        pass
