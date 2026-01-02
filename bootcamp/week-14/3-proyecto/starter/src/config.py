"""
Configuración centralizada de la aplicación.

Usa pydantic-settings para cargar variables de entorno
con validación y valores por defecto.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    
    # Entorno
    environment: str = "development"
    debug: bool = False
    
    # Base de datos
    database_url: str = "sqlite:///./tasks.db"
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # Seguridad
    secret_key: str = "change-me-in-production"
    allowed_origins: str = "http://localhost:3000"
    
    # Rate Limiting
    rate_limit_enabled: bool = True
    rate_limit_default: str = "100/minute"
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "json"
    
    # Métricas
    metrics_enabled: bool = True
    
    @property
    def allowed_origins_list(self) -> list[str]:
        """Retorna lista de orígenes permitidos."""
        return [origin.strip() for origin in self.allowed_origins.split(",")]
    
    @property
    def is_development(self) -> bool:
        """Verifica si está en desarrollo."""
        return self.environment == "development"
    
    @property
    def is_production(self) -> bool:
        """Verifica si está en producción."""
        return self.environment == "production"


@lru_cache
def get_settings() -> Settings:
    """
    Retorna configuración cacheada.
    
    Usa lru_cache para evitar leer .env múltiples veces.
    """
    return Settings()
