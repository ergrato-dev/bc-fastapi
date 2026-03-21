"""Entidad Notification."""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class NotificationStatus(Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"


class NotificationChannel(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"


@dataclass
class Notification:
    recipient: str
    channel: NotificationChannel
    message: str
    subject: str | None = None
    id: int | None = None
    status: NotificationStatus = NotificationStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    sent_at: datetime | None = None
    error_message: str | None = None
    
    def mark_as_sent(self) -> None:
        self.status = NotificationStatus.SENT
        self.sent_at = datetime.now()
    
    def mark_as_failed(self, error: str) -> None:
        self.status = NotificationStatus.FAILED
        self.error_message = error
