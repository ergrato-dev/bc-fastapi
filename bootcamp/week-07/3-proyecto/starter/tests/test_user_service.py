# ============================================
# Tests para UserService
# ============================================
"""
Tests unitarios para UserService usando FakeRepositories.

TODO: Implementar tests:
- test_create_user_success
- test_create_user_duplicate_username
- test_create_user_duplicate_email
- test_get_user_success
- test_get_user_not_found
- test_update_user_success
- test_delete_user_success
"""

import pytest

from src.schemas.user import UserCreate, UserUpdate
from src.services.user import UserService, UserNotFoundError, UserAlreadyExistsError
from tests.fakes.repositories import FakeUnitOfWork


class TestUserService:
    """Tests para UserService"""
    
    def test_create_user_success(self):
        """
        TODO: Implementar
        1. Crear FakeUnitOfWork
        2. Crear UserService con fake UoW
        3. Llamar create_user con datos válidos
        4. Verificar usuario creado correctamente
        """
        pass
    
    def test_create_user_duplicate_username(self):
        """
        TODO: Implementar
        Verificar que lanza UserAlreadyExistsError
        si el username ya existe
        """
        pass
    
    def test_create_user_duplicate_email(self):
        """
        TODO: Implementar
        Verificar que lanza UserAlreadyExistsError
        si el email ya existe
        """
        pass
    
    def test_get_user_success(self):
        """
        TODO: Implementar
        1. Crear usuario
        2. Obtenerlo por ID
        3. Verificar datos
        """
        pass
    
    def test_get_user_not_found(self):
        """
        TODO: Implementar
        Verificar que lanza UserNotFoundError
        si el usuario no existe
        """
        pass
    
    def test_update_user_success(self):
        """
        TODO: Implementar
        1. Crear usuario
        2. Actualizarlo
        3. Verificar cambios
        """
        pass
    
    def test_delete_user_success(self):
        """
        TODO: Implementar
        1. Crear usuario
        2. Eliminarlo
        3. Verificar que ya no existe
        """
        pass
