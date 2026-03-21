# ============================================
# Blog API - Database Configuration
# ============================================
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

# Engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # Mostrar SQL (útil para debug)
    connect_args={"check_same_thread": False}  # Solo para SQLite
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()


def get_db():
    """
    Dependency para obtener sesión de DB.
    Se usa en los routers con Depends(get_db).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
