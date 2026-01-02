# router.py
"""
Router de usuarios con endpoints protegidos.

Endpoints:
- GET /users/me - Perfil del usuario autenticado
- PATCH /users/me - Actualizar perfil
- GET /admin/users - Listar usuarios (solo admin)
- PATCH /admin/users/{user_id}/role - Cambiar rol (solo admin)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.auth.schemas import UserResponse, UserUpdate, RoleUpdate
from src.auth.dependencies import get_current_active_user, require_role
from src.users.models import User
from src.users.crud import get_users, get_user_by_id, update_user_role, update_user_name


router = APIRouter(tags=["Users"])


# ============================================
# ENDPOINTS DE USUARIO AUTENTICADO
# ============================================

@router.get("/users/me", response_model=UserResponse)
async def read_current_user(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> UserResponse:
    """
    Retorna los datos del usuario autenticado.
    
    Requiere token de acceso válido.
    """
    # TODO: Implementar
    # Simplemente retornar current_user (Pydantic lo serializa automáticamente)
    pass


@router.patch("/users/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(get_db)],
) -> UserResponse:
    """
    Actualiza el perfil del usuario autenticado.
    
    Solo permite actualizar full_name.
    """
    # TODO: Implementar
    # 1. Si user_update.full_name está presente, actualizar usando update_user_name()
    # 2. Retornar current_user actualizado
    pass


# ============================================
# ENDPOINTS DE ADMINISTRACIÓN
# ============================================

@router.get("/admin/users", response_model=list[UserResponse])
async def list_users(
    db: Annotated[Session, Depends(get_db)],
    admin: Annotated[User, Depends(require_role("admin"))],
    skip: int = 0,
    limit: int = 100,
) -> list[UserResponse]:
    """
    Lista todos los usuarios.
    
    Solo accesible para administradores.
    """
    # TODO: Implementar
    # Usar get_users(db, skip, limit)
    pass


@router.patch("/admin/users/{user_id}/role", response_model=UserResponse)
async def change_user_role(
    user_id: int,
    role_update: RoleUpdate,
    db: Annotated[Session, Depends(get_db)],
    admin: Annotated[User, Depends(require_role("admin"))],
) -> UserResponse:
    """
    Cambia el rol de un usuario.
    
    Solo accesible para administradores.
    """
    # TODO: Implementar
    # 1. Buscar usuario por ID usando get_user_by_id()
    # 2. Si no existe, lanzar HTTPException 404 con detail="User not found"
    # 3. Actualizar rol usando update_user_role()
    # 4. Retornar usuario actualizado
    pass
