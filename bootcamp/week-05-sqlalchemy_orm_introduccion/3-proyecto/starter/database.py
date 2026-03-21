"""
Database Configuration
======================
Configuración de SQLAlchemy para la Library API.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from typing import Generator

# URL de conexión SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./library.db"

# Engine con configuración para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario para SQLite + FastAPI
)

# Factory de sesiones
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    """Clase base para todos los modelos SQLAlchemy"""
    pass


def get_db() -> Generator[Session, None, None]:
    """
    Dependency que provee una sesión de base de datos.
    
    Uso en endpoints:
        @app.get("/items")
        def list_items(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
