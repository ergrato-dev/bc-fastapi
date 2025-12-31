"""
Simulación de Base de Datos
===========================

Base de datos en memoria para el proyecto.
"""

# "Base de datos" en memoria
contacts_db: dict[int, dict] = {}

# Contador para IDs
_id_counter = 0


def get_next_id() -> int:
    """Obtener siguiente ID disponible."""
    global _id_counter
    _id_counter += 1
    return _id_counter


def find_by_email(email: str) -> dict | None:
    """Buscar contacto por email."""
    email_lower = email.lower()
    for contact in contacts_db.values():
        if contact["email"].lower() == email_lower:
            return contact
    return None


def reset_db() -> None:
    """Resetear base de datos (útil para tests)."""
    global _id_counter
    contacts_db.clear()
    _id_counter = 0
