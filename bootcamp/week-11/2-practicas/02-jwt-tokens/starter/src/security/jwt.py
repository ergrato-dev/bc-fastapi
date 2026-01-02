# jwt.py
"""
Utilidades para crear y validar JSON Web Tokens (JWT).

Este módulo proporciona funciones para:
- Crear access tokens de corta duración
- Crear refresh tokens de larga duración
- Decodificar y validar tokens
"""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt, JWTError, ExpiredSignatureError


# ============================================
# CONFIGURACIÓN
# ============================================

# Clave secreta para firmar tokens
# En producción, usar variable de entorno
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7


# ============================================
# PASO 1: Excepciones personalizadas
# ============================================
print("--- Paso 1: Excepciones personalizadas ---")

class TokenExpiredError(Exception):
    """Excepción cuando el token ha expirado."""
    pass


class InvalidTokenError(Exception):
    """Excepción cuando el token es inválido."""
    pass


# ============================================
# PASO 2: Dataclass para datos del token
# ============================================
print("--- Paso 2: TokenData dataclass ---")

@dataclass
class TokenData:
    """Datos extraídos de un token decodificado."""
    sub: str  # Subject (ID o email del usuario)
    exp: datetime  # Fecha de expiración
    iat: datetime  # Fecha de creación
    token_type: str  # "access" o "refresh"
    extra_claims: dict[str, Any]  # Claims adicionales


# ============================================
# PASO 3: Crear Access Token
# ============================================
print("--- Paso 3: Función create_access_token ---")

def create_access_token(
    subject: str,
    extra_claims: dict[str, Any] | None = None,
    expires_delta: timedelta | None = None,
) -> str:
    """
    Crea un JWT access token de corta duración.
    
    Args:
        subject: Identificador del usuario (email o ID)
        extra_claims: Claims adicionales (rol, permisos, etc.)
        expires_delta: Tiempo de expiración personalizado
        
    Returns:
        Token JWT codificado como string
        
    Example:
        >>> token = create_access_token("user@email.com", {"role": "admin"})
        >>> token.startswith("eyJ")
        True
    """
    # Calcular tiempo de expiración
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Descomenta las siguientes líneas:
    
    # # Construir payload con claims estándar
    # to_encode = {
    #     "sub": subject,           # Subject (quién es)
    #     "exp": expire,            # Expiration time
    #     "iat": datetime.now(timezone.utc),  # Issued at
    #     "type": "access",         # Tipo de token
    # }
    
    # # Agregar claims extra si los hay
    # if extra_claims:
    #     to_encode.update(extra_claims)
    
    # # Codificar y firmar el token
    # encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # return encoded_jwt
    
    # TODO: Implementar - eliminar esta línea
    raise NotImplementedError("Implementar create_access_token")


# ============================================
# PASO 4: Crear Refresh Token
# ============================================
print("--- Paso 4: Función create_refresh_token ---")

def create_refresh_token(
    subject: str,
    expires_delta: timedelta | None = None,
) -> str:
    """
    Crea un JWT refresh token de larga duración.
    
    Los refresh tokens tienen menos claims que los access tokens
    ya que solo se usan para obtener nuevos access tokens.
    
    Args:
        subject: Identificador del usuario
        expires_delta: Tiempo de expiración personalizado
        
    Returns:
        Token JWT codificado como string
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    # Descomenta las siguientes líneas:
    
    # to_encode = {
    #     "sub": subject,
    #     "exp": expire,
    #     "iat": datetime.now(timezone.utc),
    #     "type": "refresh",  # Diferente tipo que access
    # }
    
    # encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # return encoded_jwt
    
    # TODO: Implementar - eliminar esta línea
    raise NotImplementedError("Implementar create_refresh_token")


# ============================================
# PASO 5: Decodificar Token
# ============================================
print("--- Paso 5: Función decode_token ---")

def decode_token(token: str) -> TokenData:
    """
    Decodifica y valida un JWT.
    
    Verifica:
    - Firma válida
    - Token no expirado
    - Estructura correcta
    
    Args:
        token: Token JWT a decodificar
        
    Returns:
        TokenData con los datos extraídos
        
    Raises:
        TokenExpiredError: Si el token ha expirado
        InvalidTokenError: Si el token es inválido
        
    Example:
        >>> token = create_access_token("user@email.com")
        >>> data = decode_token(token)
        >>> data.sub
        'user@email.com'
    """
    # Descomenta las siguientes líneas:
    
    # try:
    #     # Decodificar token (verifica firma y expiración automáticamente)
    #     payload = jwt.decode(
    #         token,
    #         SECRET_KEY,
    #         algorithms=[ALGORITHM]
    #     )
        
    #     # Extraer claims estándar
    #     sub = payload.get("sub")
    #     if sub is None:
    #         raise InvalidTokenError("Token missing 'sub' claim")
        
    #     # Convertir timestamps a datetime
    #     exp = datetime.fromtimestamp(payload["exp"], tz=timezone.utc)
    #     iat = datetime.fromtimestamp(payload["iat"], tz=timezone.utc)
    #     token_type = payload.get("type", "access")
        
    #     # Claims extra (todo lo que no es estándar)
    #     standard_claims = {"sub", "exp", "iat", "type"}
    #     extra_claims = {k: v for k, v in payload.items() if k not in standard_claims}
        
    #     return TokenData(
    #         sub=sub,
    #         exp=exp,
    #         iat=iat,
    #         token_type=token_type,
    #         extra_claims=extra_claims,
    #     )
        
    # except ExpiredSignatureError:
    #     raise TokenExpiredError("Token has expired")
        
    # except JWTError as e:
    #     raise InvalidTokenError(f"Invalid token: {e}")
    
    # TODO: Implementar - eliminar esta línea
    raise NotImplementedError("Implementar decode_token")


# ============================================
# PASO 6: Verificar tipo de token
# ============================================
print("--- Paso 6: Función verify_token_type ---")

def verify_token_type(token: str, expected_type: str) -> TokenData:
    """
    Decodifica un token y verifica que sea del tipo esperado.
    
    Args:
        token: Token JWT
        expected_type: "access" o "refresh"
        
    Returns:
        TokenData si el tipo coincide
        
    Raises:
        InvalidTokenError: Si el tipo no coincide
    """
    # Descomenta las siguientes líneas:
    
    # data = decode_token(token)
    
    # if data.token_type != expected_type:
    #     raise InvalidTokenError(
    #         f"Expected '{expected_type}' token, got '{data.token_type}'"
    #     )
    
    # return data
    
    # TODO: Implementar - eliminar esta línea
    raise NotImplementedError("Implementar verify_token_type")


# ============================================
# PASO 7: Probar las funciones (opcional)
# ============================================
if __name__ == "__main__":
    print("\n=== Probando funciones JWT ===\n")
    
    # Test create_access_token
    try:
        token = create_access_token(
            "user@email.com",
            extra_claims={"role": "admin", "permissions": ["read", "write"]}
        )
        print(f"✅ Access token creado: {token[:50]}...")
    except NotImplementedError:
        print("❌ create_access_token no implementada")
    
    # Test create_refresh_token
    try:
        refresh = create_refresh_token("user@email.com")
        print(f"✅ Refresh token creado: {refresh[:50]}...")
    except NotImplementedError:
        print("❌ create_refresh_token no implementada")
    
    # Test decode_token
    try:
        token = create_access_token("test@test.com", {"role": "user"})
        data = decode_token(token)
        print(f"✅ Token decodificado: sub={data.sub}, type={data.token_type}")
        print(f"   Extra claims: {data.extra_claims}")
    except NotImplementedError:
        print("❌ decode_token no implementada")
    
    # Test token expirado
    try:
        expired_token = create_access_token(
            "user@email.com",
            expires_delta=timedelta(seconds=-1)  # Ya expirado
        )
        decode_token(expired_token)
        print("❌ Debería haber lanzado TokenExpiredError")
    except TokenExpiredError:
        print("✅ TokenExpiredError lanzado correctamente")
    except NotImplementedError:
        print("❌ Funciones no implementadas")
