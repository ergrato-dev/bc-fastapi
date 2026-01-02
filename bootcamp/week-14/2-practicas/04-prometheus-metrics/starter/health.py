"""
Módulo de Health Checks.

Este módulo implementa endpoints de health check para
monitoreo y orquestación (Kubernetes, Docker, etc).
"""

from datetime import datetime
from enum import Enum


class HealthStatus(str, Enum):
    """Estados posibles de health."""
    
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"


# ============================================
# PASO 4: Health Check Functions
# ============================================
print("--- Paso 4: Health Check Functions ---")

# Health checks verifican el estado de la aplicación:
# - Liveness: ¿La aplicación está corriendo? (simple)
# - Readiness: ¿La aplicación puede recibir tráfico? (verifica deps)
# - Startup: ¿La aplicación terminó de iniciar? (una vez)

# Descomenta las siguientes líneas:
# async def check_database() -> tuple[bool, str]:
#     """
#     Verifica conexión a la base de datos.
#     
#     Returns:
#         tuple: (está_sana, mensaje)
#     """
#     try:
#         # Simular verificación de DB
#         # En producción: ejecutar query simple como SELECT 1
#         return True, "Database connection OK"
#     except Exception as e:
#         return False, f"Database error: {str(e)}"
#
#
# async def check_redis() -> tuple[bool, str]:
#     """
#     Verifica conexión a Redis.
#     
#     Returns:
#         tuple: (está_sano, mensaje)
#     """
#     try:
#         # Simular verificación de Redis
#         # En producción: ejecutar PING
#         return True, "Redis connection OK"
#     except Exception as e:
#         return False, f"Redis error: {str(e)}"
#
#
# async def check_external_api() -> tuple[bool, str]:
#     """
#     Verifica disponibilidad de API externa.
#     
#     Returns:
#         tuple: (está_sana, mensaje)
#     """
#     try:
#         # Simular verificación de API externa
#         # En producción: hacer request a endpoint de salud
#         return True, "External API available"
#     except Exception as e:
#         return False, f"External API error: {str(e)}"
#
#
# async def get_liveness() -> dict:
#     """
#     Liveness check - verifica si la aplicación está corriendo.
#     
#     Este check es SIMPLE y rápido. Si falla, Kubernetes
#     reiniciará el container.
#     
#     Returns:
#         dict: Estado de liveness
#     """
#     return {
#         "status": HealthStatus.HEALTHY,
#         "timestamp": datetime.utcnow().isoformat(),
#         "service": "api",
#     }
#
#
# async def get_readiness() -> dict:
#     """
#     Readiness check - verifica si puede recibir tráfico.
#     
#     Este check verifica TODAS las dependencias. Si falla,
#     Kubernetes deja de enviar tráfico pero NO reinicia.
#     
#     Returns:
#         dict: Estado de readiness con checks de dependencias
#     """
#     checks = {}
#     overall_healthy = True
#     
#     # Verificar database
#     db_ok, db_msg = await check_database()
#     checks["database"] = {"healthy": db_ok, "message": db_msg}
#     if not db_ok:
#         overall_healthy = False
#     
#     # Verificar Redis
#     redis_ok, redis_msg = await check_redis()
#     checks["redis"] = {"healthy": redis_ok, "message": redis_msg}
#     if not redis_ok:
#         overall_healthy = False
#     
#     # Verificar API externa (opcional - puede ser degraded)
#     api_ok, api_msg = await check_external_api()
#     checks["external_api"] = {"healthy": api_ok, "message": api_msg}
#     
#     # Determinar estado general
#     if overall_healthy and api_ok:
#         status = HealthStatus.HEALTHY
#     elif overall_healthy:
#         status = HealthStatus.DEGRADED  # Funcional pero sin API externa
#     else:
#         status = HealthStatus.UNHEALTHY
#     
#     return {
#         "status": status,
#         "timestamp": datetime.utcnow().isoformat(),
#         "service": "api",
#         "checks": checks,
#     }


# Versiones placeholder para que el código funcione:
async def check_database() -> tuple[bool, str]:
    """Placeholder - descomenta el código real arriba."""
    return True, "Database connection OK"


async def check_redis() -> tuple[bool, str]:
    """Placeholder - descomenta el código real arriba."""
    return True, "Redis connection OK"


async def check_external_api() -> tuple[bool, str]:
    """Placeholder - descomenta el código real arriba."""
    return True, "External API available"


async def get_liveness() -> dict:
    """Placeholder - descomenta el código real arriba."""
    return {
        "status": HealthStatus.HEALTHY,
        "timestamp": datetime.utcnow().isoformat(),
        "service": "api",
    }


async def get_readiness() -> dict:
    """Placeholder - descomenta el código real arriba."""
    return {
        "status": HealthStatus.HEALTHY,
        "timestamp": datetime.utcnow().isoformat(),
        "service": "api",
        "checks": {
            "database": {"healthy": True, "message": "OK"},
            "redis": {"healthy": True, "message": "OK"},
        },
    }
