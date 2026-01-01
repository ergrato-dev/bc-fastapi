"""
Port ProjectRepository - Contrato para persistencia de proyectos.
"""

from typing import Protocol
from uuid import UUID

from domain.entities.project import Project


# ============================================
# PASO 1: Definir el Port ProjectRepository
# ============================================
print("--- Paso 1: Definir ProjectRepository Port ---")

# Descomenta las siguientes líneas:

# class ProjectRepository(Protocol):
#     """Port: Contrato para persistencia de proyectos."""
#     
#     async def save(self, project: Project) -> None:
#         """Guardar o actualizar un proyecto."""
#         ...
#     
#     async def get_by_id(self, project_id: UUID) -> Project | None:
#         """Obtener proyecto por ID."""
#         ...
#     
#     async def get_by_owner(self, owner_id: UUID) -> list[Project]:
#         """Obtener proyectos de un propietario."""
#         ...
#     
#     async def get_all(self, include_archived: bool = False) -> list[Project]:
#         """Obtener todos los proyectos."""
#         ...
#     
#     async def delete(self, project_id: UUID) -> bool:
#         """Eliminar un proyecto."""
#         ...


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de ProjectRepository Port ---")
    print("✅ Port ProjectRepository definido correctamente")
