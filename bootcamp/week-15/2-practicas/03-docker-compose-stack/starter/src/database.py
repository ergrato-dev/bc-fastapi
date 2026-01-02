"""
Database connection - Práctica 03
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency to get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_db_connection() -> dict:
    """Check database connectivity."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.scalar()
            return {
                "status": "connected",
                "database": "postgresql",
                "version": version,
            }
    except Exception as e:
        return {
            "status": "error",
            "database": "postgresql",
            "error": str(e),
        }
