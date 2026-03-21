"""
Fixtures de pytest para tests.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.main import app
from src.database import Base, get_db
from src.auth import create_access_token, get_password_hash
from src.models import User, Room


# Base de datos en memoria para tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """Crea DB fresca para cada test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    """Cliente de test con DB override."""
    def override_get_db():
        try:
            yield db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as c:
        yield c
    
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(db) -> User:
    """Crea un usuario de test."""
    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password=get_password_hash("testpass123")
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def test_user_token(test_user) -> str:
    """Token JWT para el usuario de test."""
    return create_access_token(data={
        "sub": str(test_user.id),
        "username": test_user.username
    })


@pytest.fixture
def auth_headers(test_user_token) -> dict:
    """Headers con autenticación."""
    return {"Authorization": f"Bearer {test_user_token}"}


@pytest.fixture
def test_room(db, test_user) -> Room:
    """Crea una sala de test."""
    room = Room(
        name="test-room",
        description="Room for testing",
        created_by_id=test_user.id
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room
