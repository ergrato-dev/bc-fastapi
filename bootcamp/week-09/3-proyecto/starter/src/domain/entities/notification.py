"""
Entidad Notification y sus enums.
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class NotificationStatus(str, Enum):
    """Estados posibles de una notificación."""
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
    DELIVERED = "delivered"


class NotificationChannel(str, Enum):
    """Canales de notificación disponibles."""
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    WEBHOOK = "webhook"


@dataclass
class Notification:
    """
    Entidad de dominio que representa una notificación.
    
    Attributes:
        recipient: Destinatario (email, teléfono, device_id, url)
        channel: Canal de envío
        message: Contenido del mensaje
        subject: Asunto (opcional, para email)
        id: Identificador único
        status: Estado actual
        created_at: Fecha de creación
        sent_at: Fecha de envío (si fue enviado)
        error_message: Mensaje de error (si falló)
        metadata: Datos adicionales
    """
    recipient: str
    channel: NotificationChannel
    message: str
    subject: str | None = None
    id: str = field(default_factory=lambda: str(uuid4()))
    status: NotificationStatus = NotificationStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    sent_at: datetime | None = None
    error_message: str | None = None
    metadata: dict = field(default_factory=dict)
    
    def mark_as_sent(self) -> None:
        """Marca la notificación como enviada."""
        self.status = NotificationStatus.SENT
        self.sent_at = datetime.now()
        self.error_message = None
    
    def mark_as_failed(self, error: str) -> None:
        """Marca la notificación como fallida."""
        self.status = NotificationStatus.FAILED
        self.error_message = error
    
    def mark_as_delivered(self) -> None:
        """Marca la notificación como entregada."""
        self.status = NotificationStatus.DELIVERED
    
    @property
    def is_pending(self) -> bool:
        """Verifica si está pendiente."""
        return self.status == NotificationStatus.PENDING
    
    @property
    def was_sent(self) -> bool:
        """Verifica si fue enviada o entregada."""
        return self.status in (NotificationStatus.SENT, NotificationStatus.DELIVERED)
