# dependencies.py
"""
Dependencias de autenticación para FastAPI.

Estas dependencias se usan para proteger endpoints
y extraer información del usuario autenticado.
"""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.database import get_db
from src.auth.schemas import TokenData
from src.auth.security import decode_token
from src.users.models import User


# OAuth2 scheme - extrae token del header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    """
    Extrae y valida el usuario del token JWT.
    
    Esta dependencia:
    1. Extrae el token del header Authorization
    2. Decodifica y valida el JWT
    3. Verifica que sea un access token
    4. Busca el usuario en la base de datos
    5. Retorna el usuario o lanza 401
    
    Args:
        token: JWT del header Authorization
        db: Sesión de base de datos
        
    Returns:
        User: Usuario autenticado
        
    Raises:
        HTTPException 401: Token inválido o usuario no existe
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # TODO: Implementar
    # 1. Decodificar el token usando decode_token()
    # 2. Si es None, lanzar credentials_exception
    # 3. Verificar que el tipo sea "access" (payload.get("type"))
    # 4. Extraer email del claim "sub"
    # 5. Buscar usuario en DB: db.query(User).filter(User.email == email).first()
    # 6. Si no existe, lanzar credentials_exception
    # 7. Retornar el usuario
    
    raise credentials_exception  # Eliminar esta línea al implementar


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    """
    Verifica que el usuario esté activo.
    
    Args:
        current_user: Usuario de get_current_user
        
    Returns:
        User: Usuario activo
        
    Raises:
        HTTPException 403: Si el usuario está inactivo
    """
    # TODO: Implementar
    # 1. Verificar current_user.is_active
    # 2. Si es False, lanzar HTTPException 403 con detail="Inactive user"
    # 3. Retornar current_user
    
    return current_user  # Modificar al implementar


def require_role(required_role: str):
    """
    Factory que crea una dependencia para verificar roles.
    
    Uso:
        @router.get("/admin")
        async def admin_only(user = Depends(require_role("admin"))):
            ...
    
    Args:
        required_role: Rol requerido ("admin", "user")
        
    Returns:
        Dependencia que verifica el rol
    """
    async def role_checker(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        # TODO: Implementar
        # 1. Verificar current_user.role == required_role
        # 2. Si no coincide, lanzar HTTPException 403 con detail="Role '{required_role}' required"
        # 3. Retornar current_user
        
        return current_user  # Modificar al implementar
    
    return role_checker
