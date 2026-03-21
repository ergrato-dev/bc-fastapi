# ============================================
# Modelo Tag + Tabla Asociativa
# ============================================
from sqlalchemy import String, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# Tabla asociativa para relación N:M entre Post y Tag
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
)


class Tag(Base):
    """
    Modelo de Tag.
    
    Relaciones:
    - N:M con Post (un tag puede estar en muchos posts)
    """
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    slug: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    
    # TODO: Definir relación N:M con Post
    # - Usar secondary=post_tags
    # - Usar back_populates="tags"
    posts: Mapped[list["Post"]] = relationship(
        secondary=post_tags,
        back_populates="tags"
    )
    
    def __repr__(self) -> str:
        return f"Tag(id={self.id}, name='{self.name}')"
