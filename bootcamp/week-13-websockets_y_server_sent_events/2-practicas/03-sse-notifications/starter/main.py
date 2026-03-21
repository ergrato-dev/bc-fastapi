"""
Práctica 03: SSE Notifications
==============================

Sistema de notificaciones en tiempo real usando
Server-Sent Events (SSE).
"""

from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse

app = FastAPI(title="SSE Notifications")

templates = Jinja2Templates(directory="templates")


# ============================================
# PASO 1: Importar el servicio
# ============================================
print("--- Paso 1: Importar servicio ---")

# Importar el servicio de notificaciones
# Descomenta la siguiente línea:

# from notifications import notification_service


# ============================================
# PASO 2: Endpoint para servir el cliente
# ============================================
print("--- Paso 2: Servir cliente HTML ---")

# Endpoint para la página principal
# Descomenta las siguientes líneas:

# @app.get("/", response_class=HTMLResponse)
# async def get_home(request: Request):
#     """Sirve el cliente de notificaciones."""
#     return templates.TemplateResponse(
#         "index.html",
#         {"request": request}
#     )


# ============================================
# PASO 3: Endpoint SSE para suscripción
# ============================================
print("--- Paso 3: Endpoint SSE ---")

# Endpoint SSE para recibir notificaciones
# Descomenta las siguientes líneas:

# @app.get("/notifications/{user_id}")
# async def subscribe_notifications(user_id: str):
#     """
#     Endpoint SSE para suscribirse a notificaciones.
#     
#     El cliente se conecta y recibe notificaciones
#     en tiempo real.
#     """
#     return EventSourceResponse(
#         notification_service.subscribe(user_id)
#     )


# ============================================
# PASO 4: Endpoints para enviar notificaciones
# ============================================
print("--- Paso 4: Enviar notificaciones ---")

# Endpoints HTTP para enviar notificaciones
# Descomenta las siguientes líneas:

# @app.post("/notify/{user_id}")
# async def send_notification(
#     user_id: str,
#     message: str = Query(..., description="Mensaje de la notificación"),
#     type: str = Query("info", description="Tipo: info, success, warning, error")
# ):
#     """Envía notificación a un usuario específico."""
#     success = await notification_service.notify(
#         user_id=user_id,
#         message=message,
#         notification_type=type
#     )
#     
#     return {
#         "success": success,
#         "user_id": user_id,
#         "message": message if success else "Usuario no está suscrito"
#     }
# 
# 
# @app.post("/broadcast")
# async def broadcast_notification(
#     message: str = Query(..., description="Mensaje a enviar"),
#     type: str = Query("info", description="Tipo: info, success, warning, error")
# ):
#     """Envía notificación a todos los suscriptores."""
#     count = await notification_service.broadcast(
#         message=message,
#         notification_type=type
#     )
#     
#     return {
#         "success": True,
#         "notified_count": count,
#         "message": message
#     }


# ============================================
# PASO 5: Endpoint de estadísticas
# ============================================
print("--- Paso 5: Estadísticas ---")

# Endpoint para ver suscriptores activos
# Descomenta las siguientes líneas:

# @app.get("/stats")
# async def get_stats():
#     """Retorna estadísticas del servicio."""
#     return {
#         "subscribers_count": notification_service.get_subscribers_count(),
#         "subscribers": notification_service.get_subscribers()
#     }


# ============================================
# PASO 6: Simulador de notificaciones
# ============================================
print("--- Paso 6: Simulador ---")

# Background task para simular notificaciones
# Descomenta las siguientes líneas:

# import asyncio
# from contextlib import asynccontextmanager
# 
# async def notification_simulator():
#     """Simula notificaciones periódicas."""
#     messages = [
#         ("info", "Nueva actualización disponible"),
#         ("success", "Tarea completada exitosamente"),
#         ("warning", "Tu sesión expirará pronto"),
#         ("info", "Tienes 3 mensajes sin leer"),
#     ]
#     
#     index = 0
#     while True:
#         await asyncio.sleep(15)  # Cada 15 segundos
#         
#         if notification_service.get_subscribers_count() > 0:
#             msg_type, message = messages[index % len(messages)]
#             await notification_service.broadcast(message, msg_type)
#             index += 1
# 
# 
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """Lifecycle para iniciar el simulador."""
#     # Startup
#     task = asyncio.create_task(notification_simulator())
#     yield
#     # Shutdown
#     task.cancel()
#     try:
#         await task
#     except asyncio.CancelledError:
#         pass
# 
# 
# # Para usar el simulador, reemplaza la línea de FastAPI por:
# # app = FastAPI(title="SSE Notifications", lifespan=lifespan)


# ============================================
# Punto de entrada
# ============================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
