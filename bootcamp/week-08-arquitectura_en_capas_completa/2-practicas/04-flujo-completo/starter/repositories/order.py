# ============================================
# ORDER REPOSITORY
# ============================================

# Descomenta las siguientes líneas:

# from sqlalchemy import select
# from sqlalchemy.orm import Session, joinedload
# from models.order import Order


# class OrderRepository:
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, order_id: int) -> Order | None:
#         return self.db.get(Order, order_id)
#     
#     def get_by_id_with_items(self, order_id: int) -> Order | None:
#         """Obtiene orden con items precargados."""
#         stmt = (
#             select(Order)
#             .options(joinedload(Order.items))
#             .where(Order.id == order_id)
#         )
#         return self.db.execute(stmt).unique().scalar_one_or_none()
#     
#     def add(self, order: Order) -> Order:
#         """Agrega orden (items se agregan por cascade)."""
#         self.db.add(order)
#         self.db.commit()
#         self.db.refresh(order)
#         return order
