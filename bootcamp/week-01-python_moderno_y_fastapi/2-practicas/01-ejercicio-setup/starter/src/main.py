# ============================================
# MAIN.PY - Aplicación FastAPI
# ============================================
# Este es el punto de entrada de nuestra API.
# Aquí definimos la aplicación y sus endpoints.

print("=" * 50)
print("Ejercicio 01: Setup del Entorno")
print("=" * 50)

# --------------------------------------------
# PASO 1: Importar FastAPI
# --------------------------------------------
# FastAPI es el framework que usamos para crear APIs
# Descomenta la siguiente línea:

# from fastapi import FastAPI


# --------------------------------------------
# PASO 2: Crear la instancia de la aplicación
# --------------------------------------------
# Creamos una instancia de FastAPI con metadata
# que aparecerá en la documentación automática
# Descomenta el siguiente bloque:

# app = FastAPI(
#     title="Mi Primera API",
#     description="API creada en el Ejercicio 01 del Bootcamp",
#     version="0.1.0",
# )


# --------------------------------------------
# PASO 3: Crear el endpoint raíz
# --------------------------------------------
# El decorador @app.get("/") define un endpoint GET
# La función retorna un diccionario que se convierte a JSON
# Descomenta el siguiente bloque:

# @app.get("/")
# async def root():
#     """
#     Endpoint raíz que retorna un mensaje de bienvenida.
#     
#     Returns:
#         dict: Mensaje de saludo
#     """
#     return {"message": "¡Hola desde FastAPI!"}


# --------------------------------------------
# PASO 4: Crear endpoint de health check
# --------------------------------------------
# Es buena práctica tener un endpoint para verificar
# que la API está funcionando correctamente
# Descomenta el siguiente bloque:

# @app.get("/health")
# async def health_check():
#     """
#     Verifica que la API está funcionando.
#     
#     Returns:
#         dict: Estado de la API
#     """
#     return {"status": "healthy", "service": "mi-primera-api"}


# --------------------------------------------
# PASO 5: Crear endpoint con información
# --------------------------------------------
# Este endpoint muestra información útil sobre la API
# Descomenta el siguiente bloque:

# @app.get("/info")
# async def api_info():
#     """
#     Retorna información sobre la API.
#     
#     Returns:
#         dict: Información de la API
#     """
#     return {
#         "name": "Mi Primera API",
#         "version": "0.1.0",
#         "framework": "FastAPI",
#         "python": "3.13+",
#         "docs_url": "/docs",
#         "redoc_url": "/redoc",
#     }


# ============================================
# VERIFICACIÓN
# ============================================
# Una vez descomentado todo, ejecuta:
#   docker compose up --build
#
# Luego visita:
#   http://localhost:8000       → Mensaje de bienvenida
#   http://localhost:8000/health → Health check
#   http://localhost:8000/info   → Información de la API
#   http://localhost:8000/docs   → Documentación Swagger
