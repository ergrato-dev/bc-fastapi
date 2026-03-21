# ============================================
# PASO 2 y 3: Modelos con Relación 1:N
# ============================================
print("--- Cargando Modelos ---")

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# ============================================
# PASO 2: Modelo Author
# ============================================
# Un autor puede tener MUCHOS posts
# Descomenta las siguientes líneas:

# class Author(Base):
#     __tablename__ = "authors"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     email: Mapped[str] = mapped_column(String(100), unique=True)
#     
#     # Relación 1:N - Un autor tiene muchos posts
#     # list["Post"] indica que es una LISTA
#     posts: Mapped[list["Post"]] = relationship(back_populates="author")
#     
#     def __repr__(self) -> str:
#         return f"Author(id={self.id}, name='{self.name}')"


# ============================================
# PASO 3: Modelo Post
# ============================================
# Cada post pertenece a UN autor
# Descomenta las siguientes líneas:

# class Post(Base):
#     __tablename__ = "posts"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(200))
#     content: Mapped[str] = mapped_column(Text)
#     
#     # Foreign Key - apunta a la tabla authors
#     # La FK siempre va en el lado "muchos" de la relación
#     author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
#     
#     # Relación inversa - cada post tiene UN autor
#     # "Author" (sin list) indica un solo objeto
#     author: Mapped["Author"] = relationship(back_populates="posts")
#     
#     def __repr__(self) -> str:
#         return f"Post(id={self.id}, title='{self.title}')"


# Placeholder para imports (elimina cuando descomentas los modelos)
Author = None
Post = None
