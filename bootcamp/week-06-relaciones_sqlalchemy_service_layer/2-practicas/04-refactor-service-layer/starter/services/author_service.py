# ============================================
# PASO 2: AuthorService
# ============================================
"""
Service para operaciones de Author.
Contiene TODA la lógica de negocio de autores.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Author
from schemas import AuthorCreate, AuthorUpdate


# ============================================
# Descomenta la clase AuthorService completa
# ============================================

# class AuthorService:
#     """
#     Service para operaciones de Author.
#     
#     Este service:
#     - Contiene lógica de negocio
#     - NO conoce HTTP (no usa HTTPException)
#     - Lanza excepciones Python normales
#     """
#     
#     def __init__(self, db: Session):
#         """Inicializa con sesión de DB"""
#         self.db = db
#     
#     def get_by_id(self, author_id: int) -> Author | None:
#         """Obtiene autor por ID"""
#         return self.db.get(Author, author_id)
#     
#     def get_by_email(self, email: str) -> Author | None:
#         """Obtiene autor por email"""
#         stmt = select(Author).where(Author.email == email)
#         return self.db.execute(stmt).scalar_one_or_none()
#     
#     def list_all(self, skip: int = 0, limit: int = 10) -> list[Author]:
#         """Lista autores con paginación"""
#         stmt = select(Author).offset(skip).limit(limit)
#         return self.db.execute(stmt).scalars().all()
#     
#     def create(self, data: AuthorCreate) -> Author:
#         """
#         Crea un nuevo autor.
#         
#         Args:
#             data: Datos del autor a crear
#             
#         Returns:
#             Author: El autor creado
#             
#         Raises:
#             ValueError: Si el email ya existe
#         """
#         # Validación de negocio
#         if self.get_by_email(data.email):
#             raise ValueError(f"Email {data.email} already registered")
#         
#         # Crear autor
#         author = Author(
#             name=data.name,
#             email=data.email
#         )
#         self.db.add(author)
#         self.db.commit()
#         self.db.refresh(author)
#         
#         return author
#     
#     def update(self, author_id: int, data: AuthorUpdate) -> Author:
#         """
#         Actualiza un autor existente.
#         
#         Raises:
#             ValueError: Si el autor no existe o el email ya está en uso
#         """
#         author = self.get_by_id(author_id)
#         if not author:
#             raise ValueError(f"Author {author_id} not found")
#         
#         # Obtener solo campos enviados
#         update_data = data.model_dump(exclude_unset=True)
#         
#         # Si actualiza email, verificar que no exista
#         if "email" in update_data:
#             existing = self.get_by_email(update_data["email"])
#             if existing and existing.id != author_id:
#                 raise ValueError(f"Email {update_data['email']} already in use")
#         
#         # Aplicar cambios
#         for key, value in update_data.items():
#             setattr(author, key, value)
#         
#         self.db.commit()
#         self.db.refresh(author)
#         
#         return author
#     
#     def delete(self, author_id: int) -> None:
#         """
#         Elimina un autor.
#         
#         Raises:
#             ValueError: Si el autor no existe
#         """
#         author = self.get_by_id(author_id)
#         if not author:
#             raise ValueError(f"Author {author_id} not found")
#         
#         self.db.delete(author)
#         self.db.commit()


# Placeholder para import (elimina cuando descomentas la clase)
class AuthorService:
    def __init__(self, db: Session):
        self.db = db
