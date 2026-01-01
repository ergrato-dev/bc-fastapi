"""
Configuración de la aplicación.

Usa variables de entorno para configurar diferentes comportamientos.
"""
from pydantic_settings import BaseSettings
from pydantic import Field
from enum import Enum


class Environment(str, Enum):
    """Entornos disponibles."""
    DEVELOPMENT = "development"
    TEST = "test"
    PRODUCTION = "production"


class Settings(BaseSettings):
    """
    Configuración principal.
    
    Las variables se cargan de entorno o .env
    """
    # Entorno
    env: Environment = Field(default=Environment.DEVELOPMENT)
    debug: bool = Field(default=True)
    
    # Notificaciones
    notification_provider: str = Field(default="console")
    
    # SMTP (para producción)
    smtp_host: str = Field(default="localhost")
    smtp_port: int = Field(default=587)
    smtp_username: str = Field(default="")
    smtp_password: str = Field(default="")
    smtp_from: str = Field(default="noreply@example.com")
    
    # SMS (para producción)
    twilio_sid: str = Field(default="")
    twilio_token: str = Field(default="")
    twilio_from: str = Field(default="")
    
    model_config = {"env_prefix": "", "env_file": ".env"}


# Instancia global
settings = Settings()
