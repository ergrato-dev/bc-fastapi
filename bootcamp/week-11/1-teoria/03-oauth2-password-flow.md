# 🔄 OAuth2 Password Flow en FastAPI

## 🎯 Objetivos de Aprendizaje

- Comprender el flujo OAuth2 Password (Resource Owner Password Credentials)
- Implementar el endpoint `/token` según especificación OAuth2
- Usar `OAuth2PasswordBearer` y `OAuth2PasswordRequestForm`
- Integrar autenticación en endpoints de FastAPI

---

## 📚 Contenido

### 1. ¿Qué es OAuth2?

![OAuth2 Flow](../0-assets/03-oauth2-flow.svg)

**OAuth2** es un estándar de autorización que define varios "flujos" para diferentes escenarios.

#### Flujos OAuth2

| Flow | Uso | Descripción |
|------|-----|-------------|
| **Password** | Apps propias | Usuario envía credenciales directamente |
| **Authorization Code** | Apps terceras | Redirección a proveedor (Google, GitHub) |
| **Client Credentials** | Machine-to-machine | Sin usuario, solo aplicaciones |
| **Implicit** | SPAs (deprecated) | Token en URL (inseguro) |

En esta semana nos enfocamos en **Password Flow** (también llamado Resource Owner Password Credentials).

### 2. OAuth2 Password Flow

#### Flujo Completo

```
┌─────────────────────────────────────────────────────────────────┐
│                    OAuth2 PASSWORD FLOW                         │
└─────────────────────────────────────────────────────────────────┘

  Cliente                                            Servidor
     │                                                  │
     │  1. POST /token                                  │
     │     Content-Type: application/x-www-form-urlencoded
     │     grant_type=password                          │
     │     username=user@email.com                      │
     │     password=secret123                           │
     │ ──────────────────────────────────────────────► │
     │                                                  │
     │                                    Validar credenciales
     │                                    Generar tokens
     │                                                  │
     │  2. 200 OK                                       │
     │     {                                            │
     │       "access_token": "eyJ...",                  │
     │       "token_type": "bearer",                    │
     │       "expires_in": 1800,                        │
     │       "refresh_token": "abc..."                  │
     │     }                                            │
     │ ◄────────────────────────────────────────────── │
     │                                                  │
     │  3. GET /users/me                                │
     │     Authorization: Bearer eyJ...                 │
     │ ──────────────────────────────────────────────► │
     │                                    Validar token │
     │  4. 200 OK                                       │
     │     { "id": 1, "email": "user@email.com" }      │
     │ ◄────────────────────────────────────────────── │
```

### 3. Implementación en FastAPI

#### 3.1 Configuración Básica

```python
# main.py
"""API con OAuth2 Password Flow."""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI(title="Auth API")

# Esquema OAuth2 - Define dónde está el endpoint de token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

#### 3.2 OAuth2PasswordBearer

Este es el componente que:
- Define la URL del endpoint de login (`tokenUrl`)
- Extrae el token del header `Authorization: Bearer <token>`
- Se integra con la documentación de Swagger

```python
from fastapi.security import OAuth2PasswordBearer

# tokenUrl es relativo a la raíz de la API
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# También puede incluir scopes (permisos)
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "read": "Read access",
        "write": "Write access",
        "admin": "Admin access"
    }
)
```

#### 3.3 OAuth2PasswordRequestForm

FastAPI proporciona este formulario que parsea automáticamente:
- `username` (requerido)
- `password` (requerido)
- `scope` (opcional)
- `grant_type` (opcional, por defecto "password")

```python
from fastapi.security import OAuth2PasswordRequestForm

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token endpoint.
    
    Recibe form data (NO JSON):
    - username: str
    - password: str
    - scope: str (opcional)
    - grant_type: str (opcional)
    """
    print(f"Username: {form_data.username}")
    print(f"Password: {form_data.password}")
    print(f"Scopes: {form_data.scopes}")  # Lista de strings
    ...
```

### 4. Endpoint de Token Completo

```python
# auth/router.py
"""Router de autenticación con OAuth2."""

from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from .security import (
    verify_password,
    create_access_token,
    create_refresh_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from .users import get_user_by_email


router = APIRouter(prefix="/auth", tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


class Token(BaseModel):
    """Respuesta del endpoint de token según OAuth2."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES * 60
    refresh_token: str | None = None


class TokenData(BaseModel):
    """Datos extraídos del token."""
    email: str | None = None


def authenticate_user(email: str, password: str):
    """
    Autentica un usuario con email y password.
    
    Returns:
        User si las credenciales son válidas
        None si no lo son
    """
    user = get_user_by_email(email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible token login.
    
    Endpoint que recibe credenciales y devuelve tokens.
    
    - **username**: Email del usuario (OAuth2 usa "username")
    - **password**: Contraseña del usuario
    
    Returns:
        Token con access_token y refresh_token
        
    Raises:
        401: Credenciales inválidas
    """
    # Autenticar usuario
    user = authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Crear tokens
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}
    )
    refresh_token = create_refresh_token(data={"sub": user.email})
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
    )
```

### 5. Obtener Usuario Actual

#### 5.1 Dependencia Básica

```python
from jose import jwt, JWTError

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
):
    """
    Dependencia que obtiene el usuario actual del token.
    
    Args:
        token: JWT extraído del header Authorization
        
    Returns:
        Usuario si el token es válido
        
    Raises:
        401: Token inválido o expirado
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decodificar token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        
        if email is None:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
    
    # Obtener usuario de la base de datos
    user = get_user_by_email(email)
    
    if user is None:
        raise credentials_exception
        
    return user
```

#### 5.2 Dependencia con Validación de Estado

```python
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """
    Verifica que el usuario esté activo.
    
    Raises:
        400: Usuario inactivo/deshabilitado
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user
```

#### 5.3 Dependencia de Admin

```python
async def get_current_admin_user(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    Verifica que el usuario sea administrador.
    
    Raises:
        403: Usuario no es admin
    """
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user
```

### 6. Proteger Endpoints

```python
# users/router.py
"""Endpoints de usuarios protegidos."""

from typing import Annotated

from fastapi import APIRouter, Depends

from auth.dependencies import (
    get_current_user,
    get_current_active_user,
    get_current_admin_user,
)
from .schemas import UserResponse


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    Obtiene el perfil del usuario autenticado.
    
    Requiere: Token válido de usuario activo
    """
    return current_user


@router.get("/me/items")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Lista los items del usuario actual."""
    return get_items_by_user(current_user.id)


@router.get("/", response_model=list[UserResponse])
async def list_all_users(
    current_user: Annotated[User, Depends(get_current_admin_user)]
):
    """
    Lista todos los usuarios (solo admin).
    
    Requiere: Token de usuario con rol admin
    """
    return get_all_users()
```

### 7. Estructura Completa

```python
# main.py
"""Aplicación principal con autenticación OAuth2."""

from fastapi import FastAPI

from auth.router import router as auth_router
from users.router import router as users_router

app = FastAPI(
    title="Auth Demo API",
    description="API con autenticación OAuth2 Password Flow",
)

# Incluir routers
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
async def root():
    """Endpoint público (no requiere autenticación)."""
    return {"message": "Welcome! Login at /auth/token"}
```

### 8. Probar con Swagger UI

FastAPI genera documentación interactiva con soporte OAuth2:

1. Ir a `/docs`
2. Click en el botón **Authorize** 🔓
3. Ingresar credenciales (username = email)
4. Click **Authorize**
5. Ahora los endpoints protegidos funcionarán

```
┌─────────────────────────────────────────┐
│           🔓 Authorize                  │
├─────────────────────────────────────────┤
│  OAuth2PasswordBearer (OAuth2, password)│
│                                         │
│  Token URL: /auth/token                 │
│                                         │
│  username: [user@email.com        ]     │
│  password: [••••••••••            ]     │
│                                         │
│  [ Authorize ]  [ Close ]               │
└─────────────────────────────────────────┘
```

### 9. Probar con cURL/HTTPie

```bash
# 1. Obtener token
curl -X POST "http://localhost:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@email.com&password=secret123"

# Respuesta:
# {
#   "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
#   "token_type": "bearer",
#   "expires_in": 1800
# }

# 2. Usar token en endpoint protegido
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."

# Con HTTPie (más legible)
http POST :8000/auth/token username=user@email.com password=secret123
http :8000/users/me "Authorization: Bearer eyJ..."
```

### 10. Manejo de Errores

```python
# auth/exceptions.py
"""Excepciones personalizadas de autenticación."""

from fastapi import HTTPException, status


class AuthenticationError(HTTPException):
    """Error de autenticación (401)."""
    
    def __init__(self, detail: str = "Could not validate credentials"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class AuthorizationError(HTTPException):
    """Error de autorización (403)."""
    
    def __init__(self, detail: str = "Not enough permissions"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )


class TokenExpiredError(AuthenticationError):
    """Token expirado."""
    
    def __init__(self):
        super().__init__(detail="Token has expired")


class InvalidTokenError(AuthenticationError):
    """Token inválido."""
    
    def __init__(self):
        super().__init__(detail="Invalid token")
```

---

## 💡 Puntos Clave

1. **OAuth2PasswordBearer** define dónde está `/token` y extrae el token
2. **OAuth2PasswordRequestForm** parsea el formulario de login
3. El token va en el header: `Authorization: Bearer <token>`
4. Usar **Depends()** para inyectar usuario actual
5. Swagger UI tiene soporte nativo para OAuth2

---

## 🔗 Recursos

- [FastAPI Security - OAuth2](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749)
- [OAuth 2.0 Simplified](https://www.oauth.com/)

---

## ✅ Checklist de Verificación

- [ ] Entiendo el flujo OAuth2 Password
- [ ] Sé usar `OAuth2PasswordBearer` y `OAuth2PasswordRequestForm`
- [ ] Puedo implementar el endpoint `/token`
- [ ] Sé crear dependencias para obtener usuario actual
- [ ] Puedo proteger endpoints con `Depends()`
