"""
Adapter: ConsoleAdapter

Adapter para desarrollo que imprime notificaciones en consola.
Útil para debugging y desarrollo local.
"""
from src.domain.entities import Notification, NotificationChannel


# ============================================
# PASO 3: Implementar ConsoleAdapter
# ============================================

# Descomenta las siguientes líneas:

# class ConsoleAdapter:
#     """
#     Adapter que imprime en consola.
#     
#     Útil para desarrollo y debugging.
#     No envía notificaciones reales.
#     """
#     
#     def __init__(self, channel: NotificationChannel = NotificationChannel.EMAIL):
#         """
#         Args:
#             channel: Canal a simular (para testing)
#         """
#         self._channel = channel
#     
#     @property
#     def channel(self) -> NotificationChannel:
#         return self._channel
#     
#     async def send(self, notification: Notification) -> bool:
#         """Imprime la notificación en consola."""
#         print("=" * 50)
#         print(f"📧 NOTIFICACIÓN [{notification.channel.value.upper()}]")
#         print("=" * 50)
#         print(f"Para: {notification.recipient}")
#         if notification.subject:
#             print(f"Asunto: {notification.subject}")
#         print(f"Mensaje: {notification.message}")
#         print(f"Estado: {notification.status.value}")
#         print("=" * 50)
#         return True
#     
#     async def send_batch(
#         self,
#         notifications: list[Notification]
#     ) -> dict[int, bool]:
#         """Imprime todas las notificaciones."""
#         results: dict[int, bool] = {}
#         for n in notifications:
#             if n.id is not None:
#                 results[n.id] = await self.send(n)
#         return results


# Placeholder temporal
class ConsoleAdapter:
    """Placeholder."""
    def __init__(self, channel: NotificationChannel = NotificationChannel.EMAIL):
        self._channel = channel
    
    @property
    def channel(self) -> NotificationChannel:
        return self._channel
    
    async def send(self, notification: Notification) -> bool:
        return True
    
    async def send_batch(self, notifications: list[Notification]) -> dict[int, bool]:
        return {}
