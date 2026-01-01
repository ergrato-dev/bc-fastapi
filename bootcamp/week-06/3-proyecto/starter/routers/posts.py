# ============================================
# Router de Posts
# ============================================
"""
Endpoints para gestión de posts.
Delega lógica al PostService.
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas import PostCreate, PostUpdate, PostResponse, PostList
from services import PostService
from exceptions import NotFoundError

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo post.
    
    - **title**: Título del post (5-200 caracteres)
    - **content**: Contenido del post (mínimo 10 caracteres)
    - **author_id**: ID del autor
    - **tag_names**: Lista opcional de tags (se crean si no existen)
    """
    service = PostService(db)
    try:
        return service.create(post)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=PostList)
def list_posts(
    skip: int = Query(0, ge=0, alias="page"),
    limit: int = Query(10, ge=1, le=100, alias="size"),
    author_id: int | None = None,
    tag: str | None = None,
    published: bool | None = None,
    db: Session = Depends(get_db)
):
    """
    Lista posts con filtros opcionales.
    
    - **author_id**: Filtrar por autor
    - **tag**: Filtrar por tag (slug)
    - **published**: Filtrar por estado de publicación
    """
    service = PostService(db)
    posts, total = service.list_all(
        skip=skip,
        limit=limit,
        author_id=author_id,
        tag_slug=tag,
        published_only=published or False
    )
    
    return PostList(
        items=posts,
        total=total,
        page=skip,
        size=limit
    )


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    """Obtiene un post con su autor y tags"""
    service = PostService(db)
    post = service.get_by_id(post_id)
    
    if not post:
        raise HTTPException(status_code=404, detail=f"Post {post_id} not found")
    
    return post


@router.put("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    db: Session = Depends(get_db)
):
    """Actualiza un post existente"""
    service = PostService(db)
    try:
        return service.update(post_id, post_data)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """Elimina un post"""
    service = PostService(db)
    try:
        service.delete(post_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/{post_id}/publish", response_model=PostResponse)
def publish_post(post_id: int, db: Session = Depends(get_db)):
    """Publica un post (cambia published a True)"""
    service = PostService(db)
    try:
        return service.publish(post_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/{post_id}/tags/{tag_name}", response_model=PostResponse)
def add_tag_to_post(
    post_id: int,
    tag_name: str,
    db: Session = Depends(get_db)
):
    """Agrega un tag a un post (lo crea si no existe)"""
    service = PostService(db)
    try:
        return service.add_tag(post_id, tag_name)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{post_id}/tags/{tag_name}", response_model=PostResponse)
def remove_tag_from_post(
    post_id: int,
    tag_name: str,
    db: Session = Depends(get_db)
):
    """Elimina un tag de un post"""
    service = PostService(db)
    try:
        return service.remove_tag(post_id, tag_name)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
