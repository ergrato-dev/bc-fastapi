"""
Fixtures compartidas para tests.

TODO: Implementar las fixtures necesarias para los tests.

Fixtures requeridas:
1. engine - Engine de base de datos de prueba
2. db_session - Sesión de BD fresca para cada test
3. client - TestClient con BD override
4. test_user - Usuario de prueba en BD
5. test_user_token - Token JWT para test_user
6. auth_headers - Headers con Authorization
7. test_task - Tarea de prueba
8. other_user - Otro usuario (para tests de permisos)
9. mock_notification_service - Mock del servicio de notificaciones
"""

import pytest

# TODO: Importar las dependencias necesarias
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.pool import StaticPool
# from unittest.mock import Mock

# from src.main import app
# from src.database import Base, get_db
# from src.models import User, Task
# from src.auth import get_password_hash, create_access_token


# ============================================
# TODO: Configuración de BD de prueba
# ============================================

# TEST_DATABASE_URL = "sqlite:///:memory:"

# TODO: Crear engine con StaticPool para SQLite en memoria
# engine = ...


# ============================================
# TODO: Fixture de sesión de BD
# ============================================

# @pytest.fixture(scope="function")
# def db_session():
#     """
#     Crear sesión de BD fresca para cada test.
    
#     Debe:
#     1. Crear todas las tablas
#     2. Crear sesión
#     3. yield sesión
#     4. Cerrar sesión
#     5. Eliminar tablas
#     """
#     # TODO: Implementar
#     pass


# ============================================
# TODO: Fixture de TestClient
# ============================================

# @pytest.fixture(scope="function")
# def client(db_session):
#     """
#     TestClient con BD de prueba.
    
#     Debe:
#     1. Override de get_db dependency
#     2. yield TestClient
#     3. Limpiar overrides
#     """
#     # TODO: Implementar
#     pass


# ============================================
# TODO: Fixture de usuario de prueba
# ============================================

# @pytest.fixture
# def test_user(db_session):
#     """
#     Crear usuario de prueba en BD.
    
#     Datos sugeridos:
#     - email: "test@example.com"
#     - password: "testpassword123"
#     - full_name: "Test User"
#     """
#     # TODO: Implementar
#     pass


# ============================================
# TODO: Fixture de token de autenticación
# ============================================

# @pytest.fixture
# def test_user_token(test_user):
#     """Crear token JWT para test_user."""
#     # TODO: Implementar
#     pass


# @pytest.fixture
# def auth_headers(test_user_token):
#     """Headers con Authorization Bearer."""
#     # TODO: Implementar
#     pass


# ============================================
# TODO: Fixture de tarea de prueba
# ============================================

# @pytest.fixture
# def test_task(db_session, test_user):
#     """
#     Crear tarea de prueba en BD.
    
#     Datos sugeridos:
#     - title: "Test Task"
#     - description: "A test task"
#     - priority: "medium"
#     - owner_id: test_user.id
#     """
#     # TODO: Implementar
#     pass


# ============================================
# TODO: Fixture de otro usuario (para permisos)
# ============================================

# @pytest.fixture
# def other_user(db_session):
#     """Otro usuario para tests de permisos."""
#     # TODO: Implementar
#     pass


# @pytest.fixture
# def other_user_headers(other_user):
#     """Headers de autorización del otro usuario."""
#     # TODO: Implementar
#     pass


# ============================================
# TODO: Mock de NotificationService
# ============================================

# @pytest.fixture
# def mock_notification_service():
#     """
#     Mock del servicio de notificaciones.
    
#     Debe mockear:
#     - notify_task_completed() -> return True
#     - notify_task_due_soon() -> return True
#     """
#     # TODO: Implementar
#     pass
