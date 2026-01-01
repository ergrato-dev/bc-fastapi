# ============================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================
print("--- Config: Configuración de la aplicación ---")

# Este módulo centraliza toda la configuración usando pydantic-settings.
# Permite cargar configuración desde variables de entorno o archivo .env

# Descomenta las siguientes líneas:

# from pydantic_settings import BaseSettings
# from functools import lru_cache


# class Settings(BaseSettings):
#     """
#     Configuración de la aplicación.
#     
#     Carga valores desde variables de entorno o .env
#     """
#     # Database
#     database_url: str = "sqlite:///./categories.db"
#     
#     # API
#     api_title: str = "Categories API"
#     api_version: str = "1.0.0"
#     debug: bool = True
#     
#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"


# @lru_cache
# def get_settings() -> Settings:
#     """
#     Retorna instancia cacheada de Settings.
#     
#     Usar @lru_cache evita recrear el objeto en cada request.
#     """
#     return Settings()
