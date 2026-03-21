"""
DTOs para User.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class UserDTO:
    """DTO de respuesta para User."""
    id: UUID
    email: str
    name: str
    is_active: bool
    created_at: datetime


@dataclass(frozen=True)
class UserListDTO:
    """DTO para lista de usuarios."""
    items: list[UserDTO]
    total: int
