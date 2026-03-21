"""Port: NotificationSender."""
from typing import Protocol
from ..entities import Notification, NotificationChannel


class NotificationSender(Protocol):
    @property
    def channel(self) -> NotificationChannel: ...
    async def send(self, notification: Notification) -> bool: ...
