# 🔐 Fundamentos de Autenticación

## 🎯 Objetivos de Aprendizaje

- Comprender la diferencia entre autenticación y autorización
- Conocer los métodos de autenticación más comunes
- Entender las amenazas de seguridad en autenticación
- Identificar las mejores prácticas de seguridad

---

## 📚 Contenido

### 1. Autenticación vs Autorización

![Auth Overview](../0-assets/01-auth-overview.svg)

Estos dos conceptos se confunden frecuentemente, pero son fundamentalmente diferentes:

#### Autenticación (AuthN)

**"¿Quién eres?"**

El proceso de verificar la identidad de un usuario o sistema.

```python
# Ejemplo conceptual de autenticación
def authenticate(username: str, password: str) -> User | None:
    """
    Verifica si el usuario es quien dice ser.
    
    Returns:
        User si las credenciales son válidas
        None si no lo son
    """
    user = get_user_by_username(username)
    if user and verify_password(password, user.hashed_password):
        return user  # ✅ Identidad verificada
    return None  # ❌ Credenciales inválidas
```

#### Autorización (AuthZ)

**"¿Qué puedes hacer?"**

El proceso de determinar qué acciones puede realizar un usuario autenticado.

```python
# Ejemplo conceptual de autorización
def authorize(user: User, resource: str, action: str) -> bool:
    """
    Verifica si el usuario tiene permiso para realizar la acción.
    
    Returns:
        True si tiene permiso
        False si no lo tiene
    """
    # El usuario ya está autenticado, ahora verificamos permisos
    if action == "delete" and user.role != "admin":
        return False  # ❌ Solo admins pueden eliminar
    return True  # ✅ Acción permitida
```

#### Comparación

| Aspecto | Autenticación | Autorización |
|---------|---------------|--------------|
| **Pregunta** | ¿Quién eres? | ¿Qué puedes hacer? |
| **Cuándo** | Primero | Después de autenticar |
| **Datos** | Credenciales | Permisos/Roles |
| **Ejemplo** | Login con password | Acceso a recurso |
| **Error HTTP** | 401 Unauthorized | 403 Forbidden |

### 2. Métodos de Autenticación

#### 2.1 Basic Authentication

El método más simple: enviar usuario y contraseña en cada request.

```http
GET /api/users HTTP/1.1
Authorization: Basic dXNlcjpwYXNzd29yZA==
```

El valor es `base64(username:password)`.

```python
import base64

# Codificar credenciales
credentials = base64.b64encode(b"user:password").decode()
# Resultado: "dXNlcjpwYXNzd29yZA=="

# Decodificar
decoded = base64.b64decode(credentials).decode()
# Resultado: "user:password"
```

**⚠️ Problemas:**
- Credenciales enviadas en cada request
- Base64 NO es encriptación (fácil de decodificar)
- Requiere HTTPS obligatoriamente
- No tiene concepto de "sesión"

#### 2.2 Session-Based Authentication

Usar cookies para mantener una sesión después del login.

```
1. POST /login (username, password)
2. Server crea sesión y envía cookie: Set-Cookie: session_id=abc123
3. Browser envía cookie automáticamente: Cookie: session_id=abc123
4. Server valida sesión en cada request
```

**✅ Ventajas:**
- Credenciales solo se envían una vez
- Fácil de revocar (eliminar sesión del servidor)
- Familiar para desarrolladores web

**❌ Desventajas:**
- Requiere almacenamiento en servidor (stateful)
- Problemas con escalabilidad horizontal
- Vulnerable a CSRF si no se protege
- No ideal para APIs móviles/SPAs

#### 2.3 Token-Based Authentication (JWT)

El método moderno más popular para APIs.

```
1. POST /token (username, password)
2. Server genera JWT y lo envía en response
3. Client almacena token y lo envía: Authorization: Bearer <jwt>
4. Server valida firma del token (sin consultar DB)
```

**✅ Ventajas:**
- Stateless (no requiere almacenamiento en servidor)
- Escalable horizontalmente
- Ideal para microservicios
- Puede contener información del usuario (claims)

**❌ Desventajas:**
- Difícil de revocar antes de expiración
- Tokens pueden ser grandes
- Si se compromete la clave, todos los tokens son inválidos

#### 2.4 OAuth2

Estándar de la industria que define varios "flujos" de autenticación.

| Flow | Uso | Ejemplo |
|------|-----|---------|
| **Password** | Apps propias | Login en tu propia app |
| **Authorization Code** | Apps terceras | "Login with Google" |
| **Client Credentials** | Machine-to-machine | Microservicios |
| **Implicit** | SPAs (legacy) | Deprecated |

En esta semana nos enfocaremos en **Password Flow**.

### 3. Amenazas de Seguridad

#### 3.1 Ataques Comunes

```
┌─────────────────────────────────────────────────────────────┐
│                    AMENAZAS DE AUTENTICACIÓN                │
├─────────────────┬───────────────────────────────────────────┤
│ Brute Force     │ Probar muchas contraseñas                 │
│ Dictionary      │ Usar lista de passwords comunes           │
│ Credential      │ Usar credenciales filtradas de otros      │
│ Stuffing        │ sitios                                    │
│ Phishing        │ Engañar al usuario para revelar datos     │
│ Session         │ Robar cookie de sesión                    │
│ Hijacking       │                                           │
│ Man-in-the-     │ Interceptar comunicación                  │
│ Middle          │                                           │
└─────────────────┴───────────────────────────────────────────┘
```

#### 3.2 Contramedidas

```python
# 1. Rate Limiting - Limitar intentos de login
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@app.post("/login")
@limiter.limit("5/minute")  # Max 5 intentos por minuto
async def login(credentials: LoginRequest):
    ...

# 2. Account Lockout - Bloquear cuenta tras N intentos
async def check_login_attempts(username: str) -> bool:
    attempts = await get_failed_attempts(username)
    if attempts >= 5:
        raise HTTPException(
            status_code=429,
            detail="Account locked. Try again in 15 minutes."
        )
    return True

# 3. Delay en respuestas - Dificultar ataques de timing
import asyncio

async def login(credentials: LoginRequest):
    start = time.time()
    result = await authenticate(credentials)
    
    # Asegurar que la respuesta tome al menos 200ms
    elapsed = time.time() - start
    if elapsed < 0.2:
        await asyncio.sleep(0.2 - elapsed)
    
    return result
```

### 4. Mejores Prácticas

#### 4.1 Contraseñas

```python
# ❌ NUNCA hacer esto
def store_password_bad(password: str) -> str:
    return password  # Texto plano
    # return hashlib.md5(password.encode()).hexdigest()  # MD5 es inseguro
    # return hashlib.sha256(password.encode()).hexdigest()  # Sin salt

# ✅ Siempre hacer esto
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hashea password con bcrypt (incluye salt automático)."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica password de forma segura (timing-safe)."""
    return pwd_context.verify(plain_password, hashed_password)
```

#### 4.2 Tokens

```python
# Configuración segura de JWT
JWT_CONFIG = {
    "algorithm": "HS256",  # O RS256 para mayor seguridad
    "access_token_expire_minutes": 15,  # Corta duración
    "refresh_token_expire_days": 7,  # Más largo para refresh
    "secret_key": os.getenv("JWT_SECRET_KEY"),  # NUNCA hardcodear
}

# ❌ NO hacer
SECRET_KEY = "mi_clave_super_secreta"  # Hardcodeada

# ✅ Hacer
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY environment variable not set")
```

#### 4.3 Headers de Seguridad

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configurado correctamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mi-frontend.com"],  # NO usar "*" en producción
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Middleware para headers de seguridad
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
```

### 5. Flujo de Autenticación Típico

```
┌──────────────────────────────────────────────────────────────────┐
│                    FLUJO DE AUTENTICACIÓN                        │
└──────────────────────────────────────────────────────────────────┘

     ┌─────────┐                              ┌─────────┐
     │ Cliente │                              │   API   │
     └────┬────┘                              └────┬────┘
          │                                        │
          │  1. POST /auth/register               │
          │     {email, password}                  │
          │ ─────────────────────────────────────► │
          │                                        │ Hash password
          │                                        │ Save to DB
          │  2. 201 Created                        │
          │     {id, email}                        │
          │ ◄───────────────────────────────────── │
          │                                        │
          │  3. POST /auth/token                   │
          │     (OAuth2 Password Flow)             │
          │ ─────────────────────────────────────► │
          │                                        │ Verify password
          │                                        │ Generate JWT
          │  4. 200 OK                             │
          │     {access_token, refresh_token}      │
          │ ◄───────────────────────────────────── │
          │                                        │
          │  5. GET /users/me                      │
          │     Authorization: Bearer <token>      │
          │ ─────────────────────────────────────► │
          │                                        │ Validate JWT
          │  6. 200 OK                             │ Get user from token
          │     {id, email, ...}                   │
          │ ◄───────────────────────────────────── │
          │                                        │
```

---

## 💡 Puntos Clave

1. **Autenticación ≠ Autorización**: Primero verificas identidad, luego permisos
2. **NUNCA almacenar passwords en texto plano**: Usar bcrypt o argon2
3. **Tokens vs Sesiones**: JWT es stateless, sesiones son stateful
4. **HTTPS obligatorio**: Sin él, todo es vulnerable
5. **Rate limiting**: Protege contra ataques de fuerza bruta

---

## 🔗 Recursos

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Have I Been Pwned](https://haveibeenpwned.com/) - Verificar si tu password fue filtrado
- [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---

## ✅ Checklist de Verificación

- [ ] Entiendo la diferencia entre autenticación y autorización
- [ ] Conozco los métodos de autenticación principales
- [ ] Identifico las amenazas de seguridad comunes
- [ ] Comprendo por qué bcrypt es mejor que MD5/SHA para passwords
- [ ] Sé cuándo usar 401 vs 403
