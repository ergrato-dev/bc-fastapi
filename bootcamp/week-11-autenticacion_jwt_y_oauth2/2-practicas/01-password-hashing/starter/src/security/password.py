# password.py
"""
Utilidades para hashing y validación de contraseñas.

Este módulo proporciona funciones seguras para:
- Hashear contraseñas con bcrypt
- Verificar contraseñas
- Validar fortaleza de contraseñas
"""

from dataclasses import dataclass
from enum import Enum

from passlib.context import CryptContext


# ============================================
# PASO 1: Configurar el contexto de passlib
# ============================================
print("--- Paso 1: Configurar CryptContext ---")

# CryptContext es la clase principal de passlib para manejar hashing
# Configúrala para usar bcrypt como algoritmo principal

# Descomenta las siguientes líneas:
# pwd_context = CryptContext(
#     schemes=["bcrypt"],  # Algoritmo a usar
#     deprecated="auto"    # Marcar algoritmos viejos como deprecated
# )


# ============================================
# PASO 2: Función para hashear contraseñas
# ============================================
print("--- Paso 2: Función hash_password ---")

def hash_password(password: str) -> str:
    """
    Hashea una contraseña de forma segura usando bcrypt.
    
    bcrypt incluye automáticamente:
    - Salt único para cada hash
    - Work factor configurable (default 12)
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        Hash bcrypt de la contraseña
        
    Example:
        >>> hashed = hash_password("mi_password")
        >>> hashed.startswith("$2b$")
        True
    """
    # Descomenta la siguiente línea:
    # return pwd_context.hash(password)
    
    # TODO: Implementar - eliminar esta línea
    raise NotImplementedError("Implementar hash_password")


# ============================================
# PASO 3: Función para verificar contraseñas
# ============================================
print("--- Paso 3: Función verify_password ---")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con su hash.
    
    Esta función es timing-safe, lo que significa que toma
    el mismo tiempo sin importar si el password es correcto
    o incorrecto (previene timing attacks).
    
    Args:
        plain_password: Contraseña en texto plano a verificar
        hashed_password: Hash almacenado en la base de datos
        
    Returns:
        True si coinciden, False si no
        
    Example:
        >>> hashed = hash_password("secret")
        >>> verify_password("secret", hashed)
        True
        >>> verify_password("wrong", hashed)
        False
    """
    # Descomenta la siguiente línea:
    # return pwd_context.verify(plain_password, hashed_password)
    
    # TODO: Implementar - eliminar esta línea
    raise NotImplementedError("Implementar verify_password")


# ============================================
# PASO 4: Enum para niveles de fortaleza
# ============================================
print("--- Paso 4: Enum PasswordStrength ---")

class PasswordStrength(Enum):
    """Niveles de fortaleza de contraseña."""
    WEAK = "weak"
    FAIR = "fair"
    STRONG = "strong"
    VERY_STRONG = "very_strong"


# ============================================
# PASO 5: Dataclass para resultado de validación
# ============================================
print("--- Paso 5: Dataclass PasswordValidationResult ---")

@dataclass
class PasswordValidationResult:
    """Resultado de validación de contraseña."""
    is_valid: bool
    strength: PasswordStrength
    errors: list[str]
    suggestions: list[str]


# ============================================
# PASO 6: Función para validar fortaleza
# ============================================
print("--- Paso 6: Función validate_password_strength ---")

def validate_password_strength(password: str) -> PasswordValidationResult:
    """
    Valida la fortaleza de una contraseña.
    
    Criterios:
    - Mínimo 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un número
    - Caracteres especiales (mejora fortaleza)
    
    Args:
        password: Contraseña a validar
        
    Returns:
        PasswordValidationResult con detalles de la validación
        
    Example:
        >>> result = validate_password_strength("weak")
        >>> result.is_valid
        False
        >>> result.strength
        <PasswordStrength.WEAK: 'weak'>
    """
    errors: list[str] = []
    suggestions: list[str] = []
    score = 0
    
    # Descomenta y completa la validación:
    
    # # Verificar longitud mínima
    # if len(password) < 8:
    #     errors.append("Password must be at least 8 characters")
    # elif len(password) >= 12:
    #     score += 2
    #     if len(password) >= 16:
    #         score += 1
    # else:
    #     score += 1
    #     suggestions.append("Use 12+ characters for better security")
    
    # # Verificar mayúsculas
    # if not any(c.isupper() for c in password):
    #     errors.append("Password must contain at least one uppercase letter")
    # else:
    #     score += 1
    
    # # Verificar minúsculas
    # if not any(c.islower() for c in password):
    #     errors.append("Password must contain at least one lowercase letter")
    # else:
    #     score += 1
    
    # # Verificar números
    # if not any(c.isdigit() for c in password):
    #     errors.append("Password must contain at least one digit")
    # else:
    #     score += 1
    
    # # Verificar caracteres especiales
    # special_chars = "!@#$%^&*(),.?\":{}|<>-_=+[]\\;'/"
    # if any(c in special_chars for c in password):
    #     score += 2
    # else:
    #     suggestions.append("Add special characters (!@#$%...) for extra security")
    
    # # Determinar fortaleza basada en score y errores
    # if errors:
    #     strength = PasswordStrength.WEAK
    # elif score <= 3:
    #     strength = PasswordStrength.FAIR
    # elif score <= 5:
    #     strength = PasswordStrength.STRONG
    # else:
    #     strength = PasswordStrength.VERY_STRONG
    
    # return PasswordValidationResult(
    #     is_valid=len(errors) == 0,
    #     strength=strength,
    #     errors=errors,
    #     suggestions=suggestions,
    # )
    
    # TODO: Implementar - eliminar estas líneas
    raise NotImplementedError("Implementar validate_password_strength")


# ============================================
# PASO 7: Probar las funciones (opcional)
# ============================================
if __name__ == "__main__":
    print("\n=== Probando funciones de password ===\n")
    
    # Test hash_password
    try:
        hashed = hash_password("MySecureP@ssw0rd!")
        print(f"✅ Hash generado: {hashed[:30]}...")
    except NotImplementedError:
        print("❌ hash_password no implementada")
    
    # Test verify_password
    try:
        hashed = hash_password("test123")
        is_valid = verify_password("test123", hashed)
        print(f"✅ Verificación correcta: {is_valid}")
        
        is_invalid = verify_password("wrong", hashed)
        print(f"✅ Verificación incorrecta: {is_invalid}")
    except NotImplementedError:
        print("❌ verify_password no implementada")
    
    # Test validate_password_strength
    try:
        weak = validate_password_strength("123")
        print(f"✅ Password débil: {weak.strength.value}, errores: {len(weak.errors)}")
        
        strong = validate_password_strength("MyStr0ng!Pass")
        print(f"✅ Password fuerte: {strong.strength.value}, válido: {strong.is_valid}")
    except NotImplementedError:
        print("❌ validate_password_strength no implementada")
