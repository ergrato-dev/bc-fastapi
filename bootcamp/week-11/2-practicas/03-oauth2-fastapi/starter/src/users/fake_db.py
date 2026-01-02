# fake_db.py
"""
Base de datos simulada de usuarios.

En una aplicación real, estos datos estarían en una base de datos.
Los passwords están hasheados con bcrypt.
"""

from src.auth.security import hash_password

# Base de datos simulada de usuarios
# Los passwords en texto plano son solo para referencia en comentarios
FAKE_USERS_DB = {
    "user@example.com": {
        "id": 1,
        "email": "user@example.com",
        "full_name": "Regular User",
        "hashed_password": hash_password("password123"),  # password123
        "role": "user",
        "is_active": True,
    },
    "admin@example.com": {
        "id": 2,
        "email": "admin@example.com",
        "full_name": "Admin User",
        "hashed_password": hash_password("admin123"),  # admin123
        "role": "admin",
        "is_active": True,
    },
    "disabled@example.com": {
        "id": 3,
        "email": "disabled@example.com",
        "full_name": "Disabled User",
        "hashed_password": hash_password("disabled123"),  # disabled123
        "role": "user",
        "is_active": False,
    },
}


def get_user_by_email(email: str) -> dict | None:
    """
    Busca un usuario por email.
    
    Args:
        email: Email del usuario a buscar
        
    Returns:
        Diccionario con datos del usuario o None si no existe
    """
    return FAKE_USERS_DB.get(email)


def get_all_users() -> list[dict]:
    """Retorna todos los usuarios."""
    return list(FAKE_USERS_DB.values())
