# ============================================
# AuthorService
# ============================================
"""
Service para operaciones de Author.
Contiene TODA la lógica de negocio de autores.
"""

from sqlalchemy import select, func
from sqlalchemy.orm import Session, selectinload

from models import Author, Post
from schemas import AuthorCreate, AuthorUpdate
from exceptions import NotFoundError, DuplicateError


class AuthorService:
    """Service para gestión de autores"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, author_id: int) -> Author | None:
        """Obtiene autor por ID"""
        return self.db.get(Author, author_id)
    
    def get_by_id_with_posts(self, author_id: int) -> Author | None:
        """Obtiene autor con sus posts cargados"""
        # TODO: Implementar query con eager loading de posts
        # Usar selectinload(Author.posts)
        stmt = (
            select(Author)
            .options(selectinload(Author.posts))
            .where(Author.id == author_id)
        )
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_by_email(self, email: str) -> Author | None:
        """Obtiene autor por email"""
        stmt = select(Author).where(Author.email == email)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def list_all(self, skip: int = 0, limit: int = 10) -> list[Author]:
        """Lista autores con paginación"""
        stmt = select(Author).offset(skip).limit(limit)
        return self.db.execute(stmt).scalars().all()
    
    def count(self) -> int:
        """Cuenta total de autores"""
        stmt = select(func.count(Author.id))
        return self.db.execute(stmt).scalar()
    
    def create(self, data: AuthorCreate) -> Author:
        """
        Crea un nuevo autor.
        
        Raises:
            DuplicateError: Si el email ya existe
        """
        # TODO: Implementar
        # 1. Verificar que el email no exista
        # 2. Crear el autor
        # 3. Commit y refresh
        # 4. Retornar el autor
        
        if self.get_by_email(data.email):
            raise DuplicateError(f"Email {data.email} already registered")
        
        author = Author(
            name=data.name,
            email=data.email,
            bio=data.bio
        )
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)
        
        return author
    
    def update(self, author_id: int, data: AuthorUpdate) -> Author:
        """
        Actualiza un autor.
        
        Raises:
            NotFoundError: Si el autor no existe
            DuplicateError: Si el nuevo email ya está en uso
        """
        author = self.get_by_id(author_id)
        if not author:
            raise NotFoundError(f"Author {author_id} not found")
        
        update_data = data.model_dump(exclude_unset=True)
        
        # Verificar email único
        if "email" in update_data:
            existing = self.get_by_email(update_data["email"])
            if existing and existing.id != author_id:
                raise DuplicateError(f"Email {update_data['email']} already in use")
        
        for key, value in update_data.items():
            setattr(author, key, value)
        
        self.db.commit()
        self.db.refresh(author)
        
        return author
    
    def delete(self, author_id: int) -> None:
        """
        Elimina un autor y sus posts.
        
        Raises:
            NotFoundError: Si el autor no existe
        """
        author = self.get_by_id(author_id)
        if not author:
            raise NotFoundError(f"Author {author_id} not found")
        
        self.db.delete(author)
        self.db.commit()
