"""
Schemas Pydantic para validación y serialización.
"""

from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


# ============================================
# Auth Schemas
# ============================================

class UserCreate(BaseModel):
    """Schema para crear usuario."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserResponse(BaseModel):
    """Schema de respuesta de usuario."""
    id: int
    username: str
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """Schema de token JWT."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Datos contenidos en el token."""
    user_id: int | None = None
    username: str | None = None


# ============================================
# Room Schemas
# ============================================

class RoomCreate(BaseModel):
    """Schema para crear sala."""
    name: str = Field(..., min_length=2, max_length=50)
    description: str = Field(default="", max_length=200)


class RoomResponse(BaseModel):
    """Schema de respuesta de sala."""
    id: int
    name: str
    description: str
    created_at: datetime
    created_by_id: int | None
    
    class Config:
        from_attributes = True


class RoomWithUsers(RoomResponse):
    """Sala con lista de usuarios conectados."""
    online_users: list[str] = []


# ============================================
# Message Schemas
# ============================================

class MessageCreate(BaseModel):
    """Schema para crear mensaje."""
    content: str = Field(..., min_length=1, max_length=1000)


class MessageResponse(BaseModel):
    """Schema de respuesta de mensaje."""
    id: int
    content: str
    created_at: datetime
    user_id: int
    room_id: int
    username: str  # Añadido para mostrar
    
    class Config:
        from_attributes = True


# ============================================
# WebSocket Schemas
# ============================================

class WSMessage(BaseModel):
    """Mensaje WebSocket entrante."""
    type: str  # "message", "typing", "ping"
    content: str = ""


class WSResponse(BaseModel):
    """Respuesta WebSocket."""
    type: str
    data: dict = {}
    timestamp: datetime = Field(default_factory=datetime.utcnow)
