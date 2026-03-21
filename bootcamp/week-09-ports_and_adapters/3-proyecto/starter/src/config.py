"""
Configuración de la aplicación.
"""
from pydantic_settings import BaseSettings
from pydantic import Field
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    TEST = "test"
    PRODUCTION = "production"


class Settings(BaseSettings):
    """Configuración principal."""
    
    # General
    env: Environment = Field(default=Environment.DEVELOPMENT)
    debug: bool = Field(default=True)
    
    # Notificaciones
    notification_provider: str = Field(default="console")
    
    # SMTP
    smtp_host: str = Field(default="localhost")
    smtp_port: int = Field(default=587)
    smtp_username: str = Field(default="")
    smtp_password: str = Field(default="")
    smtp_from: str = Field(default="noreply@example.com")
    
    # Twilio SMS
    twilio_sid: str = Field(default="")
    twilio_token: str = Field(default="")
    twilio_from: str = Field(default="")
    
    # Webhook
    webhook_timeout: int = Field(default=30)
    
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
