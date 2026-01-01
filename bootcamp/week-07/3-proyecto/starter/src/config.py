# ============================================
# Configuración de la aplicación
# ============================================
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    app_name: str = "Task Manager API"
    debug: bool = True
    database_url: str = "sqlite:///./tasks.db"
    
    class Config:
        env_file = ".env"


settings = Settings()
