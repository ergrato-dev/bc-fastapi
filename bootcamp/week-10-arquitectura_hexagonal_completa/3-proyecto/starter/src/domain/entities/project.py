"""
Entidad: Project (Proyecto).

El proyecto agrupa tareas relacionadas.
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid4


@dataclass
class Project:
    """
    Entidad Project - Representa un proyecto del sistema.
    
    Atributos:
        id: Identificador único (UUID)
        name: Nombre del proyecto
        description: Descripción del proyecto
        owner_id: ID del usuario propietario
        created_at: Fecha de creación
        updated_at: Fecha de última actualización
    """
    
    id: UUID
    name: str
    description: str
    owner_id: UUID
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    
    # ============================================
    # FACTORY METHOD
    # ============================================
    
    @classmethod
    def create(
        cls,
        name: str,
        description: str,
        owner_id: UUID,
    ) -> "Project":
        """
        Factory method para crear un nuevo proyecto.
        
        TODO: Implementar la creación del proyecto con:
        - Generar UUID con uuid4()
        - Establecer timestamps
        """
        # TODO: Implementar
        pass
    
    # ============================================
    # COMPORTAMIENTOS
    # ============================================
    
    def update_info(self, name: str | None = None, description: str | None = None) -> None:
        """
        Actualizar información del proyecto.
        
        TODO: Implementar:
        - Actualizar name si se proporciona
        - Actualizar description si se proporciona
        - Actualizar updated_at
        """
        # TODO: Implementar
        pass
    
    def _update_timestamp(self) -> None:
        """Actualizar timestamp de modificación."""
        self.updated_at = datetime.now(UTC)
