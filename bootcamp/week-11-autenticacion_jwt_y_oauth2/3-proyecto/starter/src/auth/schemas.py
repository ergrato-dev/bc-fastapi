# schemas.py
"""Schemas Pydantic para autenticación y usuarios."""

from pydantic import BaseModel, EmailStr, Field, ConfigDict


# ============================================
# Schemas de Usuario
# ============================================

class UserBase(BaseModel):
    """Schema base para usuarios."""
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=100)


class UserCreate(UserBase):
    """Schema para crear usuario."""
    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """Schema para actualizar usuario."""
    full_name: str | None = Field(None, min_length=2, max_length=100)


class UserResponse(UserBase):
    """Schema de respuesta de usuario."""
    id: int
    role: str
    is_active: bool
    
    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserResponse):
    """Usuario con password hasheado (uso interno)."""
    hashed_password: str


# ============================================
# Schemas de Token
# ============================================

class Token(BaseModel):
    """Respuesta de token según OAuth2."""
    access_token: str
    refresh_token: str | None = None
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Datos extraídos del token."""
    email: str | None = None
    role: str | None = None
    token_type: str | None = None


class RefreshTokenRequest(BaseModel):
    """Request para refresh token."""
    refresh_token: str


# ============================================
# Schemas de Rol
# ============================================

class RoleUpdate(BaseModel):
    """Schema para actualizar rol."""
    role: str = Field(..., pattern="^(user|admin)$")
