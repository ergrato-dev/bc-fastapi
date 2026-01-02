# security.py
"""
Funciones de seguridad para autenticación.

Este módulo contiene las funciones para:
- Hashear y verificar passwords con bcrypt
- Crear y decodificar tokens JWT
"""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt, JWTError
from passlib.context import CryptContext

from src.config import settings


# Contexto de password con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ============================================
# FUNCIONES DE PASSWORD
# ============================================

def hash_password(password: str) -> str:
    """
    Hashea una contraseña usando bcrypt.
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        str: Hash de la contraseña
    """
    # TODO: Implementar usando pwd_context.hash()
    pass


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica una contraseña contra su hash.
    
    Args:
        plain_password: Contraseña en texto plano
        hashed_password: Hash almacenado
        
    Returns:
        bool: True si coincide, False si no
    """
    # TODO: Implementar usando pwd_context.verify()
    pass


# ============================================
# FUNCIONES DE JWT
# ============================================

def create_access_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:
    """
    Crea un JWT access token.
    
    Args:
        data: Datos a incluir en el payload (debe incluir "sub")
        expires_delta: Tiempo de expiración (opcional)
        
    Returns:
        str: Token JWT codificado
        
    El token debe incluir:
    - Los datos proporcionados
    - "exp": Tiempo de expiración
    - "iat": Tiempo de creación
    - "type": "access"
    """
    # TODO: Implementar
    # 1. Copiar data para no modificar el original
    # 2. Calcular expiración (usar settings.ACCESS_TOKEN_EXPIRE_MINUTES si no se proporciona)
    # 3. Añadir claims: exp, iat, type="access"
    # 4. Codificar con jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    pass


def create_refresh_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:
    """
    Crea un JWT refresh token.
    
    Similar a access_token pero:
    - Mayor tiempo de expiración (REFRESH_TOKEN_EXPIRE_DAYS)
    - type="refresh"
    """
    # TODO: Implementar (similar a create_access_token pero con type="refresh")
    pass


def decode_token(token: str) -> dict[str, Any] | None:
    """
    Decodifica y valida un token JWT.
    
    Args:
        token: Token JWT a decodificar
        
    Returns:
        dict: Payload del token si es válido
        None: Si el token es inválido o expirado
    """
    # TODO: Implementar
    # 1. Usar jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    # 2. Capturar JWTError y retornar None si falla
    pass


def verify_token_type(token: str, expected_type: str) -> dict[str, Any] | None:
    """
    Verifica que un token sea del tipo esperado.
    
    Args:
        token: Token JWT
        expected_type: "access" o "refresh"
        
    Returns:
        dict: Payload si el tipo coincide
        None: Si no coincide o es inválido
    """
    # TODO: Implementar
    # 1. Decodificar el token
    # 2. Verificar que payload.get("type") == expected_type
    # 3. Retornar payload si coincide, None si no
    pass
