# Routers package
from routers.authors import router as authors_router
from routers.posts import router as posts_router
from routers.tags import router as tags_router

__all__ = ["authors_router", "posts_router", "tags_router"]
