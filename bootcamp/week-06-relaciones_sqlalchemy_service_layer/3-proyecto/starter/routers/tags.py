# ============================================
# Router de Tags
# ============================================
"""
Endpoints para gestión de tags.
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas import TagCreate, TagResponse, TagWithCount, PostResponse
from services import TagService
from exceptions import NotFoundError, DuplicateError

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo tag.
    
    - **name**: Nombre del tag (solo letras, números y guiones)
    """
    service = TagService(db)
    try:
        return service.create(tag)
    except DuplicateError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/", response_model=list[TagWithCount])
def list_tags(db: Session = Depends(get_db)):
    """Lista todos los tags con conteo de posts"""
    service = TagService(db)
    results = service.list_all()
    
    return [
        TagWithCount(
            id=tag.id,
            name=tag.name,
            slug=tag.slug,
            post_count=count
        )
        for tag, count in results
    ]


@router.get("/{slug}", response_model=TagResponse)
def get_tag(slug: str, db: Session = Depends(get_db)):
    """Obtiene un tag por slug"""
    service = TagService(db)
    tag = service.get_by_slug(slug)
    
    if not tag:
        raise HTTPException(status_code=404, detail=f"Tag '{slug}' not found")
    
    return tag


@router.get("/{slug}/posts", response_model=list[PostResponse])
def get_posts_by_tag(
    slug: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Lista posts que tienen un tag específico"""
    service = TagService(db)
    try:
        posts, _ = service.get_posts_by_tag(slug, skip=skip, limit=limit)
        return posts
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
