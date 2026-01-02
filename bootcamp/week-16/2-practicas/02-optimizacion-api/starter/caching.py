"""
============================================
PRÁCTICA 02: Optimización de API
Archivo: caching.py
============================================

Implementa caching para reducir carga en la base de datos
y mejorar tiempos de respuesta.
"""

import json
import time
from datetime import datetime, timedelta
from functools import wraps
from typing import Any, Callable, TypeVar

# ============================================
# PASO 1: Cache en memoria simple
# ============================================
print("--- Paso 1: Cache en memoria simple ---")

MEMORY_CACHE = """
# Cache simple usando diccionario
# Útil para desarrollo y apps pequeñas

from datetime import datetime, timedelta
from typing import Any

class SimpleCache:
    '''Cache en memoria con TTL.'''
    
    def __init__(self):
        self._cache: dict[str, tuple[Any, datetime]] = {}
    
    def get(self, key: str) -> Any | None:
        '''Obtiene valor del cache si no ha expirado.'''
        if key not in self._cache:
            return None
        
        value, expires_at = self._cache[key]
        
        if datetime.now() > expires_at:
            del self._cache[key]
            return None
        
        return value
    
    def set(self, key: str, value: Any, ttl_seconds: int = 300) -> None:
        '''Guarda valor en cache con TTL (default 5 min).'''
        expires_at = datetime.now() + timedelta(seconds=ttl_seconds)
        self._cache[key] = (value, expires_at)
    
    def delete(self, key: str) -> None:
        '''Elimina key del cache.'''
        self._cache.pop(key, None)
    
    def clear(self) -> None:
        '''Limpia todo el cache.'''
        self._cache.clear()
    
    def get_or_set(
        self, 
        key: str, 
        func: Callable[[], Any], 
        ttl_seconds: int = 300
    ) -> Any:
        '''Obtiene del cache o ejecuta función y guarda resultado.'''
        value = self.get(key)
        if value is not None:
            return value
        
        value = func()
        self.set(key, value, ttl_seconds)
        return value

# Instancia global
cache = SimpleCache()

# Uso en endpoint:
@router.get("/stats")
async def get_stats(db: AsyncSession = Depends(get_db)):
    # Cache por 1 hora (stats no cambian frecuentemente)
    return cache.get_or_set(
        "global_stats",
        lambda: calculate_stats(db),
        ttl_seconds=3600
    )
"""
print(MEMORY_CACHE)


# ============================================
# PASO 2: Decorador de cache
# ============================================
print("\n--- Paso 2: Decorador de cache ---")

T = TypeVar("T")

CACHE_DECORATOR = """
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")

def cached(ttl_seconds: int = 300, key_prefix: str = ""):
    '''
    Decorador para cachear resultados de funciones.
    
    Args:
        ttl_seconds: Tiempo de vida del cache
        key_prefix: Prefijo para la key de cache
    '''
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            # Generar key única basada en función y argumentos
            cache_key = f"{key_prefix}{func.__name__}:{hash(str(args) + str(kwargs))}"
            
            # Intentar obtener del cache
            cached_value = cache.get(cache_key)
            if cached_value is not None:
                return cached_value
            
            # Ejecutar función y cachear resultado
            result = await func(*args, **kwargs)
            cache.set(cache_key, result, ttl_seconds)
            
            return result
        
        return wrapper
    return decorator

# Uso:
@cached(ttl_seconds=600, key_prefix="users:")
async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    return await db.get(User, user_id)

@cached(ttl_seconds=300)
async def get_popular_products(db: AsyncSession, limit: int = 10) -> list[Product]:
    query = select(Product).order_by(Product.views.desc()).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
"""
print(CACHE_DECORATOR)


# ============================================
# PASO 3: Cache con Redis (producción)
# ============================================
print("\n--- Paso 3: Cache con Redis ---")

REDIS_CACHE = """
# Para producción, usa Redis
# Instalar: uv add redis

import redis.asyncio as redis
import json
from typing import Any

class RedisCache:
    '''Cache usando Redis para producción.'''
    
    def __init__(self, url: str = "redis://localhost:6379"):
        self.redis = redis.from_url(url, decode_responses=True)
    
    async def get(self, key: str) -> Any | None:
        '''Obtiene valor deserializado del cache.'''
        value = await self.redis.get(key)
        if value is None:
            return None
        return json.loads(value)
    
    async def set(
        self, 
        key: str, 
        value: Any, 
        ttl_seconds: int = 300
    ) -> None:
        '''Guarda valor serializado en cache.'''
        await self.redis.setex(
            key,
            ttl_seconds,
            json.dumps(value, default=str)
        )
    
    async def delete(self, key: str) -> None:
        '''Elimina key del cache.'''
        await self.redis.delete(key)
    
    async def delete_pattern(self, pattern: str) -> int:
        '''Elimina todas las keys que coinciden con patrón.'''
        keys = await self.redis.keys(pattern)
        if keys:
            return await self.redis.delete(*keys)
        return 0
    
    async def get_or_set(
        self,
        key: str,
        func: Callable,
        ttl_seconds: int = 300
    ) -> Any:
        '''Obtiene del cache o ejecuta función async.'''
        value = await self.get(key)
        if value is not None:
            return value
        
        value = await func()
        await self.set(key, value, ttl_seconds)
        return value

# Dependency para FastAPI:
async def get_cache() -> RedisCache:
    return RedisCache(settings.redis_url)

# Uso:
@router.get("/products/{product_id}")
async def get_product(
    product_id: int,
    cache: RedisCache = Depends(get_cache),
    db: AsyncSession = Depends(get_db)
):
    cache_key = f"product:{product_id}"
    
    product = await cache.get(cache_key)
    if product:
        return product
    
    product = await db.get(Product, product_id)
    if product:
        await cache.set(cache_key, product.to_dict(), ttl_seconds=600)
    
    return product
"""
print(REDIS_CACHE)


# ============================================
# PASO 4: Invalidación de cache
# ============================================
print("\n--- Paso 4: Invalidación de cache ---")

CACHE_INVALIDATION = """
# El cache debe invalidarse cuando los datos cambian

class UserService:
    def __init__(self, db: AsyncSession, cache: RedisCache):
        self.db = db
        self.cache = cache
    
    async def get_user(self, user_id: int) -> User | None:
        cache_key = f"user:{user_id}"
        
        # Try cache first
        cached = await self.cache.get(cache_key)
        if cached:
            return User(**cached)
        
        # Fetch from DB
        user = await self.db.get(User, user_id)
        if user:
            await self.cache.set(cache_key, user.to_dict())
        
        return user
    
    async def update_user(self, user_id: int, data: UserUpdate) -> User:
        user = await self.db.get(User, user_id)
        
        # Update in DB
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        await self.db.commit()
        
        # Invalidate cache
        await self.cache.delete(f"user:{user_id}")
        
        # También invalidar listas que incluyan este usuario
        await self.cache.delete_pattern("users:list:*")
        
        return user
    
    async def delete_user(self, user_id: int) -> None:
        await self.db.execute(
            delete(User).where(User.id == user_id)
        )
        await self.db.commit()
        
        # Invalidar todo el cache relacionado
        await self.cache.delete(f"user:{user_id}")
        await self.cache.delete_pattern("users:*")

# Patrones de invalidación:
# 1. Invalidar key específica: cache.delete("user:123")
# 2. Invalidar por patrón: cache.delete_pattern("user:*")
# 3. TTL corto para datos que cambian frecuentemente
# 4. Eventos/hooks para invalidar al modificar
"""
print(CACHE_INVALIDATION)


# ============================================
# PASO 5: Estrategias de caching
# ============================================
print("\n--- Paso 5: Estrategias de caching ---")

CACHING_STRATEGIES = """
┌──────────────────┬────────────────────────────────────────────────┐
│ Estrategia       │ Descripción                                    │
├──────────────────┼────────────────────────────────────────────────┤
│ Cache-Aside      │ App lee cache, si miss → lee DB → escribe cache│
│ (Lazy Loading)   │ Más común, flexible                            │
├──────────────────┼────────────────────────────────────────────────┤
│ Write-Through    │ Escribe en cache y DB simultáneamente          │
│                  │ Cache siempre actualizado                      │
├──────────────────┼────────────────────────────────────────────────┤
│ Write-Behind     │ Escribe en cache, DB se actualiza async        │
│ (Write-Back)     │ Mejor performance, riesgo de pérdida de datos  │
├──────────────────┼────────────────────────────────────────────────┤
│ Read-Through     │ Cache maneja lectura de DB automáticamente     │
│                  │ Simplifica código de aplicación                │
└──────────────────┴────────────────────────────────────────────────┘

Qué cachear:
✅ Datos que se leen frecuentemente y cambian poco
✅ Resultados de queries costosas
✅ Datos de sesión/usuario
✅ Configuraciones

❌ No cachear:
• Datos que cambian muy frecuentemente
• Datos sensibles sin encriptar
• Datos específicos de request
• Resultados de queries únicas

TTLs recomendados:
• Sesiones: 30 min - 24 horas
• Datos de usuario: 5-15 minutos
• Listas/catálogos: 1-5 minutos
• Stats/reportes: 1-24 horas
"""
print(CACHING_STRATEGIES)


# ============================================
# EJERCICIO PRÁCTICO
# ============================================
print("\n" + "="*50)
print("📝 EJERCICIO: Implementa cache en tu proyecto")
print("="*50)
print("""
1. Implementa SimpleCache para desarrollo

2. Identifica 3 endpoints que se beneficiarían de cache:
   - Endpoint de listado (GET /items)
   - Endpoint de detalle frecuente (GET /items/{id})
   - Endpoint de stats/dashboard

3. Agrega el decorador @cached a estos endpoints

4. Implementa invalidación en endpoints de escritura

5. Mide mejora en tiempo de respuesta

Resultado esperado:
- Endpoints cacheados responden < 50ms en cache hit
- Cache se invalida correctamente al modificar datos
- Sin datos stale visibles al usuario
""")
