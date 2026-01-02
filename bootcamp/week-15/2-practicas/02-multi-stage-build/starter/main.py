"""
FastAPI Application - Práctica 02: Multi-Stage Build
"""

from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(
    title="Multi-Stage Build API",
    description="API para practicar multi-stage builds",
    version="1.0.0",
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/info")
async def get_info():
    """Información del contenedor."""
    import pwd
    
    try:
        current_user = pwd.getpwuid(os.getuid()).pw_name
    except Exception:
        current_user = "unknown"
    
    return {
        "app": "Multi-Stage Build API",
        "version": "1.0.0",
        "user": current_user,
        "uid": os.getuid(),
        "is_root": os.getuid() == 0,
        "hostname": os.environ.get("HOSTNAME", "unknown"),
        "venv_path": os.environ.get("PATH", "").split(":")[0] if "/opt/venv" in os.environ.get("PATH", "") else "no venv in path",
    }


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to Multi-Stage Build API",
        "docs": "/docs",
        "health": "/health",
    }
