"""
Tests demonstrating patch techniques.

Instrucciones:
1. Descomenta cada sección de tests
2. Ejecuta `uv run pytest tests/test_patching.py -v -s`
"""

import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from datetime import datetime

from src.services import get_greeting, calculate_age
from src.notifications import NotificationService, EmailSender, EmailConfig
from src.external_api import GitHubClient, WeatherClient


# ============================================
# PASO 1: patch como decorador
# ============================================
print("--- Paso 1: patch decorador ---")

# Descomenta las siguientes líneas:

# @patch("src.services.datetime")
# def test_greeting_morning(mock_datetime):
#     """Mockear datetime para simular mañana."""
#     mock_datetime.now.return_value = datetime(2024, 1, 15, 9, 0, 0)
    
#     result = get_greeting()
    
#     assert result == "Good morning!"


# @patch("src.services.datetime")
# def test_greeting_afternoon(mock_datetime):
#     """Mockear datetime para simular tarde."""
#     mock_datetime.now.return_value = datetime(2024, 1, 15, 15, 0, 0)
    
#     result = get_greeting()
    
#     assert result == "Good afternoon!"


# @patch("src.services.datetime")
# def test_greeting_evening(mock_datetime):
#     """Mockear datetime para simular noche."""
#     mock_datetime.now.return_value = datetime(2024, 1, 15, 20, 0, 0)
    
#     result = get_greeting()
    
#     assert result == "Good evening!"


# ============================================
# PASO 2: patch como context manager
# ============================================
print("--- Paso 2: patch context manager ---")

# Descomenta las siguientes líneas:

# def test_calculate_age_context_manager():
#     """Usar patch como context manager."""
#     with patch("src.services.datetime") as mock_dt:
#         # Simular fecha actual: 15 de julio de 2024
#         mock_dt.now.return_value = datetime(2024, 7, 15)
        
#         # Persona nacida el 1 de enero de 2000
#         birth_date = datetime(2000, 1, 1)
#         age = calculate_age(birth_date)
        
#         assert age == 24


# def test_calculate_age_before_birthday():
#     """Test de edad antes del cumpleaños."""
#     with patch("src.services.datetime") as mock_dt:
#         # Simular fecha actual: 15 de enero de 2024
#         mock_dt.now.return_value = datetime(2024, 1, 15)
        
#         # Persona nacida el 20 de enero de 2000 (cumple en 5 días)
#         birth_date = datetime(2000, 1, 20)
#         age = calculate_age(birth_date)
        
#         # Todavía tiene 23 porque no ha cumplido
#         assert age == 23


# ============================================
# PASO 3: patch SMTP para notificaciones
# ============================================
print("--- Paso 3: patch SMTP ---")

# Descomenta las siguientes líneas:

# @patch("src.notifications.smtplib.SMTP")
# def test_notification_service_sends_email(mock_smtp):
#     """Test de NotificationService con SMTP mockeado."""
#     # Configurar mock
#     mock_server = MagicMock()
#     mock_smtp.return_value.__enter__.return_value = mock_server
    
#     # Crear servicio
#     config = EmailConfig(
#         smtp_host="smtp.test.com",
#         smtp_port=587,
#         username="test@test.com",
#         password="password"
#     )
#     sender = EmailSender(config)
#     service = NotificationService(sender)
    
#     # Enviar notificación
#     result = service.notify_user("user@example.com", "Hello!")
    
#     assert result is True
#     mock_smtp.assert_called_once_with("smtp.test.com", 587)
#     mock_server.send_message.assert_called_once()


# @patch("src.notifications.smtplib.SMTP")
# def test_notification_service_multiple_users(mock_smtp):
#     """Test de envío a múltiples usuarios."""
#     mock_server = MagicMock()
#     mock_smtp.return_value.__enter__.return_value = mock_server
    
#     config = EmailConfig("smtp.test.com", 587, "test@test.com", "pass")
#     sender = EmailSender(config)
#     service = NotificationService(sender)
    
#     emails = ["user1@test.com", "user2@test.com", "user3@test.com"]
#     result = service.notify_multiple(emails, "Broadcast message")
    
#     assert len(result["success"]) == 3
#     assert len(result["failed"]) == 0
#     assert mock_server.send_message.call_count == 3


# ============================================
# PASO 4: pytest-mock (mocker fixture)
# ============================================
print("--- Paso 4: pytest-mock ---")

# Descomenta las siguientes líneas:

# def test_with_mocker(mocker):
#     """Usar pytest-mock para simplificar."""
#     # mocker.patch es más limpio que @patch
#     mock_dt = mocker.patch("src.services.datetime")
#     mock_dt.now.return_value = datetime(2024, 1, 15, 10, 0, 0)
    
#     result = get_greeting()
    
#     assert result == "Good morning!"


# def test_mocker_spy(mocker):
#     """Spy: llama al código real pero permite verificar."""
#     # Crear un objeto real
#     data = {"count": 0}
    
#     def increment():
#         data["count"] += 1
#         return data["count"]
    
#     # Spy sobre la función (NO la reemplaza, solo observa)
#     spy = mocker.spy(data, "get")
    
#     # La función real se ejecuta
#     result = data.get("count")
    
#     assert result == 0
#     spy.assert_called_once_with("count")


# ============================================
# PASO 5: Mockear httpx (API externa)
# ============================================
print("--- Paso 5: Mockear HTTP ---")

# Descomenta las siguientes líneas:

# @patch("src.external_api.httpx.Client")
# def test_github_client_get_user(mock_client_class):
#     """Mockear cliente HTTP."""
#     # Configurar mock
#     mock_response = MagicMock()
#     mock_response.json.return_value = {
#         "login": "testuser",
#         "name": "Test User",
#         "followers": 100,
#     }
#     mock_response.raise_for_status = MagicMock()
    
#     mock_client = MagicMock()
#     mock_client.get.return_value = mock_response
#     mock_client_class.return_value.__enter__.return_value = mock_client
    
#     # Usar el cliente
#     client = GitHubClient(token="fake-token")
#     user = client.get_user("testuser")
    
#     assert user["login"] == "testuser"
#     assert user["followers"] == 100


# ============================================
# PASO 6: AsyncMock para código async
# ============================================
print("--- Paso 6: AsyncMock ---")

# Descomenta las siguientes líneas:

# @pytest.mark.asyncio
# @patch("src.external_api.httpx.AsyncClient")
# async def test_weather_client_async(mock_client_class):
#     """Mockear cliente HTTP asíncrono."""
#     # Configurar mock async
#     mock_response = MagicMock()
#     mock_response.json.return_value = {
#         "location": {"name": "Madrid"},
#         "current": {
#             "temp_c": 25.0,
#             "condition": {"text": "Sunny"},
#             "humidity": 40,
#         }
#     }
#     mock_response.raise_for_status = MagicMock()
    
#     mock_client = AsyncMock()
#     mock_client.get.return_value = mock_response
#     mock_client_class.return_value.__aenter__.return_value = mock_client
    
#     # Usar cliente
#     client = WeatherClient(api_key="fake-key")
#     weather = await client.get_current_weather("Madrid")
    
#     assert weather.city == "Madrid"
#     assert weather.temperature == 25.0
#     assert weather.description == "Sunny"


# ============================================
# PASO 7: patch.object para métodos
# ============================================
print("--- Paso 7: patch.object ---")

# Descomenta las siguientes líneas:

# def test_patch_object_method():
#     """Patchear un método específico de una instancia."""
#     client = GitHubClient(token="test")
    
#     with patch.object(client, "get_user") as mock_get_user:
#         mock_get_user.return_value = {
#             "login": "mocked",
#             "followers": 999,
#         }
        
#         result = client.get_user("anyone")
        
#         assert result["login"] == "mocked"
#         mock_get_user.assert_called_once_with("anyone")


# def test_patch_object_for_complex_method():
#     """Patchear método que llama a otros."""
#     client = GitHubClient(token="test")
    
#     # Patchear métodos que get_repo_stats usa internamente
#     with patch.object(client, "get_user") as mock_user:
#         mock_user.return_value = {"login": "owner", "followers": 100}
        
#         with patch("src.external_api.httpx.Client") as mock_http:
#             mock_response = MagicMock()
#             mock_response.json.return_value = {
#                 "name": "repo",
#                 "stargazers_count": 50,
#                 "forks_count": 10,
#             }
#             mock_response.raise_for_status = MagicMock()
#             mock_http.return_value.__enter__.return_value.get.return_value = mock_response
            
#             stats = client.get_repo_stats("owner", "repo")
            
#             assert stats["owner"] == "owner"
#             assert stats["stars"] == 50
