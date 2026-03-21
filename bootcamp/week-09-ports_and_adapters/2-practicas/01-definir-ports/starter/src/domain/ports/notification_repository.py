"""
Port: NotificationRepository

Define el contrato para persistir y recuperar notificaciones.
Permite guardar historial, consultar estados, etc.
"""
from typing import Protocol
from datetime import datetime

from ..entities import Notification, NotificationStatus, NotificationChannel


# ============================================
# PASO 3: Definir el Protocol NotificationRepository
# ============================================
# Este Port define cómo el dominio persiste notificaciones.
# La implementación puede ser SQLAlchemy, MongoDB, Redis, etc.

# Descomenta las siguientes líneas:

# class NotificationRepository(Protocol):
#     """
#     Port para persistencia de notificaciones.
#     
#     Define las operaciones CRUD y queries necesarias
#     para gestionar notificaciones en el sistema.
#     """
#     
#     async def save(self, notification: Notification) -> Notification:
#         """
#         Guarda una notificación (crear o actualizar).
#         
#         Si notification.id es None, crea una nueva.
#         Si notification.id existe, actualiza la existente.
#         
#         Args:
#             notification: Notificación a guardar
#             
#         Returns:
#             Notification: La notificación guardada (con id asignado si es nueva)
#         """
#         ...
#     
#     async def get_by_id(self, notification_id: int) -> Notification | None:
#         """
#         Obtiene una notificación por su ID.
#         
#         Args:
#             notification_id: ID de la notificación
#             
#         Returns:
#             Notification si existe, None si no
#         """
#         ...
#     
#     async def get_by_recipient(
#         self,
#         recipient: str,
#         limit: int = 100,
#         offset: int = 0
#     ) -> list[Notification]:
#         """
#         Obtiene notificaciones de un destinatario.
#         
#         Args:
#             recipient: Email, teléfono, etc. del destinatario
#             limit: Máximo de resultados
#             offset: Desplazamiento para paginación
#             
#         Returns:
#             Lista de notificaciones del destinatario
#         """
#         ...
#     
#     async def get_by_status(
#         self,
#         status: NotificationStatus,
#         limit: int = 100
#     ) -> list[Notification]:
#         """
#         Obtiene notificaciones por estado.
#         
#         Útil para procesar pendientes o reintentar fallidas.
#         
#         Args:
#             status: Estado a filtrar
#             limit: Máximo de resultados
#             
#         Returns:
#             Lista de notificaciones con ese estado
#         """
#         ...
#     
#     async def get_pending_before(
#         self,
#         before: datetime,
#         limit: int = 100
#     ) -> list[Notification]:
#         """
#         Obtiene notificaciones pendientes creadas antes de una fecha.
#         
#         Útil para detectar notificaciones "atascadas".
#         
#         Args:
#             before: Fecha límite
#             limit: Máximo de resultados
#             
#         Returns:
#             Lista de notificaciones pendientes antiguas
#         """
#         ...
#     
#     async def count_by_channel(
#         self,
#         channel: NotificationChannel,
#         since: datetime | None = None
#     ) -> int:
#         """
#         Cuenta notificaciones por canal.
#         
#         Args:
#             channel: Canal a contar
#             since: Fecha desde la cual contar (opcional)
#             
#         Returns:
#             Número de notificaciones
#         """
#         ...
#     
#     async def delete(self, notification_id: int) -> bool:
#         """
#         Elimina una notificación.
#         
#         Args:
#             notification_id: ID de la notificación a eliminar
#             
#         Returns:
#             True si se eliminó, False si no existía
#         """
#         ...


# Placeholder temporal
class NotificationRepository(Protocol):
    """Placeholder - reemplazar con el Protocol real."""
    ...
