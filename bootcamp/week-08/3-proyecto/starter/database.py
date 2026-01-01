# ============================================
# DATABASE
# ============================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
    echo=settings.debug
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Generador de sesiones para dependency injection."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
