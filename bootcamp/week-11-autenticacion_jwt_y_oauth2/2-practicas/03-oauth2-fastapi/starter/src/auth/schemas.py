# schemas.py
"""Schemas Pydantic para autenticación."""

from pydantic import BaseModel


class Token(BaseModel):
    """
    Respuesta del endpoint de token según OAuth2.
    
    Attributes:
        access_token: JWT de acceso
        token_type: Siempre "bearer" según OAuth2
        refresh_token: JWT para renovar access token (opcional)
    """
    access_token: str
    token_type: str = "bearer"
    refresh_token: str | None = None


class TokenData(BaseModel):
    """
    Datos extraídos de un token decodificado.
    
    Se usa internamente para tipar los datos del token.
    """
    email: str | None = None
    role: str | None = None
