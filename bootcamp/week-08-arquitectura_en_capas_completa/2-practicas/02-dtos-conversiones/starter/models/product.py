# ============================================
# MODELO PRODUCT (ENTITY)
# ============================================
print("--- Model: Product Entity ---")

# Este modelo tiene campos que NO queremos exponer al cliente:
# - cost_price: precio de costo (información interna)
# - internal_notes: notas internas del equipo
# - supplier_id: referencia a proveedor (sensible)

# Descomenta las siguientes líneas:

# from datetime import datetime
# from sqlalchemy import String, Float, Integer, DateTime, Text
# from sqlalchemy.orm import Mapped, mapped_column
# from database import Base


# class Product(Base):
#     """
#     Entidad Product - representa un producto en inventario.
#     
#     Algunos campos son INTERNOS y no deben exponerse:
#     - cost_price: precio de compra/costo
#     - internal_notes: notas del equipo
#     - supplier_id: ID del proveedor
#     """
#     __tablename__ = "products"
#     
#     # Campos públicos
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(200))
#     sku: Mapped[str] = mapped_column(String(50), unique=True, index=True)
#     description: Mapped[str | None] = mapped_column(Text, nullable=True)
#     price: Mapped[float] = mapped_column(Float)  # Precio de venta
#     stock: Mapped[int] = mapped_column(Integer, default=0)
#     
#     # Campos INTERNOS - NO exponer al cliente
#     cost_price: Mapped[float] = mapped_column(Float, default=0)  # Precio costo
#     internal_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
#     supplier_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
#     
#     # Timestamps
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     updated_at: Mapped[datetime | None] = mapped_column(
#         DateTime,
#         onupdate=datetime.utcnow,
#         nullable=True
#     )
#     
#     @property
#     def profit_margin(self) -> float:
#         """Calcula margen de ganancia."""
#         if self.cost_price == 0:
#             return 0
#         return ((self.price - self.cost_price) / self.cost_price) * 100
#     
#     def __repr__(self) -> str:
#         return f"<Product(id={self.id}, sku='{self.sku}', name='{self.name}')>"
