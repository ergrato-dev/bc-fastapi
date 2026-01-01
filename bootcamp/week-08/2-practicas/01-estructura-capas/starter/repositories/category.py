# ============================================
# CATEGORY REPOSITORY
# ============================================
print("--- Repository: Category Repository ---")

# CategoryRepository hereda de BaseRepository y agrega
# métodos específicos para categorías.
# Pertenece a la capa de Data Access.

# Descomenta las siguientes líneas:

# from sqlalchemy import select
# from sqlalchemy.orm import Session

# from repositories.base import BaseRepository
# from models.category import Category


# class CategoryRepository(BaseRepository[Category]):
#     """
#     Repository para operaciones con Category.
#     
#     Hereda operaciones CRUD de BaseRepository
#     y agrega métodos específicos.
#     """
#     
#     def __init__(self, db: Session):
#         super().__init__(db, Category)
#     
#     def get_by_name(self, name: str) -> Category | None:
#         """
#         Busca categoría por nombre exacto.
#         
#         Args:
#             name: Nombre a buscar
#             
#         Returns:
#             Category si existe, None si no
#         """
#         stmt = select(Category).where(Category.name == name)
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     def get_active(self) -> list[Category]:
#         """
#         Obtiene solo categorías activas.
#         
#         Returns:
#             Lista de categorías activas
#         """
#         stmt = select(Category).where(Category.is_active == True)
#         return list(self.db.execute(stmt).scalars().all())
#     
#     def exists_by_name(self, name: str) -> bool:
#         """
#         Verifica si existe categoría con ese nombre.
#         
#         Args:
#             name: Nombre a verificar
#             
#         Returns:
#             True si existe, False si no
#         """
#         return self.get_by_name(name) is not None
