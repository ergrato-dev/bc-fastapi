"""
Ejercicio 02: Field y Restricciones
===================================

Este ejercicio te enseña a usar Field() para validaciones avanzadas.
Descomenta cada sección y ejecuta para ver los resultados.

Ejecutar:
    docker compose up --build
    # o
    uv run python main.py
"""

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    EmailStr,
    HttpUrl,
    ValidationError,
    StringConstraints,
)
from typing import Annotated

print("=" * 60)
print("EJERCICIO 02: Field y Restricciones")
print("=" * 60)


# ============================================
# PASO 1: Validaciones Numéricas con Field
# ============================================
print("\n--- Paso 1: Validaciones Numéricas ---")

# Field() permite agregar restricciones numéricas:
# - gt: greater than (>)
# - ge: greater than or equal (>=)
# - lt: less than (<)
# - le: less than or equal (<=)

# Descomenta las siguientes líneas:
# class Product(BaseModel):
#     """Producto con validaciones numéricas."""
#     name: str
#     price: float = Field(gt=0, description="Precio debe ser positivo")
#     quantity: int = Field(ge=0, le=10000, description="Stock disponible")
#     discount: float = Field(ge=0, le=100, default=0, description="Porcentaje de descuento")
#     rating: float = Field(ge=1, le=5, default=5, description="Calificación 1-5")
#
# # Producto válido
# product = Product(
#     name="Laptop",
#     price=999.99,
#     quantity=50,
#     discount=10,
#     rating=4.5
# )
# print(f"Producto válido: {product}")
#
# # Intentar precio negativo
# try:
#     invalid = Product(name="Test", price=-10, quantity=5)
# except ValidationError as e:
#     print(f"\nError precio negativo:\n{e}")
#
# # Intentar cantidad fuera de rango
# try:
#     invalid = Product(name="Test", price=100, quantity=99999)
# except ValidationError as e:
#     print(f"\nError cantidad fuera de rango:\n{e}")


# ============================================
# PASO 2: Validaciones de Strings
# ============================================
print("\n--- Paso 2: Validaciones de Strings ---")

# Field() para strings:
# - min_length: longitud mínima
# - max_length: longitud máxima
# - pattern: expresión regular (regex)

# Descomenta las siguientes líneas:
# class User(BaseModel):
#     """Usuario con validaciones de strings."""
#     username: str = Field(
#         min_length=3,
#         max_length=20,
#         description="Username de 3-20 caracteres"
#     )
#     bio: str = Field(
#         max_length=500,
#         default="",
#         description="Biografía opcional"
#     )
#     # Regex: exactamente 10 dígitos
#     phone: str = Field(
#         pattern=r"^\d{10}$",
#         description="Teléfono de 10 dígitos"
#     )
#     # Regex: formato de código postal mexicano
#     zip_code: str = Field(
#         pattern=r"^\d{5}$",
#         description="Código postal de 5 dígitos"
#     )
#
# # Usuario válido
# user = User(
#     username="alice_dev",
#     bio="Desarrolladora Python",
#     phone="5551234567",
#     zip_code="06600"
# )
# print(f"Usuario válido: {user}")
#
# # Username muy corto
# try:
#     invalid = User(username="ab", phone="5551234567", zip_code="06600")
# except ValidationError as e:
#     print(f"\nError username corto:\n{e}")
#
# # Teléfono inválido
# try:
#     invalid = User(username="alice", phone="123", zip_code="06600")
# except ValidationError as e:
#     print(f"\nError teléfono inválido:\n{e}")


# ============================================
# PASO 3: Tipos Especiales de Pydantic
# ============================================
print("\n--- Paso 3: Tipos Especiales ---")

# Pydantic incluye tipos que validan formatos específicos.
# Requiere: uv add pydantic[email]

# Descomenta las siguientes líneas:
# class Contact(BaseModel):
#     """Contacto con tipos especiales."""
#     email: EmailStr                    # Email válido
#     website: HttpUrl                   # URL http/https
#     backup_email: EmailStr | None = None
#
# # Contacto válido
# contact = Contact(
#     email="alice@example.com",
#     website="https://alice.dev"
# )
# print(f"Contacto válido: {contact}")
#
# # Email inválido
# try:
#     invalid = Contact(email="not-an-email", website="https://test.com")
# except ValidationError as e:
#     print(f"\nError email inválido:\n{e}")
#
# # URL sin https
# try:
#     invalid = Contact(email="test@test.com", website="not-a-url")
# except ValidationError as e:
#     print(f"\nError URL inválida:\n{e}")


# ============================================
# PASO 4: Tipos Reutilizables con Annotated
# ============================================
print("\n--- Paso 4: Tipos Reutilizables ---")

# Annotated permite crear tipos personalizados reutilizables.

# Descomenta las siguientes líneas:
# # Definir tipos reutilizables
# Username = Annotated[
#     str,
#     StringConstraints(min_length=3, max_length=20, pattern=r"^[a-z0-9_]+$")
# ]
# 
# PositiveFloat = Annotated[float, Field(gt=0)]
# PositiveInt = Annotated[int, Field(gt=0)]
# Percentage = Annotated[float, Field(ge=0, le=100)]
# Port = Annotated[int, Field(ge=1, le=65535)]
#
# # Usar tipos personalizados
# class ServerConfig(BaseModel):
#     """Configuración de servidor con tipos reutilizables."""
#     host: str
#     port: Port
#     max_connections: PositiveInt
#     timeout: PositiveFloat
#     cpu_threshold: Percentage
#
# config = ServerConfig(
#     host="localhost",
#     port=8080,
#     max_connections=100,
#     timeout=30.5,
#     cpu_threshold=80
# )
# print(f"Config válida: {config}")
#
# # Usar Username en otro modelo
# class Account(BaseModel):
#     username: Username
#     display_name: str
#
# account = Account(username="alice_123", display_name="Alice")
# print(f"Account: {account}")
#
# # Username inválido (caracteres no permitidos)
# try:
#     invalid = Account(username="Alice@123", display_name="Alice")
# except ValidationError as e:
#     print(f"\nError username inválido:\n{e}")


# ============================================
# PASO 5: Alias y Documentación
# ============================================
print("\n--- Paso 5: Alias y Documentación ---")

# Field() permite definir alias (nombres alternativos) y documentación.

# Descomenta las siguientes líneas:
# class APIUser(BaseModel):
#     """Usuario de API con alias para JSON camelCase."""
#     model_config = ConfigDict(populate_by_name=True)
#     
#     user_id: int = Field(alias="userId")
#     full_name: str = Field(
#         alias="fullName",
#         description="Nombre completo del usuario",
#         examples=["John Doe", "Jane Smith"]
#     )
#     email_address: EmailStr = Field(
#         alias="emailAddress",
#         description="Correo electrónico"
#     )
#     is_active: bool = Field(
#         alias="isActive",
#         default=True,
#         description="Si el usuario está activo"
#     )
#
# # Crear desde JSON con camelCase (usando alias)
# json_data = {
#     "userId": 1,
#     "fullName": "Alice García",
#     "emailAddress": "alice@example.com",
#     "isActive": True
# }
# user = APIUser(**json_data)
# print(f"Usuario desde JSON: {user}")
#
# # También funciona con nombres Python (por populate_by_name=True)
# user2 = APIUser(
#     user_id=2,
#     full_name="Bob Smith",
#     email_address="bob@example.com"
# )
# print(f"Usuario desde Python: {user2}")
#
# # Serializar con alias (para devolver JSON camelCase)
# print(f"\nJSON con alias:\n{user.model_dump_json(by_alias=True, indent=2)}")
#
# # Serializar sin alias (nombres Python)
# print(f"\nJSON sin alias:\n{user.model_dump_json(indent=2)}")


# ============================================
# RESUMEN
# ============================================
print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
print("""
✅ Field(gt=, ge=, lt=, le=): Validaciones numéricas
✅ Field(min_length=, max_length=): Validaciones de longitud
✅ Field(pattern=): Validación con regex
✅ EmailStr, HttpUrl: Tipos especiales de Pydantic
✅ Annotated + StringConstraints: Tipos reutilizables
✅ Field(alias=): Nombres alternativos para JSON
✅ Field(description=, examples=): Documentación
""")
