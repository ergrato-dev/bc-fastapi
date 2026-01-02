# ============================================
# Database Connection - SQLAlchemy
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para configurar
# la conexión a PostgreSQL con SQLAlchemy.
# ============================================

from typing import Generator

# TODO: Importar SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

from src.config import get_settings

settings = get_settings()


# ============================================
# TODO 1: Definir Base para modelos
# ============================================
# class Base(DeclarativeBase):
#     """Base class for SQLAlchemy models"""
#     pass


# ============================================
# TODO 2: Crear engine y session
# ============================================
# engine = create_engine(
#     settings.database_url,
#     pool_pre_ping=True,  # Verify connections before using
#     pool_size=5,
#     max_overflow=10,
# )
#
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )


# ============================================
# TODO 3: Dependency para obtener DB session
# ============================================
# def get_db() -> Generator[Session, None, None]:
#     """
#     Database session dependency.
#     
#     Yields a database session and ensures it's closed after use.
#     """
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# ============================================
# TODO 4: Función para inicializar DB
# ============================================
# def init_db() -> None:
#     """Create all database tables"""
#     Base.metadata.create_all(bind=engine)


# ============================================
# Placeholder mientras se implementa
# ============================================
class Base:
    """Placeholder - implement real DeclarativeBase above"""

    pass


def get_db() -> Generator:
    """Placeholder - implement real session dependency above"""
    yield None


def init_db() -> None:
    """Placeholder - implement real init_db above"""
    pass
