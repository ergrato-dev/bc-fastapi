"""
Entry point de la aplicación.

Este archivo simplemente importa y expone la app de FastAPI.
"""

from infrastructure.api.main import app

__all__ = ["app"]


if __name__ == "__main__":
    import uvicorn
    from infrastructure.config import get_settings
    
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
