"""
Práctica 01: WebSocket Básico
============================

En esta práctica crearás tu primer servidor WebSocket con FastAPI.

Conceptos:
- Endpoint WebSocket
- Aceptar conexiones
- Enviar/recibir mensajes
- Manejar desconexiones
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from datetime import datetime
import json

app = FastAPI(title="WebSocket Echo Server")

templates = Jinja2Templates(directory="templates")


# ============================================
# PASO 1: Endpoint HTTP para servir el cliente
# ============================================
print("--- Paso 1: Servir cliente HTML ---")

# Este endpoint sirve la página HTML con el cliente WebSocket
# Descomenta las siguientes líneas:

# @app.get("/", response_class=HTMLResponse)
# async def get_home(request: Request):
#     """Sirve el cliente HTML."""
#     return templates.TemplateResponse(
#         "index.html",
#         {"request": request}
#     )


# ============================================
# PASO 2: WebSocket básico (Echo)
# ============================================
print("--- Paso 2: WebSocket Echo básico ---")

# Este es el endpoint WebSocket más simple: recibe texto y lo devuelve
# Descomenta las siguientes líneas:

# @app.websocket("/ws/echo")
# async def websocket_echo(websocket: WebSocket):
#     """
#     Echo server simple.
#     
#     Recibe mensajes de texto y los devuelve prefijados con "Echo: "
#     """
#     # Aceptar la conexión (handshake)
#     await websocket.accept()
#     
#     # Loop infinito para recibir mensajes
#     while True:
#         # Esperar mensaje del cliente
#         data = await websocket.receive_text()
#         
#         # Enviar respuesta
#         await websocket.send_text(f"Echo: {data}")


# ============================================
# PASO 3: Manejo de conexión/desconexión
# ============================================
print("--- Paso 3: Manejo de conexiones ---")

# Mejoramos el endpoint para manejar desconexiones correctamente
# Descomenta las siguientes líneas:

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     """
#     WebSocket con manejo completo de conexión/desconexión.
#     """
#     client_id = id(websocket)
#     print(f"[{datetime.now().strftime('%H:%M:%S')}] Cliente {client_id} conectando...")
#     
#     # Aceptar conexión
#     await websocket.accept()
#     print(f"[{datetime.now().strftime('%H:%M:%S')}] Cliente {client_id} conectado ✓")
#     
#     # Enviar mensaje de bienvenida
#     await websocket.send_text("¡Bienvenido al servidor WebSocket!")
#     
#     try:
#         while True:
#             # Recibir mensaje
#             data = await websocket.receive_text()
#             print(f"[{datetime.now().strftime('%H:%M:%S')}] Cliente {client_id}: {data}")
#             
#             # Responder
#             response = f"Echo: {data}"
#             await websocket.send_text(response)
#     
#     except WebSocketDisconnect:
#         print(f"[{datetime.now().strftime('%H:%M:%S')}] Cliente {client_id} desconectado")
#     
#     except Exception as e:
#         print(f"[{datetime.now().strftime('%H:%M:%S')}] Error con cliente {client_id}: {e}")


# ============================================
# PASO 4: Mensajes JSON estructurados
# ============================================
print("--- Paso 4: Mensajes JSON ---")

# Ahora usamos JSON para mensajes más estructurados
# Descomenta las siguientes líneas:

# @app.websocket("/ws/json")
# async def websocket_json(websocket: WebSocket):
#     """
#     WebSocket con mensajes JSON estructurados.
#     
#     Formato de mensaje:
#     {
#         "type": "message" | "ping" | "command",
#         "content": "..."
#     }
#     """
#     await websocket.accept()
#     
#     # Mensaje de bienvenida en JSON
#     await websocket.send_json({
#         "type": "welcome",
#         "message": "Conectado al servidor",
#         "timestamp": datetime.now().isoformat()
#     })
#     
#     try:
#         while True:
#             # Recibir JSON del cliente
#             data = await websocket.receive_json()
#             
#             # Procesar según tipo de mensaje
#             message_type = data.get("type", "unknown")
#             
#             match message_type:
#                 case "ping":
#                     # Responder con pong
#                     await websocket.send_json({
#                         "type": "pong",
#                         "timestamp": datetime.now().isoformat()
#                     })
#                 
#                 case "message":
#                     # Echo del mensaje
#                     await websocket.send_json({
#                         "type": "echo",
#                         "content": data.get("content", ""),
#                         "original": data,
#                         "timestamp": datetime.now().isoformat()
#                     })
#                 
#                 case "command":
#                     # Procesar comando
#                     command = data.get("command", "")
#                     result = process_command(command)
#                     await websocket.send_json({
#                         "type": "command_result",
#                         "command": command,
#                         "result": result,
#                         "timestamp": datetime.now().isoformat()
#                     })
#                 
#                 case _:
#                     # Tipo desconocido
#                     await websocket.send_json({
#                         "type": "error",
#                         "message": f"Tipo de mensaje desconocido: {message_type}",
#                         "timestamp": datetime.now().isoformat()
#                     })
#     
#     except WebSocketDisconnect:
#         print("Cliente JSON desconectado")
#     
#     except json.JSONDecodeError:
#         await websocket.send_json({
#             "type": "error",
#             "message": "JSON inválido"
#         })


# ============================================
# PASO 5: Función auxiliar para comandos
# ============================================
print("--- Paso 5: Procesador de comandos ---")

# Función para procesar comandos del cliente
# Descomenta las siguientes líneas:

# def process_command(command: str) -> str:
#     """Procesa comandos del cliente."""
#     match command.lower():
#         case "time":
#             return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         case "help":
#             return "Comandos disponibles: time, help, info"
#         case "info":
#             return "WebSocket Echo Server v1.0"
#         case _:
#             return f"Comando desconocido: {command}"


# ============================================
# Punto de entrada
# ============================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
