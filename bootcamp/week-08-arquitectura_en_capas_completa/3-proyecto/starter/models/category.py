# ============================================
# MODELO CATEGORY
# ============================================

from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Category(Base):
    """
    Entidad Category.
    
    TODO: Completar los campos del modelo
    """
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # TODO: Agregar campo name (String 100, unique)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    
    # TODO: Agregar campo description (Text, nullable)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    # TODO: Agregar campo is_active (Boolean, default True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # TODO: Agregar campo created_at (DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Relación con products
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    
    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name='{self.name}')>"
