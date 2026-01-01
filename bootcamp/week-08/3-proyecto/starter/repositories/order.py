# ============================================
# ORDER REPOSITORY
# ============================================

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from .base import BaseRepository
from models.order import Order


class OrderRepository(BaseRepository[Order]):
    """Repository para Order."""
    
    def __init__(self, db: Session):
        super().__init__(db, Order)
    
    def get_by_id_with_items(self, order_id: int) -> Order | None:
        """
        Obtiene orden con items precargados.
        
        TODO: Usar joinedload para cargar items
        """
        stmt = (
            select(Order)
            .options(joinedload(Order.items))
            .where(Order.id == order_id)
        )
        return self.db.execute(stmt).unique().scalar_one_or_none()
    
    def get_by_user(self, user_id: int) -> list[Order]:
        """
        Obtiene pedidos de un usuario.
        
        TODO: Implementar query con items
        """
        stmt = (
            select(Order)
            .options(joinedload(Order.items))
            .where(Order.user_id == user_id)
        )
        return list(self.db.execute(stmt).unique().scalars().all())
