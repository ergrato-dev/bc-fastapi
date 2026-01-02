"""
Shared fixtures for mocking tests.
"""

import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture
def mock_email_sender():
    """Mock email sender that always succeeds."""
    sender = Mock()
    sender.send.return_value = True
    return sender


@pytest.fixture
def mock_payment_gateway():
    """Mock payment gateway."""
    gateway = Mock()
    gateway.charge.return_value = {
        "success": True,
        "payment_id": "pay_123abc",
    }
    return gateway


@pytest.fixture
def mock_inventory_service():
    """Mock inventory service."""
    service = Mock()
    service.check_stock.return_value = True
    service.get_price.return_value = 10.0
    service.reserve.return_value = True
    return service
