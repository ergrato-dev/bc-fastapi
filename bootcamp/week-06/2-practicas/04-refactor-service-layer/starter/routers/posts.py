# ============================================
# PASO 5: Router de Posts (Refactorizado)
# ============================================
"""
Router para endpoints de Post.
Delega toda la lógica al PostService.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import PostCreate, PostUpdate, PostResponse
from services.post_service import PostService

router = APIRouter(prefix="/posts", tags=["posts"])


# ============================================
# Descomenta los endpoints
# ============================================

# @router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
# def create_post(post: PostCreate, db: Session = Depends(get_db)):
#     """
#     Crea un nuevo post.
#     
#     Observa cómo el endpoint es simple:
#     - Instancia el service
#     - Llama al método
#     - Maneja excepciones
#     """
#     service = PostService(db)
#     try:
#         return service.create(post)
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e)
#         )


# @router.get("/", response_model=list[PostResponse])
# def list_posts(
#     skip: int = 0,
#     limit: int = 10,
#     author_id: int | None = None,
#     tag: str | None = None,
#     db: Session = Depends(get_db)
# ):
#     """Lista posts con filtros opcionales"""
#     service = PostService(db)
#     return service.list_all(
#         skip=skip,
#         limit=limit,
#         author_id=author_id,
#         tag_name=tag
#     )


# @router.get("/{post_id}", response_model=PostResponse)
# def get_post(post_id: int, db: Session = Depends(get_db)):
#     """Obtiene un post con sus relaciones"""
#     service = PostService(db)
#     post = service.get_by_id(post_id)
#     
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post {post_id} not found"
#         )
#     
#     return post


# @router.put("/{post_id}", response_model=PostResponse)
# def update_post(
#     post_id: int,
#     post_data: PostUpdate,
#     db: Session = Depends(get_db)
# ):
#     """Actualiza un post existente"""
#     service = PostService(db)
#     try:
#         return service.update(post_id, post_data)
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e)
#         )


# @router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(post_id: int, db: Session = Depends(get_db)):
#     """Elimina un post"""
#     service = PostService(db)
#     try:
#         service.delete(post_id)
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e)
#         )


# @router.post("/{post_id}/tags/{tag_name}", response_model=PostResponse)
# def add_tag_to_post(
#     post_id: int,
#     tag_name: str,
#     db: Session = Depends(get_db)
# ):
#     """Agrega un tag a un post"""
#     service = PostService(db)
#     try:
#         return service.add_tag(post_id, tag_name)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))


# @router.delete("/{post_id}/tags/{tag_name}", response_model=PostResponse)
# def remove_tag_from_post(
#     post_id: int,
#     tag_name: str,
#     db: Session = Depends(get_db)
# ):
#     """Elimina un tag de un post"""
#     service = PostService(db)
#     try:
#         return service.remove_tag(post_id, tag_name)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
