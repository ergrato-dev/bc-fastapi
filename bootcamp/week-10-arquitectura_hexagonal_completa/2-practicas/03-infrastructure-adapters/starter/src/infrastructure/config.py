"""
Configuración de la aplicación.

Usa Pydantic Settings para leer variables de entorno
y archivos .env automáticamente.
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


# ============================================
# PASO 1: Definir Settings
# ============================================
print("--- Paso 1: Definir Settings ---")

# Descomenta las siguientes líneas:

# class Settings(BaseSettings):
#     """
#     Configuración de la aplicación.
#     
#     Lee automáticamente de variables de entorno y .env
#     """
#     
#     # API
#     app_name: str = "Task Management API"
#     app_version: str = "1.0.0"
#     debug: bool = False
#     
#     # Server
#     host: str = "0.0.0.0"
#     port: int = 8000
#     
#     # Persistence
#     persistence_type: str = "memory"  # "memory" | "sqlite"
#     database_url: str = "sqlite:///./tasks.db"
#     
#     model_config = {
#         "env_file": ".env",
#         "env_file_encoding": "utf-8",
#         "extra": "ignore",
#     }


# ============================================
# PASO 2: Función para obtener settings (cacheada)
# ============================================
print("--- Paso 2: Función get_settings ---")

# Descomenta las siguientes líneas:

# @lru_cache
# def get_settings() -> Settings:
#     """
#     Obtener configuración (singleton).
#     
#     @lru_cache asegura que solo se lea una vez.
#     """
#     return Settings()


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Settings ---")
    # settings = get_settings()
    # print(f"App: {settings.app_name}")
    # print(f"Debug: {settings.debug}")
    print("✅ Settings configurado correctamente")
