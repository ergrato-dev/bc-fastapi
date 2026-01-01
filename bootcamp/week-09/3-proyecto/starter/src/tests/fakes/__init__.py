"""
Fakes para testing del proyecto.
"""
from src.tests.fakes.fake_sender import FakeNotificationSender
from src.tests.fakes.fake_repository import FakeNotificationRepository

__all__ = ["FakeNotificationSender", "FakeNotificationRepository"]
