"""
Adapter: EmailAdapter

Implementación del NotificationSender Protocol para envío de emails.
En esta práctica es simulado (no envía emails reales).
"""
import logging
from dataclasses import dataclass

from src.domain.entities import Notification, NotificationChannel

logger = logging.getLogger(__name__)


# ============================================
# Configuración del adapter
# ============================================
@dataclass
class EmailConfig:
    """Configuración para el EmailAdapter."""
    smtp_host: str = "localhost"
    smtp_port: int = 587
    username: str = ""
    password: str = ""
    from_address: str = "noreply@example.com"
    use_tls: bool = True


# ============================================
# PASO 1: Implementar EmailAdapter
# ============================================
# Este adapter implementa NotificationSender Protocol
# SIN heredar de él (duck typing).

# Descomenta las siguientes líneas:

# class EmailAdapter:
#     """
#     Adapter para envío de emails.
#     
#     Implementa NotificationSender Protocol.
#     En producción usaría aiosmtplib o similar.
#     """
#     
#     def __init__(self, config: EmailConfig):
#         """
#         Constructor recibe configuración inyectada.
#         
#         Args:
#             config: Configuración SMTP
#         """
#         self._config = config
#     
#     @property
#     def channel(self) -> NotificationChannel:
#         """Retorna el canal EMAIL."""
#         return NotificationChannel.EMAIL
#     
#     async def send(self, notification: Notification) -> bool:
#         """
#         Simula envío de email.
#         
#         En producción, aquí iría la lógica real de SMTP.
#         """
#         try:
#             # Validar que es el canal correcto
#             if notification.channel != NotificationChannel.EMAIL:
#                 logger.warning(
#                     f"EmailAdapter recibió notificación de canal "
#                     f"{notification.channel.value}"
#                 )
#                 return False
#             
#             # Simular envío (en producción: aiosmtplib)
#             logger.info(
#                 f"[EMAIL] Enviando a {notification.recipient}: "
#                 f"'{notification.subject}'"
#             )
#             
#             # Simular latencia de red
#             # await asyncio.sleep(0.1)
#             
#             logger.info(f"[EMAIL] Enviado exitosamente a {notification.recipient}")
#             return True
#             
#         except Exception as e:
#             logger.error(f"[EMAIL] Error enviando a {notification.recipient}: {e}")
#             return False
#     
#     async def send_batch(
#         self,
#         notifications: list[Notification]
#     ) -> dict[int, bool]:
#         """
#         Envía múltiples emails.
#         
#         En producción podría optimizarse con conexión SMTP persistente.
#         """
#         results: dict[int, bool] = {}
#         
#         for notification in notifications:
#             if notification.id is not None:
#                 result = await self.send(notification)
#                 results[notification.id] = result
#         
#         return results


# Placeholder temporal - ELIMINAR cuando desccomentes el código
class EmailAdapter:
    """Placeholder."""
    def __init__(self, config: EmailConfig):
        self._config = config
    
    @property
    def channel(self) -> NotificationChannel:
        return NotificationChannel.EMAIL
    
    async def send(self, notification: Notification) -> bool:
        return True
    
    async def send_batch(self, notifications: list[Notification]) -> dict[int, bool]:
        return {}
