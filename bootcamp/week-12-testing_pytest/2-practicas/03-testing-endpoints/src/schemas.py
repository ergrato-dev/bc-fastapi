"""
Pydantic schemas for request/response validation.
"""

from pydantic import BaseModel, EmailStr, Field


# ============================================
# USER SCHEMAS
# ============================================

class UserCreate(BaseModel):
    """Schema for creating a user."""
    email: EmailStr
    password: str = Field(min_length=6)
    full_name: str | None = None


class UserResponse(BaseModel):
    """Schema for user response."""
    id: int
    email: EmailStr
    full_name: str | None
    is_active: bool
    
    model_config = {"from_attributes": True}


# ============================================
# ITEM SCHEMAS
# ============================================

class ItemCreate(BaseModel):
    """Schema for creating an item."""
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None
    price: float = Field(gt=0)


class ItemUpdate(BaseModel):
    """Schema for updating an item."""
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    price: float | None = Field(default=None, gt=0)


class ItemResponse(BaseModel):
    """Schema for item response."""
    id: int
    name: str
    description: str | None
    price: float
    owner_id: int | None
    
    model_config = {"from_attributes": True}


# ============================================
# AUTH SCHEMAS
# ============================================

class Token(BaseModel):
    """Schema for authentication token."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Schema for token payload."""
    email: str | None = None
