# ============================================
# Configuration - Pydantic Settings
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para configurar
# la aplicación con Pydantic Settings.
# ============================================

from functools import lru_cache

# TODO: Importar BaseSettings y SettingsConfigDict de pydantic_settings
# from pydantic_settings import BaseSettings, SettingsConfigDict


# ============================================
# TODO 1: Definir la clase Settings
# ============================================
# class Settings(BaseSettings):
#     """Application settings loaded from environment"""
#
#     # Database
#     database_url: str = "sqlite:///./test.db"
#
#     # Redis
#     redis_url: str = "redis://localhost:6379/0"
#
#     # Security
#     secret_key: str = "dev-secret-change-in-production"
#
#     # Environment
#     environment: str = "development"
#     log_level: str = "debug"
#
#     # API
#     api_host: str = "0.0.0.0"
#     api_port: int = 8000
#
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         env_file_encoding="utf-8",
#         case_sensitive=False,
#     )
#
#     @property
#     def is_production(self) -> bool:
#         return self.environment == "production"


# ============================================
# TODO 2: Función para obtener settings (cached)
# ============================================
# @lru_cache
# def get_settings() -> Settings:
#     """Get cached settings instance"""
#     return Settings()


# ============================================
# Placeholder mientras se implementa
# ============================================
class Settings:
    """Placeholder - implement the real Settings class above"""

    database_url: str = "sqlite:///./test.db"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "dev-secret"
    environment: str = "development"
    log_level: str = "debug"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    @property
    def is_production(self) -> bool:
        return self.environment == "production"


@lru_cache
def get_settings() -> Settings:
    """Get settings instance"""
    return Settings()
