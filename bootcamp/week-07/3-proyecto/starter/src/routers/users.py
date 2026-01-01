# ============================================
# Users Router
# ============================================
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.user import UserCreate, UserUpdate, UserResponse
from ..unit_of_work import UnitOfWork
from ..services.user import UserService, UserNotFoundError, UserAlreadyExistsError

router = APIRouter(prefix="/users", tags=["users"])


def get_uow(db: Session = Depends(get_db)) -> UnitOfWork:
    """Dependency para obtener UnitOfWork"""
    return UnitOfWork(db)


def get_user_service(uow: UnitOfWork = Depends(get_uow)) -> UserService:
    """Dependency para obtener UserService"""
    return UserService(uow)


# ============================================
# TODO: Implementar endpoints
# ============================================

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Crear nuevo usuario.
    
    TODO: Implementar
    1. Llamar service.create_user(data)
    2. Hacer uow.commit()
    3. Manejar UserAlreadyExistsError -> 400
    """
    pass


@router.get("/", response_model=list[UserResponse])
def list_users(
    skip: int = 0,
    limit: int = 100,
    service: UserService = Depends(get_user_service)
):
    """
    Listar usuarios con paginación.
    
    TODO: Implementar
    """
    pass


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    """
    Obtener usuario por ID.
    
    TODO: Implementar
    Manejar UserNotFoundError -> 404
    """
    pass


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Actualizar usuario.
    
    TODO: Implementar
    """
    pass


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
    uow: UnitOfWork = Depends(get_uow)
):
    """
    Eliminar usuario.
    
    TODO: Implementar
    """
    pass
