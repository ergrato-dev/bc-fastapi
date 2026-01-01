"""
Ejercicio 02: Modelos Declarativos
==================================
Practica la creación de modelos con diferentes tipos y restricciones.

Instrucciones:
1. Lee cada sección
2. Descomenta el código paso a paso
3. Ejecuta: uv run python main.py
"""

# ============================================
# PASO 1: Setup Inicial
# ============================================
print("=== Paso 1: Setup completado ===")

# Configuración base: Engine, Base, SessionLocal

# Descomenta las siguientes líneas:
# from sqlalchemy import create_engine, String, CheckConstraint
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
# from datetime import datetime
#
# engine = create_engine("sqlite:///./models_test.db", echo=False)
#
# class Base(DeclarativeBase):
#     pass
#
# SessionLocal = sessionmaker(bind=engine)


# ============================================
# PASO 2: Modelo con Tipos Básicos
# ============================================
print("=== Paso 2: Modelo Product definido ===")

# Product demuestra tipos básicos:
# - int: ID autoincremental
# - str: requiere String(length) para el tamaño máximo
# - float: para precios y decimales
# - bool: con valor por defecto

# Descomenta las siguientes líneas:
# class Product(Base):
#     __tablename__ = "products"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     price: Mapped[float]
#     in_stock: Mapped[bool] = mapped_column(default=True)
#     
#     def __repr__(self) -> str:
#         return f"Product(id={self.id}, name='{self.name}', price={self.price}, in_stock={self.in_stock})"


# ============================================
# PASO 3: Modelo con Campos Opcionales
# ============================================
print("=== Paso 3: Modelo Customer definido ===")

# Customer demuestra campos nullable:
# - Mapped[str] → NOT NULL (requerido)
# - Mapped[str | None] → NULL permitido (opcional)

# Descomenta las siguientes líneas:
# class Customer(Base):
#     __tablename__ = "customers"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))  # Requerido
#     email: Mapped[str | None] = mapped_column(String(255))  # Opcional
#     phone: Mapped[str | None] = mapped_column(String(20))   # Opcional
#     
#     def __repr__(self) -> str:
#         return f"Customer(id={self.id}, name='{self.name}', email={self.email}, phone={self.phone})"


# ============================================
# PASO 4: Modelo con Valores por Defecto
# ============================================
print("=== Paso 4: Modelo Order definido ===")

# Order demuestra defaults de Python:
# - default="pending" → Python asigna antes del INSERT
# - default=datetime.utcnow → Función ejecutada en INSERT
# NOTA: datetime.utcnow sin () para que se llame en cada insert

# Descomenta las siguientes líneas:
# class Order(Base):
#     __tablename__ = "orders"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     status: Mapped[str] = mapped_column(String(20), default="pending")
#     total: Mapped[float] = mapped_column(default=0.0)
#     created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
#     
#     def __repr__(self) -> str:
#         return f"Order(id={self.id}, status='{self.status}', total={self.total}, created_at={self.created_at})"


# ============================================
# PASO 5: Modelo con Restricciones
# ============================================
print("=== Paso 5: Modelo User definido ===")

# User demuestra constraints:
# - unique=True → No permite valores duplicados
# - index=True → Crea índice para búsquedas rápidas
# - CheckConstraint → Validación a nivel de base de datos

# Descomenta las siguientes líneas:
# class User(Base):
#     __tablename__ = "users"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(50), unique=True)
#     email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
#     age: Mapped[int | None] = mapped_column(CheckConstraint("age >= 0"), default=None)
#     
#     def __repr__(self) -> str:
#         return f"User(id={self.id}, username='{self.username}', email='{self.email}', age={self.age})"


# ============================================
# PASO 6: Crear Tablas y Probar
# ============================================
print("=== Paso 6: Probando modelos ===")

# Descomenta las siguientes líneas:
# # Crear todas las tablas
# Base.metadata.create_all(bind=engine)
#
# with SessionLocal() as session:
#     # Probar Product (tipos básicos)
#     product = Product(name="Laptop", price=999.99)
#     session.add(product)
#     session.commit()
#     session.refresh(product)
#     print(f"Product: {product}")
#     
#     # Probar Customer (campos nullable)
#     customer = Customer(name="John")  # email y phone son None
#     session.add(customer)
#     session.commit()
#     session.refresh(customer)
#     print(f"Customer: {customer}")
#     
#     # Probar Order (defaults)
#     order = Order()  # status='pending', total=0.0, created_at=now
#     session.add(order)
#     session.commit()
#     session.refresh(order)
#     print(f"Order: {order}")
#     
#     # Probar User (constraints)
#     user = User(username="john_doe", email="john@example.com", age=25)
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     print(f"User: {user}")


# ============================================
# RESUMEN
# ============================================
print("\n=== Resumen de Tipos ===")
print("""
Mapeo de Tipos Python → SQLAlchemy → SQL:

| Python          | SQLAlchemy  | SQL         |
|-----------------|-------------|-------------|
| int             | Integer     | INTEGER     |
| str             | String(n)   | VARCHAR(n)  |
| float           | Float       | FLOAT       |
| bool            | Boolean     | BOOLEAN     |
| datetime        | DateTime    | DATETIME    |
| T | None        | nullable    | NULL allowed|

Restricciones útiles:
- primary_key=True  → Clave primaria
- unique=True       → Valores únicos
- index=True        → Índice para búsquedas
- default=value     → Valor por defecto (Python)
- CheckConstraint   → Validación en DB
""")
