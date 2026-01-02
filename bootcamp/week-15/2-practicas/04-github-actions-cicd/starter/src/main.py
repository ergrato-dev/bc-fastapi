# ============================================
# FastAPI Application for CI/CD Practice
# Semana 15 - Práctica 04
# ============================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="CI/CD Practice API",
    description="API para practicar GitHub Actions",
    version="1.0.0",
)


# ============================================
# Schemas
# ============================================

class UserCreate(BaseModel):
    """Schema for creating a user"""

    name: str
    email: EmailStr


class UserResponse(BaseModel):
    """Schema for user response"""

    id: int
    name: str
    email: EmailStr


class HealthResponse(BaseModel):
    """Health check response"""

    status: str
    version: str


# ============================================
# In-memory database (for demo purposes)
# ============================================

fake_db: dict[int, dict] = {}
counter = 0


# ============================================
# Endpoints
# ============================================


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint"""
    return HealthResponse(status="healthy", version="1.0.0")


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint"""
    return {"message": "Welcome to CI/CD Practice API"}


@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate) -> UserResponse:
    """Create a new user"""
    global counter
    counter += 1

    user_data = {"id": counter, "name": user.name, "email": user.email}
    fake_db[counter] = user_data

    return UserResponse(**user_data)


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    """Get a user by ID"""
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(**fake_db[user_id])


@app.get("/users", response_model=list[UserResponse])
async def list_users() -> list[UserResponse]:
    """List all users"""
    return [UserResponse(**user) for user in fake_db.values()]


@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int) -> None:
    """Delete a user"""
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    del fake_db[user_id]
