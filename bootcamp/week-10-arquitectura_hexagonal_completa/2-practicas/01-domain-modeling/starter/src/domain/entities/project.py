"""
Entidad Project - Representa un proyecto que agrupa tareas.

Un proyecto es un contenedor lógico para tareas relacionadas.
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


# ============================================
# PASO 1: Definir la entidad Project
# ============================================
print("--- Paso 1: Definir la entidad Project ---")

# Descomenta las siguientes líneas:

# @dataclass
# class Project:
#     """
#     Entidad Project.
#     
#     Un proyecto agrupa tareas relacionadas y tiene un propietario.
#     """
#     
#     id: UUID
#     name: str
#     description: str
#     owner_id: UUID
#     created_at: datetime = field(default_factory=datetime.now)
#     updated_at: datetime = field(default_factory=datetime.now)
#     is_archived: bool = field(default=False)
#     
#     @classmethod
#     def create(
#         cls,
#         name: str,
#         owner_id: UUID,
#         description: str = "",
#     ) -> "Project":
#         """Factory method para crear un proyecto."""
#         if not name or not name.strip():
#             raise ValueError("Project name cannot be empty")
#         
#         return cls(
#             id=uuid4(),
#             name=name.strip(),
#             description=description.strip(),
#             owner_id=owner_id,
#         )
#     
#     def rename(self, new_name: str) -> None:
#         """Renombrar el proyecto."""
#         if not new_name or not new_name.strip():
#             raise ValueError("Project name cannot be empty")
#         self.name = new_name.strip()
#         self._touch()
#     
#     def archive(self) -> None:
#         """Archivar el proyecto."""
#         self.is_archived = True
#         self._touch()
#     
#     def unarchive(self) -> None:
#         """Desarchivar el proyecto."""
#         self.is_archived = False
#         self._touch()
#     
#     def transfer_ownership(self, new_owner_id: UUID) -> None:
#         """Transferir propiedad del proyecto."""
#         self.owner_id = new_owner_id
#         self._touch()
#     
#     def _touch(self) -> None:
#         """Actualizar timestamp de modificación."""
#         self.updated_at = datetime.now()


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Project ---")
    
    # Descomentar para probar:
    # from uuid import uuid4
    # owner = uuid4()
    # project = Project.create(name="Mi Proyecto", owner_id=owner)
    # print(f"Project creado: {project.id}")
    # print(f"Nombre: {project.name}")
    # print(f"Owner: {project.owner_id}")
    
    print("✅ Entidad Project implementada correctamente")
