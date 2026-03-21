# ============================================
# PASO 3: PostService
# ============================================
"""
Service para operaciones de Post.
Contiene TODA la lógica de negocio de posts.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload

from models import Author, Post, Tag
from schemas import PostCreate, PostUpdate


# ============================================
# Descomenta la clase PostService completa
# ============================================

# class PostService:
#     """
#     Service para operaciones de Post.
#     
#     Maneja:
#     - CRUD de posts
#     - Gestión de tags (N:M)
#     - Queries optimizadas con relaciones
#     """
#     
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, post_id: int) -> Post | None:
#         """Obtiene post con sus relaciones cargadas"""
#         stmt = (
#             select(Post)
#             .options(
#                 joinedload(Post.author),
#                 selectinload(Post.tags)
#             )
#             .where(Post.id == post_id)
#         )
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     def list_all(
#         self,
#         skip: int = 0,
#         limit: int = 10,
#         author_id: int | None = None,
#         tag_name: str | None = None
#     ) -> list[Post]:
#         """Lista posts con filtros opcionales"""
#         stmt = (
#             select(Post)
#             .options(
#                 joinedload(Post.author),
#                 selectinload(Post.tags)
#             )
#         )
#         
#         if author_id:
#             stmt = stmt.where(Post.author_id == author_id)
#         
#         if tag_name:
#             stmt = stmt.join(Post.tags).where(Tag.name == tag_name)
#         
#         stmt = stmt.offset(skip).limit(limit)
#         
#         return self.db.execute(stmt).scalars().unique().all()
#     
#     def create(self, data: PostCreate) -> Post:
#         """
#         Crea un nuevo post.
#         
#         Raises:
#             ValueError: Si el autor no existe
#         """
#         # Validar que el autor existe
#         author = self.db.get(Author, data.author_id)
#         if not author:
#             raise ValueError(f"Author {data.author_id} not found")
#         
#         # Procesar tags
#         tags = self._get_or_create_tags(data.tag_names or [])
#         
#         # Crear post
#         post = Post(
#             title=data.title,
#             content=data.content,
#             author_id=data.author_id,
#             tags=tags
#         )
#         self.db.add(post)
#         self.db.commit()
#         self.db.refresh(post)
#         
#         # Recargar con relaciones
#         return self.get_by_id(post.id)
#     
#     def update(self, post_id: int, data: PostUpdate) -> Post:
#         """Actualiza un post existente"""
#         post = self.db.get(Post, post_id)
#         if not post:
#             raise ValueError(f"Post {post_id} not found")
#         
#         update_data = data.model_dump(exclude_unset=True)
#         
#         # Actualizar tags si se envían
#         if "tag_names" in update_data:
#             post.tags = self._get_or_create_tags(update_data.pop("tag_names"))
#         
#         # Actualizar otros campos
#         for key, value in update_data.items():
#             setattr(post, key, value)
#         
#         self.db.commit()
#         
#         return self.get_by_id(post_id)
#     
#     def delete(self, post_id: int) -> None:
#         """Elimina un post"""
#         post = self.db.get(Post, post_id)
#         if not post:
#             raise ValueError(f"Post {post_id} not found")
#         
#         self.db.delete(post)
#         self.db.commit()
#     
#     def add_tag(self, post_id: int, tag_name: str) -> Post:
#         """Agrega un tag a un post"""
#         post = self.db.get(Post, post_id)
#         if not post:
#             raise ValueError(f"Post {post_id} not found")
#         
#         tag = self._get_or_create_tag(tag_name)
#         
#         if tag not in post.tags:
#             post.tags.append(tag)
#             self.db.commit()
#         
#         return self.get_by_id(post_id)
#     
#     def remove_tag(self, post_id: int, tag_name: str) -> Post:
#         """Elimina un tag de un post"""
#         post = self.db.get(Post, post_id)
#         if not post:
#             raise ValueError(f"Post {post_id} not found")
#         
#         for tag in post.tags:
#             if tag.name == tag_name:
#                 post.tags.remove(tag)
#                 self.db.commit()
#                 break
#         
#         return self.get_by_id(post_id)
#     
#     # -----------------------------------------
#     # Métodos privados
#     # -----------------------------------------
#     def _get_or_create_tag(self, name: str) -> Tag:
#         """Obtiene un tag o lo crea si no existe"""
#         stmt = select(Tag).where(Tag.name == name)
#         tag = self.db.execute(stmt).scalar_one_or_none()
#         
#         if not tag:
#             tag = Tag(name=name)
#             self.db.add(tag)
#             self.db.flush()
#         
#         return tag
#     
#     def _get_or_create_tags(self, names: list[str]) -> list[Tag]:
#         """Obtiene o crea múltiples tags"""
#         return [self._get_or_create_tag(name) for name in names]


# Placeholder para import (elimina cuando descomentas la clase)
class PostService:
    def __init__(self, db: Session):
        self.db = db
