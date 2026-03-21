# ============================================
# USER SERVICE
# ============================================

from models.user import User
from schemas.user import UserCreate, UserResponse
from repositories.user import UserRepository
from mappers.user import UserMapper
from exceptions.user import UserNotFoundError


class UserService:
    """Service para lógica de negocio de User."""
    
    def __init__(self, repo: UserRepository):
        self.repo = repo
    
    def get_all(self) -> list[UserResponse]:
        """Lista todos los usuarios."""
        entities = self.repo.get_all()
        return UserMapper.to_response_list(entities)
    
    def get_by_id(self, user_id: int) -> UserResponse:
        """
        Obtiene usuario por ID.
        
        TODO: Lanzar UserNotFoundError si no existe
        """
        entity = self.repo.get_by_id(user_id)
        if not entity:
            raise UserNotFoundError(user_id)
        return UserMapper.to_response(entity)
    
    def create(self, data: UserCreate) -> UserResponse:
        """
        Crea nuevo usuario.
        
        TODO: Hashear password antes de guardar
        NOTA: En producción usar bcrypt o argon2
        """
        # Hashear password (simplificado - usar bcrypt en producción)
        password_hash = f"hashed_{data.password}"
        
        entity = UserMapper.to_entity(data, password_hash)
        saved = self.repo.add(entity)
        return UserMapper.to_response(saved)
