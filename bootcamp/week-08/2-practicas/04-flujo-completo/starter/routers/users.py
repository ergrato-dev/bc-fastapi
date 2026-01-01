# ============================================
# ROUTER USERS (auxiliar)
# ============================================

# Descomenta para crear usuarios de prueba:

# from fastapi import APIRouter, Depends, status
# from sqlalchemy.orm import Session

# from database import get_db
# from models.user import User
# from schemas.user import UserCreate, UserResponse
# from repositories.user import UserRepository

# router = APIRouter(prefix="/users", tags=["users"])


# @router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# def create_user(data: UserCreate, db: Session = Depends(get_db)):
#     repo = UserRepository(db)
#     user = User(name=data.name, email=data.email)
#     return repo.add(user)
