"""
Entidad de Dominio: Notification

Esta entidad representa una notificación en el sistema.
Es independiente de la infraestructura (no sabe de BD, email, etc.)
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class NotificationStatus(Enum):
    """Estados posibles de una notificación."""
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
    CANCELLED = "cancelled"


class NotificationChannel(Enum):
    """Canales de envío disponibles."""
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    WEBHOOK = "webhook"


@dataclass
class Notification:
    """
    Entidad de dominio que representa una notificación.
    
    Attributes:
        id: Identificador único (None si no ha sido persistida)
        recipient: Destinatario (email, teléfono, URL, etc.)
        channel: Canal de envío
        subject: Asunto (opcional, no aplica a todos los canales)
        message: Contenido del mensaje
        status: Estado actual de la notificación
        created_at: Fecha de creación
        sent_at: Fecha de envío (None si no ha sido enviada)
        error_message: Mensaje de error si falló
        metadata: Datos adicionales en formato dict
    """
    recipient: str
    channel: NotificationChannel
    message: str
    subject: str | None = None
    id: int | None = None
    status: NotificationStatus = NotificationStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    sent_at: datetime | None = None
    error_message: str | None = None
    metadata: dict[str, str] = field(default_factory=dict)
    
    def mark_as_sent(self) -> None:
        """Marca la notificación como enviada."""
        self.status = NotificationStatus.SENT
        self.sent_at = datetime.now()
        self.error_message = None
    
    def mark_as_failed(self, error: str) -> None:
        """Marca la notificación como fallida."""
        self.status = NotificationStatus.FAILED
        self.error_message = error
    
    def cancel(self) -> None:
        """Cancela la notificación si está pendiente."""
        if self.status == NotificationStatus.PENDING:
            self.status = NotificationStatus.CANCELLED
    
    @property
    def is_sent(self) -> bool:
        """Indica si la notificación fue enviada."""
        return self.status == NotificationStatus.SENT
    
    @property
    def can_retry(self) -> bool:
        """Indica si se puede reintentar el envío."""
        return self.status == NotificationStatus.FAILED
