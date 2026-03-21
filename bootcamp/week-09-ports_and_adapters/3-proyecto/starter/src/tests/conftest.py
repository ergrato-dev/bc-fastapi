"""
Pytest configuration and fixtures.
"""
import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app
from src.domain.entities.notification import NotificationChannel
from src.application.services.notification_service import NotificationService
from src.tests.fakes.fake_sender import FakeNotificationSender
from src.tests.fakes.fake_repository import FakeNotificationRepository
from src.presentation.dependencies import (
    override_service,
    override_repository,
    reset_dependencies,
)


@pytest.fixture
def fake_repository():
    """Fixture: repositorio fake."""
    return FakeNotificationRepository()


@pytest.fixture
def fake_email_sender():
    """Fixture: sender fake para email."""
    return FakeNotificationSender(channel=NotificationChannel.EMAIL)


@pytest.fixture
def fake_sms_sender():
    """Fixture: sender fake para SMS."""
    return FakeNotificationSender(channel=NotificationChannel.SMS)


@pytest.fixture
def fake_senders(fake_email_sender, fake_sms_sender):
    """Fixture: diccionario de senders fake."""
    return {
        NotificationChannel.EMAIL: fake_email_sender,
        NotificationChannel.SMS: fake_sms_sender,
    }


@pytest.fixture
def notification_service(fake_senders, fake_repository):
    """Fixture: servicio con fakes inyectados."""
    return NotificationService(
        senders=fake_senders,
        repository=fake_repository,
    )


@pytest.fixture
async def test_client(notification_service, fake_repository):
    """Fixture: cliente HTTP para tests de integración."""
    # Sobrescribir dependencias
    override_service(notification_service)
    override_repository(fake_repository)
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
    
    # Limpiar después del test
    reset_dependencies()
