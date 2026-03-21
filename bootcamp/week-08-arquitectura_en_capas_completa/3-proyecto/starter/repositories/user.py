# ============================================
# USER REPOSITORY
# ============================================

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .base import BaseRepository
from models.user import User
from exceptions.user import UserAlreadyExistsError


class UserRepository(BaseRepository[User]):
    """Repository para User."""
    
    def __init__(self, db: Session):
        super().__init__(db, User)
    
    def get_by_email(self, email: str) -> User | None:
        """
        Obtiene usuario por email.
        
        TODO: Implementar query
        """
        stmt = select(User).where(User.email == email)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def add(self, user: User) -> User:
        """
        Agrega usuario con manejo de duplicados.
        
        TODO: Capturar IntegrityError y lanzar UserAlreadyExistsError
        """
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            raise UserAlreadyExistsError(user.email)
