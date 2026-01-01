"""
Router: Notifications

Endpoints para el manejo de notificaciones.
"""
from fastapi import APIRouter, Depends, HTTPException, status

from src.domain.entities.notification import NotificationStatus
from src.application.services.notification_service import NotificationService
from src.application.dtos.notification_dtos import (
    NotificationCreate,
    NotificationResponse,
    NotificationBatchCreate,
)
from src.presentation.dependencies import get_notification_service


router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post(
    "/",
    response_model=NotificationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Enviar notificación",
    description="Envía una notificación a través del canal especificado.",
)
async def send_notification(
    data: NotificationCreate,
    service: NotificationService = Depends(get_notification_service),
) -> NotificationResponse:
    """
    Envía una nueva notificación.
    
    TODO: Implementar:
    1. Verificar que el canal esté disponible (service.has_channel)
    2. Si no está disponible, lanzar HTTPException 400
    3. Llamar a service.send_notification() con los datos
    4. Convertir el resultado a NotificationResponse
    5. Retornar la respuesta
    """
    # TODO: Implementar
    pass


@router.get(
    "/",
    response_model=list[NotificationResponse],
    summary="Listar notificaciones",
    description="Obtiene todas las notificaciones, opcionalmente filtradas por estado.",
)
async def list_notifications(
    status_filter: NotificationStatus | None = None,
    service: NotificationService = Depends(get_notification_service),
) -> list[NotificationResponse]:
    """
    Lista notificaciones.
    
    TODO: Implementar:
    1. Si status_filter tiene valor, usar service.get_by_status()
    2. Si no, usar service.get_all_notifications()
    3. Convertir cada resultado a NotificationResponse
    4. Retornar la lista
    """
    # TODO: Implementar
    pass


@router.get(
    "/channels",
    response_model=list[str],
    summary="Canales disponibles",
    description="Obtiene la lista de canales de notificación disponibles.",
)
async def get_channels(
    service: NotificationService = Depends(get_notification_service),
) -> list[str]:
    """
    Obtiene canales disponibles.
    
    TODO: Implementar usando service.get_available_channels().
    Convertir cada canal a su valor string.
    """
    # TODO: Implementar
    pass


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse,
    summary="Obtener notificación",
    description="Obtiene una notificación por su ID.",
)
async def get_notification(
    notification_id: str,
    service: NotificationService = Depends(get_notification_service),
) -> NotificationResponse:
    """
    Obtiene una notificación por ID.
    
    TODO: Implementar:
    1. Llamar a service.get_notification(notification_id)
    2. Si retorna None, lanzar HTTPException 404
    3. Convertir a NotificationResponse y retornar
    """
    # TODO: Implementar
    pass


@router.delete(
    "/{notification_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar notificación",
    description="Elimina una notificación por su ID.",
)
async def delete_notification(
    notification_id: str,
    service: NotificationService = Depends(get_notification_service),
) -> None:
    """
    Elimina una notificación.
    
    TODO: Implementar:
    1. Llamar a service.delete_notification(notification_id)
    2. Si retorna False, lanzar HTTPException 404
    3. No retornar nada (204 No Content)
    """
    # TODO: Implementar
    pass


@router.post(
    "/batch",
    response_model=list[NotificationResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Enviar múltiples notificaciones",
    description="Envía múltiples notificaciones en una sola petición.",
)
async def send_batch(
    data: NotificationBatchCreate,
    service: NotificationService = Depends(get_notification_service),
) -> list[NotificationResponse]:
    """
    Envía múltiples notificaciones.
    
    TODO: Implementar:
    1. Convertir data.notifications a lista de dicts
    2. Llamar a service.send_batch()
    3. Convertir resultados a NotificationResponse
    4. Retornar la lista
    """
    # TODO: Implementar
    pass


@router.post(
    "/retry-failed",
    response_model=list[NotificationResponse],
    summary="Reintentar fallidas",
    description="Reintenta enviar todas las notificaciones fallidas.",
)
async def retry_failed(
    service: NotificationService = Depends(get_notification_service),
) -> list[NotificationResponse]:
    """
    Reintenta notificaciones fallidas.
    
    TODO: Implementar:
    1. Llamar a service.retry_failed()
    2. Convertir resultados a NotificationResponse
    3. Retornar la lista
    """
    # TODO: Implementar
    pass
