# ============================================
# CATEGORY SERVICE
# ============================================

from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from repositories.category import CategoryRepository
from exceptions.category import CategoryNotFoundError, CategoryHasProductsError


class CategoryService:
    """Service para lógica de negocio de Category."""
    
    def __init__(self, repo: CategoryRepository):
        self.repo = repo
    
    def get_all(self) -> list[CategoryResponse]:
        """Lista todas las categorías."""
        entities = self.repo.get_all()
        return [CategoryResponse.model_validate(e) for e in entities]
    
    def get_by_id(self, category_id: int) -> CategoryResponse:
        """
        Obtiene categoría por ID.
        
        TODO: Lanzar CategoryNotFoundError si no existe
        """
        entity = self.repo.get_by_id(category_id)
        if not entity:
            raise CategoryNotFoundError(category_id)
        return CategoryResponse.model_validate(entity)
    
    def create(self, data: CategoryCreate) -> CategoryResponse:
        """Crea nueva categoría."""
        entity = Category(
            name=data.name,
            description=data.description
        )
        saved = self.repo.add(entity)
        return CategoryResponse.model_validate(saved)
    
    def update(self, category_id: int, data: CategoryUpdate) -> CategoryResponse:
        """
        Actualiza categoría.
        
        TODO: Aplicar solo campos enviados (exclude_unset)
        """
        entity = self.repo.get_by_id(category_id)
        if not entity:
            raise CategoryNotFoundError(category_id)
        
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(entity, field, value)
        
        saved = self.repo.update(entity)
        return CategoryResponse.model_validate(saved)
    
    def delete(self, category_id: int) -> None:
        """
        Elimina categoría.
        
        TODO: Validar que no tenga productos antes de eliminar
        """
        entity = self.repo.get_by_id(category_id)
        if not entity:
            raise CategoryNotFoundError(category_id)
        
        # Validar que no tenga productos
        product_count = self.repo.count_products(category_id)
        if product_count > 0:
            raise CategoryHasProductsError(category_id, product_count)
        
        self.repo.delete(entity)
