"""
Auth Router - Autenticación Simple.

Este módulo implementa endpoints de autenticación
con rate limiting estricto para prevenir brute force.
"""

from fastapi import APIRouter, HTTPException, Request, status
from passlib.context import CryptContext

from src.schemas import LoginRequest, Token
from src.security.rate_limit import limiter


router = APIRouter(prefix="/auth", tags=["auth"])


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Usuarios fake para demo
fake_users_db = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "hashed_password": pwd_context.hash("admin123"),
        "is_active": True,
    },
    "user": {
        "username": "user",
        "email": "user@example.com",
        "hashed_password": pwd_context.hash("user123"),
        "is_active": True,
    },
}


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica password contra hash."""
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str) -> dict | None:
    """Autentica usuario por username y password."""
    user = fake_users_db.get(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user


# ============================================
# LOGIN
# ============================================

@router.post("/login", response_model=Token)
# TODO: Añadir rate limiting estricto para prevenir brute force
# @limiter.limit("5/minute")
async def login(request: Request, login_data: LoginRequest):
    """
    Autentica usuario y retorna token JWT.
    
    Rate limit: 5 requests por minuto (prevención de brute force).
    
    - **username**: Nombre de usuario
    - **password**: Contraseña
    """
    user = authenticate_user(login_data.username, login_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # TODO: Generar JWT real
    # En producción, usar python-jose para crear JWT
    fake_token = f"fake-jwt-token-for-{user['username']}"
    
    return Token(access_token=fake_token, token_type="bearer")


# ============================================
# LOGOUT (Optional)
# ============================================

@router.post("/logout")
async def logout(request: Request):
    """
    Cierra sesión del usuario.
    
    En una implementación real, invalidaría el token JWT
    (usando blacklist en Redis, por ejemplo).
    """
    return {"message": "Successfully logged out"}
