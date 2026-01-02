# main.py
"""
Aplicación FastAPI con endpoints protegidos.

Demuestra autenticación y autorización basada en roles.
"""

from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.users.router import router as users_router

app = FastAPI(
    title="Protected Endpoints Demo",
    description="API con endpoints protegidos por JWT y roles",
    version="1.0.0",
)

# Routers
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
async def root():
    """Endpoint público."""
    return {
        "message": "Welcome! Use /docs to explore the API",
        "public_endpoints": ["/", "/auth/token"],
        "protected_endpoints": ["/users/me", "/admin/dashboard"],
    }
