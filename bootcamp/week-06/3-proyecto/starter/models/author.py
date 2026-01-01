# ============================================
# Modelo Author
# ============================================
from datetime import datetime
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Author(Base):
    """
    Modelo de Autor.
    
    Relaciones:
    - 1:N con Post (un autor tiene muchos posts)
    """
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    # TODO: Definir relación 1:N con Post
    # - Un autor tiene muchos posts
    # - Usar back_populates="author"
    # - Agregar cascade="all, delete-orphan"
    posts: Mapped[list["Post"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"Author(id={self.id}, name='{self.name}')"
