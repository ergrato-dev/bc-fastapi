# ============================================
# Práctica 04: Código ANTES del Refactor
# Este archivo muestra endpoints "gordos"
# ============================================
"""
⚠️ ESTE ARCHIVO ES SOLO PARA REFERENCIA
Muestra cómo NO estructurar el código.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from models import Base, Author, Post, Tag
from schemas import AuthorCreate, PostCreate

# Setup
engine = create_engine("sqlite:///./blog_before.db")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API - ANTES del refactor")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================
# ❌ ENDPOINT "GORDO" - Todo mezclado
# ============================================
@app.post("/authors")
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    """
    Endpoint con toda la lógica mezclada:
    - Validación de negocio
    - Acceso a DB
    - Lógica HTTP
    """
    # Validación de negocio (debería estar en Service)
    existing = db.execute(
        select(Author).where(Author.email == author.email)
    ).scalar_one_or_none()
    
    if existing:
        raise HTTPException(
            status_code=409,
            detail=f"Email {author.email} already registered"
        )
    
    # Creación (debería estar en Service)
    db_author = Author(name=author.name, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    
    return db_author


@app.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Endpoint MUY gordo - todo está aquí:
    - Validación del autor
    - Procesamiento de tags
    - Creación del post
    """
    # Validar que el autor existe (debería estar en Service)
    author = db.get(Author, post.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    # Procesar tags (debería estar en Service)
    tags = []
    for tag_name in (post.tag_names or []):
        tag = db.execute(
            select(Tag).where(Tag.name == tag_name)
        ).scalar_one_or_none()
        
        if not tag:
            tag = Tag(name=tag_name)
            db.add(tag)
        tags.append(tag)
    
    # Crear post (debería estar en Service)
    db_post = Post(
        title=post.title,
        content=post.content,
        author_id=post.author_id,
        tags=tags
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    
    return db_post


@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    """Obtener post - mezclado con lógica de DB"""
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.get("/authors")
def list_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Listar autores - query directa en endpoint"""
    stmt = select(Author).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()


# ============================================
# PROBLEMAS DE ESTE ENFOQUE:
# ============================================
# 1. No se puede testear la lógica sin HTTP
# 2. No se puede reutilizar (ej: crear post desde CLI)
# 3. Difícil de mantener cuando crece
# 4. Difícil de entender qué hace cada parte
# ============================================
