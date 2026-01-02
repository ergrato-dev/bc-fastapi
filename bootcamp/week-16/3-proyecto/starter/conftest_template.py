"""
============================================
PROYECTO FINAL - Template de conftest.py
============================================

Fixtures de pytest para tests de tu API FastAPI.
Copia y adapta a tu proyecto.
"""

import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# Importa tu app y dependencias
# from src.main import app
# from src.database import get_db
# from src.models.base import Base
# from src.models.user import User
# from src.utils.security import hash_password


# ============================================
# DATABASE FIXTURES
# ============================================

# URL de base de datos para tests (SQLite en memoria)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def anyio_backend():
    """Backend para pytest-asyncio."""
    return "asyncio"


@pytest.fixture(scope="function")
async def test_engine():
    """
    Crea un engine de base de datos para tests.
    Scope 'function' asegura DB limpia por test.
    """
    engine = create_async_engine(
        TEST_DATABASE_URL,
        echo=False,  # True para debug de queries
    )
    
    # Crear tablas
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    # Limpiar después del test
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()


@pytest.fixture(scope="function")
async def db_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """
    Proporciona una sesión de DB para cada test.
    """
    async_session = async_sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    
    async with async_session() as session:
        yield session
        await session.rollback()


# ============================================
# CLIENT FIXTURES
# ============================================

@pytest.fixture(scope="function")
async def client(db_session) -> AsyncGenerator[AsyncClient, None]:
    """
    Cliente HTTP para tests de la API.
    Sobrescribe la dependencia get_db con la sesión de test.
    """
    # def override_get_db():
    #     yield db_session
    
    # app.dependency_overrides[get_db] = override_get_db
    
    # async with AsyncClient(
    #     transport=ASGITransport(app=app),
    #     base_url="http://test"
    # ) as ac:
    #     yield ac
    
    # app.dependency_overrides.clear()
    
    # Placeholder hasta que configures tu app
    yield None


# ============================================
# USER FIXTURES
# ============================================

@pytest.fixture
async def test_user(db_session) -> dict:
    """
    Crea un usuario de prueba en la DB.
    Retorna dict con datos del usuario.
    """
    user_data = {
        "email": "test@example.com",
        "password": "TestPassword123!",
        "full_name": "Test User",
    }
    
    # user = User(
    #     email=user_data["email"],
    #     hashed_password=hash_password(user_data["password"]),
    #     full_name=user_data["full_name"],
    # )
    # db_session.add(user)
    # await db_session.commit()
    # await db_session.refresh(user)
    
    # user_data["id"] = user.id
    return user_data


@pytest.fixture
async def test_admin(db_session) -> dict:
    """
    Crea un usuario admin de prueba.
    """
    admin_data = {
        "email": "admin@example.com",
        "password": "AdminPassword123!",
        "full_name": "Admin User",
        "is_admin": True,
    }
    
    # admin = User(
    #     email=admin_data["email"],
    #     hashed_password=hash_password(admin_data["password"]),
    #     full_name=admin_data["full_name"],
    #     is_admin=True,
    # )
    # db_session.add(admin)
    # await db_session.commit()
    # await db_session.refresh(admin)
    
    # admin_data["id"] = admin.id
    return admin_data


# ============================================
# AUTH FIXTURES
# ============================================

@pytest.fixture
async def auth_headers(client, test_user) -> dict:
    """
    Retorna headers con token de autenticación.
    Útil para tests de endpoints protegidos.
    """
    # Login para obtener token
    # response = await client.post(
    #     "/api/v1/auth/login",
    #     data={
    #         "username": test_user["email"],
    #         "password": test_user["password"],
    #     }
    # )
    # token = response.json()["access_token"]
    # return {"Authorization": f"Bearer {token}"}
    
    return {"Authorization": "Bearer test-token"}


@pytest.fixture
async def admin_headers(client, test_admin) -> dict:
    """
    Headers con token de admin.
    """
    # response = await client.post(
    #     "/api/v1/auth/login",
    #     data={
    #         "username": test_admin["email"],
    #         "password": test_admin["password"],
    #     }
    # )
    # token = response.json()["access_token"]
    # return {"Authorization": f"Bearer {token}"}
    
    return {"Authorization": "Bearer admin-token"}


# ============================================
# DATA FIXTURES
# ============================================

@pytest.fixture
async def sample_project(db_session, test_user) -> dict:
    """
    Crea un proyecto de prueba.
    """
    project_data = {
        "name": "Test Project",
        "description": "A test project for testing",
    }
    
    # project = Project(
    #     name=project_data["name"],
    #     description=project_data["description"],
    #     owner_id=test_user["id"],
    # )
    # db_session.add(project)
    # await db_session.commit()
    # await db_session.refresh(project)
    
    # project_data["id"] = project.id
    return project_data


@pytest.fixture
async def sample_task(db_session, sample_project, test_user) -> dict:
    """
    Crea una tarea de prueba.
    """
    task_data = {
        "title": "Test Task",
        "description": "A test task",
        "priority": "medium",
    }
    
    # task = Task(
    #     title=task_data["title"],
    #     description=task_data["description"],
    #     priority=task_data["priority"],
    #     project_id=sample_project["id"],
    #     assignee_id=test_user["id"],
    # )
    # db_session.add(task)
    # await db_session.commit()
    # await db_session.refresh(task)
    
    # task_data["id"] = task.id
    return task_data


# ============================================
# UTILITY FUNCTIONS
# ============================================

def assert_response_ok(response, expected_status: int = 200):
    """Helper para verificar response exitoso."""
    assert response.status_code == expected_status, (
        f"Expected {expected_status}, got {response.status_code}: {response.text}"
    )


def assert_response_error(response, expected_status: int, detail_contains: str = None):
    """Helper para verificar response de error."""
    assert response.status_code == expected_status
    if detail_contains:
        assert detail_contains.lower() in response.json().get("detail", "").lower()
