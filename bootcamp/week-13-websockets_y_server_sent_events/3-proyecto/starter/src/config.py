"""
Configuración del proyecto.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    # Database
    DATABASE_URL: str = "sqlite:///./chat.db"
    
    # JWT
    SECRET_KEY: str = "your-super-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # App
    APP_NAME: str = "Realtime Chat"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()
