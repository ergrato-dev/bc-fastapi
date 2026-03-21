# test_password.py
"""Tests para funciones de password."""

import pytest
from src.security.password import (
    hash_password,
    verify_password,
    validate_password_strength,
    PasswordStrength,
)


class TestHashPassword:
    """Tests para hash_password."""
    
    def test_hash_returns_string(self):
        """El hash debe ser un string."""
        result = hash_password("test_password")
        assert isinstance(result, str)
    
    def test_hash_starts_with_bcrypt_prefix(self):
        """El hash debe tener el prefijo de bcrypt."""
        result = hash_password("test_password")
        assert result.startswith("$2b$")
    
    def test_hash_is_different_each_time(self):
        """Cada hash debe ser único (salt diferente)."""
        hash1 = hash_password("same_password")
        hash2 = hash_password("same_password")
        assert hash1 != hash2
    
    def test_hash_has_correct_length(self):
        """El hash bcrypt debe tener 60 caracteres."""
        result = hash_password("test")
        assert len(result) == 60


class TestVerifyPassword:
    """Tests para verify_password."""
    
    def test_verify_correct_password(self):
        """Debe retornar True para password correcto."""
        hashed = hash_password("correct_password")
        assert verify_password("correct_password", hashed) is True
    
    def test_verify_incorrect_password(self):
        """Debe retornar False para password incorrecto."""
        hashed = hash_password("correct_password")
        assert verify_password("wrong_password", hashed) is False
    
    def test_verify_empty_password(self):
        """Debe manejar password vacío."""
        hashed = hash_password("some_password")
        assert verify_password("", hashed) is False
    
    def test_verify_with_special_characters(self):
        """Debe funcionar con caracteres especiales."""
        password = "P@$$w0rd!#%^&*()"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True


class TestValidatePasswordStrength:
    """Tests para validate_password_strength."""
    
    def test_weak_password_too_short(self):
        """Password muy corto es débil."""
        result = validate_password_strength("abc")
        assert result.is_valid is False
        assert result.strength == PasswordStrength.WEAK
        assert any("8 characters" in e for e in result.errors)
    
    def test_weak_password_no_uppercase(self):
        """Password sin mayúsculas es débil."""
        result = validate_password_strength("password123")
        assert result.is_valid is False
        assert any("uppercase" in e for e in result.errors)
    
    def test_weak_password_no_lowercase(self):
        """Password sin minúsculas es débil."""
        result = validate_password_strength("PASSWORD123")
        assert result.is_valid is False
        assert any("lowercase" in e for e in result.errors)
    
    def test_weak_password_no_digit(self):
        """Password sin números es débil."""
        result = validate_password_strength("PasswordABC")
        assert result.is_valid is False
        assert any("digit" in e for e in result.errors)
    
    def test_valid_password_meets_requirements(self):
        """Password que cumple requisitos mínimos es válido."""
        result = validate_password_strength("Password1")
        assert result.is_valid is True
        assert len(result.errors) == 0
    
    def test_strong_password_with_special_chars(self):
        """Password con caracteres especiales es más fuerte."""
        result = validate_password_strength("MyP@ssw0rd!")
        assert result.is_valid is True
        assert result.strength in [PasswordStrength.STRONG, PasswordStrength.VERY_STRONG]
    
    def test_very_strong_password(self):
        """Password largo y complejo es muy fuerte."""
        result = validate_password_strength("MyV3ryStr0ng!P@ssword")
        assert result.is_valid is True
        assert result.strength == PasswordStrength.VERY_STRONG
    
    def test_suggestions_for_improvement(self):
        """Debe sugerir mejoras para passwords válidos pero débiles."""
        result = validate_password_strength("Password1")
        # Debe sugerir caracteres especiales o más longitud
        assert len(result.suggestions) > 0
