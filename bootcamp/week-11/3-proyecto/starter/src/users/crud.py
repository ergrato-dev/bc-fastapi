# crud.py
"""
Operaciones CRUD para usuarios.

Este módulo contiene las funciones para interactuar
con la base de datos de usuarios.
"""

from sqlalchemy.orm import Session

from src.users.models import User
from src.auth.schemas import UserCreate
from src.auth.security import hash_password


def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Busca un usuario por email.
    
    Args:
        db: Sesión de base de datos
        email: Email a buscar
        
    Returns:
        User si existe, None si no
    """
    # TODO: Implementar
    # Usar: db.query(User).filter(User.email == email).first()
    pass


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """
    Busca un usuario por ID.
    
    Args:
        db: Sesión de base de datos
        user_id: ID del usuario
        
    Returns:
        User si existe, None si no
    """
    # TODO: Implementar
    # Usar: db.query(User).filter(User.id == user_id).first()
    pass


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """
    Lista usuarios con paginación.
    
    Args:
        db: Sesión de base de datos
        skip: Registros a saltar
        limit: Máximo de registros
        
    Returns:
        Lista de usuarios
    """
    # TODO: Implementar
    # Usar: db.query(User).offset(skip).limit(limit).all()
    pass


def create_user(db: Session, user_data: UserCreate) -> User:
    """
    Crea un nuevo usuario.
    
    Args:
        db: Sesión de base de datos
        user_data: Datos del usuario (email, full_name, password)
        
    Returns:
        Usuario creado
    """
    # TODO: Implementar
    # 1. Hashear password: hashed = hash_password(user_data.password)
    # 2. Crear instancia: user = User(email=..., full_name=..., hashed_password=hashed)
    # 3. Añadir a sesión: db.add(user)
    # 4. Commit: db.commit()
    # 5. Refresh: db.refresh(user)
    # 6. Retornar user
    pass


def update_user_role(db: Session, user: User, new_role: str) -> User:
    """
    Actualiza el rol de un usuario.
    
    Args:
        db: Sesión de base de datos
        user: Usuario a actualizar
        new_role: Nuevo rol
        
    Returns:
        Usuario actualizado
    """
    # TODO: Implementar
    # 1. user.role = new_role
    # 2. db.commit()
    # 3. db.refresh(user)
    # 4. Retornar user
    pass


def update_user_name(db: Session, user: User, new_name: str) -> User:
    """
    Actualiza el nombre de un usuario.
    
    Args:
        db: Sesión de base de datos
        user: Usuario a actualizar
        new_name: Nuevo nombre
        
    Returns:
        Usuario actualizado
    """
    # TODO: Implementar
    pass
