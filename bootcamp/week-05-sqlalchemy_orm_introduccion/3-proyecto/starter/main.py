"""
Library API
===========
API REST para gestionar una biblioteca con libros y autores.

Ejecutar:
    uv run fastapi dev main.py
    
Documentación:
    http://localhost:8000/docs
"""

from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Author, Book
from schemas import (
    AuthorCreate, AuthorUpdate, AuthorResponse, PaginatedAuthors,
    BookCreate, BookUpdate, BookResponse, PaginatedBooks
)

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library API",
    description="API para gestionar biblioteca con autores y libros",
    version="1.0.0"
)


# ============================================
# AUTHOR ENDPOINTS
# ============================================

@app.post(
    "/authors",
    response_model=AuthorResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["authors"]
)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    """Crea un nuevo autor"""
    # TODO: Implementar
    # 1. Crear instancia de Author con los datos recibidos
    # 2. Agregar a la sesión (db.add)
    # 3. Commit y refresh
    # 4. Retornar el autor creado
    pass


@app.get(
    "/authors",
    response_model=PaginatedAuthors,
    tags=["authors"]
)
def list_authors(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Lista autores con paginación"""
    # TODO: Implementar
    # 1. Contar total de autores
    # 2. Obtener autores con offset y limit
    # 3. Retornar PaginatedAuthors
    pass


@app.get(
    "/authors/{author_id}",
    response_model=AuthorResponse,
    tags=["authors"]
)
def get_author(author_id: int, db: Session = Depends(get_db)):
    """Obtiene un autor por ID"""
    # TODO: Implementar
    # 1. Buscar autor por ID (db.get)
    # 2. Si no existe, lanzar HTTPException 404
    # 3. Retornar el autor
    pass


@app.put(
    "/authors/{author_id}",
    response_model=AuthorResponse,
    tags=["authors"]
)
def update_author(
    author_id: int,
    author_data: AuthorUpdate,
    db: Session = Depends(get_db)
):
    """Actualiza un autor existente"""
    # TODO: Implementar
    # 1. Buscar autor por ID
    # 2. Si no existe, lanzar HTTPException 404
    # 3. Actualizar campos con model_dump(exclude_unset=True)
    # 4. Commit y refresh
    # 5. Retornar autor actualizado
    pass


@app.delete(
    "/authors/{author_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["authors"]
)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """Elimina un autor"""
    # TODO: Implementar
    # 1. Buscar autor por ID
    # 2. Si no existe, lanzar HTTPException 404
    # 3. Eliminar (db.delete) y commit
    # Nota: Considera qué pasa con los libros del autor
    pass


# ============================================
# BOOK ENDPOINTS
# ============================================

@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["books"]
)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Crea un nuevo libro"""
    # TODO: Implementar
    # 1. Verificar que el autor existe
    # 2. Verificar que el ISBN no esté duplicado
    # 3. Crear el libro
    # 4. Retornar el libro creado
    pass


@app.get(
    "/books",
    response_model=PaginatedBooks,
    tags=["books"]
)
def list_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    author_id: int | None = Query(None, description="Filtrar por autor"),
    db: Session = Depends(get_db)
):
    """Lista libros con paginación y filtro opcional por autor"""
    # TODO: Implementar
    # 1. Crear query base
    # 2. Si author_id, agregar filtro
    # 3. Contar total
    # 4. Aplicar paginación
    # 5. Retornar PaginatedBooks
    pass


@app.get(
    "/books/{book_id}",
    response_model=BookResponse,
    tags=["books"]
)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Obtiene un libro por ID"""
    # TODO: Implementar
    pass


@app.put(
    "/books/{book_id}",
    response_model=BookResponse,
    tags=["books"]
)
def update_book(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db)
):
    """Actualiza un libro existente"""
    # TODO: Implementar
    # Nota: Si se actualiza author_id, verificar que el autor existe
    pass


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["books"]
)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Elimina un libro"""
    # TODO: Implementar
    pass


# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health", tags=["health"])
def health_check(db: Session = Depends(get_db)):
    """Verifica estado de la API y base de datos"""
    from sqlalchemy import text
    
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database error: {str(e)}"
        )
