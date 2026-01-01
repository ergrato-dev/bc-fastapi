# ============================================
# TagService
# ============================================
"""
Service para operaciones de Tag.
"""

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Tag, Post
from schemas import TagCreate
from exceptions import NotFoundError, DuplicateError


class TagService:
    """Service para gestión de tags"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, tag_id: int) -> Tag | None:
        """Obtiene tag por ID"""
        return self.db.get(Tag, tag_id)
    
    def get_by_slug(self, slug: str) -> Tag | None:
        """Obtiene tag por slug"""
        stmt = select(Tag).where(Tag.slug == slug)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def list_all(self) -> list[tuple[Tag, int]]:
        """Lista tags con conteo de posts"""
        # TODO: Implementar query que retorne tags con su conteo de posts
        stmt = (
            select(Tag, func.count(Post.id).label("post_count"))
            .outerjoin(Tag.posts)
            .group_by(Tag.id)
            .order_by(func.count(Post.id).desc())
        )
        return self.db.execute(stmt).all()
    
    def create(self, data: TagCreate) -> Tag:
        """
        Crea un nuevo tag.
        
        Raises:
            DuplicateError: Si el tag ya existe
        """
        slug = data.name.lower().replace(" ", "-")
        
        if self.get_by_slug(slug):
            raise DuplicateError(f"Tag '{data.name}' already exists")
        
        tag = Tag(name=data.name, slug=slug)
        self.db.add(tag)
        self.db.commit()
        self.db.refresh(tag)
        
        return tag
    
    def get_posts_by_tag(
        self,
        slug: str,
        skip: int = 0,
        limit: int = 10
    ) -> tuple[list[Post], int]:
        """Obtiene posts de un tag"""
        tag = self.get_by_slug(slug)
        if not tag:
            raise NotFoundError(f"Tag '{slug}' not found")
        
        # Contar total
        total = len(tag.posts)
        
        # Paginar (en memoria para este caso simple)
        posts = tag.posts[skip:skip + limit]
        
        return posts, total
