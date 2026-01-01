# ============================================
# Router de Authors
# ============================================
"""
Endpoints para gestión de autores.
Delega lógica al AuthorService.
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas import AuthorCreate, AuthorUpdate, AuthorResponse, AuthorWithPosts
from services import AuthorService
from exceptions import NotFoundError, DuplicateError

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.post("/", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo autor.
    
    - **name**: Nombre del autor (2-100 caracteres)
    - **email**: Email único del autor
    - **bio**: Biografía opcional
    """
    service = AuthorService(db)
    try:
        return service.create(author)
    except DuplicateError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )


@router.get("/", response_model=list[AuthorResponse])
def list_authors(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Lista autores con paginación"""
    service = AuthorService(db)
    return service.list_all(skip=skip, limit=limit)


@router.get("/{author_id}", response_model=AuthorWithPosts)
def get_author(author_id: int, db: Session = Depends(get_db)):
    """Obtiene un autor con sus posts"""
    service = AuthorService(db)
    author = service.get_by_id_with_posts(author_id)
    
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author {author_id} not found"
        )
    
    return author


@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(
    author_id: int,
    author_data: AuthorUpdate,
    db: Session = Depends(get_db)
):
    """Actualiza un autor existente"""
    service = AuthorService(db)
    try:
        return service.update(author_id, author_data)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except DuplicateError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """Elimina un autor y todos sus posts"""
    service = AuthorService(db)
    try:
        service.delete(author_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
