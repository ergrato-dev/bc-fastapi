"""
SpyNotificationSender - Spy para testing.

Este spy implementa el Protocol NotificationSender
y registra todas las llamadas para verificación.
"""
from dataclasses import dataclass, field
from datetime import datetime

from src.domain.entities import Notification, NotificationChannel


@dataclass
class SendCall:
    """Registro de una llamada a send()."""
    notification: Notification
    timestamp: datetime = field(default_factory=datetime.now)
    result: bool = True


# ============================================
# PASO 2: Implementar SpyNotificationSender
# ============================================
# Este spy registra todas las llamadas para verificar en tests.

# Descomenta las siguientes líneas:

# class SpyNotificationSender:
#     """
#     Spy sender para testing.
#     
#     Registra todas las llamadas a send() para verificación.
#     Permite configurar si debe fallar.
#     """
#     
#     def __init__(self, channel: NotificationChannel = NotificationChannel.EMAIL):
#         self._channel = channel
#         self.calls: list[SendCall] = []
#         self.should_fail: bool = False
#     
#     @property
#     def channel(self) -> NotificationChannel:
#         return self._channel
#     
#     async def send(self, notification: Notification) -> bool:
#         """
#         Registra la llamada y retorna según configuración.
#         """
#         result = not self.should_fail
#         
#         self.calls.append(SendCall(
#             notification=notification,
#             result=result,
#         ))
#         
#         return result
#     
#     # Métodos de verificación para tests
#     
#     def was_called(self) -> bool:
#         """Verifica si se llamó al menos una vez."""
#         return len(self.calls) > 0
#     
#     def call_count(self) -> int:
#         """Retorna número de llamadas."""
#         return len(self.calls)
#     
#     def was_called_with_recipient(self, recipient: str) -> bool:
#         """Verifica si se llamó con este recipient."""
#         return any(c.notification.recipient == recipient for c in self.calls)
#     
#     def last_call(self) -> SendCall | None:
#         """Retorna la última llamada."""
#         return self.calls[-1] if self.calls else None
#     
#     def reset(self) -> None:
#         """Limpia historial de llamadas."""
#         self.calls.clear()
#         self.should_fail = False


# Placeholder temporal
class SpyNotificationSender:
    """Placeholder."""
    def __init__(self, channel: NotificationChannel = NotificationChannel.EMAIL):
        self._channel = channel
        self.calls: list[SendCall] = []
        self.should_fail: bool = False
    
    @property
    def channel(self) -> NotificationChannel:
        return self._channel
    
    async def send(self, notification: Notification) -> bool:
        result = not self.should_fail
        self.calls.append(SendCall(notification=notification, result=result))
        return result
    
    def was_called(self) -> bool:
        return len(self.calls) > 0
    
    def call_count(self) -> int:
        return len(self.calls)
    
    def was_called_with_recipient(self, recipient: str) -> bool:
        return any(c.notification.recipient == recipient for c in self.calls)
    
    def last_call(self) -> SendCall | None:
        return self.calls[-1] if self.calls else None
    
    def reset(self) -> None:
        self.calls.clear()
        self.should_fail = False
