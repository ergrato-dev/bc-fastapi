# ============================================
# MODELOS ORDER Y ORDER ITEM
# ============================================

from datetime import datetime
from enum import Enum
from sqlalchemy import String, DateTime, Text, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class OrderStatus(str, Enum):
    """Estados posibles de un pedido."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order(Base):
    """
    Entidad Order.
    
    TODO: Completar los campos del modelo
    """
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # TODO: Agregar campo user_id (ForeignKey)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    # TODO: Agregar campo status (String 20, default PENDING)
    status: Mapped[str] = mapped_column(String(20), default=OrderStatus.PENDING)
    
    # TODO: Agregar campos de montos (subtotal, tax, shipping_cost, total)
    subtotal: Mapped[float] = mapped_column(Float, default=0)
    tax: Mapped[float] = mapped_column(Float, default=0)
    shipping_cost: Mapped[float] = mapped_column(Float, default=0)
    total: Mapped[float] = mapped_column(Float, default=0)
    
    # TODO: Agregar campo shipping_address (Text)
    shipping_address: Mapped[str] = mapped_column(Text)
    
    # TODO: Agregar campo created_at (DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Relaciones
    user: Mapped["User"] = relationship(back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"<Order(id={self.id}, status='{self.status}')>"


class OrderItem(Base):
    """
    Entidad OrderItem.
    
    TODO: Completar los campos del modelo
    """
    __tablename__ = "order_items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # TODO: Agregar campo order_id (ForeignKey)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    
    # TODO: Agregar campo product_id (ForeignKey)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    
    # TODO: Agregar campo product_name (String 200) - snapshot
    product_name: Mapped[str] = mapped_column(String(200))
    
    # TODO: Agregar campos quantity, unit_price, subtotal
    quantity: Mapped[int] = mapped_column(Integer)
    unit_price: Mapped[float] = mapped_column(Float)
    subtotal: Mapped[float] = mapped_column(Float)
    
    # Relación
    order: Mapped["Order"] = relationship(back_populates="items")
    
    def __repr__(self) -> str:
        return f"<OrderItem(id={self.id}, product='{self.product_name}')>"
