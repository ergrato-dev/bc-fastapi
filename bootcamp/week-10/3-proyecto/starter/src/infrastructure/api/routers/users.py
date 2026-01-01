"""
Users Router - Endpoints de usuarios.

TODO: Implementar todos los endpoints.
"""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status

from application.services.user_service import UserService
from application.commands.user_commands import CreateUserCommand
from infrastructure.api.schemas.user_schemas import (
    UserCreateRequest,
    UserResponse,
    UserListResponse,
)


router = APIRouter(prefix="/api/v1/users", tags=["Users"])


def get_user_service() -> UserService:
    """Placeholder - se configura en main.py."""
    raise NotImplementedError("Configure in main.py")


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    request: UserCreateRequest,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Crear nuevo usuario. TODO: Implementar."""
    pass


@router.get("/", response_model=UserListResponse)
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    service: UserService = Depends(get_user_service),
) -> UserListResponse:
    """Listar usuarios. TODO: Implementar."""
    pass


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Obtener usuario. TODO: Implementar."""
    pass
