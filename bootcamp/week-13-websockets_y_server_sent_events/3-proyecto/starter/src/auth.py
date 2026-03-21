"""
Autenticación y autorización JWT.

TODO: Completar las funciones marcadas con TODO
"""

from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, Query
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from .config import settings
from .database import get_db
from .models import User
from .schemas import TokenData


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña coincide con el hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Genera hash de contraseña."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Crea un token JWT.
    
    TODO: Implementar la creación del token
    
    Args:
        data: Datos a incluir en el token
        expires_delta: Tiempo de expiración
        
    Returns:
        Token JWT codificado
    """
    # TODO: Implementar
    # 1. Copiar data para no modificar original
    # 2. Calcular tiempo de expiración
    # 3. Añadir "exp" al payload
    # 4. Codificar con jwt.encode()
    pass


def decode_token(token: str) -> TokenData | None:
    """
    Decodifica y valida un token JWT.
    
    TODO: Implementar la decodificación del token
    
    Args:
        token: Token JWT
        
    Returns:
        TokenData si es válido, None si no
    """
    # TODO: Implementar
    # 1. Decodificar con jwt.decode()
    # 2. Extraer user_id y username
    # 3. Retornar TokenData
    # 4. Manejar JWTError retornando None
    pass


def get_user_by_username(db: Session, username: str) -> User | None:
    """Obtiene usuario por username."""
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    """Obtiene usuario por email."""
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """Obtiene usuario por ID."""
    return db.query(User).filter(User.id == user_id).first()


def authenticate_user(db: Session, username: str, password: str) -> User | None:
    """
    Autentica un usuario con username y password.
    
    TODO: Implementar autenticación
    
    Args:
        db: Sesión de DB
        username: Nombre de usuario
        password: Contraseña en texto plano
        
    Returns:
        User si credenciales válidas, None si no
    """
    # TODO: Implementar
    # 1. Obtener usuario por username
    # 2. Verificar password
    # 3. Retornar user o None
    pass


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency para obtener usuario actual del token.
    
    TODO: Implementar obtención de usuario actual
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # TODO: Implementar
    # 1. Decodificar token
    # 2. Obtener usuario de DB
    # 3. Retornar usuario o raise exception
    pass


async def get_current_user_ws(
    token: str = Query(...),
    db: Session = Depends(get_db)
) -> User:
    """
    Obtiene usuario actual para WebSocket (token en query).
    
    TODO: Implementar - similar a get_current_user pero para WS
    """
    # TODO: Implementar
    # Similar a get_current_user pero recibe token de query param
    pass
