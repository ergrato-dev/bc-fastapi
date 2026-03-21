# router.py
"""
Router de autenticación.

Endpoints:
- POST /auth/register - Registro de usuarios
- POST /auth/token - Login (OAuth2)
- POST /auth/refresh - Renovar tokens
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database import get_db
from src.auth.schemas import (
    UserCreate,
    UserResponse,
    Token,
    RefreshTokenRequest,
)
from src.auth.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_token_type,
)
from src.users.crud import get_user_by_email, create_user


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: Annotated[Session, Depends(get_db)],
) -> UserResponse:
    """
    Registra un nuevo usuario.
    
    - Valida que el email no exista
    - Hashea el password
    - Crea usuario con rol "user"
    """
    # TODO: Implementar
    # 1. Verificar si el email ya existe usando get_user_by_email(db, user_data.email)
    # 2. Si existe, lanzar HTTPException 400 con detail="Email already registered"
    # 3. Crear usuario usando create_user(db, user_data)
    # 4. Retornar el usuario creado
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Register not implemented yet"
    )


@router.post("/token", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
) -> Token:
    """
    OAuth2 compatible token login.
    
    Recibe credenciales como form-data y retorna tokens JWT.
    """
    # TODO: Implementar
    # 1. Buscar usuario por email: get_user_by_email(db, form_data.username)
    # 2. Si no existe, lanzar HTTPException 401
    # 3. Verificar password: verify_password(form_data.password, user.hashed_password)
    # 4. Si no coincide, lanzar HTTPException 401
    # 5. Verificar que el usuario esté activo
    # 6. Crear access_token con data={"sub": user.email, "role": user.role}
    # 7. Crear refresh_token con data={"sub": user.email}
    # 8. Retornar Token con ambos tokens
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Login not implemented yet"
    )


@router.post("/refresh", response_model=Token)
async def refresh_token(
    request: RefreshTokenRequest,
    db: Annotated[Session, Depends(get_db)],
) -> Token:
    """
    Obtiene nuevos tokens usando el refresh token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # TODO: Implementar
    # 1. Verificar token usando verify_token_type(request.refresh_token, "refresh")
    # 2. Si es None, lanzar credentials_exception
    # 3. Extraer email del payload["sub"]
    # 4. Buscar usuario en DB
    # 5. Si no existe o no está activo, lanzar credentials_exception
    # 6. Crear nuevos access_token y refresh_token
    # 7. Retornar Token con nuevos tokens
    
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Refresh not implemented yet"
    )
