# ============================================
# PASO 4: Router de Authors (Refactorizado)
# ============================================
"""
Router para endpoints de Author.

Este router:
- SOLO maneja HTTP (rutas, códigos de estado)
- Delega lógica al AuthorService
- Convierte excepciones Python a HTTP
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import AuthorCreate, AuthorUpdate, AuthorResponse
from services.author_service import AuthorService

router = APIRouter(prefix="/authors", tags=["authors"])


# ============================================
# Descomenta los endpoints
# ============================================

# @router.post("/", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
# def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
#     """
#     Crea un nuevo autor.
#     
#     El router:
#     1. Recibe la request HTTP
#     2. Llama al Service
#     3. Convierte excepciones a códigos HTTP
#     4. Retorna la response
#     """
#     service = AuthorService(db)
#     try:
#         return service.create(author)
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail=str(e)
#         )


# @router.get("/", response_model=list[AuthorResponse])
# def list_authors(
#     skip: int = 0,
#     limit: int = 10,
#     db: Session = Depends(get_db)
# ):
#     """Lista autores con paginación"""
#     service = AuthorService(db)
#     return service.list_all(skip=skip, limit=limit)


# @router.get("/{author_id}", response_model=AuthorResponse)
# def get_author(author_id: int, db: Session = Depends(get_db)):
#     """Obtiene un autor por ID"""
#     service = AuthorService(db)
#     author = service.get_by_id(author_id)
#     
#     if not author:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Author {author_id} not found"
#         )
#     
#     return author


# @router.put("/{author_id}", response_model=AuthorResponse)
# def update_author(
#     author_id: int,
#     author_data: AuthorUpdate,
#     db: Session = Depends(get_db)
# ):
#     """Actualiza un autor existente"""
#     service = AuthorService(db)
#     try:
#         return service.update(author_id, author_data)
#     except ValueError as e:
#         error_msg = str(e).lower()
#         if "not found" in error_msg:
#             raise HTTPException(status_code=404, detail=str(e))
#         raise HTTPException(status_code=409, detail=str(e))


# @router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_author(author_id: int, db: Session = Depends(get_db)):
#     """Elimina un autor"""
#     service = AuthorService(db)
#     try:
#         service.delete(author_id)
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e)
#         )
