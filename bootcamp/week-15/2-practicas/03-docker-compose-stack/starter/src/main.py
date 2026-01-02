"""
FastAPI Application - Práctica 03: Docker Compose Stack
"""

from fastapi import FastAPI
from datetime import datetime
import redis
from src.config import get_settings
from src.database import check_db_connection

settings = get_settings()

app = FastAPI(
    title="Docker Compose Stack API",
    description="API con PostgreSQL y Redis",
    version="1.0.0",
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "debug": settings.debug,
    }


@app.get("/db-check")
async def database_check():
    """Check PostgreSQL connection."""
    return check_db_connection()


@app.get("/redis-check")
async def redis_check():
    """Check Redis connection."""
    try:
        r = redis.from_url(settings.redis_url)
        r.ping()
        info = r.info()
        return {
            "status": "connected",
            "database": "redis",
            "version": info.get("redis_version", "unknown"),
        }
    except Exception as e:
        return {
            "status": "error",
            "database": "redis",
            "error": str(e),
        }


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Docker Compose Stack API",
        "endpoints": {
            "health": "/health",
            "db_check": "/db-check",
            "redis_check": "/redis-check",
        },
    }


@app.post("/cache/{key}")
async def set_cache(key: str, value: str):
    """Set a value in Redis cache."""
    try:
        r = redis.from_url(settings.redis_url)
        r.set(key, value, ex=300)  # 5 min expiry
        return {"status": "ok", "key": key, "value": value}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@app.get("/cache/{key}")
async def get_cache(key: str):
    """Get a value from Redis cache."""
    try:
        r = redis.from_url(settings.redis_url)
        value = r.get(key)
        if value:
            return {"status": "ok", "key": key, "value": value.decode()}
        return {"status": "not_found", "key": key}
    except Exception as e:
        return {"status": "error", "error": str(e)}
