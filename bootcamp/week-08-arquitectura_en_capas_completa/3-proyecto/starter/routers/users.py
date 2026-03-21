# ============================================
# USERS ROUTER
# ============================================

from fastapi import APIRouter, Depends, status

from schemas.user import UserCreate, UserResponse
from services.user import UserService
from dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponse])
def list_users(service: UserService = Depends(get_user_service)):
    """Lista todos los usuarios."""
    return service.get_all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    """Obtiene usuario por ID."""
    return service.get_by_id(user_id)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    """Crea nuevo usuario."""
    return service.create(data)
