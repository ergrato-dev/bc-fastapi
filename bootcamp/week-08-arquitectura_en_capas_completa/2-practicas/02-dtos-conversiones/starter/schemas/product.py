# ============================================
# SCHEMAS PRODUCT (DTOs)
# ============================================
print("--- Schemas: Product DTOs ---")

# Diferentes DTOs para diferentes propósitos:
# - ProductCreate: Lo que el cliente envía para crear
# - ProductUpdate: Campos opcionales para actualizar
# - ProductResponse: Lo que el cliente ve (SIN campos internos)
# - ProductDetail: Respuesta extendida con más información

# Descomenta las siguientes líneas:

# from datetime import datetime
# from pydantic import BaseModel, Field, ConfigDict


# # ============================================
# # INPUT DTOs
# # ============================================

# class ProductCreate(BaseModel):
#     """
#     DTO para CREAR producto.
#     
#     El cliente envía estos campos.
#     NO incluye: id, timestamps, campos calculados.
#     SÍ incluye: cost_price (solo admin puede crear)
#     """
#     name: str = Field(..., min_length=1, max_length=200)
#     sku: str = Field(..., pattern=r"^[A-Z]{2,4}-\d{3,6}$")
#     description: str | None = Field(None, max_length=2000)
#     price: float = Field(..., gt=0, description="Precio de venta")
#     stock: int = Field(default=0, ge=0)
#     cost_price: float = Field(default=0, ge=0, description="Precio de costo")
#     supplier_id: int | None = None


# class ProductUpdate(BaseModel):
#     """
#     DTO para ACTUALIZAR producto (PATCH).
#     
#     Todos los campos son opcionales.
#     El cliente solo envía lo que quiere cambiar.
#     """
#     name: str | None = Field(None, min_length=1, max_length=200)
#     description: str | None = Field(None, max_length=2000)
#     price: float | None = Field(None, gt=0)
#     stock: int | None = Field(None, ge=0)
#     cost_price: float | None = Field(None, ge=0)
#     # SKU NO se puede cambiar (regla de negocio)


# # ============================================
# # OUTPUT DTOs
# # ============================================

# class ProductResponse(BaseModel):
#     """
#     DTO de respuesta PÚBLICA.
#     
#     Solo campos que el cliente puede ver.
#     NO incluye: cost_price, internal_notes, supplier_id
#     """
#     model_config = ConfigDict(from_attributes=True)
#     
#     id: int
#     name: str
#     sku: str
#     description: str | None
#     price: float
#     stock: int
#     created_at: datetime
#     # NO: cost_price, internal_notes, supplier_id


# class ProductDetail(ProductResponse):
#     """
#     DTO de respuesta DETALLADA.
#     
#     Extiende ProductResponse con información adicional.
#     Usado para endpoints de detalle o admin.
#     """
#     updated_at: datetime | None
#     is_available: bool = True
#     
#     @property
#     def in_stock(self) -> bool:
#         return self.stock > 0


# class ProductAdmin(ProductResponse):
#     """
#     DTO para administradores - incluye campos internos.
#     
#     Solo usar en endpoints protegidos para admins.
#     """
#     cost_price: float
#     supplier_id: int | None
#     profit_margin: float  # Campo calculado
