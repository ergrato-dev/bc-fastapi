"""
============================================
PROYECTO FINAL - Template de Configuración
============================================

Este archivo muestra cómo configurar tu aplicación
usando Pydantic Settings para manejo de variables de entorno.

Copia y adapta a tu proyecto.
"""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, PostgresDsn


class Settings(BaseSettings):
    """
    Configuración de la aplicación.
    
    Las variables se cargan de:
    1. Variables de entorno del sistema
    2. Archivo .env (si existe)
    
    Orden de prioridad: env vars > .env > defaults
    """
    
    # ============================================
    # APP
    # ============================================
    app_name: str = "Task Management API"
    app_version: str = "1.0.0"
    environment: str = Field(default="development", pattern="^(development|staging|production)$")
    debug: bool = False
    log_level: str = "INFO"
    
    # ============================================
    # DATABASE
    # ============================================
    database_url: str = Field(
        default="sqlite+aiosqlite:///./app.db",
        description="URL de conexión a la base de datos"
    )
    
    # Pool settings (para PostgreSQL)
    db_pool_size: int = 5
    db_max_overflow: int = 10
    db_pool_timeout: int = 30
    
    # ============================================
    # SECURITY
    # ============================================
    secret_key: str = Field(
        default="change-me-in-production-use-at-least-32-chars",
        min_length=32,
        description="Clave secreta para JWT"
    )
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7
    
    # ============================================
    # CORS
    # ============================================
    cors_origins: list[str] = ["http://localhost:3000"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ["*"]
    cors_allow_headers: list[str] = ["*"]
    
    # ============================================
    # RATE LIMITING (opcional)
    # ============================================
    rate_limit_requests: int = 100
    rate_limit_window_seconds: int = 60
    
    # ============================================
    # PAGINATION
    # ============================================
    default_page_size: int = 20
    max_page_size: int = 100
    
    # ============================================
    # PYDANTIC SETTINGS CONFIG
    # ============================================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # Ignorar variables no definidas
    )
    
    # ============================================
    # COMPUTED PROPERTIES
    # ============================================
    @property
    def is_production(self) -> bool:
        """Retorna True si estamos en producción."""
        return self.environment == "production"
    
    @property
    def is_development(self) -> bool:
        """Retorna True si estamos en desarrollo."""
        return self.environment == "development"
    
    @property
    def database_url_sync(self) -> str:
        """URL de DB para Alembic (sync)."""
        return self.database_url.replace("+asyncpg", "").replace("+aiosqlite", "")


@lru_cache
def get_settings() -> Settings:
    """
    Retorna instancia cacheada de Settings.
    
    El decorador @lru_cache asegura que solo se cree
    una instancia durante toda la vida de la aplicación.
    """
    return Settings()


# Instancia global (conveniente pero opcional)
settings = get_settings()


# ============================================
# EJEMPLO DE USO
# ============================================
if __name__ == "__main__":
    # Para debug, imprime la configuración
    s = get_settings()
    
    print("=== Configuración Actual ===")
    print(f"App: {s.app_name} v{s.app_version}")
    print(f"Environment: {s.environment}")
    print(f"Debug: {s.debug}")
    print(f"Database: {s.database_url[:50]}...")
    print(f"Secret Key: {s.secret_key[:10]}...")
    print(f"Token Expire: {s.access_token_expire_minutes} min")
    print(f"Is Production: {s.is_production}")
