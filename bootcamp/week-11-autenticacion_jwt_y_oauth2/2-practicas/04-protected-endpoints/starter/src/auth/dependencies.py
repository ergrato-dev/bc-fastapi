# dependencies.py
"""
Dependencias de autenticación para FastAPI.

Este módulo contiene las dependencias que protegen los endpoints.
"""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from .schemas import TokenData
from .security import SECRET_KEY, ALGORITHM
from src.users.fake_db import get_user_by_email


# OAuth2 scheme - extrae el token del header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


# ============================================
# PASO 1: Dependencia get_current_user
# ============================================
print("--- Paso 1: get_current_user ---")

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
) -> dict:
    """
    Extrae y valida el usuario del token JWT.
    
    Esta dependencia:
    1. Recibe el token del header Authorization
    2. Decodifica y valida el JWT
    3. Extrae el email del claim "sub"
    4. Busca el usuario en la base de datos
    5. Retorna el usuario o lanza 401
    
    Args:
        token: JWT extraído automáticamente por OAuth2PasswordBearer
        
    Returns:
        dict: Datos del usuario autenticado
        
    Raises:
        HTTPException 401: Si el token es inválido o el usuario no existe
    """
    # Excepción reutilizable
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Descomenta las siguientes líneas:
    
    # try:
    #     # Decodificar el token
    #     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #     
    #     # Extraer email del claim "sub"
    #     email: str | None = payload.get("sub")
    #     if email is None:
    #         raise credentials_exception
    #     
    #     # Crear TokenData para validar estructura
    #     token_data = TokenData(email=email, role=payload.get("role"))
    #     
    # except JWTError:
    #     # Token inválido, expirado, o firma incorrecta
    #     raise credentials_exception
    # 
    # # Buscar usuario en la base de datos
    # user = get_user_by_email(token_data.email)
    # if user is None:
    #     raise credentials_exception
    # 
    # return user
    
    # TODO: Implementar - eliminar esta línea
    raise credentials_exception


# ============================================
# PASO 2: Dependencia get_current_active_user
# ============================================
print("--- Paso 2: get_current_active_user ---")

async def get_current_active_user(
    current_user: Annotated[dict, Depends(get_current_user)]
) -> dict:
    """
    Verifica que el usuario esté activo.
    
    Esta dependencia añade una capa extra de verificación,
    asegurando que el usuario no esté deshabilitado.
    
    Args:
        current_user: Usuario obtenido de get_current_user
        
    Returns:
        dict: Usuario activo
        
    Raises:
        HTTPException 403: Si el usuario está deshabilitado
    """
    # Descomenta las siguientes líneas:
    
    # if not current_user.get("is_active", False):
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="Inactive user"
    #     )
    # return current_user
    
    # TODO: Implementar - eliminar esta línea
    return current_user


# ============================================
# PASO 3: Factory para requerir roles específicos
# ============================================
print("--- Paso 3: require_role factory ---")

def require_role(required_role: str):
    """
    Factory que crea una dependencia para verificar roles.
    
    Uso:
        @router.get("/admin")
        async def admin_only(user = Depends(require_role("admin"))):
            return {"message": "Welcome, admin!"}
    
    Args:
        required_role: Rol requerido ("admin", "user", etc.)
        
    Returns:
        Dependencia que verifica el rol
    """
    # Descomenta las siguientes líneas:
    
    # async def role_checker(
    #     current_user: Annotated[dict, Depends(get_current_active_user)]
    # ) -> dict:
    #     user_role = current_user.get("role", "")
    #     if user_role != required_role:
    #         raise HTTPException(
    #             status_code=status.HTTP_403_FORBIDDEN,
    #             detail=f"Role '{required_role}' required"
    #         )
    #     return current_user
    # 
    # return role_checker
    
    # TODO: Implementar - eliminar estas líneas
    async def role_checker(
        current_user: Annotated[dict, Depends(get_current_active_user)]
    ) -> dict:
        return current_user
    
    return role_checker
