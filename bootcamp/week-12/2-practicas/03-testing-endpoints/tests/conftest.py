"""
Fixtures for FastAPI testing.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.main import app
from src.database import Base, get_db
from src.models import User, Item
from src.auth import get_password_hash, create_access_token


# Test database in memory
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database for each test."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    
    yield session
    
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client with database override."""
    def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(db_session):
    """Create a test user in the database."""
    user = User(
        email="test@example.com",
        hashed_password=get_password_hash("testpassword123"),
        full_name="Test User",
        is_active=True,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def test_user_token(test_user):
    """Create an access token for the test user."""
    return create_access_token(data={"sub": test_user.email})


@pytest.fixture
def auth_headers(test_user_token):
    """Headers with authorization token."""
    return {"Authorization": f"Bearer {test_user_token}"}


@pytest.fixture
def test_item(db_session, test_user):
    """Create a test item in the database."""
    item = Item(
        name="Test Item",
        description="A test item description",
        price=29.99,
        owner_id=test_user.id,
    )
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)
    return item


@pytest.fixture
def other_user(db_session):
    """Create another user (for permission tests)."""
    user = User(
        email="other@example.com",
        hashed_password=get_password_hash("otherpassword"),
        full_name="Other User",
        is_active=True,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def other_user_headers(other_user):
    """Headers for the other user."""
    token = create_access_token(data={"sub": other_user.email})
    return {"Authorization": f"Bearer {token}"}
