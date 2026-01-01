# ============================================
# MODELOS ORDER Y ORDER ITEM
# ============================================

# Descomenta las siguientes líneas:

# from datetime import datetime
# from enum import Enum
# from sqlalchemy import String, Float, Integer, DateTime, ForeignKey, Text
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from database import Base


# class OrderStatus(str, Enum):
#     """Estados posibles de un pedido."""
#     PENDING = "pending"
#     CONFIRMED = "confirmed"
#     SHIPPED = "shipped"
#     DELIVERED = "delivered"
#     CANCELLED = "cancelled"


# class Order(Base):
#     """Pedido de un usuario."""
#     __tablename__ = "orders"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     status: Mapped[str] = mapped_column(String(20), default=OrderStatus.PENDING)
#     
#     # Montos
#     subtotal: Mapped[float] = mapped_column(Float, default=0)
#     tax: Mapped[float] = mapped_column(Float, default=0)
#     shipping_cost: Mapped[float] = mapped_column(Float, default=0)
#     total: Mapped[float] = mapped_column(Float, default=0)
#     
#     # Dirección
#     shipping_address: Mapped[str] = mapped_column(Text)
#     
#     # Timestamps
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     
#     # Relaciones
#     user: Mapped["User"] = relationship(back_populates="orders")
#     items: Mapped[list["OrderItem"]] = relationship(
#         back_populates="order",
#         cascade="all, delete-orphan"
#     )


# class OrderItem(Base):
#     """Item de un pedido."""
#     __tablename__ = "order_items"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
#     product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
#     
#     # Snapshot del producto al momento de la compra
#     product_name: Mapped[str] = mapped_column(String(200))
#     quantity: Mapped[int] = mapped_column(Integer)
#     unit_price: Mapped[float] = mapped_column(Float)
#     subtotal: Mapped[float] = mapped_column(Float)
#     
#     # Relación
#     order: Mapped["Order"] = relationship(back_populates="items")
