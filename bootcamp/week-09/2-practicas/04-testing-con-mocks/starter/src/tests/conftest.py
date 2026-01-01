"""
Conftest - Fixtures compartidos para tests.
"""
import pytest

from src.domain.entities import NotificationChannel
from src.application import NotificationService
from src.tests.fakes import FakeNotificationRepository, SpyNotificationSender


# ============================================
# PASO 3: Configurar fixtures
# ============================================

# Descomenta las siguientes líneas:

# @pytest.fixture
# def fake_repository():
#     """Fake repository limpio para cada test."""
#     return FakeNotificationRepository()
# 
# 
# @pytest.fixture
# def spy_email_sender():
#     """Spy sender para emails."""
#     return SpyNotificationSender(NotificationChannel.EMAIL)
# 
# 
# @pytest.fixture
# def spy_sms_sender():
#     """Spy sender para SMS."""
#     return SpyNotificationSender(NotificationChannel.SMS)
# 
# 
# @pytest.fixture
# def notification_service(fake_repository, spy_email_sender, spy_sms_sender):
#     """
#     NotificationService con todas las dependencias fake.
#     
#     Este service es idéntico al de producción pero usa fakes.
#     """
#     return NotificationService(
#         repository=fake_repository,
#         email_sender=spy_email_sender,
#         sms_sender=spy_sms_sender,
#     )


# Placeholders temporales
@pytest.fixture
def fake_repository():
    return FakeNotificationRepository()

@pytest.fixture
def spy_email_sender():
    return SpyNotificationSender(NotificationChannel.EMAIL)

@pytest.fixture
def spy_sms_sender():
    return SpyNotificationSender(NotificationChannel.SMS)

@pytest.fixture
def notification_service(fake_repository, spy_email_sender, spy_sms_sender):
    return NotificationService(
        repository=fake_repository,
        email_sender=spy_email_sender,
        sms_sender=spy_sms_sender,
    )
