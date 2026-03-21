"""
Port: NotificationSender

Define el contrato para enviar notificaciones a través de diferentes canales.
El dominio usa este Protocol sin conocer la implementación concreta.
"""
from typing import Protocol

from ..entities import Notification, NotificationChannel


# ============================================
# PASO 1: Definir el Protocol NotificationSender
# ============================================
# Este Port define cómo el dominio envía notificaciones.
# La implementación puede ser Email, SMS, Push, Webhook, etc.

# Descomenta las siguientes líneas:

# class NotificationSender(Protocol):
#     """
#     Port para envío de notificaciones.
#     
#     Este Protocol define el contrato que deben cumplir
#     todos los adapters de envío de notificaciones.
#     
#     Implementaciones posibles:
#     - EmailAdapter (SMTP, SendGrid, etc.)
#     - SMSAdapter (Twilio, AWS SNS, etc.)
#     - PushAdapter (Firebase, OneSignal, etc.)
#     - WebhookAdapter (HTTP POST a URLs)
#     """
#     
#     @property
#     def channel(self) -> NotificationChannel:
#         """
#         Canal de notificación que implementa este sender.
#         
#         Returns:
#             NotificationChannel: El tipo de canal (EMAIL, SMS, etc.)
#         """
#         ...
#     
#     async def send(self, notification: Notification) -> bool:
#         """
#         Envía una notificación.
#         
#         Este método debe:
#         1. Intentar enviar la notificación
#         2. NO modificar el estado de la notificación (eso lo hace el servicio)
#         3. Retornar True si el envío fue exitoso
#         4. Retornar False si falló (no lanzar excepciones)
#         
#         Args:
#             notification: La notificación a enviar
#             
#         Returns:
#             bool: True si se envió correctamente, False si falló
#         """
#         ...
#     
#     async def send_batch(
#         self,
#         notifications: list[Notification]
#     ) -> dict[int, bool]:
#         """
#         Envía múltiples notificaciones en lote.
#         
#         Útil para optimizar envíos masivos (ej: campañas de email).
#         
#         Args:
#             notifications: Lista de notificaciones a enviar
#             
#         Returns:
#             dict: Mapeo de notification.id -> resultado (True/False)
#         """
#         ...


# ============================================
# PASO 2: Verificar que el Protocol está bien definido
# ============================================
# Ejecuta: uv run mypy src/domain/ports/notification_sender.py
# No debe haber errores de tipo


# Placeholder temporal para que el import funcione
# ELIMINA ESTO cuando desccomentes el Protocol de arriba
class NotificationSender(Protocol):
    """Placeholder - reemplazar con el Protocol real."""
    ...
