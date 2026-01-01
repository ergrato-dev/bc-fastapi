# ============================================
# CONFIGURACIÓN
# ============================================

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    # Database
    database_url: str = "sqlite:///./ecommerce.db"
    
    # API
    api_title: str = "E-Commerce API"
    api_version: str = "1.0.0"
    api_description: str = "API de E-Commerce con arquitectura en capas"
    debug: bool = True
    
    # Business
    tax_rate: float = 0.16
    free_shipping_threshold: float = 100.0
    shipping_cost: float = 10.0
    
    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
