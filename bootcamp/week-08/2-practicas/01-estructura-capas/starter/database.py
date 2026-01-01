# ============================================
# CONFIGURACIÓN DE BASE DE DATOS
# ============================================
print("--- Database: Conexión a SQLite ---")

# Este módulo configura la conexión a la base de datos
# y proporciona el generador de sesiones.

# Descomenta las siguientes líneas:

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import get_settings

# settings = get_settings()

# # Engine - conexión a la base de datos
# engine = create_engine(
#     settings.database_url,
#     connect_args={"check_same_thread": False},  # Solo para SQLite
#     echo=settings.debug  # Log de SQL en debug
# )

# # SessionLocal - fábrica de sesiones
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# # Base para modelos
# Base = declarative_base()


# def get_db():
#     """
#     Generador de sesiones para inyección de dependencias.
#     
#     Yields:
#         Session: Sesión de base de datos
#     """
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
