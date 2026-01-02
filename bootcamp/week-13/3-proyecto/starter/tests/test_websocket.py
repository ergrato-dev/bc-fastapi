"""
Tests de WebSocket.

TODO: Completar los tests marcados con TODO
"""

import pytest
from fastapi.testclient import TestClient


class TestWebSocketConnection:
    """Tests de conexión WebSocket."""
    
    def test_connect_without_token(self, client, test_room):
        """
        Test conexión sin token debe fallar.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Intentar conectar sin token
        # 2. Verificar que falla
        pass
    
    def test_connect_with_invalid_token(self, client, test_room):
        """
        Test conexión con token inválido.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        pass
    
    def test_connect_with_valid_token(self, client, test_user_token, test_room):
        """
        Test conexión exitosa con token válido.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Conectar con token válido
        # 2. Verificar que recibe mensaje de bienvenida
        pass
    
    def test_connect_to_nonexistent_room(self, client, test_user_token):
        """
        Test conexión a sala inexistente.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        pass


class TestWebSocketChat:
    """Tests de chat WebSocket."""
    
    def test_send_message(self, client, test_user_token, test_room):
        """
        Test enviar mensaje.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Conectar al WebSocket
        # 2. Recibir bienvenida
        # 3. Enviar mensaje
        # 4. Verificar que recibe el mensaje de vuelta (broadcast)
        pass
    
    def test_receive_broadcast(self, client, test_user_token, test_room):
        """
        Test recibir broadcast de otro usuario.
        
        TODO: Implementar test (más avanzado, puede requerir threads)
        """
        # TODO: Implementar si el tiempo lo permite
        pass
    
    def test_ping_pong(self, client, test_user_token, test_room):
        """
        Test ping/pong para keepalive.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Conectar
        # 2. Enviar {"type": "ping"}
        # 3. Verificar que recibe {"type": "pong"}
        pass


class TestConnectionManager:
    """Tests del Connection Manager."""
    
    def test_user_joins_room(self, client, test_user_token, test_room):
        """
        Test que usuario aparece en lista al unirse.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        # 1. Conectar al WebSocket
        # 2. GET /rooms/{room_id}
        # 3. Verificar que usuario está en online_users
        pass
    
    def test_user_leaves_room(self, client, test_user_token, test_room):
        """
        Test que usuario desaparece al salir.
        
        TODO: Implementar test
        """
        # TODO: Implementar
        pass
