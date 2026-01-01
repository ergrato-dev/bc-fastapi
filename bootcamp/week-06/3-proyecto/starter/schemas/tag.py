# ============================================
# Schemas de Tag
# ============================================
from pydantic import BaseModel, Field, ConfigDict, field_validator
import re


class TagBase(BaseModel):
    """Base schema para Tag"""
    name: str = Field(..., min_length=2, max_length=50)


class TagCreate(TagBase):
    """Schema para crear Tag"""
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        # Solo letras, números y guiones
        if not re.match(r"^[a-zA-Z0-9-]+$", v):
            raise ValueError("Tag name can only contain letters, numbers, and hyphens")
        return v.lower()


class TagResponse(TagBase):
    """Schema de respuesta para Tag"""
    id: int
    slug: str
    
    model_config = ConfigDict(from_attributes=True)


class TagWithCount(TagResponse):
    """Schema de Tag con conteo de posts"""
    post_count: int = 0
