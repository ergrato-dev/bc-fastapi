# 🎫 JSON Web Tokens (JWT) en Profundidad

## 🎯 Objetivos de Aprendizaje

- Comprender la estructura de un JWT (Header, Payload, Signature)
- Conocer los claims estándar y personalizados
- Entender los algoritmos de firma (HS256, RS256)
- Implementar creación y validación de JWT con Python

---

## 📚 Contenido

### 1. ¿Qué es un JWT?

![JWT Structure](../0-assets/02-jwt-structure.svg)

**JSON Web Token (JWT)** es un estándar abierto (RFC 7519) que define una forma compacta y autocontenida de transmitir información entre partes como un objeto JSON firmado.

#### Características Clave

| Característica | Descripción |
|----------------|-------------|
| **Compacto** | Pequeño tamaño, ideal para URLs y headers |
| **Autocontenido** | Contiene toda la información necesaria |
| **Firmado** | Garantiza integridad y autenticidad |
| **Stateless** | No requiere almacenamiento en servidor |

#### Ejemplo de JWT

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.
POstGetfAytaZS82wHcjoTyoqhMyxXiWdR7Nn7A28cM
```

Las tres partes separadas por puntos (`.`):
1. **Header** (rojo)
2. **Payload** (púrpura)
3. **Signature** (azul)

### 2. Estructura del JWT

#### 2.1 Header

Contiene metadatos sobre el token.

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

| Campo | Descripción |
|-------|-------------|
| `alg` | Algoritmo de firma (HS256, RS256, etc.) |
| `typ` | Tipo de token (siempre "JWT") |

#### 2.2 Payload (Claims)

Contiene los datos (claims) del token.

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin",
  "iat": 1516239022,
  "exp": 1516242622
}
```

##### Claims Registrados (Estándar)

| Claim | Nombre | Descripción |
|-------|--------|-------------|
| `iss` | Issuer | Quién emitió el token |
| `sub` | Subject | ID del usuario/entidad |
| `aud` | Audience | Destinatario del token |
| `exp` | Expiration | Cuándo expira (timestamp) |
| `nbf` | Not Before | Válido desde (timestamp) |
| `iat` | Issued At | Cuándo se creó (timestamp) |
| `jti` | JWT ID | Identificador único del token |

##### Claims Personalizados

Puedes agregar cualquier dato adicional:

```json
{
  "sub": "user123",
  "email": "user@example.com",
  "role": "admin",
  "permissions": ["read", "write", "delete"],
  "department": "engineering"
}
```

**⚠️ Cuidado:** No incluir información sensible (passwords, datos personales críticos) ya que el payload es solo codificado en Base64, NO encriptado.

#### 2.3 Signature

La firma garantiza que el token no ha sido modificado.

```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret_key
)
```

### 3. Algoritmos de Firma

#### 3.1 HS256 (Symmetric)

Usa la misma clave para firmar y verificar.

```python
# Una sola clave secreta (compartida)
SECRET_KEY = "mi_clave_secreta_muy_larga_y_segura"

# Firmar
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Verificar (misma clave)
decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
```

**✅ Ventajas:**
- Simple de implementar
- Rápido

**❌ Desventajas:**
- La clave debe compartirse con quien verifique
- Si se compromete, todos los tokens son vulnerables

#### 3.2 RS256 (Asymmetric)

Usa un par de claves: privada para firmar, pública para verificar.

```python
# Par de claves
PRIVATE_KEY = open("private.pem").read()  # Solo el servidor
PUBLIC_KEY = open("public.pem").read()    # Puede compartirse

# Firmar (clave privada)
token = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")

# Verificar (clave pública)
decoded = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
```

**✅ Ventajas:**
- Clave pública puede compartirse sin riesgo
- Ideal para microservicios

**❌ Desventajas:**
- Más lento
- Más complejo de configurar

#### Comparación

| Aspecto | HS256 | RS256 |
|---------|-------|-------|
| **Tipo** | Simétrico | Asimétrico |
| **Claves** | 1 (secreta) | 2 (privada + pública) |
| **Velocidad** | Rápido | Más lento |
| **Uso** | Apps simples | Microservicios |
| **Seguridad** | Buena | Mejor |

### 4. Implementación con Python

#### 4.1 Instalación

```bash
uv add python-jose[cryptography]
# O alternativamente:
uv add pyjwt
```

#### 4.2 Crear JWT

```python
# security/jwt.py
"""Utilidades para manejo de JWT."""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt, JWTError

# Configuración
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None
) -> str:
    """
    Crea un JWT access token.
    
    Args:
        data: Datos a incluir en el payload
        expires_delta: Tiempo de expiración personalizado
        
    Returns:
        Token JWT codificado
    """
    to_encode = data.copy()
    
    # Calcular expiración
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Agregar claims estándar
    to_encode.update({
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    })
    
    # Codificar y firmar
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Ejemplo de uso
token = create_access_token(
    data={
        "sub": "user@example.com",
        "role": "admin"
    }
)
print(token)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW...
```

#### 4.3 Validar y Decodificar JWT

```python
from jose import jwt, JWTError, ExpiredSignatureError


def decode_token(token: str) -> dict[str, Any] | None:
    """
    Decodifica y valida un JWT.
    
    Args:
        token: Token JWT a validar
        
    Returns:
        Payload decodificado si es válido
        None si es inválido
        
    Raises:
        JWTError: Si el token es inválido
        ExpiredSignatureError: Si el token expiró
    """
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
        
    except ExpiredSignatureError:
        # Token expirado
        raise ValueError("Token has expired")
        
    except JWTError as e:
        # Token inválido (firma incorrecta, formato malo, etc.)
        raise ValueError(f"Invalid token: {e}")


# Ejemplo de uso
try:
    payload = decode_token(token)
    print(f"User: {payload['sub']}")
    print(f"Role: {payload['role']}")
    print(f"Expires: {payload['exp']}")
except ValueError as e:
    print(f"Error: {e}")
```

#### 4.4 Clase Completa de JWT

```python
# security/jwt_handler.py
"""Handler completo para JWT."""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any
import os

from jose import jwt, JWTError, ExpiredSignatureError


@dataclass
class TokenData:
    """Datos extraídos de un token."""
    sub: str
    exp: datetime
    iat: datetime
    role: str | None = None
    
    @property
    def is_expired(self) -> bool:
        """Verifica si el token ha expirado."""
        return datetime.now(timezone.utc) > self.exp


class JWTHandler:
    """Maneja creación y validación de JWT."""
    
    def __init__(
        self,
        secret_key: str | None = None,
        algorithm: str = "HS256",
        access_token_expire_minutes: int = 30,
        refresh_token_expire_days: int = 7,
    ):
        self.secret_key = secret_key or os.getenv("JWT_SECRET_KEY")
        if not self.secret_key:
            raise ValueError("JWT_SECRET_KEY is required")
            
        self.algorithm = algorithm
        self.access_expire = timedelta(minutes=access_token_expire_minutes)
        self.refresh_expire = timedelta(days=refresh_token_expire_days)
    
    def create_access_token(
        self,
        subject: str,
        extra_claims: dict[str, Any] | None = None,
    ) -> str:
        """Crea un access token de corta duración."""
        claims = {
            "sub": subject,
            "type": "access",
            "exp": datetime.now(timezone.utc) + self.access_expire,
            "iat": datetime.now(timezone.utc),
        }
        if extra_claims:
            claims.update(extra_claims)
            
        return jwt.encode(claims, self.secret_key, algorithm=self.algorithm)
    
    def create_refresh_token(self, subject: str) -> str:
        """Crea un refresh token de larga duración."""
        claims = {
            "sub": subject,
            "type": "refresh",
            "exp": datetime.now(timezone.utc) + self.refresh_expire,
            "iat": datetime.now(timezone.utc),
        }
        return jwt.encode(claims, self.secret_key, algorithm=self.algorithm)
    
    def decode_token(self, token: str) -> TokenData:
        """
        Decodifica y valida un token.
        
        Raises:
            ValueError: Si el token es inválido o expiró
        """
        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm]
            )
            return TokenData(
                sub=payload["sub"],
                exp=datetime.fromtimestamp(payload["exp"], tz=timezone.utc),
                iat=datetime.fromtimestamp(payload["iat"], tz=timezone.utc),
                role=payload.get("role"),
            )
        except ExpiredSignatureError:
            raise ValueError("Token has expired")
        except JWTError as e:
            raise ValueError(f"Invalid token: {e}")
    
    def verify_token_type(self, token: str, expected_type: str) -> TokenData:
        """Verifica que el token sea del tipo esperado."""
        payload = jwt.decode(
            token,
            self.secret_key,
            algorithms=[self.algorithm]
        )
        if payload.get("type") != expected_type:
            raise ValueError(f"Expected {expected_type} token")
        return self.decode_token(token)


# Uso
jwt_handler = JWTHandler(secret_key="mi_clave_secreta")

# Crear tokens
access = jwt_handler.create_access_token("user@email.com", {"role": "admin"})
refresh = jwt_handler.create_refresh_token("user@email.com")

# Validar
data = jwt_handler.decode_token(access)
print(f"User: {data.sub}, Role: {data.role}")
```

### 5. Decodificar sin Verificar (Debug)

Útil para debugging, pero **NUNCA** usar en producción sin verificar firma.

```python
import base64
import json


def decode_jwt_without_verification(token: str) -> dict:
    """
    Decodifica un JWT SIN verificar la firma.
    
    ⚠️ SOLO USAR PARA DEBUGGING
    """
    # Separar las partes
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Invalid JWT format")
    
    # Decodificar header y payload (agregar padding si es necesario)
    def decode_part(part: str) -> dict:
        # Agregar padding para Base64
        padding = 4 - len(part) % 4
        if padding != 4:
            part += "=" * padding
        decoded = base64.urlsafe_b64decode(part)
        return json.loads(decoded)
    
    return {
        "header": decode_part(parts[0]),
        "payload": decode_part(parts[1]),
        # La firma no se puede decodificar como JSON
    }


# Ejemplo
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGVtYWlsLmNvbSJ9.xxx"
decoded = decode_jwt_without_verification(token)
print(json.dumps(decoded, indent=2))
# {
#   "header": {"alg": "HS256", "typ": "JWT"},
#   "payload": {"sub": "user@email.com"}
# }
```

### 6. Buenas Prácticas

#### ✅ Hacer

```python
# 1. Usar expiración corta para access tokens
ACCESS_TOKEN_EXPIRE = timedelta(minutes=15)  # 15-30 minutos

# 2. Validar el algoritmo explícitamente
jwt.decode(token, key, algorithms=["HS256"])  # Especificar algoritmo

# 3. Incluir tipo de token para evitar confusiones
{"sub": "user", "type": "access"}  # vs "refresh"

# 4. Usar claims estándar
{"sub": "user_id", "exp": timestamp, "iat": timestamp}

# 5. Clave secreta fuerte y desde variable de entorno
SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Mínimo 256 bits
```

#### ❌ Evitar

```python
# 1. Tokens sin expiración
{"sub": "user"}  # ❌ Sin "exp"

# 2. Información sensible en payload
{"password": "123456", "ssn": "123-45-6789"}  # ❌ NUNCA

# 3. Clave secreta débil o hardcodeada
SECRET_KEY = "secret"  # ❌ Muy corta
SECRET_KEY = "mi_clave"  # ❌ Hardcodeada

# 4. Aceptar cualquier algoritmo
jwt.decode(token, key, algorithms=jwt.ALGORITHMS)  # ❌ Peligroso

# 5. Ignorar errores de validación
try:
    jwt.decode(token, key, algorithms=["HS256"])
except:
    pass  # ❌ Silenciar errores
```

---

## 💡 Puntos Clave

1. **JWT = Header.Payload.Signature** (3 partes Base64)
2. **El payload NO está encriptado**, solo codificado
3. **La firma garantiza integridad**, no confidencialidad
4. **HS256** usa una clave, **RS256** usa par de claves
5. **Siempre validar** `exp`, `algorithm`, y la firma

---

## 🔗 Recursos

- [JWT.io](https://jwt.io/) - Debugger interactivo
- [RFC 7519](https://tools.ietf.org/html/rfc7519) - Especificación JWT
- [python-jose Documentation](https://python-jose.readthedocs.io/)

---

## ✅ Checklist de Verificación

- [ ] Entiendo las 3 partes de un JWT
- [ ] Conozco los claims estándar (sub, exp, iat)
- [ ] Sé la diferencia entre HS256 y RS256
- [ ] Puedo crear y validar JWT con python-jose
- [ ] Comprendo que el payload no está encriptado
