# ============================================
# CATEGORY SERVICE
# ============================================
print("--- Service: Category Service ---")

# CategoryService contiene la lógica de negocio para categorías.
# Recibe DTOs, aplica reglas de negocio, y usa el repository.
# Pertenece a la capa de Application.

# Descomenta las siguientes líneas:

# from models.category import Category
# from schemas.category import CategoryCreate, CategoryUpdate
# from repositories.category import CategoryRepository


# class CategoryService:
#     """
#     Service para lógica de negocio de Category.
#     
#     Attributes:
#         repo: Repository de categorías
#     """
#     
#     def __init__(self, repo: CategoryRepository):
#         self.repo = repo
#     
#     def get_all(self, skip: int = 0, limit: int = 100) -> list[Category]:
#         """
#         Obtiene todas las categorías.
#         
#         Returns:
#             Lista de categorías
#         """
#         return self.repo.get_all(skip=skip, limit=limit)
#     
#     def get_by_id(self, category_id: int) -> Category:
#         """
#         Obtiene categoría por ID.
#         
#         Args:
#             category_id: ID de la categoría
#             
#         Returns:
#             Category encontrada
#             
#         Raises:
#             ValueError: Si no existe
#         """
#         category = self.repo.get_by_id(category_id)
#         if not category:
#             raise ValueError(f"Category {category_id} not found")
#         return category
#     
#     def create(self, data: CategoryCreate) -> Category:
#         """
#         Crea nueva categoría.
#         
#         Args:
#             data: DTO con datos de creación
#             
#         Returns:
#             Category creada
#             
#         Raises:
#             ValueError: Si el nombre ya existe
#         """
#         # Regla de negocio: nombre único
#         if self.repo.exists_by_name(data.name):
#             raise ValueError(f"Category '{data.name}' already exists")
#         
#         # Crear entidad desde DTO
#         category = Category(
#             name=data.name,
#             description=data.description
#         )
#         
#         return self.repo.add(category)
#     
#     def update(self, category_id: int, data: CategoryUpdate) -> Category:
#         """
#         Actualiza categoría existente.
#         
#         Args:
#             category_id: ID de la categoría
#             data: DTO con datos a actualizar
#             
#         Returns:
#             Category actualizada
#         """
#         category = self.get_by_id(category_id)
#         
#         # Aplicar cambios solo de campos enviados
#         update_data = data.model_dump(exclude_unset=True)
#         
#         # Si cambia el nombre, verificar que no exista
#         if "name" in update_data:
#             existing = self.repo.get_by_name(update_data["name"])
#             if existing and existing.id != category_id:
#                 raise ValueError(f"Category '{update_data['name']}' already exists")
#         
#         for field, value in update_data.items():
#             setattr(category, field, value)
#         
#         return self.repo.update(category)
#     
#     def delete(self, category_id: int) -> None:
#         """
#         Elimina categoría.
#         
#         Args:
#             category_id: ID de la categoría
#         """
#         category = self.get_by_id(category_id)
#         self.repo.delete(category)
