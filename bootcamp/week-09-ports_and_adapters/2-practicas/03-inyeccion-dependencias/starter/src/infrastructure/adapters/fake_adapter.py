"""FakeNotificationSender - para testing."""
from src.domain.entities import Notification, NotificationChannel


class FakeNotificationSender:
    """Fake sender para testing."""
    
    def __init__(self, channel: NotificationChannel = NotificationChannel.EMAIL):
        self._channel = channel
        self.sent: list[Notification] = []
        self.should_fail = False
    
    @property
    def channel(self) -> NotificationChannel:
        return self._channel
    
    async def send(self, notification: Notification) -> bool:
        if self.should_fail:
            return False
        self.sent.append(notification)
        return True
