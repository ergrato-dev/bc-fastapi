"""
Ejercicio 01: Configuración SQLAlchemy
======================================
Aprende a configurar Engine, Base y Session.

Instrucciones:
1. Lee cada sección
2. Descomenta el código paso a paso
3. Ejecuta: uv run python main.py
"""

# ============================================
# PASO 1: Crear el Engine
# ============================================
print("=== Paso 1: Engine creado ===")

# El Engine es el punto de entrada a la base de datos.
# create_engine() crea la conexión usando una URL.
# echo=True muestra el SQL generado (útil para aprender).

# Descomenta las siguientes líneas:
# from sqlalchemy import create_engine
#
# engine = create_engine(
#     "sqlite:///./test.db",  # Archivo SQLite local
#     echo=True               # Mostrar SQL en consola
# )


# ============================================
# PASO 2: Crear la Base Declarativa
# ============================================
print("=== Paso 2: Base declarativa lista ===")

# DeclarativeBase es la clase padre de todos los modelos.
# Cada modelo que herede de Base será una tabla.

# Descomenta las siguientes líneas:
# from sqlalchemy.orm import DeclarativeBase
#
# class Base(DeclarativeBase):
#     """Clase base para todos los modelos"""
#     pass


# ============================================
# PASO 3: Definir un Modelo Simple
# ============================================
print("=== Paso 3: Modelo Item definido ===")

# Un modelo representa una tabla en la base de datos.
# - __tablename__: nombre de la tabla
# - Mapped[T]: tipo de la columna en Python
# - mapped_column(): configuración de la columna

# Descomenta las siguientes líneas:
# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column
#
# class Item(Base):
#     __tablename__ = "items"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     
#     def __repr__(self) -> str:
#         return f"Item(id={self.id}, name='{self.name}')"


# ============================================
# PASO 4: Crear las Tablas
# ============================================
print("=== Paso 4: Tablas creadas ===")

# create_all() examina todas las clases que heredan de Base
# y crea las tablas correspondientes si no existen.

# Descomenta la siguiente línea:
# Base.metadata.create_all(bind=engine)


# ============================================
# PASO 5: Configurar SessionLocal
# ============================================
print("=== Paso 5: SessionLocal configurado ===")

# sessionmaker crea una "fábrica" de sesiones.
# Cada vez que llamamos SessionLocal() obtenemos una nueva sesión.
# - autocommit=False: debemos hacer commit explícito
# - autoflush=False: controlamos cuándo sincronizar con DB

# Descomenta las siguientes líneas:
# from sqlalchemy.orm import sessionmaker
#
# SessionLocal = sessionmaker(
#     bind=engine,
#     autocommit=False,
#     autoflush=False
# )


# ============================================
# PASO 6: Probar la Sesión
# ============================================
print("=== Paso 6: Probando sesión ===")

# La sesión maneja transacciones.
# - add(): marca objeto para insertar
# - commit(): guarda cambios en DB
# - El context manager (with) cierra la sesión automáticamente

# Descomenta las siguientes líneas:
# from sqlalchemy import select
#
# with SessionLocal() as session:
#     # Crear un item
#     item = Item(name="Test Item")
#     session.add(item)
#     session.commit()
#     
#     # El ID se genera después del commit
#     print(f"Item creado con ID: {item.id}")
#     
#     # Consultar todos los items
#     stmt = select(Item)
#     items = session.execute(stmt).scalars().all()
#     print(f"Items en DB: {items}")


# ============================================
# RESUMEN
# ============================================
print("\n=== Resumen ===")
print("""
Componentes de SQLAlchemy:

1. Engine      → Conexión a la base de datos
2. Base        → Clase padre para modelos (tablas)
3. Model       → Clase que representa una tabla
4. Session     → Maneja transacciones (add, commit, query)
5. sessionmaker → Factory para crear sesiones

Flujo típico:
Engine → Base → Models → create_all() → Session → CRUD
""")
