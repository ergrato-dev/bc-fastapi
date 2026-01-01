"""
Adapter: SMSAdapter

Implementación del NotificationSender Protocol para envío de SMS.
"""
import logging
from dataclasses import dataclass

from src.domain.entities import Notification, NotificationChannel

logger = logging.getLogger(__name__)


@dataclass
class SMSConfig:
    """Configuración para SMS (ej: Twilio)."""
    account_sid: str = ""
    auth_token: str = ""
    from_number: str = "+1234567890"


# ============================================
# PASO 2: Implementar SMSAdapter
# ============================================

# Descomenta las siguientes líneas:

# class SMSAdapter:
#     """
#     Adapter para envío de SMS.
#     
#     Implementa NotificationSender Protocol.
#     """
#     
#     def __init__(self, config: SMSConfig):
#         self._config = config
#     
#     @property
#     def channel(self) -> NotificationChannel:
#         return NotificationChannel.SMS
#     
#     async def send(self, notification: Notification) -> bool:
#         """Simula envío de SMS."""
#         try:
#             if notification.channel != NotificationChannel.SMS:
#                 return False
#             
#             # Truncar mensaje a 160 caracteres (límite SMS)
#             message = notification.message[:160]
#             
#             logger.info(
#                 f"[SMS] Enviando a {notification.recipient}: "
#                 f"'{message}'"
#             )
#             
#             return True
#             
#         except Exception as e:
#             logger.error(f"[SMS] Error: {e}")
#             return False
#     
#     async def send_batch(
#         self,
#         notifications: list[Notification]
#     ) -> dict[int, bool]:
#         """Envía múltiples SMS."""
#         results: dict[int, bool] = {}
#         for n in notifications:
#             if n.id is not None:
#                 results[n.id] = await self.send(n)
#         return results


# Placeholder temporal
class SMSAdapter:
    """Placeholder."""
    def __init__(self, config: SMSConfig):
        self._config = config
    
    @property
    def channel(self) -> NotificationChannel:
        return NotificationChannel.SMS
    
    async def send(self, notification: Notification) -> bool:
        return True
    
    async def send_batch(self, notifications: list[Notification]) -> dict[int, bool]:
        return {}
