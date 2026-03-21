"""
Configuración de la aplicación con Pydantic Settings.
"""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    
    # App
    app_name: str = "Task Management API"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Persistence
    persistence_type: str = "memory"
    database_url: str = "sqlite:///./tasks.db"


@lru_cache
def get_settings() -> Settings:
    """Factory singleton para Settings."""
    return Settings()
