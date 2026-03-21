# ============================================
# PostService
# ============================================
"""
Service para operaciones de Post.
Maneja relaciones con Author y Tags.
"""

from sqlalchemy import select, func
from sqlalchemy.orm import Session, joinedload, selectinload

from models import Author, Post, Tag
from schemas import PostCreate, PostUpdate
from exceptions import NotFoundError, ValidationError


class PostService:
    """Service para gestión de posts"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, post_id: int) -> Post | None:
        """Obtiene post con sus relaciones"""
        # TODO: Implementar query optimizada
        # Cargar author con joinedload y tags con selectinload
        stmt = (
            select(Post)
            .options(
                joinedload(Post.author),
                selectinload(Post.tags)
            )
            .where(Post.id == post_id)
        )
        return self.db.execute(stmt).scalar_one_or_none()
    
    def list_all(
        self,
        skip: int = 0,
        limit: int = 10,
        author_id: int | None = None,
        tag_slug: str | None = None,
        published_only: bool = False
    ) -> tuple[list[Post], int]:
        """
        Lista posts con filtros.
        
        Returns:
            tuple: (lista de posts, total)
        """
        # TODO: Implementar query con filtros
        # 1. Base query con eager loading
        # 2. Aplicar filtros si existen
        # 3. Paginación
        # 4. Contar total
        
        stmt = (
            select(Post)
            .options(
                joinedload(Post.author),
                selectinload(Post.tags)
            )
        )
        
        # Filtros
        if author_id:
            stmt = stmt.where(Post.author_id == author_id)
        
        if tag_slug:
            stmt = stmt.join(Post.tags).where(Tag.slug == tag_slug)
        
        if published_only:
            stmt = stmt.where(Post.published == True)
        
        # Total (antes de paginar)
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = self.db.execute(count_stmt).scalar()
        
        # Paginación
        stmt = stmt.offset(skip).limit(limit)
        posts = self.db.execute(stmt).scalars().unique().all()
        
        return posts, total
    
    def create(self, data: PostCreate) -> Post:
        """
        Crea un nuevo post.
        
        Raises:
            NotFoundError: Si el autor no existe
        """
        # TODO: Implementar
        # 1. Verificar que el autor existe
        # 2. Procesar tags (get or create)
        # 3. Crear post con relaciones
        # 4. Retornar post con relaciones cargadas
        
        # Verificar autor
        author = self.db.get(Author, data.author_id)
        if not author:
            raise NotFoundError(f"Author {data.author_id} not found")
        
        # Procesar tags
        tags = self._get_or_create_tags(data.tag_names or [])
        
        # Crear post
        post = Post(
            title=data.title,
            content=data.content,
            author_id=data.author_id,
            tags=tags
        )
        self.db.add(post)
        self.db.commit()
        
        # Retornar con relaciones
        return self.get_by_id(post.id)
    
    def update(self, post_id: int, data: PostUpdate) -> Post:
        """Actualiza un post"""
        post = self.db.get(Post, post_id)
        if not post:
            raise NotFoundError(f"Post {post_id} not found")
        
        update_data = data.model_dump(exclude_unset=True)
        
        # Actualizar tags si se envían
        if "tag_names" in update_data:
            post.tags = self._get_or_create_tags(update_data.pop("tag_names"))
        
        # Actualizar otros campos
        for key, value in update_data.items():
            setattr(post, key, value)
        
        self.db.commit()
        
        return self.get_by_id(post_id)
    
    def delete(self, post_id: int) -> None:
        """Elimina un post"""
        post = self.db.get(Post, post_id)
        if not post:
            raise NotFoundError(f"Post {post_id} not found")
        
        self.db.delete(post)
        self.db.commit()
    
    def publish(self, post_id: int) -> Post:
        """Publica un post"""
        post = self.db.get(Post, post_id)
        if not post:
            raise NotFoundError(f"Post {post_id} not found")
        
        post.published = True
        self.db.commit()
        
        return self.get_by_id(post_id)
    
    def add_tag(self, post_id: int, tag_name: str) -> Post:
        """Agrega un tag a un post"""
        post = self.db.get(Post, post_id)
        if not post:
            raise NotFoundError(f"Post {post_id} not found")
        
        tag = self._get_or_create_tag(tag_name)
        
        if tag not in post.tags:
            post.tags.append(tag)
            self.db.commit()
        
        return self.get_by_id(post_id)
    
    def remove_tag(self, post_id: int, tag_name: str) -> Post:
        """Elimina un tag de un post"""
        post = self.db.get(Post, post_id)
        if not post:
            raise NotFoundError(f"Post {post_id} not found")
        
        for tag in post.tags:
            if tag.name == tag_name or tag.slug == tag_name:
                post.tags.remove(tag)
                self.db.commit()
                break
        
        return self.get_by_id(post_id)
    
    # -----------------------------------------
    # Métodos privados
    # -----------------------------------------
    def _get_or_create_tag(self, name: str) -> Tag:
        """Obtiene o crea un tag"""
        slug = name.lower().replace(" ", "-")
        
        stmt = select(Tag).where(Tag.slug == slug)
        tag = self.db.execute(stmt).scalar_one_or_none()
        
        if not tag:
            tag = Tag(name=name, slug=slug)
            self.db.add(tag)
            self.db.flush()
        
        return tag
    
    def _get_or_create_tags(self, names: list[str]) -> list[Tag]:
        """Obtiene o crea múltiples tags"""
        return [self._get_or_create_tag(name) for name in names]
