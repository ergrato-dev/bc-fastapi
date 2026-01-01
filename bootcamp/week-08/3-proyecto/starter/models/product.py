# ============================================
# MODELO PRODUCT
# ============================================

from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, Text, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Product(Base):
    """
    Entidad Product.
    
    TODO: Completar los campos del modelo
    """
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # TODO: Agregar campo name (String 200)
    name: Mapped[str] = mapped_column(String(200))
    
    # TODO: Agregar campo sku (String 50, unique, index)
    sku: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    
    # TODO: Agregar campo description (Text, nullable)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    # TODO: Agregar campo price (Float)
    price: Mapped[float] = mapped_column(Float)
    
    # TODO: Agregar campo stock (Integer, default 0)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    
    # TODO: Agregar campo category_id (ForeignKey)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    
    # TODO: Agregar campo is_active (Boolean, default True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # TODO: Agregar campo created_at (DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Relación con category
    category: Mapped["Category"] = relationship(back_populates="products")
    
    def __repr__(self) -> str:
        return f"<Product(id={self.id}, sku='{self.sku}')>"
