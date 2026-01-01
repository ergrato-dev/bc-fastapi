"""
Dependencies - Factories para inyección de dependencias.

Aquí se decide QUÉ implementación usar según la configuración.
"""
from typing import Annotated
from fastapi import Depends

from src.config import settings, Environment
from src.domain.ports import NotificationSender, NotificationRepository
from src.domain.entities import NotificationChannel
from src.infrastructure.adapters import (
    ConsoleAdapter,
    InMemoryNotificationRepository,
    FakeNotificationSender,
)
from src.application.services import NotificationService


# ============================================
# Instancias singleton (para desarrollo)
# ============================================
_repository = InMemoryNotificationRepository()


# ============================================
# PASO 3: Implementar factories de dependencias
# ============================================
# Las factories deciden qué adapter crear según configuración.

# Descomenta las siguientes líneas:

# def get_notification_repository() -> NotificationRepository:
#     """
#     Factory para el repositorio.
#     
#     En producción podría retornar SQLAlchemyNotificationRepository.
#     """
#     return _repository
# 
# 
# def get_email_sender() -> NotificationSender:
#     """
#     Factory para el sender de email.
#     
#     Retorna diferente adapter según el entorno.
#     """
#     if settings.env == Environment.TEST:
#         return FakeNotificationSender(NotificationChannel.EMAIL)
#     
#     # En desarrollo usamos console
#     return ConsoleAdapter(NotificationChannel.EMAIL)
# 
# 
# def get_sms_sender() -> NotificationSender:
#     """
#     Factory para el sender de SMS.
#     """
#     if settings.env == Environment.TEST:
#         return FakeNotificationSender(NotificationChannel.SMS)
#     
#     return ConsoleAdapter(NotificationChannel.SMS)
# 
# 
# def get_notification_service(
#     repository: Annotated[NotificationRepository, Depends(get_notification_repository)],
#     email_sender: Annotated[NotificationSender, Depends(get_email_sender)],
#     sms_sender: Annotated[NotificationSender, Depends(get_sms_sender)],
# ) -> NotificationService:
#     """
#     Factory para el NotificationService.
#     
#     FastAPI inyecta automáticamente las dependencias.
#     """
#     return NotificationService(
#         repository=repository,
#         email_sender=email_sender,
#         sms_sender=sms_sender,
#     )


# Placeholders temporales
def get_notification_repository() -> NotificationRepository:
    return _repository

def get_email_sender() -> NotificationSender:
    return ConsoleAdapter(NotificationChannel.EMAIL)

def get_sms_sender() -> NotificationSender:
    return ConsoleAdapter(NotificationChannel.SMS)

def get_notification_service(
    repository: Annotated[NotificationRepository, Depends(get_notification_repository)],
    email_sender: Annotated[NotificationSender, Depends(get_email_sender)],
    sms_sender: Annotated[NotificationSender, Depends(get_sms_sender)],
) -> NotificationService:
    return NotificationService(
        repository=repository,
        email_sender=email_sender,
        sms_sender=sms_sender,
    )
