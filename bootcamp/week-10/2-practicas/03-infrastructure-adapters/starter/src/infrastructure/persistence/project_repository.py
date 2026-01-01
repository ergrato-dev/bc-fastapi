"""
Driven Adapter: Repository en memoria para proyectos.
"""

from uuid import UUID

from domain.entities.project import Project


# ============================================
# PASO 1: Implementar InMemoryProjectRepository
# ============================================

# Descomenta las siguientes líneas:

# class InMemoryProjectRepository:
#     """Driven Adapter: Persistencia en memoria para proyectos."""
#     
#     def __init__(self) -> None:
#         self._projects: dict[UUID, Project] = {}
#     
#     async def save(self, project: Project) -> None:
#         """Guardar o actualizar un proyecto."""
#         self._projects[project.id] = project
#     
#     async def get_by_id(self, project_id: UUID) -> Project | None:
#         """Obtener proyecto por ID."""
#         return self._projects.get(project_id)
#     
#     async def get_by_owner(self, owner_id: UUID) -> list[Project]:
#         """Obtener proyectos de un propietario."""
#         return [
#             p for p in self._projects.values()
#             if p.owner_id == owner_id
#         ]
#     
#     async def get_all(self, include_archived: bool = False) -> list[Project]:
#         """Obtener todos los proyectos."""
#         projects = list(self._projects.values())
#         if not include_archived:
#             projects = [p for p in projects if not p.is_archived]
#         return projects
#     
#     async def delete(self, project_id: UUID) -> bool:
#         """Eliminar un proyecto."""
#         if project_id in self._projects:
#             del self._projects[project_id]
#             return True
#         return False
#     
#     def clear(self) -> None:
#         """Limpiar todos los datos."""
#         self._projects.clear()


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("✅ ProjectRepository implementado correctamente")
