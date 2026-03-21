"""
Ejercicio 03: Validadores Personalizados
========================================

Este ejercicio te enseña a crear validadores con @field_validator y @model_validator.
Descomenta cada sección y ejecuta para ver los resultados.

Ejecutar:
    docker compose up --build
    # o
    uv run python main.py
"""

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)
from typing import Any
import re

print("=" * 60)
print("EJERCICIO 03: Validadores Personalizados")
print("=" * 60)


# ============================================
# PASO 1: Field Validator Básico
# ============================================
print("\n--- Paso 1: Field Validator Básico ---")

# @field_validator valida y puede transformar campos.
# Siempre usa @classmethod debajo del decorador.

# Descomenta las siguientes líneas:
# class User(BaseModel):
#     """Usuario con validador de nombre."""
#     name: str
#     email: str
#     
#     @field_validator("name")
#     @classmethod
#     def validate_name(cls, v: str) -> str:
#         """Valida y capitaliza el nombre."""
#         # Validar
#         if len(v.strip()) < 2:
#             raise ValueError("Name must be at least 2 characters")
#         # Transformar
#         return v.strip().title()
#     
#     @field_validator("email")
#     @classmethod
#     def validate_email(cls, v: str) -> str:
#         """Convierte email a minúsculas."""
#         return v.lower().strip()
#
# # El validador transforma los datos
# user = User(name="  alice  ", email="  ALICE@Example.COM  ")
# print(f"Usuario: {user}")
# print(f"Nombre: '{user.name}'")  # 'Alice'
# print(f"Email: '{user.email}'")  # 'alice@example.com'
#
# # Error de validación
# try:
#     invalid = User(name="A", email="test@test.com")
# except ValidationError as e:
#     print(f"\nError validación:\n{e}")


# ============================================
# PASO 2: Validar Múltiples Campos
# ============================================
print("\n--- Paso 2: Validar Múltiples Campos ---")

# Un validador puede aplicarse a varios campos.

# Descomenta las siguientes líneas:
# class Person(BaseModel):
#     """Persona con validador para múltiples campos."""
#     first_name: str
#     last_name: str
#     nickname: str | None = None
#     
#     @field_validator("first_name", "last_name", "nickname")
#     @classmethod
#     def validate_names(cls, v: str | None) -> str | None:
#         """Limpia y capitaliza todos los nombres."""
#         if v is None:
#             return None
#         cleaned = v.strip()
#         if cleaned and len(cleaned) < 2:
#             raise ValueError("Name must be at least 2 characters")
#         return cleaned.title() if cleaned else None
#
# person = Person(
#     first_name="  john  ",
#     last_name="  DOE  ",
#     nickname="  johnny  "
# )
# print(f"Persona: {person}")
#
# # Sin nickname
# person2 = Person(first_name="jane", last_name="smith")
# print(f"Persona 2: {person2}")


# ============================================
# PASO 3: mode='before' vs mode='after'
# ============================================
print("\n--- Paso 3: mode='before' vs 'after' ---")

# mode='after' (default): Recibe el valor YA convertido al tipo
# mode='before': Recibe el valor RAW antes de conversión

# Descomenta las siguientes líneas:
# class Article(BaseModel):
#     """Artículo que acepta tags como string o lista."""
#     title: str
#     tags: list[str]
#     views: int = 0
#     
#     @field_validator("tags", mode="before")
#     @classmethod
#     def parse_tags(cls, v: Any) -> list[str]:
#         """Convierte string separado por comas a lista."""
#         # mode='before' recibe el valor raw
#         if isinstance(v, str):
#             # Si es string, dividir por comas
#             return [tag.strip() for tag in v.split(",") if tag.strip()]
#         return v
#     
#     @field_validator("tags", mode="after")
#     @classmethod
#     def validate_tags(cls, v: list[str]) -> list[str]:
#         """Valida y normaliza los tags."""
#         # mode='after' recibe la lista ya convertida
#         return [tag.lower() for tag in v]
#     
#     @field_validator("views", mode="before")
#     @classmethod
#     def parse_views(cls, v: Any) -> int:
#         """Acepta 'k' para miles."""
#         if isinstance(v, str) and v.endswith("k"):
#             return int(float(v[:-1]) * 1000)
#         return v
#
# # Tags como lista
# article1 = Article(title="FastAPI", tags=["Python", "API", "Backend"])
# print(f"Artículo 1: {article1.tags}")  # ['python', 'api', 'backend']
#
# # Tags como string (mode='before' lo convierte)
# article2 = Article(title="Pydantic", tags="Validation, Data, Models")
# print(f"Artículo 2: {article2.tags}")  # ['validation', 'data', 'models']
#
# # Views con 'k'
# article3 = Article(title="Popular", tags=["viral"], views="10.5k")
# print(f"Artículo 3 views: {article3.views}")  # 10500


# ============================================
# PASO 4: Model Validator
# ============================================
print("\n--- Paso 4: Model Validator ---")

# @model_validator valida el modelo completo.
# Útil para validaciones que dependen de múltiples campos.

# Descomenta las siguientes líneas:
# class UserRegistration(BaseModel):
#     """Registro de usuario con validación de contraseñas."""
#     email: str
#     password: str = Field(min_length=8)
#     confirm_password: str
#     
#     @model_validator(mode="after")
#     def validate_passwords_match(self) -> "UserRegistration":
#         """Valida que las contraseñas coincidan."""
#         if self.password != self.confirm_password:
#             raise ValueError("Passwords do not match")
#         return self
#
# # Válido
# user = UserRegistration(
#     email="test@example.com",
#     password="secret123",
#     confirm_password="secret123"
# )
# print(f"Usuario registrado: {user.email}")
#
# # Inválido
# try:
#     invalid = UserRegistration(
#         email="test@example.com",
#         password="secret123",
#         confirm_password="different"
#     )
# except ValidationError as e:
#     print(f"\nError passwords:\n{e}")
#
#
# # Model validator mode='before' para transformar datos
# class Config(BaseModel):
#     """Configuración que acepta diferentes formatos."""
#     host: str
#     port: int
#     
#     @model_validator(mode="before")
#     @classmethod
#     def parse_url(cls, data: Any) -> dict:
#         """Si recibe string URL, extraer host y port."""
#         if isinstance(data, str):
#             # Parsear "localhost:8080" o "host:port"
#             if ":" in data:
#                 host, port = data.rsplit(":", 1)
#                 return {"host": host, "port": port}
#         return data
#
# # Desde dict
# config1 = Config(host="localhost", port=8080)
# print(f"\nConfig 1: {config1}")
#
# # Desde string URL (model_validator lo parsea)
# config2 = Config.model_validate("192.168.1.1:3000")
# print(f"Config 2: {config2}")


# ============================================
# PASO 5: Validadores Prácticos
# ============================================
print("\n--- Paso 5: Validadores Prácticos ---")

# Ejemplos del mundo real.

# Descomenta las siguientes líneas:
# class SecureUser(BaseModel):
#     """Usuario con validación de contraseña segura."""
#     email: str
#     password: str
#     
#     @field_validator("password")
#     @classmethod
#     def validate_password_strength(cls, v: str) -> str:
#         """Valida que la contraseña sea segura."""
#         errors = []
#         if len(v) < 8:
#             errors.append("at least 8 characters")
#         if not re.search(r"[A-Z]", v):
#             errors.append("uppercase letter")
#         if not re.search(r"[a-z]", v):
#             errors.append("lowercase letter")
#         if not re.search(r"\d", v):
#             errors.append("digit")
#         if not re.search(r"[!@#$%^&*]", v):
#             errors.append("special character (!@#$%^&*)")
#         
#         if errors:
#             raise ValueError(f"Password must contain: {', '.join(errors)}")
#         return v
#
# # Contraseña válida
# secure_user = SecureUser(email="test@test.com", password="Secret123!")
# print(f"Usuario seguro: {secure_user.email}")
#
# # Contraseña inválida
# try:
#     invalid = SecureUser(email="test@test.com", password="weak")
# except ValidationError as e:
#     print(f"\nError contraseña débil:\n{e}")
#
#
# class Contact(BaseModel):
#     """Contacto con normalización de teléfono."""
#     name: str
#     phone: str
#     
#     @field_validator("phone", mode="before")
#     @classmethod
#     def normalize_phone(cls, v: str) -> str:
#         """Normaliza teléfono a formato estándar."""
#         # Eliminar todo excepto dígitos
#         digits = re.sub(r"\D", "", v)
#         
#         # Formato: +52 XXX XXX XXXX
#         if len(digits) == 10:
#             return f"+52 {digits[:3]} {digits[3:6]} {digits[6:]}"
#         elif len(digits) == 12 and digits.startswith("52"):
#             digits = digits[2:]
#             return f"+52 {digits[:3]} {digits[3:6]} {digits[6:]}"
#         
#         raise ValueError("Phone must have 10 digits")
#
# # Varios formatos de entrada
# c1 = Contact(name="Alice", phone="5551234567")
# c2 = Contact(name="Bob", phone="(555) 123-4567")
# c3 = Contact(name="Charlie", phone="+52 555 123 4567")
#
# print(f"\nContacto 1: {c1.phone}")  # +52 555 123 4567
# print(f"Contacto 2: {c2.phone}")  # +52 555 123 4567
# print(f"Contacto 3: {c3.phone}")  # +52 555 123 4567
#
#
# class BlogPost(BaseModel):
#     """Post con slug automático."""
#     title: str
#     slug: str | None = None
#     
#     @model_validator(mode="after")
#     def generate_slug(self) -> "BlogPost":
#         """Genera slug desde el título si no se proporciona."""
#         if self.slug is None:
#             # Generar slug desde título
#             slug = self.title.lower()
#             slug = re.sub(r"[^\w\s-]", "", slug)  # Quitar caracteres especiales
#             slug = re.sub(r"[\s_]+", "-", slug)   # Espacios a guiones
#             self.slug = slug.strip("-")
#         return self
#
# post1 = BlogPost(title="Hello World!")
# post2 = BlogPost(title="Introducción a FastAPI", slug="intro-fastapi")
#
# print(f"\nPost 1: '{post1.title}' -> '{post1.slug}'")
# print(f"Post 2: '{post2.title}' -> '{post2.slug}'")


# ============================================
# RESUMEN
# ============================================
print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
print("""
✅ @field_validator("campo"): Validar un campo específico
✅ @field_validator("a", "b"): Validar múltiples campos
✅ mode='before': Antes de conversión de tipos (input raw)
✅ mode='after': Después de conversión (tipo final)
✅ @model_validator: Validar modelo completo
✅ raise ValueError: Para errores de validación
✅ return self: Siempre retornar el valor/modelo
""")
