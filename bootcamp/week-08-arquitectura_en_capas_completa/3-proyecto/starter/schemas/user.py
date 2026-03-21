# ============================================
# SCHEMAS USER
# ============================================

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserCreate(BaseModel):
    """
    DTO para crear usuario.
    
    TODO: Definir los campos con validaciones
    """
    # TODO: email con EmailStr
    email: EmailStr
    
    # TODO: name con min_length y max_length
    name: str = Field(..., min_length=1, max_length=100)
    
    # TODO: password con min_length
    password: str = Field(..., min_length=8)


class UserResponse(BaseModel):
    """
    DTO de respuesta para usuario.
    
    NO incluye password_hash.
    """
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    email: str
    name: str
    is_active: bool
    created_at: datetime
    # NO incluir password_hash
