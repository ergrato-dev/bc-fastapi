# ============================================
# Health Endpoints
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para implementar
# los endpoints de health check.
# ============================================

from fastapi import APIRouter, Depends

from src.config import get_settings, Settings
from src.schemas import HealthResponse, ReadinessResponse

router = APIRouter(prefix="/health", tags=["Health"])


# ============================================
# TODO 1: Health Check básico
# ============================================
@router.get("", response_model=HealthResponse)
async def health_check(
    settings: Settings = Depends(get_settings),
) -> HealthResponse:
    """
    Basic health check endpoint.

    Returns the application status, version, and environment.
    """
    # TODO: Implementar
    # return HealthResponse(
    #     status="healthy",
    #     version="1.0.0",
    #     environment=settings.environment,
    # )

    # Placeholder
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        environment="development",
    )


# ============================================
# TODO 2: Liveness Check
# ============================================
@router.get("/live")
async def liveness() -> dict[str, str]:
    """
    Kubernetes liveness probe.

    Returns 200 if the application is running.
    Used by Kubernetes to know if the pod should be restarted.
    """
    return {"status": "alive"}


# ============================================
# TODO 3: Readiness Check (con DB y Redis)
# ============================================
@router.get("/ready", response_model=ReadinessResponse)
async def readiness() -> ReadinessResponse:
    """
    Kubernetes readiness probe.

    Checks if the application is ready to receive traffic.
    Verifies database and cache connections.
    """
    # TODO: Implementar verificación real de DB y Redis
    # try:
    #     # Check database
    #     db = next(get_db())
    #     db.execute(text("SELECT 1"))
    #     db_status = "connected"
    # except Exception:
    #     db_status = "disconnected"
    #
    # try:
    #     # Check Redis
    #     redis_client = redis.from_url(settings.redis_url)
    #     redis_client.ping()
    #     redis_status = "connected"
    # except Exception:
    #     redis_status = "disconnected"
    #
    # status = "ready" if db_status == "connected" else "not_ready"
    #
    # return ReadinessResponse(
    #     status=status,
    #     database=db_status,
    #     redis=redis_status,
    # )

    # Placeholder
    return ReadinessResponse(
        status="ready",
        database="connected",
        redis="connected",
    )
