# schemas.py
"""Schemas de autenticación."""

from pydantic import BaseModel


class Token(BaseModel):
    """Respuesta de token OAuth2."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Datos extraídos del token."""
    email: str | None = None
    role: str | None = None
