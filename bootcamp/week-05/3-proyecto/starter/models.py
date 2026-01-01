"""
SQLAlchemy Models
=================
Modelos de base de datos para la Library API.

Modelos a implementar:
- Author: Autores de libros
- Book: Libros (relacionado con Author)
"""

from datetime import datetime
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Author(Base):
    """
    Modelo de Autor
    
    Campos:
    - id: Primary key autoincremental
    - name: Nombre del autor (requerido, max 100 caracteres)
    - country: País de origen (opcional, max 50 caracteres)
    - created_at: Fecha de creación (default: ahora)
    """
    __tablename__ = "authors"
    
    # TODO: Implementar campos del modelo
    # Hint: Usar Mapped[T] y mapped_column()
    
    id: Mapped[int] = mapped_column(primary_key=True)
    # TODO: Agregar campo 'name' (str, requerido, String(100))
    # TODO: Agregar campo 'country' (str | None, opcional, String(50))
    # TODO: Agregar campo 'created_at' (datetime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"Author(id={self.id}, name='{self.name}')"


class Book(Base):
    """
    Modelo de Libro
    
    Campos:
    - id: Primary key autoincremental
    - title: Título del libro (requerido, max 200 caracteres)
    - isbn: ISBN único (requerido, unique, max 13 caracteres)
    - year: Año de publicación (opcional)
    - author_id: Foreign key al autor
    - created_at: Fecha de creación (default: ahora)
    """
    __tablename__ = "books"
    
    # TODO: Implementar campos del modelo
    
    id: Mapped[int] = mapped_column(primary_key=True)
    # TODO: Agregar campo 'title' (str, requerido, String(200))
    # TODO: Agregar campo 'isbn' (str, requerido, String(13), unique=True)
    # TODO: Agregar campo 'year' (int | None, opcional)
    # TODO: Agregar campo 'author_id' (int, ForeignKey("authors.id"))
    # TODO: Agregar campo 'created_at' (datetime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}')"
