"""
FastAPI Application - Práctica 01: Dockerfile
Una aplicación simple para aprender Docker.
"""

from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(
    title="Docker Practice API",
    description="API simple para practicar Docker",
    version="1.0.0",
)


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Usado por Docker HEALTHCHECK y orquestadores.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/info")
async def get_info():
    """
    Información del contenedor y entorno.
    """
    return {
        "app": "Docker Practice API",
        "version": "1.0.0",
        "python_version": os.popen("python --version").read().strip(),
        "hostname": os.environ.get("HOSTNAME", "unknown"),
        "environment": {
            "PYTHONDONTWRITEBYTECODE": os.environ.get("PYTHONDONTWRITEBYTECODE", "not set"),
            "PYTHONUNBUFFERED": os.environ.get("PYTHONUNBUFFERED", "not set"),
        },
    }


@app.get("/items")
async def list_items():
    """
    Endpoint de ejemplo que retorna items.
    """
    return {
        "items": [
            {"id": 1, "name": "Item 1", "price": 10.0},
            {"id": 2, "name": "Item 2", "price": 20.0},
            {"id": 3, "name": "Item 3", "price": 30.0},
        ],
        "total": 3,
    }


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """
    Obtener un item por ID.
    """
    items = {
        1: {"id": 1, "name": "Item 1", "price": 10.0},
        2: {"id": 2, "name": "Item 2", "price": 20.0},
        3: {"id": 3, "name": "Item 3", "price": 30.0},
    }
    
    if item_id not in items:
        return {"error": "Item not found"}, 404
    
    return items[item_id]
