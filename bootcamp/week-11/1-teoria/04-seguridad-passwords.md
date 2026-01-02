# 🔒 Seguridad de Contraseñas

## 🎯 Objetivos de Aprendizaje

- Comprender por qué NO almacenar contraseñas en texto plano
- Conocer algoritmos de hashing seguros (bcrypt, argon2)
- Implementar hashing y verificación con passlib
- Aplicar mejores prácticas de seguridad en passwords

---

## 📚 Contenido

### 1. ¿Por Qué Hashear Contraseñas?

#### El Problema

```python
# ❌ NUNCA HACER ESTO
class User:
    email: str
    password: str  # "secret123" en texto plano

# Si alguien accede a la base de datos:
# - Ve TODAS las contraseñas
# - Puede usarlas en otros sitios (credential stuffing)
# - Violación de privacidad masiva
```

#### La Solución: Hashing

```python
# ✅ SIEMPRE HACER ESTO
class User:
    email: str
    hashed_password: str  # "$2b$12$..." (hash irreversible)

# Si alguien accede a la base de datos:
# - Solo ve hashes
# - No puede obtener la contraseña original
# - Cada hash es único (salt)
```

### 2. Hash vs Encriptación

| Aspecto | Hash | Encriptación |
|---------|------|--------------|
| **Dirección** | Unidireccional (irreversible) | Bidireccional (reversible) |
| **Clave** | No necesita clave para hashear | Necesita clave para encriptar/desencriptar |
| **Propósito** | Verificar integridad | Proteger confidencialidad |
| **Ejemplo** | bcrypt, argon2 | AES, RSA |

```
PASSWORD "secret123"
        │
        ▼
   ┌─────────┐
   │  HASH   │  ──► "$2b$12$LQv3c1..." (irreversible)
   └─────────┘
        ▲
        │
   No se puede
   revertir a
   "secret123"
```

### 3. Algoritmos de Hashing

#### ❌ NO Usar

```python
import hashlib

# MD5 - Roto, vulnerable a colisiones
hashlib.md5(b"password").hexdigest()

# SHA-1 - Obsoleto
hashlib.sha1(b"password").hexdigest()

# SHA-256 sin salt - Vulnerable a rainbow tables
hashlib.sha256(b"password").hexdigest()
```

**Problemas:**
- **Rápidos**: Permiten billones de intentos por segundo
- **Sin salt**: Mismo input = mismo output (rainbow tables)
- **Colisiones**: MD5/SHA1 tienen colisiones conocidas

#### ✅ Usar

| Algoritmo | Características | Recomendación |
|-----------|-----------------|---------------|
| **bcrypt** | Lento, salt incluido, configuratable | ✅ Estándar actual |
| **argon2** | Ganador PHC 2015, memory-hard | ✅ Más moderno |
| **scrypt** | Memory-hard, CPU-hard | ✅ Alternativa |
| **PBKDF2** | Estándar NIST, configurable | ⚠️ Aceptable |

### 4. bcrypt en Detalle

#### Características

```
$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.Txm5VhVv.wWbdi
 │  │  │                              │
 │  │  └── Salt (22 chars)            └── Hash (31 chars)
 │  └── Cost factor (2^12 = 4096 iteraciones)
 └── Versión del algoritmo
```

- **Salt automático**: Cada hash es único
- **Work factor configurable**: Más lento = más seguro
- **Timing-safe comparison**: Previene timing attacks

#### Work Factor

```python
# Work factor = 12 (default, recomendado)
# Tiempo: ~250ms por hash

# Work factor = 14
# Tiempo: ~1s por hash (más seguro, más lento)

# Regla: Aumentar work factor cuando el hardware mejore
# Meta: ~250ms por verificación
```

### 5. Implementación con passlib

#### Instalación

```bash
uv add passlib[bcrypt]
# O para argon2:
uv add passlib[argon2]
```

#### Configuración Básica

```python
# security/password.py
"""Utilidades para hashing de contraseñas."""

from passlib.context import CryptContext

# Configurar contexto con bcrypt
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Hashea una contraseña de forma segura.
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        Hash bcrypt de la contraseña
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica una contraseña contra su hash.
    
    Args:
        plain_password: Contraseña en texto plano
        hashed_password: Hash almacenado
        
    Returns:
        True si coinciden, False si no
    """
    return pwd_context.verify(plain_password, hashed_password)


# Ejemplo de uso
hashed = hash_password("mi_password_secreto")
print(hashed)
# $2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.Txm5VhVv.wWbdi

is_valid = verify_password("mi_password_secreto", hashed)
print(is_valid)  # True

is_valid = verify_password("password_incorrecto", hashed)
print(is_valid)  # False
```

#### Configuración Avanzada

```python
from passlib.context import CryptContext

pwd_context = CryptContext(
    # Algoritmos soportados (en orden de preferencia)
    schemes=["argon2", "bcrypt"],
    
    # Marcar algoritmos antiguos como deprecated
    deprecated="auto",
    
    # Configuración específica de bcrypt
    bcrypt__rounds=12,  # Work factor
    
    # Configuración de argon2
    argon2__memory_cost=65536,  # 64MB
    argon2__time_cost=3,        # 3 iteraciones
    argon2__parallelism=4,      # 4 threads
)
```

#### Rehashing Automático

```python
def verify_and_update_password(
    plain_password: str,
    hashed_password: str
) -> tuple[bool, str | None]:
    """
    Verifica password y actualiza hash si es necesario.
    
    Útil cuando cambias el work factor o algoritmo.
    
    Returns:
        (is_valid, new_hash or None)
    """
    is_valid = pwd_context.verify(plain_password, hashed_password)
    
    if is_valid:
        # Verificar si necesita rehash (algoritmo viejo, work factor bajo)
        needs_update = pwd_context.needs_update(hashed_password)
        
        if needs_update:
            new_hash = pwd_context.hash(plain_password)
            return True, new_hash
    
    return is_valid, None


# Uso en login
is_valid, new_hash = verify_and_update_password(password, user.hashed_password)

if is_valid:
    if new_hash:
        # Actualizar hash en la base de datos
        user.hashed_password = new_hash
        db.commit()
    return user
return None
```

### 6. Integración con Modelos

```python
# models/user.py
"""Modelo de usuario con password hasheado."""

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import validates

from database import Base
from security.password import hash_password


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    def set_password(self, password: str) -> None:
        """Establece la contraseña (hashea automáticamente)."""
        self.hashed_password = hash_password(password)
    
    def check_password(self, password: str) -> bool:
        """Verifica si la contraseña es correcta."""
        from security.password import verify_password
        return verify_password(password, self.hashed_password)


# Uso
user = User(email="user@email.com")
user.set_password("mi_password_secreto")  # Hashea automáticamente
db.add(user)
db.commit()

# Verificar
if user.check_password("mi_password_secreto"):
    print("Password correcto!")
```

### 7. Validación de Contraseñas

```python
# schemas/user.py
"""Schemas de validación para usuarios."""

import re
from pydantic import BaseModel, field_validator


class UserCreate(BaseModel):
    """Schema para crear usuario."""
    email: str
    password: str
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """
        Valida que la contraseña sea segura.
        
        Requisitos:
        - Mínimo 8 caracteres
        - Al menos una mayúscula
        - Al menos una minúscula
        - Al menos un número
        - Al menos un carácter especial
        """
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character")
        
        return v


class PasswordChange(BaseModel):
    """Schema para cambiar contraseña."""
    current_password: str
    new_password: str
    
    @field_validator("new_password")
    @classmethod
    def validate_new_password(cls, v: str, info) -> str:
        """Valida que la nueva contraseña sea diferente."""
        # Acceder a otros valores
        if "current_password" in info.data:
            if v == info.data["current_password"]:
                raise ValueError("New password must be different from current")
        
        # Reutilizar validación de UserCreate
        UserCreate.validate_password(v)
        return v
```

### 8. Función de Validación Reutilizable

```python
# security/validators.py
"""Validadores de seguridad."""

from dataclasses import dataclass
from enum import Enum


class PasswordStrength(Enum):
    """Niveles de fortaleza de contraseña."""
    WEAK = "weak"
    FAIR = "fair"
    STRONG = "strong"
    VERY_STRONG = "very_strong"


@dataclass
class PasswordValidationResult:
    """Resultado de validación de contraseña."""
    is_valid: bool
    strength: PasswordStrength
    errors: list[str]
    suggestions: list[str]


def validate_password_strength(password: str) -> PasswordValidationResult:
    """
    Valida la fortaleza de una contraseña.
    
    Returns:
        PasswordValidationResult con detalles
    """
    errors = []
    suggestions = []
    score = 0
    
    # Longitud
    if len(password) < 8:
        errors.append("Must be at least 8 characters")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
        suggestions.append("Use 12+ characters for better security")
    
    # Mayúsculas
    if not any(c.isupper() for c in password):
        errors.append("Must contain uppercase letter")
    else:
        score += 1
    
    # Minúsculas
    if not any(c.islower() for c in password):
        errors.append("Must contain lowercase letter")
    else:
        score += 1
    
    # Números
    if not any(c.isdigit() for c in password):
        errors.append("Must contain a digit")
    else:
        score += 1
    
    # Caracteres especiales
    special_chars = "!@#$%^&*(),.?\":{}|<>-_=+[]\\;'/"
    if not any(c in special_chars for c in password):
        suggestions.append("Add special characters for extra security")
    else:
        score += 2
    
    # Determinar fortaleza
    if errors:
        strength = PasswordStrength.WEAK
    elif score <= 3:
        strength = PasswordStrength.FAIR
    elif score <= 5:
        strength = PasswordStrength.STRONG
    else:
        strength = PasswordStrength.VERY_STRONG
    
    return PasswordValidationResult(
        is_valid=len(errors) == 0,
        strength=strength,
        errors=errors,
        suggestions=suggestions,
    )


# Uso
result = validate_password_strength("MyP@ssw0rd!")
print(f"Valid: {result.is_valid}")
print(f"Strength: {result.strength.value}")
print(f"Errors: {result.errors}")
print(f"Suggestions: {result.suggestions}")
```

### 9. Mejores Prácticas

#### ✅ Hacer

```python
# 1. Usar bcrypt o argon2
pwd_context = CryptContext(schemes=["bcrypt"])

# 2. Validar fortaleza de password
if len(password) < 8:
    raise ValueError("Password too short")

# 3. Usar timing-safe comparison (passlib lo hace automáticamente)
pwd_context.verify(plain, hashed)  # ✅

# 4. Almacenar solo el hash
user.hashed_password = hash_password(password)

# 5. Usar variables de entorno para secretos
PEPPER = os.getenv("PASSWORD_PEPPER")  # Secreto adicional opcional
```

#### ❌ Evitar

```python
# 1. MD5 o SHA sin salt
hashlib.md5(password.encode()).hexdigest()  # ❌

# 2. Comparación directa de strings
if hashed == expected:  # ❌ Vulnerable a timing attacks
    ...

# 3. Almacenar password en texto plano
user.password = password  # ❌ NUNCA

# 4. Hardcodear secretos
PEPPER = "my_secret_pepper"  # ❌

# 5. Logs con passwords
logger.info(f"Login attempt: {username}:{password}")  # ❌ NUNCA
```

---

## 💡 Puntos Clave

1. **NUNCA** almacenar contraseñas en texto plano
2. Usar **bcrypt** o **argon2** (NO MD5, SHA1, SHA256)
3. **passlib** maneja salt y timing-safe comparison automáticamente
4. Validar fortaleza de contraseña antes de almacenar
5. Considerar **rehashing** cuando cambies configuración

---

## 🔗 Recursos

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [passlib Documentation](https://passlib.readthedocs.io/)
- [How bcrypt Works](https://auth0.com/blog/hashing-in-action-understanding-bcrypt/)

---

## ✅ Checklist de Verificación

- [ ] Entiendo por qué hashear contraseñas
- [ ] Conozco la diferencia entre hash y encriptación
- [ ] Sé usar passlib con bcrypt
- [ ] Puedo validar fortaleza de contraseñas
- [ ] Entiendo qué es el work factor
