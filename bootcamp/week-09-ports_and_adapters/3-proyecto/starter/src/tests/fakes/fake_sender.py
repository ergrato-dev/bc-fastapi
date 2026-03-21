"""
FakeNotificationSender - Fake para testing.
"""
from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entities.notification import Notification, NotificationChannel


@dataclass
class SendCall:
    """Registro de una llamada a send()."""
    notification: Notification
    timestamp: datetime = field(default_factory=datetime.now)


class FakeNotificationSender:
    """
    Fake sender para testing.
    
    - Registra todas las llamadas a send()
    - Permite configurar si debe fallar o no
    - Permite verificar qué notificaciones se "enviaron"
    """
    
    def __init__(
        self,
        channel: NotificationChannel = NotificationChannel.EMAIL,
        should_fail: bool = False,
    ):
        self._channel = channel
        self._should_fail = should_fail
        self._calls: list[SendCall] = []
    
    @property
    def channel(self) -> NotificationChannel:
        return self._channel
    
    async def send(self, notification: Notification) -> bool:
        """Registra la llamada y retorna según configuración."""
        self._calls.append(SendCall(notification=notification))
        return not self._should_fail
    
    async def send_batch(self, notifications: list[Notification]) -> dict[str, bool]:
        """Envía cada notificación y retorna resultados."""
        results = {}
        for notification in notifications:
            results[notification.id] = await self.send(notification)
        return results
    
    # Métodos de verificación para tests
    
    def was_called(self) -> bool:
        """Verifica si se llamó al menos una vez."""
        return len(self._calls) > 0
    
    def call_count(self) -> int:
        """Retorna número de llamadas."""
        return len(self._calls)
    
    def get_calls(self) -> list[SendCall]:
        """Retorna todas las llamadas."""
        return self._calls.copy()
    
    def get_last_call(self) -> SendCall | None:
        """Retorna la última llamada o None."""
        return self._calls[-1] if self._calls else None
    
    def reset(self) -> None:
        """Limpia el historial de llamadas."""
        self._calls.clear()
    
    def set_should_fail(self, should_fail: bool) -> None:
        """Configura si debe fallar."""
        self._should_fail = should_fail
