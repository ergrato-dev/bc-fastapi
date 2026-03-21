"""
Tests demonstrating mocking techniques.

Instrucciones:
1. Descomenta cada sección de tests
2. Ejecuta `uv run pytest tests/test_mocking.py -v -s`
3. Observa cómo funcionan los mocks
"""

import pytest
from unittest.mock import Mock, MagicMock, call

from src.services import UserService, OrderService


# ============================================
# PASO 1: Mock básico
# ============================================
print("--- Paso 1: Mock básico ---")

# Descomenta las siguientes líneas:

# def test_mock_basic():
#     """Crear y configurar un mock básico."""
#     # Crear mock
#     mock = Mock()
    
#     # Configurar retorno
#     mock.some_method.return_value = "mocked value"
    
#     # Usar el mock
#     result = mock.some_method()
    
#     # Verificar
#     assert result == "mocked value"
#     mock.some_method.assert_called_once()


# def test_mock_with_arguments():
#     """Mock que verifica argumentos."""
#     mock = Mock()
#     mock.greet.return_value = "Hello, John!"
    
#     # Llamar con argumentos
#     result = mock.greet("John")
    
#     # Verificar argumentos
#     mock.greet.assert_called_once_with("John")
#     assert result == "Hello, John!"


# ============================================
# PASO 2: Usar Mock en UserService
# ============================================
print("--- Paso 2: Mock en servicio ---")

# Descomenta las siguientes líneas:

# def test_user_service_register(mock_email_sender):
#     """Test de registro con email mockeado."""
#     # El mock viene del conftest.py
#     service = UserService(email_sender=mock_email_sender)
    
#     # Ejecutar
#     user = service.register_user("test@example.com", "Test User")
    
#     # Verificar usuario creado
#     assert user["email"] == "test@example.com"
#     assert user["name"] == "Test User"
    
#     # Verificar que se envió email
#     mock_email_sender.send.assert_called_once_with(
#         to="test@example.com",
#         subject="Welcome to our platform!",
#         body="Hello Test User, welcome aboard!"
#     )


# def test_user_service_reset_password(mock_email_sender):
#     """Test de reset de password."""
#     service = UserService(email_sender=mock_email_sender)
    
#     result = service.reset_password("user@example.com")
    
#     assert result is True
#     mock_email_sender.send.assert_called_once()
    
#     # Verificar argumentos de la llamada
#     call_args = mock_email_sender.send.call_args
#     assert call_args.kwargs["to"] == "user@example.com"
#     assert "Password Reset" in call_args.kwargs["subject"]


# ============================================
# PASO 3: Mock con side_effect
# ============================================
print("--- Paso 3: side_effect ---")

# Descomenta las siguientes líneas:

# def test_mock_side_effect_exception():
#     """Mock que lanza excepción."""
#     mock = Mock()
#     mock.risky_operation.side_effect = ValueError("Something went wrong")
    
#     with pytest.raises(ValueError, match="Something went wrong"):
#         mock.risky_operation()


# def test_mock_side_effect_multiple_returns():
#     """Mock que retorna diferentes valores."""
#     mock = Mock()
#     mock.get_next.side_effect = [1, 2, 3]
    
#     assert mock.get_next() == 1
#     assert mock.get_next() == 2
#     assert mock.get_next() == 3


# def test_mock_side_effect_function():
#     """Mock con función personalizada."""
#     def custom_behavior(x):
#         return x * 2
    
#     mock = Mock()
#     mock.double.side_effect = custom_behavior
    
#     assert mock.double(5) == 10
#     assert mock.double(3) == 6


# ============================================
# PASO 4: OrderService con múltiples mocks
# ============================================
print("--- Paso 4: Múltiples mocks ---")

# Descomenta las siguientes líneas:

# def test_order_service_success(mock_payment_gateway, mock_inventory_service):
#     """Test de crear orden exitosa."""
#     service = OrderService(
#         payment_gateway=mock_payment_gateway,
#         inventory_service=mock_inventory_service
#     )
    
#     items = [
#         {"product_id": 1, "quantity": 2},
#         {"product_id": 2, "quantity": 1},
#     ]
    
#     order = service.create_order(user_id=1, items=items)
    
#     # Verificar orden
#     assert order["status"] == "confirmed"
#     assert order["total"] == 30.0  # 3 items * 10.0
    
#     # Verificar que se verificó stock
#     assert mock_inventory_service.check_stock.call_count == 2
    
#     # Verificar que se cobró
#     mock_payment_gateway.charge.assert_called_once_with(1, 30.0)
    
#     # Verificar que se reservó inventario
#     assert mock_inventory_service.reserve.call_count == 2


# def test_order_service_insufficient_stock(mock_payment_gateway, mock_inventory_service):
#     """Test cuando no hay stock suficiente."""
#     # Configurar mock para que falle en check_stock
#     mock_inventory_service.check_stock.return_value = False
    
#     service = OrderService(
#         payment_gateway=mock_payment_gateway,
#         inventory_service=mock_inventory_service
#     )
    
#     with pytest.raises(ValueError, match="Insufficient stock"):
#         service.create_order(user_id=1, items=[{"product_id": 1, "quantity": 100}])
    
#     # Verificar que NO se intentó cobrar
#     mock_payment_gateway.charge.assert_not_called()


# def test_order_service_payment_failed(mock_payment_gateway, mock_inventory_service):
#     """Test cuando falla el pago."""
#     # Configurar mock para que falle el pago
#     mock_payment_gateway.charge.return_value = {"success": False}
    
#     service = OrderService(
#         payment_gateway=mock_payment_gateway,
#         inventory_service=mock_inventory_service
#     )
    
#     with pytest.raises(ValueError, match="Payment failed"):
#         service.create_order(user_id=1, items=[{"product_id": 1, "quantity": 1}])
    
#     # Verificar que NO se reservó inventario
#     mock_inventory_service.reserve.assert_not_called()


# ============================================
# PASO 5: Verificar llamadas múltiples
# ============================================
print("--- Paso 5: Verificar llamadas ---")

# Descomenta las siguientes líneas:

# def test_verify_multiple_calls():
#     """Verificar múltiples llamadas a un mock."""
#     mock = Mock()
    
#     # Hacer varias llamadas
#     mock.process("item1")
#     mock.process("item2")
#     mock.process("item3")
    
#     # Verificar número de llamadas
#     assert mock.process.call_count == 3
    
#     # Verificar todas las llamadas en orden
#     mock.process.assert_has_calls([
#         call("item1"),
#         call("item2"),
#         call("item3"),
#     ])
    
#     # Verificar que se llamó con un valor específico (cualquier orden)
#     mock.process.assert_any_call("item2")


# ============================================
# PASO 6: MagicMock para métodos mágicos
# ============================================
print("--- Paso 6: MagicMock ---")

# Descomenta las siguientes líneas:

# def test_magic_mock_len():
#     """MagicMock soporta __len__."""
#     mock_list = MagicMock()
#     mock_list.__len__.return_value = 5
    
#     assert len(mock_list) == 5


# def test_magic_mock_context_manager():
#     """MagicMock como context manager."""
#     mock_file = MagicMock()
#     mock_file.__enter__.return_value = mock_file
#     mock_file.read.return_value = "file content"
    
#     with mock_file as f:
#         content = f.read()
    
#     assert content == "file content"
#     mock_file.__enter__.assert_called_once()
#     mock_file.__exit__.assert_called_once()


# def test_magic_mock_iteration():
#     """MagicMock como iterador."""
#     mock_iter = MagicMock()
#     mock_iter.__iter__.return_value = iter([1, 2, 3])
    
#     result = list(mock_iter)
    
#     assert result == [1, 2, 3]
