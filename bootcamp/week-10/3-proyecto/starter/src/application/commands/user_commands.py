"""
Commands para User.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserCommand:
    """Comando: Crear nuevo usuario."""
    email: str
    name: str
