# ============================================
# PRODUCT SERVICE
# ============================================

from models.product import Product
from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from repositories.product import ProductRepository
from repositories.category import CategoryRepository
from mappers.product import ProductMapper
from exceptions.product import ProductNotFoundError
from exceptions.category import CategoryNotFoundError


class ProductService:
    """Service para lógica de negocio de Product."""
    
    def __init__(
        self,
        product_repo: ProductRepository,
        category_repo: CategoryRepository
    ):
        self.product_repo = product_repo
        self.category_repo = category_repo
    
    def get_all(self) -> list[ProductResponse]:
        """Lista todos los productos."""
        entities = self.product_repo.get_all()
        return ProductMapper.to_response_list(entities)
    
    def get_by_id(self, product_id: int) -> ProductResponse:
        """
        Obtiene producto por ID.
        
        TODO: Lanzar ProductNotFoundError si no existe
        """
        entity = self.product_repo.get_by_id(product_id)
        if not entity:
            raise ProductNotFoundError(product_id)
        return ProductMapper.to_response(entity)
    
    def get_by_category(self, category_id: int) -> list[ProductResponse]:
        """
        Obtiene productos de una categoría.
        
        TODO: Validar que categoría exista
        """
        category = self.category_repo.get_by_id(category_id)
        if not category:
            raise CategoryNotFoundError(category_id)
        
        entities = self.product_repo.get_by_category(category_id)
        return ProductMapper.to_response_list(entities)
    
    def create(self, data: ProductCreate) -> ProductResponse:
        """
        Crea nuevo producto.
        
        TODO: Validar que categoría exista
        """
        # Validar categoría
        category = self.category_repo.get_by_id(data.category_id)
        if not category:
            raise CategoryNotFoundError(data.category_id)
        
        entity = ProductMapper.to_entity(data)
        saved = self.product_repo.add(entity)
        return ProductMapper.to_response(saved)
    
    def update(self, product_id: int, data: ProductUpdate) -> ProductResponse:
        """
        Actualiza producto.
        
        TODO: Si cambia category_id, validar que exista
        """
        entity = self.product_repo.get_by_id(product_id)
        if not entity:
            raise ProductNotFoundError(product_id)
        
        # Si cambia categoría, validar
        if data.category_id is not None:
            category = self.category_repo.get_by_id(data.category_id)
            if not category:
                raise CategoryNotFoundError(data.category_id)
        
        updated = ProductMapper.update_entity(entity, data)
        saved = self.product_repo.update(updated)
        return ProductMapper.to_response(saved)
    
    def delete(self, product_id: int) -> None:
        """Elimina producto."""
        entity = self.product_repo.get_by_id(product_id)
        if not entity:
            raise ProductNotFoundError(product_id)
        
        self.product_repo.delete(entity)
