"""
Servicios de lógica de negocio.

TODO: Completar las funciones de servicio
"""

from sqlalchemy.orm import Session
from datetime import datetime

from .models import User, Room, Message
from .schemas import UserCreate, RoomCreate, MessageCreate
from .auth import get_password_hash


# ============================================
# User Services
# ============================================

def create_user(db: Session, user_data: UserCreate) -> User:
    """
    Crea un nuevo usuario.
    
    TODO: Implementar
    
    Args:
        db: Sesión de DB
        user_data: Datos del usuario
        
    Returns:
        Usuario creado
    """
    # TODO: Implementar
    # 1. Hashear password
    # 2. Crear instancia de User
    # 3. Guardar en DB
    # 4. Retornar usuario
    pass


# ============================================
# Room Services
# ============================================

def create_room(db: Session, room_data: RoomCreate, user_id: int) -> Room:
    """
    Crea una nueva sala.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


def get_room(db: Session, room_id: int) -> Room | None:
    """Obtiene una sala por ID."""
    return db.query(Room).filter(Room.id == room_id).first()


def get_room_by_name(db: Session, name: str) -> Room | None:
    """Obtiene una sala por nombre."""
    return db.query(Room).filter(Room.name == name).first()


def get_rooms(db: Session, skip: int = 0, limit: int = 100) -> list[Room]:
    """
    Lista todas las salas.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


def get_or_create_default_room(db: Session) -> Room:
    """
    Obtiene o crea la sala 'general' por defecto.
    
    TODO: Implementar
    """
    # TODO: Implementar
    # 1. Buscar sala "general"
    # 2. Si no existe, crearla
    # 3. Retornar sala
    pass


# ============================================
# Message Services
# ============================================

def create_message(
    db: Session,
    room_id: int,
    user_id: int,
    content: str
) -> Message:
    """
    Crea un nuevo mensaje.
    
    TODO: Implementar
    """
    # TODO: Implementar
    pass


def get_room_messages(
    db: Session,
    room_id: int,
    skip: int = 0,
    limit: int = 50
) -> list[Message]:
    """
    Obtiene mensajes de una sala.
    
    TODO: Implementar
    
    Returns:
        Lista de mensajes ordenados por fecha (más recientes primero)
    """
    # TODO: Implementar
    # Ordenar por created_at descendente
    pass


def get_message_with_username(message: Message) -> dict:
    """
    Convierte mensaje a dict incluyendo username.
    """
    return {
        "id": message.id,
        "content": message.content,
        "created_at": message.created_at.isoformat(),
        "user_id": message.user_id,
        "room_id": message.room_id,
        "username": message.user.username if message.user else "Unknown"
    }
