# ============================================
# USER MAPPER
# ============================================

from models.user import User
from schemas.user import UserCreate, UserResponse


class UserMapper:
    """Mapper para conversiones de User."""
    
    @staticmethod
    def to_entity(dto: UserCreate, password_hash: str) -> User:
        """
        Convierte UserCreate → User entity.
        
        TODO: Implementar conversión
        """
        # TODO: Crear User con los campos del DTO
        # NOTA: password viene como texto plano, se debe hashear antes
        return User(
            email=dto.email,
            name=dto.name,
            password_hash=password_hash
        )
    
    @staticmethod
    def to_response(entity: User) -> UserResponse:
        """
        Convierte User entity → UserResponse.
        
        TODO: Implementar usando model_validate
        """
        return UserResponse.model_validate(entity)
    
    @staticmethod
    def to_response_list(entities: list[User]) -> list[UserResponse]:
        """Convierte lista de entities."""
        return [UserMapper.to_response(e) for e in entities]
