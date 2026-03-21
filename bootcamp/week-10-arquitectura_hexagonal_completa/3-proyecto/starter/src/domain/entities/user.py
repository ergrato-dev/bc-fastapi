"""
Entidad: User (Usuario).

El usuario puede ser propietario de proyectos y asignado a tareas.
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid4


@dataclass
class User:
    """
    Entidad User - Representa un usuario del sistema.
    
    Atributos:
        id: Identificador único (UUID)
        email: Email único del usuario
        name: Nombre del usuario
        is_active: Si el usuario está activo
        created_at: Fecha de creación
    """
    
    id: UUID
    email: str
    name: str
    is_active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    
    # ============================================
    # FACTORY METHOD
    # ============================================
    
    @classmethod
    def create(cls, email: str, name: str) -> "User":
        """
        Factory method para crear un nuevo usuario.
        
        TODO: Implementar la creación del usuario con:
        - Generar UUID con uuid4()
        - Establecer is_active = True
        - Establecer created_at
        """
        # TODO: Implementar
        pass
    
    # ============================================
    # COMPORTAMIENTOS
    # ============================================
    
    def deactivate(self) -> None:
        """
        Desactivar usuario.
        
        TODO: Implementar:
        - Establecer is_active = False
        """
        # TODO: Implementar
        pass
    
    def activate(self) -> None:
        """
        Activar usuario.
        
        TODO: Implementar:
        - Establecer is_active = True
        """
        # TODO: Implementar
        pass
