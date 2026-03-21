# ============================================
# PRODUCT MAPPER
# ============================================

from models.product import Product
from schemas.product import ProductCreate, ProductUpdate, ProductResponse


class ProductMapper:
    """Mapper para conversiones de Product."""
    
    @staticmethod
    def to_entity(dto: ProductCreate) -> Product:
        """
        Convierte ProductCreate → Product entity.
        
        TODO: Implementar conversión
        """
        return Product(
            name=dto.name,
            sku=dto.sku,
            description=dto.description,
            price=dto.price,
            stock=dto.stock,
            category_id=dto.category_id
        )
    
    @staticmethod
    def to_response(entity: Product) -> ProductResponse:
        """
        Convierte Product entity → ProductResponse.
        
        TODO: Implementar usando model_validate
        """
        return ProductResponse.model_validate(entity)
    
    @staticmethod
    def update_entity(entity: Product, dto: ProductUpdate) -> Product:
        """
        Aplica cambios de ProductUpdate a entity.
        
        TODO: Implementar actualización parcial
        """
        update_data = dto.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(entity, field, value)
        return entity
    
    @staticmethod
    def to_response_list(entities: list[Product]) -> list[ProductResponse]:
        """Convierte lista de entities."""
        return [ProductMapper.to_response(e) for e in entities]
