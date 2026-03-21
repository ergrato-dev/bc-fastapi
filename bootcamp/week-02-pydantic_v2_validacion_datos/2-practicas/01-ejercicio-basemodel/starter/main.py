"""
Ejercicio 01: BaseModel Básico
==============================

Este ejercicio te enseña a crear modelos Pydantic básicos.
Descomenta cada sección y ejecuta para ver los resultados.

Ejecutar:
    docker compose up --build
    # o
    uv run python main.py
"""

from pydantic import BaseModel, ConfigDict, ValidationError

print("=" * 60)
print("EJERCICIO 01: BaseModel Básico")
print("=" * 60)


# ============================================
# PASO 1: BaseModel Simple
# ============================================
print("\n--- Paso 1: BaseModel Simple ---")

# Un BaseModel básico define campos con sus tipos.
# Todos los campos sin valor por defecto son REQUERIDOS.

# Descomenta las siguientes líneas:
# class User(BaseModel):
#     """Modelo de usuario básico."""
#     name: str
#     email: str
#     age: int
#
# # Crear instancia válida
# user = User(name="Alice", email="alice@example.com", age=30)
# print(f"Usuario creado: {user}")
# print(f"Nombre: {user.name}")
# print(f"Email: {user.email}")
# print(f"Edad: {user.age}")
#
# # Pydantic convierte tipos automáticamente (coerción)
# user2 = User(name="Bob", email="bob@test.com", age="25")  # age como string
# print(f"\nUsuario 2 (age era string): {user2}")
# print(f"Tipo de age: {type(user2.age)}")  # int, no str
#
# # Intentar crear con datos inválidos
# try:
#     invalid_user = User(name="Charlie", email="charlie@test.com", age="no-es-numero")
# except ValidationError as e:
#     print(f"\nError de validación:\n{e}")


# ============================================
# PASO 2: Campos Opcionales
# ============================================
print("\n--- Paso 2: Campos Opcionales ---")

# Los campos con valor por defecto son OPCIONALES.
# Los campos requeridos deben ir ANTES que los opcionales.

# Descomenta las siguientes líneas:
# class Product(BaseModel):
#     """Modelo de producto con campos opcionales."""
#     # Campos requeridos (sin default)
#     name: str
#     price: float
#     
#     # Campos opcionales (con default)
#     description: str | None = None
#     quantity: int = 0
#     active: bool = True
#     tags: list[str] = []  # ⚠️ Cuidado con mutables como default
#
# # Solo campos requeridos
# product1 = Product(name="Laptop", price=999.99)
# print(f"Producto 1: {product1}")
#
# # Con algunos opcionales
# product2 = Product(
#     name="Mouse",
#     price=29.99,
#     description="Wireless mouse",
#     quantity=50
# )
# print(f"Producto 2: {product2}")
#
# # Todos los campos
# product3 = Product(
#     name="Keyboard",
#     price=79.99,
#     description="Mechanical keyboard",
#     quantity=25,
#     active=True,
#     tags=["electronics", "gaming"]
# )
# print(f"Producto 3: {product3}")


# ============================================
# PASO 3: Configuración con model_config
# ============================================
print("\n--- Paso 3: model_config ---")

# model_config permite configurar el comportamiento del modelo.

# Descomenta las siguientes líneas:
# class StrictUser(BaseModel):
#     """Usuario con configuración estricta."""
#     model_config = ConfigDict(
#         str_strip_whitespace=True,  # Quitar espacios al inicio/final
#         extra="forbid",              # No permitir campos extra
#     )
#     
#     name: str
#     email: str
#
# # str_strip_whitespace quita espacios
# user = StrictUser(name="  Alice  ", email="  alice@test.com  ")
# print(f"Usuario (espacios eliminados): '{user.name}' / '{user.email}'")
#
# # extra="forbid" rechaza campos no definidos
# try:
#     invalid = StrictUser(name="Bob", email="bob@test.com", age=30)  # age no existe
# except ValidationError as e:
#     print(f"\nError por campo extra:\n{e}")
#
#
# # Modelo que permite campos extra
# class FlexibleUser(BaseModel):
#     model_config = ConfigDict(extra="allow")
#     name: str
#
# flex_user = FlexibleUser(name="Charlie", nickname="Chuck", role="admin")
# print(f"\nUsuario flexible: {flex_user}")
# print(f"Campos extra: {flex_user.model_dump()}")


# ============================================
# PASO 4: Serialización
# ============================================
print("\n--- Paso 4: Serialización ---")

# Los modelos tienen métodos para convertir a dict/JSON.

# Descomenta las siguientes líneas:
# class Article(BaseModel):
#     """Modelo de artículo para serialización."""
#     title: str
#     content: str
#     published: bool = False
#     views: int = 0
#
# article = Article(
#     title="Introducción a Pydantic",
#     content="Pydantic es una biblioteca de validación...",
#     published=True,
#     views=100
# )
#
# # Convertir a diccionario
# article_dict = article.model_dump()
# print(f"Como dict: {article_dict}")
# print(f"Tipo: {type(article_dict)}")
#
# # Convertir a JSON string
# article_json = article.model_dump_json(indent=2)
# print(f"\nComo JSON:\n{article_json}")
#
# # Excluir campos
# print(f"\nSin 'views': {article.model_dump(exclude={'views'})}")
#
# # Solo incluir ciertos campos
# print(f"Solo título y publicado: {article.model_dump(include={'title', 'published'})}")


# ============================================
# PASO 5: Modelos Anidados
# ============================================
print("\n--- Paso 5: Modelos Anidados ---")

# Los modelos pueden contener otros modelos.

# Descomenta las siguientes líneas:
# class Address(BaseModel):
#     """Dirección postal."""
#     street: str
#     city: str
#     country: str = "México"
#     zip_code: str | None = None
#
# class Company(BaseModel):
#     """Empresa."""
#     name: str
#     address: Address
#
# class Employee(BaseModel):
#     """Empleado con empresa."""
#     name: str
#     email: str
#     company: Company
#     home_address: Address | None = None
#
# # Crear desde diccionarios anidados
# employee_data = {
#     "name": "Alice García",
#     "email": "alice@techcorp.com",
#     "company": {
#         "name": "TechCorp",
#         "address": {
#             "street": "Av. Reforma 123",
#             "city": "CDMX",
#             "zip_code": "06600"
#         }
#     },
#     "home_address": {
#         "street": "Calle Roble 456",
#         "city": "CDMX"
#     }
# }
#
# employee = Employee(**employee_data)
# # También funciona: Employee.model_validate(employee_data)
#
# print(f"Empleado: {employee.name}")
# print(f"Empresa: {employee.company.name}")
# print(f"Ciudad empresa: {employee.company.address.city}")
# print(f"Dirección casa: {employee.home_address.street if employee.home_address else 'N/A'}")
#
# # Serializar (todo se convierte a dicts anidados)
# print(f"\nComo JSON:\n{employee.model_dump_json(indent=2)}")


# ============================================
# RESUMEN
# ============================================
print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
print("""
✅ BaseModel: Clase base para modelos Pydantic
✅ Campos requeridos: Sin valor por defecto
✅ Campos opcionales: Con valor por defecto o | None
✅ model_config: Configuración del modelo
✅ model_dump(): Convertir a diccionario
✅ model_dump_json(): Convertir a JSON string
✅ Modelos anidados: Modelos dentro de modelos
""")
