# ============================================
# MODELO CATEGORY (ENTITY)
# ============================================
print("--- Model: Category Entity ---")

# Este es el modelo SQLAlchemy que representa la tabla categories.
# Los modelos pertenecen a la capa de Data Access.

# Descomenta las siguientes líneas:

# from datetime import datetime
# from sqlalchemy import String, DateTime, Boolean
# from sqlalchemy.orm import Mapped, mapped_column
# from database import Base


# class Category(Base):
#     """
#     Entidad Category - representa una categoría de productos.
#     
#     Attributes:
#         id: Identificador único
#         name: Nombre de la categoría
#         description: Descripción opcional
#         is_active: Si está activa
#         created_at: Fecha de creación
#         updated_at: Fecha de última actualización
#     """
#     __tablename__ = "categories"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
#     description: Mapped[str | None] = mapped_column(String(500), nullable=True)
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True)
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime,
#         default=datetime.utcnow
#     )
#     updated_at: Mapped[datetime | None] = mapped_column(
#         DateTime,
#         onupdate=datetime.utcnow,
#         nullable=True
#     )
#     
#     def __repr__(self) -> str:
#         return f"<Category(id={self.id}, name='{self.name}')>"
