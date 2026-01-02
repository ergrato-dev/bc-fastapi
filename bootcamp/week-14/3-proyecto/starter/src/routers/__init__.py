"""Routers package."""

from src.routers.tasks import router as tasks_router
from src.routers.auth import router as auth_router

__all__ = ["tasks_router", "auth_router"]
