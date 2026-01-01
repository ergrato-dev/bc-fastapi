"""
Router de Notificaciones.

Los endpoints usan Depends() para recibir el service.
"""
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr

from src.domain.entities import NotificationChannel
from src.application.services import NotificationService
from src.presentation.dependencies import get_notification_service


router = APIRouter(prefix="/notifications", tags=["Notifications"])


# ============================================
# DTOs para la API
# ============================================
class NotificationCreate(BaseModel):
    """DTO para crear notificación."""
    recipient: str
    channel: NotificationChannel
    message: str
    subject: str | None = None


class NotificationResponse(BaseModel):
    """DTO de respuesta."""
    id: int
    recipient: str
    channel: str
    message: str
    subject: str | None
    status: str
    
    model_config = {"from_attributes": True}


# ============================================
# PASO 4: Implementar endpoints con inyección
# ============================================

# Descomenta las siguientes líneas:

# @router.post("/", response_model=NotificationResponse, status_code=201)
# async def create_notification(
#     data: NotificationCreate,
#     service: Annotated[NotificationService, Depends(get_notification_service)],
# ):
#     """
#     Crea y envía una notificación.
#     
#     El service se inyecta automáticamente via Depends().
#     """
#     notification = await service.send_notification(
#         recipient=data.recipient,
#         channel=data.channel,
#         message=data.message,
#         subject=data.subject,
#     )
#     
#     return NotificationResponse(
#         id=notification.id,  # type: ignore
#         recipient=notification.recipient,
#         channel=notification.channel.value,
#         message=notification.message,
#         subject=notification.subject,
#         status=notification.status.value,
#     )
# 
# 
# @router.get("/{notification_id}", response_model=NotificationResponse)
# async def get_notification(
#     notification_id: int,
#     service: Annotated[NotificationService, Depends(get_notification_service)],
# ):
#     """Obtiene una notificación por ID."""
#     notification = await service.get_notification(notification_id)
#     
#     if notification is None:
#         raise HTTPException(status_code=404, detail="Notificación no encontrada")
#     
#     return NotificationResponse(
#         id=notification.id,  # type: ignore
#         recipient=notification.recipient,
#         channel=notification.channel.value,
#         message=notification.message,
#         subject=notification.subject,
#         status=notification.status.value,
#     )


# Placeholders temporales
@router.post("/", response_model=NotificationResponse, status_code=201)
async def create_notification(
    data: NotificationCreate,
    service: Annotated[NotificationService, Depends(get_notification_service)],
):
    notification = await service.send_notification(
        recipient=data.recipient,
        channel=data.channel,
        message=data.message,
        subject=data.subject,
    )
    return NotificationResponse(
        id=notification.id or 0,
        recipient=notification.recipient,
        channel=notification.channel.value,
        message=notification.message,
        subject=notification.subject,
        status=notification.status.value,
    )


@router.get("/{notification_id}", response_model=NotificationResponse)
async def get_notification(
    notification_id: int,
    service: Annotated[NotificationService, Depends(get_notification_service)],
):
    notification = await service.get_notification(notification_id)
    if notification is None:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return NotificationResponse(
        id=notification.id or 0,
        recipient=notification.recipient,
        channel=notification.channel.value,
        message=notification.message,
        subject=notification.subject,
        status=notification.status.value,
    )
