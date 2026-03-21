# fake_db.py
"""Base de datos simulada de usuarios."""

from src.auth.security import hash_password

FAKE_USERS_DB = {
    "user@example.com": {
        "id": 1,
        "email": "user@example.com",
        "full_name": "Regular User",
        "hashed_password": hash_password("password123"),
        "role": "user",
        "is_active": True,
    },
    "admin@example.com": {
        "id": 2,
        "email": "admin@example.com",
        "full_name": "Admin User",
        "hashed_password": hash_password("admin123"),
        "role": "admin",
        "is_active": True,
    },
    "disabled@example.com": {
        "id": 3,
        "email": "disabled@example.com",
        "full_name": "Disabled User",
        "hashed_password": hash_password("disabled123"),
        "role": "user",
        "is_active": False,
    },
}


def get_user_by_email(email: str) -> dict | None:
    """Busca usuario por email."""
    return FAKE_USERS_DB.get(email)
