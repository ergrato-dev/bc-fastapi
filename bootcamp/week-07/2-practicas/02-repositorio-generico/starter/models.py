# ============================================
# Modelos
# ============================================
from datetime import datetime
from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Category(Base):
    """Modelo de Categoría"""
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str | None] = mapped_column(String(200), nullable=True)
    
    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Product(Base):
    """Modelo de Producto"""
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    category: Mapped[Category | None] = relationship(back_populates="products")
