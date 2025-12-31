# ============================================
# PROYECTO: API DE SALUDO
# ============================================
# Semana 01 - Bootcamp FastAPI Zero to Hero
#
# En este proyecto implementarás una API de saludos
# que demuestra el uso de:
# - FastAPI
# - Type hints
# - Path parameters
# - Query parameters
# - Documentación automática
# ============================================

from fastapi import FastAPI

# ============================================
# DATOS DE CONFIGURACIÓN
# ============================================

# Diccionario de saludos por idioma
GREETINGS: dict[str, str] = {
    "es": "¡Hola, {name}!",
    "en": "Hello, {name}!",
    "fr": "Bonjour, {name}!",
    "de": "Hallo, {name}!",
    "it": "Ciao, {name}!",
    "pt": "Olá, {name}!",
}

# Idiomas soportados (para documentación)
SUPPORTED_LANGUAGES = list(GREETINGS.keys())


# ============================================
# TODO 1: CREAR LA INSTANCIA DE FASTAPI
# ============================================
# Crea una instancia de FastAPI con la siguiente configuración:
# - title: "Greeting API"
# - description: "API de saludos multiidioma"
# - version: "1.0.0"
#
# Ejemplo:
#   app = FastAPI(title="...", description="...", version="...")

app = None  # TODO: Reemplaza None con la instancia de FastAPI


# ============================================
# TODO 2: ENDPOINT RAÍZ
# ============================================
# Implementa el endpoint GET /
#
# Debe retornar:
# {
#     "name": "Greeting API",
#     "version": "1.0.0",
#     "docs": "/docs",
#     "languages": ["es", "en", "fr", "de", "it", "pt"]
# }
#
# Recuerda:
# - Usar el decorador @app.get("/")
# - Definir la función como async
# - Agregar docstring para la documentación

# @app.get("/")
# async def root() -> dict[str, str | list[str]]:
#     """Información de la API."""
#     # TODO: Implementar
#     pass


# ============================================
# TODO 3: SALUDO PERSONALIZADO
# ============================================
# Implementa el endpoint GET /greet/{name}
#
# Parámetros:
# - name (path): Nombre de la persona a saludar
# - language (query, default="es"): Idioma del saludo
#
# Debe retornar:
# {
#     "greeting": "¡Hola, Carlos!",
#     "language": "es",
#     "name": "Carlos"
# }
#
# Si el idioma no existe, usar español por defecto.

# @app.get("/greet/{name}")
# async def greet(
#     name: str,
#     language: str = "es",
# ) -> dict[str, str]:
#     """
#     Saluda a una persona en el idioma especificado.
#     
#     Args:
#         name: Nombre de la persona
#         language: Código de idioma (es, en, fr, de, it, pt)
#     
#     Returns:
#         dict: Saludo personalizado
#     """
#     # TODO: Implementar
#     # 1. Obtener el template del saludo (usar .get() para default)
#     # 2. Formatear el saludo con el nombre
#     # 3. Retornar el diccionario con greeting, language y name
#     pass


# ============================================
# TODO 4: SALUDO FORMAL
# ============================================
# Implementa el endpoint GET /greet/{name}/formal
#
# Parámetros:
# - name (path): Nombre/apellido de la persona
# - title (query, default="Sr./Sra."): Título formal
#
# Debe retornar:
# {
#     "greeting": "Estimado/a Dr. García, es un placer saludarle.",
#     "title": "Dr.",
#     "name": "García"
# }

# @app.get("/greet/{name}/formal")
# async def greet_formal(
#     name: str,
#     title: str = "Sr./Sra.",
# ) -> dict[str, str]:
#     """
#     Genera un saludo formal con título.
#     
#     Args:
#         name: Nombre o apellido de la persona
#         title: Título formal (Dr., Ing., Prof., Lic., etc.)
#     
#     Returns:
#         dict: Saludo formal
#     """
#     # TODO: Implementar
#     # 1. Construir el saludo formal
#     # 2. Retornar el diccionario
#     pass


# ============================================
# TODO 5: SALUDO SEGÚN LA HORA
# ============================================
# Implementa el endpoint GET /greet/{name}/time-based
#
# Parámetros:
# - name (path): Nombre de la persona
# - hour (query): Hora del día (0-23)
#
# Lógica:
# - 5 <= hour < 12: "Buenos días, {name}!"
# - 12 <= hour < 18: "Buenas tardes, {name}!"
# - else: "Buenas noches, {name}!"
#
# Debe retornar:
# {
#     "greeting": "Buenos días, Ana!",
#     "hour": 10,
#     "period": "morning"
# }

# Función auxiliar para determinar el período del día
def get_day_period(hour: int) -> tuple[str, str]:
    """
    Determina el saludo y período según la hora.
    
    Args:
        hour: Hora del día (0-23)
    
    Returns:
        tuple: (saludo, período)
    """
    # TODO: Implementar
    # Retorna una tupla con (saludo, period)
    # Ejemplo: ("Buenos días", "morning")
    pass


# @app.get("/greet/{name}/time-based")
# async def greet_time_based(
#     name: str,
#     hour: int,
# ) -> dict[str, str | int]:
#     """
#     Saluda según la hora del día.
#     
#     Args:
#         name: Nombre de la persona
#         hour: Hora del día (0-23)
#     
#     Returns:
#         dict: Saludo con período del día
#     """
#     # TODO: Implementar
#     # 1. Validar que hour esté entre 0-23
#     # 2. Usar get_day_period() para obtener el saludo
#     # 3. Retornar el diccionario
#     pass


# ============================================
# TODO 6: HEALTH CHECK
# ============================================
# Implementa el endpoint GET /health
#
# Debe retornar:
# {
#     "status": "healthy",
#     "service": "greeting-api",
#     "version": "1.0.0"
# }

# @app.get("/health")
# async def health_check() -> dict[str, str]:
#     """Verifica el estado de la API."""
#     # TODO: Implementar
#     pass


# ============================================
# VERIFICACIÓN
# ============================================
# Una vez completados todos los TODOs:
#
# 1. Ejecutar:
#    docker compose up --build
#
# 2. Probar en el navegador:
#    http://localhost:8000/docs
#
# 3. Verificar cada endpoint:
#    - GET /
#    - GET /greet/Carlos
#    - GET /greet/Carlos?language=en
#    - GET /greet/García/formal?title=Dr.
#    - GET /greet/Ana/time-based?hour=10
#    - GET /health
# ============================================
