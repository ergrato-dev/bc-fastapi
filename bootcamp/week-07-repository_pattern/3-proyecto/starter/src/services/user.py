# ============================================
# User Service
# ============================================
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from ..unit_of_work import UnitOfWork


class UserNotFoundError(Exception):
    """Usuario no encontrado"""
    pass


class UserAlreadyExistsError(Exception):
    """Usuario ya existe (username o email duplicado)"""
    pass


class UserService:
    """
    Servicio de usuarios con lógica de negocio.
    
    Usa UnitOfWork para acceder a repositorios.
    NO accede directamente a la base de datos.
    
    TODO: Implementar métodos:
    - create_user(data) -> User
    - get_user(id) -> User
    - get_users(skip, limit) -> list[User]
    - update_user(id, data) -> User
    - delete_user(id) -> None
    - deactivate_user(id) -> User
    """
    
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    def create_user(self, data: UserCreate) -> User:
        """
        Crea un nuevo usuario.
        
        Validaciones:
        - Username no debe existir
        - Email no debe existir
        """
        # TODO: Implementar
        # 1. Verificar username único
        # 2. Verificar email único
        # 3. Crear User con los datos
        # 4. Agregar via uow.users.add()
        # 5. Retornar usuario creado
        pass
    
    def get_user(self, user_id: int) -> User:
        """
        Obtiene usuario por ID.
        
        Raises:
            UserNotFoundError: Si no existe
        """
        # TODO: Implementar
        pass
    
    def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """Obtiene lista de usuarios con paginación"""
        # TODO: Implementar
        pass
    
    def update_user(self, user_id: int, data: UserUpdate) -> User:
        """
        Actualiza usuario existente.
        
        Validaciones:
        - Usuario debe existir
        - Si cambia username, verificar único
        - Si cambia email, verificar único
        """
        # TODO: Implementar
        pass
    
    def delete_user(self, user_id: int) -> None:
        """
        Elimina usuario.
        
        Raises:
            UserNotFoundError: Si no existe
        """
        # TODO: Implementar
        pass
    
    def deactivate_user(self, user_id: int) -> User:
        """
        Desactiva usuario (soft delete).
        
        En lugar de eliminar, marca is_active=False
        """
        # TODO: Implementar
        pass
