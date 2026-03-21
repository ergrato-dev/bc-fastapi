# config.py
"""
Configuración de la aplicación.

En producción, estas variables vendrían de variables de entorno.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    # Base de datos
    DATABASE_URL: str = "sqlite:///./auth_system.db"
    
    # JWT
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # App
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"


# Instancia global de configuración
settings = Settings()
