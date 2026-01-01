# ============================================
# MODELO PRODUCT
# ============================================

from datetime import datetime
from sqlalchemy import String, Float, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Product(Base):
    """Entidad Product."""
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    sku: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
