# ============================================
# Modelo Post
# ============================================
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.tag import post_tags


class Post(Base):
    """
    Modelo de Post.
    
    Relaciones:
    - N:1 con Author (cada post pertenece a un autor)
    - N:M con Tag (un post puede tener muchos tags)
    """
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    published: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(
        default=None,
        onupdate=datetime.utcnow
    )
    
    # TODO: Definir FK y relación N:1 con Author
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="posts")
    
    # TODO: Definir relación N:M con Tag
    # - Usar secondary=post_tags
    # - Usar back_populates="posts"
    tags: Mapped[list["Tag"]] = relationship(
        secondary=post_tags,
        back_populates="posts"
    )
    
    def __repr__(self) -> str:
        return f"Post(id={self.id}, title='{self.title}')"
