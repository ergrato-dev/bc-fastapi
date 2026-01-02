# 🔒 Seguridad de APIs con FastAPI

## 📋 Contenido

1. [Principios de Seguridad](#principios-de-seguridad)
2. [OWASP API Security Top 10](#owasp-api-security-top-10)
3. [CORS - Cross-Origin Resource Sharing](#cors---cross-origin-resource-sharing)
4. [Security Headers](#security-headers)
5. [Prevención de Ataques Comunes](#prevención-de-ataques-comunes)
6. [Validación y Sanitización](#validación-y-sanitización)
7. [Mejores Prácticas](#mejores-prácticas)

---

## Principios de Seguridad

### Defensa en Profundidad

No confíes en una sola capa de seguridad. Implementa múltiples capas:

![Security Layers](../0-assets/02-security-layers.svg)

```
┌─────────────────────────────────────────────────────────┐
│                    CAPAS DE SEGURIDAD                    │
├─────────────────────────────────────────────────────────┤
│  1. Rate Limiting      - Previene abusos                │
│  2. Authentication     - Verifica identidad              │
│  3. Authorization      - Verifica permisos               │
│  4. Input Validation   - Valida datos de entrada         │
│  5. Security Headers   - Protege el navegador            │
│  6. Logging/Monitoring - Detecta anomalías               │
└─────────────────────────────────────────────────────────┘
```

### Principio de Mínimo Privilegio

> Un usuario/proceso solo debe tener los permisos mínimos necesarios.

```python
# ❌ MAL: Permisos amplios
@app.get("/admin/users")
async def get_all_users(current_user: User = Depends(get_current_user)):
    # Cualquier usuario autenticado puede ver todos los usuarios
    return await get_all_users_from_db()


# ✅ BIEN: Verificar rol específico
@app.get("/admin/users")
async def get_all_users(
    current_user: User = Depends(get_current_admin_user)  # Solo admins
):
    return await get_all_users_from_db()
```

### Fail Secure

> En caso de error, el sistema debe fallar de forma segura.

```python
# ❌ MAL: En error, permite acceso
async def verify_permission(user: User, resource: str) -> bool:
    try:
        return await check_permission(user, resource)
    except Exception:
        return True  # 💥 Error = acceso permitido


# ✅ BIEN: En error, deniega acceso
async def verify_permission(user: User, resource: str) -> bool:
    try:
        return await check_permission(user, resource)
    except Exception:
        logger.error("Error verificando permisos")
        return False  # ✅ Error = acceso denegado
```

---

## OWASP API Security Top 10

OWASP (Open Web Application Security Project) define los 10 riesgos más críticos:

### 1. Broken Object Level Authorization (BOLA)

El atacante accede a objetos de otros usuarios manipulando IDs.

```python
# ❌ VULNERABLE
@app.get("/users/{user_id}/data")
async def get_user_data(user_id: int):
    # Cualquiera puede acceder a datos de cualquier usuario
    return await db.get_user_data(user_id)


# ✅ SEGURO
@app.get("/users/{user_id}/data")
async def get_user_data(
    user_id: int,
    current_user: User = Depends(get_current_user)
):
    # Verificar que el usuario actual puede acceder
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    return await db.get_user_data(user_id)
```

### 2. Broken Authentication

Implementación deficiente de autenticación.

```python
# ✅ Buenas prácticas de autenticación
from passlib.context import CryptContext
from datetime import timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashear passwords correctamente
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Tokens con expiración corta
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # No días ni semanas

# Refresh tokens para renovar acceso
REFRESH_TOKEN_EXPIRE_DAYS = 7
```

### 3. Broken Object Property Level Authorization

Exposición de propiedades sensibles en respuestas.

```python
from pydantic import BaseModel, EmailStr

# ❌ VULNERABLE: Expone todo
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    password_hash: str  # 💥 Nunca exponer!
    is_admin: bool
    api_key: str  # 💥 Nunca exponer!


# ✅ SEGURO: Solo lo necesario
class UserPublicResponse(BaseModel):
    id: int
    email: EmailStr
    # Sin campos sensibles

class UserAdminResponse(UserPublicResponse):
    is_admin: bool
    created_at: datetime
    # api_key y password_hash NUNCA se exponen
```

### 4. Unrestricted Resource Consumption

Sin límites en recursos consumidos.

```python
# ❌ VULNERABLE
@app.get("/search")
async def search(query: str):
    # Sin límite de resultados
    return await db.search(query)


# ✅ SEGURO
@app.get("/search")
@limiter.limit("30/minute")  # Rate limiting
async def search(
    request: Request,
    query: str,
    limit: int = Query(default=20, le=100),  # Máximo 100 resultados
    offset: int = Query(default=0, ge=0)
):
    return await db.search(query, limit=limit, offset=offset)
```

### 5. Broken Function Level Authorization

Endpoints sensibles sin protección adecuada.

```python
# ❌ VULNERABLE
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Cualquiera puede eliminar usuarios!
    return await db.delete_user(user_id)


# ✅ SEGURO
@app.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    current_user: User = Depends(require_admin_role)  # Solo admins
):
    return await db.delete_user(user_id)
```

---

## CORS - Cross-Origin Resource Sharing

CORS controla qué dominios pueden acceder a tu API desde el navegador.

### ¿Por qué es necesario?

```
Sin CORS (bloqueado por navegador):
┌─────────────────┐          ┌─────────────────┐
│  evil-site.com  │ ───X───▶ │  tu-api.com     │
│  (JavaScript)   │          │                 │
└─────────────────┘          └─────────────────┘
        El navegador bloquea la request

Con CORS configurado:
┌─────────────────┐          ┌─────────────────┐
│  tu-frontend.com│ ───────▶ │  tu-api.com     │
│  (JavaScript)   │          │  Origin: OK ✅   │
└─────────────────┘          └─────────────────┘
```

### Configuración en FastAPI

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ❌ MAL: Permitir todo (solo para desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 💥 Peligroso en producción!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ BIEN: Orígenes específicos
ALLOWED_ORIGINS = [
    "https://mi-frontend.com",
    "https://admin.mi-frontend.com",
]

# En desarrollo, agregar localhost
if settings.environment == "development":
    ALLOWED_ORIGINS.extend([
        "http://localhost:3000",
        "http://localhost:5173",
    ])

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=600,  # Cache preflight por 10 minutos
)
```

### Opciones de CORS

| Opción | Descripción | Recomendación |
|--------|-------------|---------------|
| `allow_origins` | Dominios permitidos | Lista específica |
| `allow_credentials` | Permitir cookies | `True` si usas cookies |
| `allow_methods` | Métodos HTTP | Solo los necesarios |
| `allow_headers` | Headers permitidos | Solo los necesarios |
| `expose_headers` | Headers visibles al cliente | X-Custom-Headers |
| `max_age` | Cache de preflight | 600 segundos |

---

## Security Headers

Headers HTTP que instruyen al navegador sobre políticas de seguridad.

### Usando la librería `secure`

```bash
uv add secure
```

```python
# src/middleware/security.py
import secure
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

# Configurar headers de seguridad
secure_headers = secure.Secure(
    # Content Security Policy
    csp=secure.ContentSecurityPolicy()
        .default_src("'self'")
        .script_src("'self'")
        .style_src("'self'", "'unsafe-inline'")
        .img_src("'self'", "data:", "https:"),
    
    # HTTP Strict Transport Security
    hsts=secure.StrictTransportSecurity()
        .max_age(31536000)
        .include_subdomains(),
    
    # Otros headers
    referrer=secure.ReferrerPolicy().no_referrer_when_downgrade(),
    cache=secure.CacheControl().no_store(),
    xxp=secure.XXSSProtection().set("1; mode=block"),
)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        secure_headers.framework.fastapi(response)
        return response


# Aplicar middleware
app.add_middleware(SecurityHeadersMiddleware)
```

### Headers Importantes

#### 1. Content-Security-Policy (CSP)

Controla qué recursos puede cargar la página.

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'
```

#### 2. Strict-Transport-Security (HSTS)

Fuerza HTTPS.

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

#### 3. X-Content-Type-Options

Previene MIME type sniffing.

```http
X-Content-Type-Options: nosniff
```

#### 4. X-Frame-Options

Previene clickjacking.

```http
X-Frame-Options: DENY
```

#### 5. X-XSS-Protection

Filtro XSS del navegador (legacy pero útil).

```http
X-XSS-Protection: 1; mode=block
```

### Implementación Manual

```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        
        # Security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
        
        # HSTS (solo en producción con HTTPS)
        if request.url.scheme == "https":
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains"
            )
        
        return response


app.add_middleware(SecurityHeadersMiddleware)
```

---

## Prevención de Ataques Comunes

### 1. SQL Injection

**Ya prevenido con SQLAlchemy ORM**, pero cuidado con raw queries.

```python
# ❌ VULNERABLE
@app.get("/search")
async def search(query: str):
    # SQL directo con interpolación de strings
    result = await db.execute(f"SELECT * FROM users WHERE name = '{query}'")
    return result


# ✅ SEGURO: Usar ORM
@app.get("/search")
async def search(query: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(User).where(User.name == query)  # SQLAlchemy maneja el escape
    )
    return result.scalars().all()


# ✅ SEGURO: Queries parametrizadas si necesitas raw SQL
@app.get("/search")
async def search(query: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        text("SELECT * FROM users WHERE name = :name"),
        {"name": query}  # Parámetro, no interpolación
    )
    return result.fetchall()
```

### 2. XSS (Cross-Site Scripting)

```python
from fastapi.responses import HTMLResponse
from markupsafe import escape  # o html.escape

# ❌ VULNERABLE
@app.get("/greet", response_class=HTMLResponse)
async def greet(name: str):
    # Si name = "<script>alert('XSS')</script>"
    return f"<h1>Hola {name}!</h1>"  # 💥 Ejecuta script!


# ✅ SEGURO: Escapar contenido
@app.get("/greet", response_class=HTMLResponse)
async def greet(name: str):
    safe_name = escape(name)  # Escapa caracteres HTML
    return f"<h1>Hola {safe_name}!</h1>"
```

### 3. CSRF (Cross-Site Request Forgery)

Para APIs REST con JWT, CSRF es menos problemático. Si usas cookies de sesión:

```python
from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel

class CsrfSettings(BaseModel):
    secret_key: str = "your-secret-key"

@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


@app.post("/transfer")
async def transfer(
    amount: float,
    csrf_protect: CsrfProtect = Depends()
):
    await csrf_protect.validate_csrf()
    # Procesar transferencia
    return {"status": "ok"}
```

### 4. Mass Assignment

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    name: str
    is_admin: bool = False
    balance: float = 0.0

# ❌ VULNERABLE: Acepta cualquier campo
@app.put("/users/{user_id}")
async def update_user(user_id: int, data: dict):
    # Usuario puede enviar {"is_admin": true, "balance": 1000000}
    return await db.update_user(user_id, **data)


# ✅ SEGURO: Schema específico para update
class UserUpdate(BaseModel):
    email: str | None = None
    name: str | None = None
    # is_admin y balance NO están aquí

@app.put("/users/{user_id}")
async def update_user(user_id: int, data: UserUpdate):
    # Solo puede actualizar email y name
    return await db.update_user(user_id, **data.model_dump(exclude_unset=True))
```

---

## Validación y Sanitización

### Validación con Pydantic

```python
from pydantic import BaseModel, Field, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    email: EmailStr  # Validación de email automática
    
    password: str = Field(..., min_length=8, max_length=128)
    
    username: str = Field(..., min_length=3, max_length=30)
    
    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        # Solo letras, números y guiones bajos
        if not re.match(r"^[a-zA-Z0-9_]+$", v):
            raise ValueError("Username solo puede contener letras, números y _")
        return v
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password debe contener al menos una mayúscula")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password debe contener al menos una minúscula")
        if not re.search(r"\d", v):
            raise ValueError("Password debe contener al menos un número")
        return v
```

### Validación de Parámetros de Query

```python
from fastapi import Query, Path

@app.get("/items/{item_id}")
async def get_item(
    item_id: int = Path(..., gt=0, le=1000000),  # ID válido
    skip: int = Query(0, ge=0, le=1000),  # Paginación limitada
    limit: int = Query(20, ge=1, le=100),  # Máximo 100 items
    search: str | None = Query(None, max_length=100)  # Búsqueda limitada
):
    pass
```

---

## Mejores Prácticas

### 1. Manejo Seguro de Errores

```python
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

# ❌ MAL: Expone información interna
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc),  # 💥 Puede exponer SQL, paths, etc.
            "traceback": traceback.format_exc()  # 💥 Nunca!
        }
    )


# ✅ BIEN: Respuesta genérica, log interno
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    # Loggear el error completo internamente
    logger.exception(f"Unhandled error: {exc}")
    
    # Respuesta genérica al cliente
    return JSONResponse(
        status_code=500,
        content={
            "error": "internal_server_error",
            "message": "An unexpected error occurred"
        }
    )
```

### 2. Variables de Entorno Seguras

```python
from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    # Nunca valores por defecto para secrets en producción
    database_url: SecretStr  # Requerido
    secret_key: SecretStr  # Requerido
    
    # Secrets se acceden con .get_secret_value()
    debug: bool = False  # False por defecto en producción
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

settings = Settings()

# Uso
db_url = settings.database_url.get_secret_value()
```

### 3. Checklist de Seguridad

```markdown
## Pre-deployment Security Checklist

### Autenticación
- [ ] Passwords hasheados con bcrypt/argon2
- [ ] Tokens JWT con expiración corta
- [ ] Refresh tokens implementados
- [ ] Rate limiting en login/register

### Autorización
- [ ] Verificación de ownership en cada endpoint
- [ ] Roles y permisos implementados
- [ ] Principio de mínimo privilegio

### Validación
- [ ] Input validado con Pydantic
- [ ] Output filtrado (sin datos sensibles)
- [ ] Límites en queries (paginación)

### Headers
- [ ] CORS configurado con orígenes específicos
- [ ] Security headers implementados
- [ ] HSTS habilitado (con HTTPS)

### Configuración
- [ ] DEBUG=False en producción
- [ ] Secrets en variables de entorno
- [ ] Logs sin información sensible

### Infraestructura
- [ ] HTTPS obligatorio
- [ ] Rate limiting global
- [ ] Health checks implementados
```

---

## 📚 Resumen

| Área | Herramienta/Práctica |
|------|---------------------|
| **CORS** | CORSMiddleware con orígenes específicos |
| **Headers** | secure library o middleware manual |
| **Validación** | Pydantic schemas estrictos |
| **SQL Injection** | SQLAlchemy ORM (nunca raw queries) |
| **XSS** | Escapar output HTML |
| **BOLA** | Verificar ownership en cada request |
| **Errores** | Respuestas genéricas, logs detallados |

---

## 🔗 Recursos

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)

---

*Siguiente: [03 - Logging Estructurado](03-logging-estructurado.md)*
