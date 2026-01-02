"""
Configuración de Logging Estructurado con structlog

Este módulo configura structlog para producir logs estructurados.
"""

import logging
import sys
from typing import Any

# ============================================
# PASO 1: Importar structlog
# ============================================
print("--- Paso 1: Importar structlog ---")

# Descomenta las siguientes líneas:
# import structlog
# from structlog.types import Processor


# ============================================
# PASO 2: Función de Configuración
# ============================================
print("--- Paso 2: Función de Configuración ---")


def setup_logging(
    json_logs: bool = True,
    log_level: str = "INFO"
) -> None:
    """
    Configura structlog para la aplicación.
    
    Args:
        json_logs: Si True, logs en JSON. Si False, formato legible.
        log_level: Nivel mínimo de logging (DEBUG, INFO, WARNING, ERROR).
    """
    # Descomenta las siguientes líneas:
    
    # # Procesadores compartidos - transforman y enriquecen los logs
    # shared_processors: list[Processor] = [
    #     # Añade nivel de log (info, warning, error, etc.)
    #     structlog.stdlib.add_log_level,
    #     
    #     # Añade timestamp en formato ISO
    #     structlog.processors.TimeStamper(fmt="iso"),
    #     
    #     # Añade información de dónde se generó el log
    #     structlog.processors.CallsiteParameterAdder(
    #         parameters=[
    #             structlog.processors.CallsiteParameter.FILENAME,
    #             structlog.processors.CallsiteParameter.LINENO,
    #         ]
    #     ),
    #     
    #     # Procesa excepciones de forma legible
    #     structlog.processors.StackInfoRenderer(),
    #     structlog.processors.UnicodeDecoder(),
    # ]
    # 
    # # Seleccionar renderer según entorno
    # if json_logs:
    #     # Producción: JSON
    #     renderer = structlog.processors.JSONRenderer()
    # else:
    #     # Desarrollo: Consola con colores
    #     renderer = structlog.dev.ConsoleRenderer(colors=True)
    # 
    # # Configurar structlog
    # structlog.configure(
    #     processors=shared_processors + [
    #         structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    #     ],
    #     logger_factory=structlog.stdlib.LoggerFactory(),
    #     cache_logger_on_first_use=True,
    # )
    # 
    # # Configurar formatter para stdlib logging
    # formatter = structlog.stdlib.ProcessorFormatter(
    #     foreign_pre_chain=shared_processors,
    #     processors=[
    #         structlog.stdlib.ProcessorFormatter.remove_processors_meta,
    #         renderer,
    #     ],
    # )
    # 
    # # Handler para stdout
    # handler = logging.StreamHandler(sys.stdout)
    # handler.setFormatter(formatter)
    # 
    # # Configurar root logger
    # root_logger = logging.getLogger()
    # root_logger.handlers.clear()
    # root_logger.addHandler(handler)
    # root_logger.setLevel(log_level)
    # 
    # # Reducir verbosidad de librerías externas
    # for logger_name in ["uvicorn", "uvicorn.access", "uvicorn.error"]:
    #     logging.getLogger(logger_name).setLevel(logging.WARNING)
    
    pass  # Remover cuando descomentas


# ============================================
# PASO 3: Procesador para Datos Sensibles
# ============================================
print("--- Paso 3: Filtrar Datos Sensibles ---")


def mask_sensitive_data(
    logger: Any,
    method_name: str,
    event_dict: dict[str, Any]
) -> dict[str, Any]:
    """
    Procesador que enmascara datos sensibles en los logs.
    
    Nunca debemos loguear passwords, tokens, API keys, etc.
    """
    # Descomenta las siguientes líneas:
    
    # sensitive_keys = {
    #     "password", "passwd", "pwd",
    #     "token", "access_token", "refresh_token",
    #     "secret", "api_key", "apikey",
    #     "authorization", "auth",
    #     "credit_card", "card_number",
    # }
    # 
    # for key in list(event_dict.keys()):
    #     key_lower = key.lower()
    #     
    #     # Si la key es sensible, enmascararla
    #     if key_lower in sensitive_keys:
    #         event_dict[key] = "***MASKED***"
    #     
    #     # Enmascarar parcialmente emails
    #     elif key_lower == "email" and isinstance(event_dict[key], str):
    #         email = event_dict[key]
    #         if "@" in email:
    #             local, domain = email.split("@", 1)
    #             event_dict[key] = f"{local[:2]}***@{domain}"
    # 
    # return event_dict
    
    return event_dict  # Remover cuando descomentas


# ============================================
# PASO 4: Helper para obtener logger
# ============================================
print("--- Paso 4: Helper para Logger ---")


def get_logger(name: str | None = None):
    """
    Obtiene un logger de structlog.
    
    Args:
        name: Nombre opcional del logger.
    
    Returns:
        Logger de structlog configurado.
    """
    # Descomenta las siguientes líneas:
    
    # import structlog
    # return structlog.get_logger(name)
    
    # Fallback temporal
    return logging.getLogger(name or __name__)
