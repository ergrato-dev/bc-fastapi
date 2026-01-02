# 🚦 Rate Limiting en FastAPI

## 📋 Contenido

1. [¿Qué es Rate Limiting?](#qué-es-rate-limiting)
2. [¿Por qué es necesario?](#por-qué-es-necesario)
3. [Algoritmos de Rate Limiting](#algoritmos-de-rate-limiting)
4. [Implementación con slowapi](#implementación-con-slowapi)
5. [Backend con Redis](#backend-con-redis)
6. [Estrategias de limitación](#estrategias-de-limitación)
7. [Headers de respuesta](#headers-de-respuesta)

---

## ¿Qué es Rate Limiting?

**Rate limiting** es una técnica para controlar la cantidad de requests que un cliente puede hacer a tu API en un período de tiempo determinado.

![Rate Limiting Flow](../0-assets/01-rate-limiting-flow.svg)

### Analogía Simple

Imagina un cajero de banco que solo atiende a **5 personas por hora**:
- Si llegas y hay cupo, te atiende inmediatamente
- Si ya atendió a 5 personas, debes esperar a la siguiente hora
- Cada hora el contador se reinicia

En APIs funciona igual: **X requests por unidad de tiempo**.

---

## ¿Por qué es necesario?

### 1. **Protección contra Abusos**

```
Sin rate limiting:
┌─────────────┐     1000 req/seg     ┌─────────────┐
│   Atacante  │ ────────────────────▶│  Tu API     │ 💥 Crash!
└─────────────┘                      └─────────────┘

Con rate limiting:
┌─────────────┐     1000 req/seg     ┌─────────────┐     10 req/seg     ┌─────────────┐
│   Atacante  │ ────────────────────▶│ Rate Limiter│ ──────────────────▶│  Tu API     │ ✅ OK
└─────────────┘                      └─────────────┘                    └─────────────┘
                                           │
                                           ▼ 429 Too Many Requests
```

### 2. **Casos de Uso Comunes**

| Escenario | Límite Típico | Razón |
|-----------|---------------|-------|
| Login/Register | 5/min por IP | Prevenir brute force |
| API pública | 100/hora | Uso justo de recursos |
| Endpoints costosos | 10/min | Proteger recursos |
| Webhooks salientes | 60/min | Evitar bloqueos externos |

### 3. **Beneficios**

- ✅ Previene ataques DDoS
- ✅ Evita brute force en autenticación
- ✅ Garantiza disponibilidad para todos
- ✅ Reduce costos de infraestructura
- ✅ Cumple SLAs con terceros

---

## Algoritmos de Rate Limiting

### 1. **Fixed Window**

El más simple: cuenta requests en ventanas de tiempo fijas.

```
Ventana: 1 minuto, Límite: 5 requests

Minuto 1 (00:00 - 00:59):
│ ✅ │ ✅ │ ✅ │ ✅ │ ✅ │ ❌ │ ❌ │
  1    2    3    4    5   6    7
                          ↑
                     Bloqueado

Minuto 2 (01:00 - 01:59):
│ ✅ │ ✅ │ ...
  1    2
  ↑
  Contador reiniciado
```

**Problema**: Burst en los bordes de ventana.

```python
# Pseudocódigo
def check_rate_limit(client_id: str, limit: int, window: int) -> bool:
    key = f"rate:{client_id}:{current_window()}"
    count = redis.incr(key)
    if count == 1:
        redis.expire(key, window)
    return count <= limit
```

### 2. **Sliding Window**

Más preciso: considera requests en una ventana deslizante.

```
Ventana deslizante de 1 minuto:

Tiempo: 00:30
├─────────────────────────────────────┤
│  Últimos 60 segundos desde 00:30    │
│  23:30 ◀─────────────────────▶ 00:30│
└─────────────────────────────────────┘
```

**Ventaja**: Distribución más uniforme, sin bursts.

### 3. **Token Bucket**

Tokens se añaden a un "cubo" a tasa constante. Cada request consume un token.

```
Capacidad: 10 tokens
Tasa: 1 token/segundo

Estado inicial: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 10/10

Después de 5 requests: [🟢🟢🟢🟢🟢⚫⚫⚫⚫⚫] 5/10

Después de 3 segundos: [🟢🟢🟢🟢🟢🟢🟢🟢⚫⚫] 8/10
                        ↑↑↑ +3 tokens regenerados
```

**Ventaja**: Permite bursts controlados.

### 4. **Leaky Bucket**

Requests entran al bucket, salen a tasa constante.

```
Requests entrantes (variable)     Bucket (cola)      Salida (constante)
        │                         ┌───────┐
    ▼▼▼▼▼▼▼                       │ ───── │               ▼
   ─────────────────────────────▶ │ ───── │ ─────────────────▶ API
                                  │ ───── │           1 req/seg
                                  └───┬───┘
                                      │
                              Overflow = 429
```

**Ventaja**: Tráfico de salida muy uniforme.

### Comparación

| Algoritmo | Complejidad | Bursts | Precisión |
|-----------|-------------|--------|-----------|
| Fixed Window | Simple | ⚠️ Permite | Baja |
| Sliding Window | Media | ✅ Controla | Alta |
| Token Bucket | Media | ✅ Permite controlados | Alta |
| Leaky Bucket | Media | ❌ No permite | Muy alta |

---

## Implementación con slowapi

**slowapi** es la librería estándar para rate limiting en FastAPI/Starlette.

### Instalación

```bash
uv add slowapi
```

### Configuración Básica

```python
# src/rate_limiter.py
from slowapi import Limiter
from slowapi.util import get_remote_address

# Crea el limiter - identifica clientes por IP
limiter = Limiter(key_func=get_remote_address)
```

### Integración con FastAPI

```python
# src/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from src.rate_limiter import limiter

app = FastAPI(title="API con Rate Limiting")

# Registrar el limiter en el estado de la app
app.state.limiter = limiter

# Handler para errores de rate limit
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
```

### Aplicar Límites a Endpoints

```python
from fastapi import FastAPI, Request
from src.rate_limiter import limiter

@app.get("/api/data")
@limiter.limit("10/minute")  # 10 requests por minuto
async def get_data(request: Request):
    return {"data": "example"}


@app.post("/auth/login")
@limiter.limit("5/minute")  # Más restrictivo para login
async def login(request: Request):
    return {"token": "..."}


@app.get("/public/info")
@limiter.limit("100/hour")  # Más permisivo para info pública
async def public_info(request: Request):
    return {"info": "public"}
```

### Formatos de Límite

```python
# Formatos válidos
@limiter.limit("5/minute")      # 5 por minuto
@limiter.limit("100/hour")      # 100 por hora
@limiter.limit("1000/day")      # 1000 por día
@limiter.limit("1/second")      # 1 por segundo
@limiter.limit("5 per minute")  # Formato alternativo
@limiter.limit("5/min")         # Abreviado

# Múltiples límites
@limiter.limit("5/minute;100/hour")  # Ambos deben cumplirse
```

### Límites Dinámicos

```python
def get_limit_by_user_type(request: Request) -> str:
    """Límite basado en tipo de usuario."""
    # Obtener usuario del token (ejemplo simplificado)
    user = getattr(request.state, "user", None)
    
    if user and user.is_premium:
        return "1000/hour"
    elif user:
        return "100/hour"
    else:
        return "20/hour"  # No autenticado


@app.get("/api/resources")
@limiter.limit(get_limit_by_user_type)
async def get_resources(request: Request):
    return {"resources": [...]}
```

### Excluir Rutas

```python
from slowapi import Limiter

limiter = Limiter(
    key_func=get_remote_address,
    # Rutas sin límite
    default_limits=["200/day", "50/hour"],
    # Excluir health checks y métricas
    application_limits=["1000/minute"],
)

@app.get("/health")
@limiter.exempt  # Sin límite
async def health_check():
    return {"status": "healthy"}
```

---

## Backend con Redis

Por defecto, slowapi usa memoria local. **Para producción, usa Redis**.

### ¿Por qué Redis?

```
Problema con memoria local:
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   Instancia 1 │  │   Instancia 2 │  │   Instancia 3 │
│   count: 3    │  │   count: 3    │  │   count: 3    │
└───────────────┘  └───────────────┘  └───────────────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                   Load Balancer
                          │
                      Cliente
                   (9 requests = 3 x 3!)
                   
Solución con Redis:
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   Instancia 1 │  │   Instancia 2 │  │   Instancia 3 │
└───────────────┘  └───────────────┘  └───────────────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                    ┌───────────┐
                    │   Redis   │
                    │ count: 9  │  ← Contador compartido
                    └───────────┘
```

### Configuración

```python
# src/rate_limiter.py
from slowapi import Limiter
from slowapi.util import get_remote_address

# Backend en memoria (desarrollo)
limiter_memory = Limiter(key_func=get_remote_address)

# Backend Redis (producción)
limiter_redis = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379/0",
    # Opciones adicionales
    storage_options={
        "socket_connect_timeout": 30,
        "socket_timeout": 30,
    }
)
```

### Docker Compose con Redis

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  redis_data:
```

### Configuración desde Settings

```python
# src/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Rate Limiting
    rate_limit_enabled: bool = True
    rate_limit_storage: str = "memory"  # "memory" o "redis://..."
    rate_limit_default: str = "100/hour"
    
    model_config = {"env_prefix": "APP_"}


# src/rate_limiter.py
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.config import Settings

settings = Settings()

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=settings.rate_limit_storage if settings.rate_limit_storage != "memory" else None,
    enabled=settings.rate_limit_enabled,
    default_limits=[settings.rate_limit_default],
)
```

---

## Estrategias de Limitación

### 1. **Por IP** (Default)

```python
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
```

⚠️ **Problema**: Usuarios detrás de NAT/proxy comparten IP.

### 2. **Por Usuario Autenticado**

```python
def get_user_identifier(request: Request) -> str:
    """Identifica por usuario o IP como fallback."""
    # Buscar usuario en el estado del request (seteado por middleware de auth)
    user = getattr(request.state, "user", None)
    if user:
        return f"user:{user.id}"
    # Fallback a IP para no autenticados
    return f"ip:{get_remote_address(request)}"


limiter = Limiter(key_func=get_user_identifier)
```

### 3. **Por API Key**

```python
def get_api_key(request: Request) -> str:
    """Identifica por API key."""
    api_key = request.headers.get("X-API-Key")
    if api_key:
        return f"key:{api_key}"
    return f"ip:{get_remote_address(request)}"


limiter = Limiter(key_func=get_api_key)
```

### 4. **Combinado (IP + Usuario)**

```python
def get_combined_identifier(request: Request) -> str:
    """Límite por IP Y por usuario."""
    ip = get_remote_address(request)
    user = getattr(request.state, "user", None)
    
    if user:
        # Usuario autenticado: límite por IP + límite por usuario
        return f"{ip}:{user.id}"
    return ip
```

---

## Headers de Respuesta

slowapi añade headers estándar automáticamente:

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 7
X-RateLimit-Reset: 1640000000
```

### Cuando se excede el límite

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 45
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1640000000
Content-Type: application/json

{
    "error": "Rate limit exceeded",
    "detail": "10 per 1 minute"
}
```

### Headers Personalizados

```python
from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded


async def custom_rate_limit_handler(
    request: Request, 
    exc: RateLimitExceeded
) -> JSONResponse:
    """Handler personalizado para errores de rate limit."""
    return JSONResponse(
        status_code=429,
        content={
            "error": "rate_limit_exceeded",
            "message": "Has excedido el límite de requests",
            "detail": str(exc.detail),
            "retry_after": exc.retry_after,
        },
        headers={
            "Retry-After": str(exc.retry_after),
            "X-RateLimit-Limit": request.headers.get("X-RateLimit-Limit", ""),
        },
    )


# Registrar handler personalizado
app.add_exception_handler(RateLimitExceeded, custom_rate_limit_handler)
```

---

## Ejemplo Completo

```python
# src/main.py
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Configurar limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="API con Rate Limiting")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Endpoints con diferentes límites
@app.get("/")
@limiter.limit("30/minute")
async def root(request: Request):
    return {"message": "Welcome!"}


@app.post("/auth/login")
@limiter.limit("5/minute")  # Muy restrictivo
async def login(request: Request):
    return {"token": "jwt_token_here"}


@app.post("/auth/register")
@limiter.limit("3/hour")  # Aún más restrictivo
async def register(request: Request):
    return {"user": "created"}


@app.get("/api/data")
@limiter.limit("100/hour")
async def get_data(request: Request):
    return {"data": [1, 2, 3]}


@app.get("/health")
@limiter.exempt  # Sin límite
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## 📚 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Rate Limiting** | Controlar requests por cliente/tiempo |
| **slowapi** | Librería estándar para FastAPI |
| **Algoritmos** | Fixed/Sliding Window, Token/Leaky Bucket |
| **Backend** | Memoria (dev) o Redis (producción) |
| **Identificación** | Por IP, usuario, API key |
| **Headers** | X-RateLimit-*, Retry-After |

---

## 🔗 Recursos

- [slowapi Documentation](https://slowapi.readthedocs.io/)
- [Rate Limiting Patterns](https://cloud.google.com/architecture/rate-limiting-strategies)
- [OWASP Rate Limiting](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html)

---

*Siguiente: [02 - Seguridad de APIs](02-seguridad-apis.md)*
