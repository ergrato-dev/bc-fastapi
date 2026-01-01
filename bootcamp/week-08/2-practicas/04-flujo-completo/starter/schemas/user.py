# ============================================
# SCHEMAS USER
# ============================================

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    email: str
    created_at: datetime
