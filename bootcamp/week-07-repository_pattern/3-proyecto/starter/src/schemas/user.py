# ============================================
# Schemas de Usuario
# ============================================
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserCreate(BaseModel):
    """
    Schema para crear usuario
    
    TODO: Implementar campos:
    - username: str (3-50 chars)
    - email: EmailStr
    """
    # TODO: Implementar
    username: str = Field(..., min_length=3, max_length=50)
    email: str  # Cambiar a EmailStr cuando implementes


class UserUpdate(BaseModel):
    """
    Schema para actualizar usuario
    
    TODO: Implementar campos opcionales:
    - username: str | None
    - email: EmailStr | None
    - is_active: bool | None
    """
    # TODO: Implementar campos opcionales
    username: str | None = None
    email: str | None = None
    is_active: bool | None = None


class UserResponse(BaseModel):
    """
    Schema de respuesta de usuario
    
    TODO: Implementar campos:
    - id: int
    - username: str
    - email: str
    - is_active: bool
    - created_at: datetime
    """
    model_config = ConfigDict(from_attributes=True)
    
    # TODO: Implementar
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
