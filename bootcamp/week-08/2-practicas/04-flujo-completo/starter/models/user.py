# ============================================
# MODELO USER
# ============================================

# Descomenta las siguientes líneas:

# from datetime import datetime
# from sqlalchemy import String, DateTime
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from database import Base


# class User(Base):
#     """Usuario del sistema."""
#     __tablename__ = "users"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     email: Mapped[str] = mapped_column(String(200), unique=True)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     
#     # Relación con orders
#     orders: Mapped[list["Order"]] = relationship(back_populates="user")
