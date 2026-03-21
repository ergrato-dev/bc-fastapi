# ============================================
# PASO 1: Configurar la Base de Datos
# ============================================
print("--- Configurando Base de Datos ---")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Descomenta las siguientes líneas:
# engine = create_engine("sqlite:///./blog.db", echo=True)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

# Placeholder para que el archivo sea importable
# (elimina esto cuando descomentas lo de arriba)
engine = None
SessionLocal = None
Base = None
