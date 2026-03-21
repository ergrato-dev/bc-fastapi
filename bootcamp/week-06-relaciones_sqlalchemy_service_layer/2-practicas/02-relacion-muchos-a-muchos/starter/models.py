# ============================================
# Práctica 02: Relación Muchos a Muchos
# Modelos con tabla asociativa
# ============================================
print("--- Cargando Modelos ---")

from sqlalchemy import String, Text, ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

# Base para los modelos
Base = declarative_base()


# ============================================
# PASO 1: Tabla Asociativa
# ============================================
# Esta tabla conecta Posts con Tags (N:M)
# No es una clase, solo una Table
# Descomenta las siguientes líneas:

# post_tags = Table(
#     "post_tags",
#     Base.metadata,
#     Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
#     Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
# )

# Placeholder
post_tags = None


# ============================================
# Modelo Author (de la práctica anterior)
# ============================================
class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    
    posts: Mapped[list["Post"]] = relationship(back_populates="author")
    
    def __repr__(self) -> str:
        return f"Author(id={self.id}, name='{self.name}')"


# ============================================
# PASO 2: Modelo Tag
# ============================================
# Descomenta las siguientes líneas:

# class Tag(Base):
#     __tablename__ = "tags"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
#     
#     # Relación N:M con Post
#     # secondary=post_tags indica qué tabla asociativa usar
#     posts: Mapped[list["Post"]] = relationship(
#         secondary=post_tags,
#         back_populates="tags"
#     )
#     
#     def __repr__(self) -> str:
#         return f"Tag(id={self.id}, name='{self.name}')"

# Placeholder
Tag = None


# ============================================
# PASO 3: Modelo Post (actualizado)
# ============================================
# Ahora incluye relación con Tags
# Descomenta las siguientes líneas:

# class Post(Base):
#     __tablename__ = "posts"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(200))
#     content: Mapped[str] = mapped_column(Text)
#     
#     # FK a Author (1:N)
#     author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
#     author: Mapped["Author"] = relationship(back_populates="posts")
#     
#     # Relación N:M con Tag
#     # Ambos lados usan el mismo secondary
#     tags: Mapped[list["Tag"]] = relationship(
#         secondary=post_tags,
#         back_populates="posts"
#     )
#     
#     def __repr__(self) -> str:
#         return f"Post(id={self.id}, title='{self.title}')"

# Placeholder (versión simplificada sin tags)
class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="posts")
    
    def __repr__(self) -> str:
        return f"Post(id={self.id}, title='{self.title}')"
