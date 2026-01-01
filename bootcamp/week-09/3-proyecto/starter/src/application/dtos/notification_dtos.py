"""
DTOs para la API de notificaciones.
"""
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

from src.domain.entities.notification import (
    Notification,
    NotificationChannel,
    NotificationStatus,
)


class NotificationCreate(BaseModel):
    """DTO para crear una notificación."""
    
    recipient: str = Field(
        ...,
        description="Destinatario (email, teléfono, url, etc.)",
        examples=["user@example.com", "+1234567890"],
    )
    channel: NotificationChannel = Field(
        ...,
        description="Canal de envío",
    )
    message: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="Contenido del mensaje",
    )
    subject: str | None = Field(
        default=None,
        max_length=200,
        description="Asunto (para email)",
    )
    metadata: dict = Field(
        default_factory=dict,
        description="Datos adicionales",
    )
    
    model_config = ConfigDict(use_enum_values=True)


class NotificationResponse(BaseModel):
    """DTO de respuesta para una notificación."""
    
    id: str
    recipient: str
    channel: NotificationChannel
    message: str
    subject: str | None
    status: NotificationStatus
    created_at: datetime
    sent_at: datetime | None
    error_message: str | None
    metadata: dict
    
    model_config = ConfigDict(from_attributes=True)
    
    @classmethod
    def from_entity(cls, notification: Notification) -> "NotificationResponse":
        """Convierte una entidad a DTO de respuesta."""
        return cls(
            id=notification.id,
            recipient=notification.recipient,
            channel=notification.channel,
            message=notification.message,
            subject=notification.subject,
            status=notification.status,
            created_at=notification.created_at,
            sent_at=notification.sent_at,
            error_message=notification.error_message,
            metadata=notification.metadata,
        )


class NotificationBatchCreate(BaseModel):
    """DTO para crear múltiples notificaciones."""
    
    notifications: list[NotificationCreate] = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Lista de notificaciones a enviar",
    )


class NotificationBatchResponse(BaseModel):
    """DTO de respuesta para envío batch."""
    
    total: int
    sent: int
    failed: int
    notifications: list[NotificationResponse]
