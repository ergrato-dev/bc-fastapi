"""
Práctica 04: Realtime Dashboard
==============================

Dashboard con métricas en tiempo real usando
WebSocket y Server-Sent Events.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
from datetime import datetime

app = FastAPI(title="Realtime Dashboard")

templates = Jinja2Templates(directory="templates")


# ============================================
# PASO 1: Importar módulos
# ============================================
print("--- Paso 1: Importar módulos ---")

# Importar el collector de métricas y tracker
# Descomenta las siguientes líneas:

# from metrics import metrics_collector, activity_tracker


# ============================================
# PASO 2: Lista de conexiones WebSocket
# ============================================
print("--- Paso 2: Connection tracking ---")

# Lista de conexiones activas para el dashboard
# Descomenta las siguientes líneas:

# active_connections: list[WebSocket] = []
# 
# async def broadcast_to_dashboard(message: dict):
#     """Envía mensaje a todos los dashboards conectados."""
#     for connection in active_connections:
#         try:
#             await connection.send_json(message)
#         except Exception:
#             pass


# ============================================
# PASO 3: Endpoint para servir dashboard
# ============================================
print("--- Paso 3: Servir dashboard ---")

# Endpoint para la página principal
# Descomenta las siguientes líneas:

# @app.get("/", response_class=HTMLResponse)
# async def get_dashboard(request: Request):
#     """Sirve el dashboard."""
#     return templates.TemplateResponse(
#         "dashboard.html",
#         {"request": request}
#     )


# ============================================
# PASO 4: Endpoint SSE para métricas
# ============================================
print("--- Paso 4: SSE métricas ---")

# Endpoint SSE que envía métricas cada segundo
# Descomenta las siguientes líneas:

# @app.get("/metrics/stream")
# async def stream_metrics():
#     """
#     Stream de métricas del sistema.
#     
#     Envía métricas cada segundo via SSE.
#     """
#     async def generate():
#         async for metrics in metrics_collector.stream_metrics(interval=1.0):
#             yield {
#                 "event": "metrics",
#                 "data": metrics
#             }
#     
#     return EventSourceResponse(generate())


# ============================================
# PASO 5: Endpoint HTTP para métricas actuales
# ============================================
print("--- Paso 5: HTTP métricas ---")

# Endpoint para obtener métricas actuales
# Descomenta las siguientes líneas:

# @app.get("/metrics")
# async def get_metrics():
#     """Retorna métricas actuales."""
#     metrics_collector.increment_requests()
#     return metrics_collector.get_all_metrics()


# ============================================
# PASO 6: WebSocket para actividad en vivo
# ============================================
print("--- Paso 6: WebSocket actividad ---")

# WebSocket para recibir actividad en tiempo real
# Descomenta las siguientes líneas:

# @app.websocket("/ws/activity")
# async def websocket_activity(websocket: WebSocket):
#     """
#     WebSocket para actividad en tiempo real.
#     
#     Envía notificaciones de actividad del sistema.
#     """
#     await websocket.accept()
#     active_connections.append(websocket)
#     
#     # Actualizar contador de usuarios
#     metrics_collector.set_connected_users(len(active_connections))
#     
#     # Notificar nueva conexión
#     await activity_tracker.add_activity(
#         "connection",
#         f"Dashboard-{id(websocket)}",
#         "Nuevo dashboard conectado"
#     )
#     
#     # Enviar actividades recientes
#     await websocket.send_json({
#         "type": "history",
#         "activities": activity_tracker.get_recent(20)
#     })
#     
#     # Registrar listener para nuevas actividades
#     async def on_activity(activity):
#         try:
#             await websocket.send_json({
#                 "type": "activity",
#                 "activity": activity
#             })
#         except Exception:
#             pass
#     
#     activity_tracker.add_listener(on_activity)
#     
#     try:
#         while True:
#             # Esperar mensajes del cliente (comandos, etc.)
#             data = await websocket.receive_json()
#             
#             # Procesar comando
#             if data.get("type") == "ping":
#                 await websocket.send_json({"type": "pong"})
#     
#     except WebSocketDisconnect:
#         pass
#     
#     finally:
#         # Cleanup
#         activity_tracker.remove_listener(on_activity)
#         if websocket in active_connections:
#             active_connections.remove(websocket)
#         
#         metrics_collector.set_connected_users(len(active_connections))
#         
#         await activity_tracker.add_activity(
#             "disconnection",
#             f"Dashboard-{id(websocket)}",
#             "Dashboard desconectado"
#         )


# ============================================
# PASO 7: Endpoints de simulación
# ============================================
print("--- Paso 7: Simulación ---")

# Endpoints para simular actividad
# Descomenta las siguientes líneas:

# @app.post("/simulate/user-login")
# async def simulate_login(username: str = "Usuario"):
#     """Simula login de usuario."""
#     await activity_tracker.add_activity(
#         "login",
#         username,
#         "Inicio de sesión"
#     )
#     return {"status": "ok"}
# 
# 
# @app.post("/simulate/error")
# async def simulate_error():
#     """Simula un error."""
#     metrics_collector.increment_errors()
#     await activity_tracker.add_activity(
#         "error",
#         "Sistema",
#         "Error simulado en el servidor"
#     )
#     return {"status": "ok"}
# 
# 
# @app.post("/simulate/request")
# async def simulate_request():
#     """Simula requests."""
#     for _ in range(10):
#         metrics_collector.increment_requests()
#     return {"status": "ok", "added": 10}


# ============================================
# Punto de entrada
# ============================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
