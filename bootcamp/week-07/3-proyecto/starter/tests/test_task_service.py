# ============================================
# Tests para TaskService
# ============================================
"""
Tests unitarios para TaskService usando FakeRepositories.

TODO: Implementar tests:
- test_create_task_success
- test_create_task_user_not_found
- test_get_task_success
- test_get_task_not_found
- test_complete_task_success
- test_reopen_task_success
- test_get_user_tasks
"""

import pytest

from src.models.task import Priority
from src.schemas.task import TaskCreate, TaskUpdate
from src.services.task import TaskService, TaskNotFoundError
from src.services.user import UserNotFoundError
from tests.fakes.repositories import FakeUnitOfWork


class TestTaskService:
    """Tests para TaskService"""
    
    def test_create_task_success(self):
        """
        TODO: Implementar
        1. Crear usuario primero
        2. Crear tarea para ese usuario
        3. Verificar tarea creada
        """
        pass
    
    def test_create_task_user_not_found(self):
        """
        TODO: Implementar
        Verificar que lanza UserNotFoundError
        si el usuario no existe
        """
        pass
    
    def test_get_task_success(self):
        """
        TODO: Implementar
        """
        pass
    
    def test_get_task_not_found(self):
        """
        TODO: Implementar
        """
        pass
    
    def test_complete_task_success(self):
        """
        TODO: Implementar
        1. Crear tarea pendiente
        2. Marcarla como completada
        3. Verificar is_completed=True
        4. Verificar completed_at no es None
        """
        pass
    
    def test_reopen_task_success(self):
        """
        TODO: Implementar
        1. Crear tarea completada
        2. Reabrirla
        3. Verificar is_completed=False
        4. Verificar completed_at es None
        """
        pass
    
    def test_get_user_tasks(self):
        """
        TODO: Implementar
        1. Crear usuario
        2. Crear varias tareas para el usuario
        3. Obtener tareas del usuario
        4. Verificar lista correcta
        """
        pass
