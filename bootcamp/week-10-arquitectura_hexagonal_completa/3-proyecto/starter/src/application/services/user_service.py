"""
UserService - Orquestador de casos de uso de usuarios.
"""

from uuid import UUID

from domain.entities.user import User
from domain.ports.user_repository import UserRepository
from domain.exceptions import UserNotFoundError, UserAlreadyExistsError

from application.commands.user_commands import CreateUserCommand
from application.dtos.user_dto import UserDTO, UserListDTO


class UserService:
    """Application Service para User."""
    
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repo = user_repository
    
    def create_user(self, command: CreateUserCommand) -> UserDTO:
        """
        Caso de uso: Crear nuevo usuario.
        
        TODO: Implementar:
        1. Verificar que el email no existe
        2. Crear la entidad User usando User.create()
        3. Guardar en el repositorio
        4. Retornar UserDTO
        """
        # TODO: Implementar
        pass
    
    def get_user(self, user_id: UUID) -> UserDTO:
        """
        Caso de uso: Obtener usuario por ID.
        
        TODO: Implementar
        """
        # TODO: Implementar
        pass
    
    def list_users(self, skip: int = 0, limit: int = 100) -> UserListDTO:
        """
        Caso de uso: Listar usuarios.
        
        TODO: Implementar
        """
        # TODO: Implementar
        pass
    
    def _to_dto(self, user: User) -> UserDTO:
        """Convertir entidad User a DTO."""
        return UserDTO(
            id=user.id,
            email=user.email,
            name=user.name,
            is_active=user.is_active,
            created_at=user.created_at,
        )
