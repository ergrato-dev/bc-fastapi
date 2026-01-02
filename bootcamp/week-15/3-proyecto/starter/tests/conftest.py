# ============================================
# Pytest Fixtures
# Semana 15 - Proyecto Integrador
# ============================================

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    """Reset fake database before each test"""
    from src.routers import tasks

    tasks.fake_db.clear()
    tasks.counter = 0
    yield
