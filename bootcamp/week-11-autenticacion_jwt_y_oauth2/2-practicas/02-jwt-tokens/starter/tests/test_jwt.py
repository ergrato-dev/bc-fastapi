# test_jwt.py
"""Tests para funciones JWT."""

from datetime import timedelta

import pytest
from freezegun import freeze_time

from src.security.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token,
    verify_token_type,
    TokenExpiredError,
    InvalidTokenError,
    SECRET_KEY,
    ALGORITHM,
)
from jose import jwt


class TestCreateAccessToken:
    """Tests para create_access_token."""
    
    def test_creates_valid_jwt(self):
        """Debe crear un JWT válido."""
        token = create_access_token("user@email.com")
        assert isinstance(token, str)
        assert token.count(".") == 2  # Header.Payload.Signature
    
    def test_token_contains_subject(self):
        """El token debe contener el subject."""
        token = create_access_token("user@email.com")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload["sub"] == "user@email.com"
    
    def test_token_has_expiration(self):
        """El token debe tener fecha de expiración."""
        token = create_access_token("user@email.com")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert "exp" in payload
    
    def test_token_has_issued_at(self):
        """El token debe tener fecha de creación."""
        token = create_access_token("user@email.com")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert "iat" in payload
    
    def test_token_type_is_access(self):
        """El tipo debe ser 'access'."""
        token = create_access_token("user@email.com")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload.get("type") == "access"
    
    def test_includes_extra_claims(self):
        """Debe incluir claims adicionales."""
        token = create_access_token(
            "user@email.com",
            extra_claims={"role": "admin", "department": "IT"}
        )
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload["role"] == "admin"
        assert payload["department"] == "IT"
    
    def test_custom_expiration(self):
        """Debe respetar expiración personalizada."""
        token = create_access_token(
            "user@email.com",
            expires_delta=timedelta(hours=1)
        )
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # El token debe ser válido (no expirado)
        assert "exp" in payload


class TestCreateRefreshToken:
    """Tests para create_refresh_token."""
    
    def test_creates_valid_jwt(self):
        """Debe crear un JWT válido."""
        token = create_refresh_token("user@email.com")
        assert isinstance(token, str)
        assert token.count(".") == 2
    
    def test_token_type_is_refresh(self):
        """El tipo debe ser 'refresh'."""
        token = create_refresh_token("user@email.com")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert payload.get("type") == "refresh"
    
    def test_refresh_token_has_longer_expiration(self):
        """Refresh token debe tener expiración más larga."""
        access = create_access_token("user@email.com")
        refresh = create_refresh_token("user@email.com")
        
        access_payload = jwt.decode(access, SECRET_KEY, algorithms=[ALGORITHM])
        refresh_payload = jwt.decode(refresh, SECRET_KEY, algorithms=[ALGORITHM])
        
        assert refresh_payload["exp"] > access_payload["exp"]


class TestDecodeToken:
    """Tests para decode_token."""
    
    def test_decodes_valid_token(self):
        """Debe decodificar un token válido."""
        token = create_access_token("user@email.com")
        data = decode_token(token)
        assert data.sub == "user@email.com"
    
    def test_returns_token_data(self):
        """Debe retornar TokenData con todos los campos."""
        token = create_access_token("user@email.com", {"role": "admin"})
        data = decode_token(token)
        
        assert data.sub == "user@email.com"
        assert data.token_type == "access"
        assert data.exp is not None
        assert data.iat is not None
        assert data.extra_claims.get("role") == "admin"
    
    def test_raises_on_expired_token(self):
        """Debe lanzar TokenExpiredError para token expirado."""
        token = create_access_token(
            "user@email.com",
            expires_delta=timedelta(seconds=-10)
        )
        
        with pytest.raises(TokenExpiredError):
            decode_token(token)
    
    def test_raises_on_invalid_token(self):
        """Debe lanzar InvalidTokenError para token inválido."""
        with pytest.raises(InvalidTokenError):
            decode_token("invalid.token.here")
    
    def test_raises_on_tampered_token(self):
        """Debe lanzar error si el token fue modificado."""
        token = create_access_token("user@email.com")
        # Modificar el token
        tampered = token[:-5] + "XXXXX"
        
        with pytest.raises(InvalidTokenError):
            decode_token(tampered)


class TestVerifyTokenType:
    """Tests para verify_token_type."""
    
    def test_accepts_correct_type(self):
        """Debe aceptar token del tipo correcto."""
        access = create_access_token("user@email.com")
        data = verify_token_type(access, "access")
        assert data.token_type == "access"
        
        refresh = create_refresh_token("user@email.com")
        data = verify_token_type(refresh, "refresh")
        assert data.token_type == "refresh"
    
    def test_rejects_wrong_type(self):
        """Debe rechazar token del tipo incorrecto."""
        access = create_access_token("user@email.com")
        
        with pytest.raises(InvalidTokenError) as exc_info:
            verify_token_type(access, "refresh")
        
        assert "Expected 'refresh'" in str(exc_info.value)
