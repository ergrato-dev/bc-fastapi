# ============================================
# Tests for CI/CD Practice
# Semana 15 - Práctica 04
# ============================================

import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


# ============================================
# Health Check Tests
# ============================================


def test_health_check() -> None:
    """Test health endpoint returns healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_root() -> None:
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


# ============================================
# User CRUD Tests
# ============================================


def test_create_user() -> None:
    """Test creating a new user"""
    user_data = {"name": "Test User", "email": "test@example.com"}
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert "id" in data


def test_create_user_invalid_email() -> None:
    """Test creating user with invalid email fails"""
    user_data = {"name": "Test User", "email": "invalid-email"}
    response = client.post("/users", json=user_data)
    assert response.status_code == 422


def test_get_user() -> None:
    """Test getting a user by ID"""
    # First create a user
    user_data = {"name": "Get Test User", "email": "gettest@example.com"}
    create_response = client.post("/users", json=user_data)
    user_id = create_response.json()["id"]

    # Then get the user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]


def test_get_user_not_found() -> None:
    """Test getting non-existent user returns 404"""
    response = client.get("/users/99999")
    assert response.status_code == 404


def test_list_users() -> None:
    """Test listing all users"""
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_user() -> None:
    """Test deleting a user"""
    # First create a user
    user_data = {"name": "Delete Test", "email": "delete@example.com"}
    create_response = client.post("/users", json=user_data)
    user_id = create_response.json()["id"]

    # Then delete
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 204

    # Verify deleted
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404


def test_delete_user_not_found() -> None:
    """Test deleting non-existent user returns 404"""
    response = client.delete("/users/99999")
    assert response.status_code == 404
