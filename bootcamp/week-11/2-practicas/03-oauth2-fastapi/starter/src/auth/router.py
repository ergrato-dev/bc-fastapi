# router.py
"""
Router de autenticación con OAuth2 Password Flow.

Este módulo implementa el endpoint /token según la especificación OAuth2.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .schemas import Token
from .security import (
    verify_password,
    create_access_token,
    create_refresh_token,
)
from src.users.fake_db import get_user_by_email


router = APIRouter(prefix="/auth", tags=["Authentication"])


# ============================================
# PASO 1: Configurar OAuth2PasswordBearer
# ============================================
print("--- Paso 1: Configurar OAuth2PasswordBearer ---")

# OAuth2PasswordBearer es un esquema de seguridad que:
# - Define dónde está el endpoint de token (tokenUrl)
# - Extrae el token del header Authorization
# - Se integra con Swagger UI

# Descomenta la siguiente línea:
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


# ============================================
# PASO 2: Función para autenticar usuario
# ============================================
print("--- Paso 2: Función authenticate_user ---")

def authenticate_user(email: str, password: str):
    """
    Autentica un usuario con email y password.
    
    1. Busca el usuario en la base de datos
    2. Verifica que el password sea correcto
    
    Args:
        email: Email del usuario
        password: Password en texto plano
        
    Returns:
        User si las credenciales son válidas
        None si no lo son
    """
    # Descomenta las siguientes líneas:
    
    # # Buscar usuario por email
    # user = get_user_by_email(email)
    # if not user:
    #     return None
    
    # # Verificar password
    # if not verify_password(password, user["hashed_password"]):
    #     return None
    
    # return user
    
    # TODO: Implementar - eliminar esta línea
    return None


# ============================================
# PASO 3: Endpoint de Token (OAuth2 Password Flow)
# ============================================
print("--- Paso 3: Endpoint POST /token ---")

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible token login endpoint.
    
    Este endpoint recibe credenciales como form data y retorna tokens.
    
    - **username**: En OAuth2 se llama username, pero usamos email
    - **password**: Contraseña del usuario
    
    El formato de respuesta sigue la especificación OAuth2:
    - access_token: Token JWT de acceso
    - token_type: "bearer"
    
    Raises:
        401 Unauthorized: Si las credenciales son inválidas
    """
    # Descomenta las siguientes líneas:
    
    # # Autenticar usuario (form_data.username contiene el email)
    # user = authenticate_user(form_data.username, form_data.password)
    
    # # Si no es válido, retornar 401
    # if not user:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Incorrect email or password",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    
    # # Crear access token con el email como subject
    # access_token = create_access_token(
    #     data={"sub": user["email"], "role": user["role"]}
    # )
    
    # # Crear refresh token
    # refresh_token = create_refresh_token(data={"sub": user["email"]})
    
    # return Token(
    #     access_token=access_token,
    #     refresh_token=refresh_token,
    # )
    
    # TODO: Implementar - eliminar estas líneas
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Token endpoint not implemented yet"
    )


# ============================================
# PASO 4: Endpoint de Refresh Token (Bonus)
# ============================================
print("--- Paso 4: Endpoint POST /refresh ---")

# @router.post("/refresh", response_model=Token)
# async def refresh_access_token(refresh_token: str):
#     """
#     Obtiene nuevos tokens usando el refresh token.
#     
#     Este endpoint permite renovar el access token sin
#     necesidad de volver a ingresar credenciales.
#     """
#     # Implementación opcional
#     pass
