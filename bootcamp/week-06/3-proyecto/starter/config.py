# ============================================
# Blog API - Configuración
# ============================================
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    # Database
    DATABASE_URL: str = "sqlite:///./blog.db"
    
    # API
    API_TITLE: str = "Blog API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API de Blog con Service Layer"
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 10
    MAX_PAGE_SIZE: int = 100
    
    class Config:
        env_file = ".env"


settings = Settings()
