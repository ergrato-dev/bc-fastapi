"""
Aplicación principal FastAPI.

TODO: Completar los endpoints marcados con TODO
"""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException, status, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse

from .config import settings
from .database import get_db, create_tables
from .models import User, Room
from .schemas import UserCreate, UserResponse, Token, RoomCreate, RoomResponse, RoomWithUsers
from .auth import (
    create_access_token, authenticate_user, get_current_user,
    get_user_by_username, get_user_by_email, get_current_user_ws, decode_token
)
from .manager import manager, create_chat_message, create_system_message, create_user_list_message
from .notifications import notification_service
from . import services


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle de la aplicación."""
    # Startup
    create_tables()
    
    # Crear sala por defecto
    db = next(get_db())
    services.get_or_create_default_room(db)
    db.close()
    
    yield
    # Shutdown


app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

templates = Jinja2Templates(directory="templates")


# ============================================
# HTML Client
# ============================================

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    """Sirve el cliente de chat."""
    return templates.TemplateResponse("chat.html", {"request": request})


# ============================================
# Auth Endpoints
# ============================================

@app.post("/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Registra un nuevo usuario.
    
    TODO: Implementar
    """
    # TODO: Implementar
    # 1. Verificar que username no exista
    # 2. Verificar que email no exista
    # 3. Crear usuario
    # 4. Retornar usuario
    pass


@app.post("/auth/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    """
    Login de usuario.
    
    TODO: Implementar
    """
    # TODO: Implementar
    # 1. Autenticar usuario
    # 2. Si falla, raise HTTPException 401
    # 3. Crear token
    # 4. Retornar token
    pass


@app.get("/auth/me", response_model=UserResponse)
async def get_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """Retorna usuario actual."""
    return current_user


# ============================================
# Room Endpoints
# ============================================

@app.post("/rooms", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
async def create_room(
    room_data: RoomCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Crea una nueva sala.
    
    TODO: Implementar
    """
    # TODO: Implementar
    # 1. Verificar que no exista sala con ese nombre
    # 2. Crear sala
    # 3. Notificar via SSE (opcional)
    # 4. Retornar sala
    pass


@app.get("/rooms", response_model=list[RoomWithUsers])
async def list_rooms(
    db: Session = Depends(get_db)
):
    """
    Lista todas las salas con usuarios online.
    
    TODO: Implementar
    """
    # TODO: Implementar
    # 1. Obtener salas de DB
    # 2. Para cada sala, agregar online_users del manager
    # 3. Retornar lista
    pass


@app.get("/rooms/{room_id}", response_model=RoomWithUsers)
async def get_room(
    room_id: int,
    db: Session = Depends(get_db)
):
    """Obtiene una sala por ID."""
    room = services.get_room(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    return RoomWithUsers(
        id=room.id,
        name=room.name,
        description=room.description,
        created_at=room.created_at,
        created_by_id=room.created_by_id,
        online_users=manager.get_room_usernames(room_id)
    )


@app.get("/rooms/{room_id}/messages")
async def get_room_messages(
    room_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Obtiene historial de mensajes de una sala.
    
    TODO: Implementar
    """
    # TODO: Implementar
    # 1. Verificar que sala existe
    # 2. Obtener mensajes
    # 3. Convertir a dict con username
    # 4. Retornar
    pass


# ============================================
# WebSocket Chat
# ============================================

@app.websocket("/ws/chat/{room_id}")
async def websocket_chat(
    websocket: WebSocket,
    room_id: int,
    token: str = Query(...),
    db: Session = Depends(get_db)
):
    """
    WebSocket para chat en una sala.
    
    TODO: Implementar el endpoint completo
    """
    # TODO: Implementar
    # 1. Validar token
    # 2. Obtener usuario
    # 3. Verificar que sala existe
    # 4. Conectar al manager
    # 5. Enviar mensaje de bienvenida
    # 6. Notificar a la sala que usuario entró
    # 7. Enviar lista de usuarios
    # 8. Loop para recibir mensajes:
    #    - type "message": guardar en DB, broadcast
    #    - type "typing": broadcast typing indicator
    #    - type "ping": responder pong
    # 9. En desconexión: cleanup y notificar
    pass


# ============================================
# SSE Notifications
# ============================================

@app.get("/notifications")
async def sse_notifications(
    token: str = Query(...),
    db: Session = Depends(get_db)
):
    """
    Endpoint SSE para notificaciones.
    
    TODO: Implementar
    """
    # TODO: Implementar
    # 1. Validar token
    # 2. Retornar EventSourceResponse con notification_service.subscribe()
    pass


# ============================================
# Health Check
# ============================================

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "online_users": sum(manager.get_user_count(rid) for rid in manager.rooms),
        "notification_subscribers": notification_service.get_subscribers_count()
    }
