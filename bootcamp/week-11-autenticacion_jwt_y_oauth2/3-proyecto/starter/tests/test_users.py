# test_users.py
"""Tests para endpoints de usuarios."""

import pytest


class TestUserProfile:
    """Tests para perfil de usuario."""
    
    def test_get_me_authenticated(self, client, auth_headers, test_user):
        """Usuario autenticado puede ver su perfil."""
        response = client.get("/users/me", headers=auth_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == test_user["email"]
        assert data["full_name"] == test_user["full_name"]
    
    def test_get_me_unauthenticated(self, client):
        """Sin token retorna 401."""
        response = client.get("/users/me")
        assert response.status_code == 401
    
    def test_get_me_invalid_token(self, client):
        """Token inválido retorna 401."""
        response = client.get(
            "/users/me",
            headers={"Authorization": "Bearer invalid.token.here"}
        )
        assert response.status_code == 401
    
    def test_update_me(self, client, auth_headers):
        """Usuario puede actualizar su nombre."""
        response = client.patch(
            "/users/me",
            json={"full_name": "Updated Name"},
            headers=auth_headers
        )
        
        assert response.status_code == 200
        assert response.json()["full_name"] == "Updated Name"


class TestAdminEndpoints:
    """Tests para endpoints de admin."""
    
    def test_list_users_as_admin(self, client, admin_user, test_user):
        """Admin puede listar usuarios."""
        response = client.get("/admin/users", headers=admin_user)
        
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) >= 1
    
    def test_list_users_as_regular_user(self, client, auth_headers):
        """Usuario regular no puede listar usuarios."""
        response = client.get("/admin/users", headers=auth_headers)
        assert response.status_code == 403
    
    def test_list_users_unauthenticated(self, client):
        """Sin autenticación no se puede listar."""
        response = client.get("/admin/users")
        assert response.status_code == 401
    
    def test_change_role_as_admin(self, client, admin_user, test_user):
        """Admin puede cambiar rol de usuario."""
        response = client.patch(
            f"/admin/users/{test_user['id']}/role",
            json={"role": "admin"},
            headers=admin_user
        )
        
        assert response.status_code == 200
        assert response.json()["role"] == "admin"
    
    def test_change_role_as_regular_user(self, client, auth_headers, test_user):
        """Usuario regular no puede cambiar roles."""
        response = client.patch(
            f"/admin/users/{test_user['id']}/role",
            json={"role": "admin"},
            headers=auth_headers
        )
        
        assert response.status_code == 403
    
    def test_change_role_invalid_role(self, client, admin_user, test_user):
        """Rol inválido retorna error de validación."""
        response = client.patch(
            f"/admin/users/{test_user['id']}/role",
            json={"role": "superadmin"},
            headers=admin_user
        )
        
        assert response.status_code == 422
    
    def test_change_role_user_not_found(self, client, admin_user):
        """Usuario inexistente retorna 404."""
        response = client.patch(
            "/admin/users/99999/role",
            json={"role": "admin"},
            headers=admin_user
        )
        
        assert response.status_code == 404
