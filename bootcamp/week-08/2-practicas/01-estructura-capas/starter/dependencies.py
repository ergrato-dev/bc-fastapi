# ============================================
# INYECCIÓN DE DEPENDENCIAS
# ============================================
print("--- Dependencies: Inyección de dependencias ---")

# Este módulo centraliza la creación de dependencias.
# FastAPI inyecta estas dependencias en los endpoints.

# Descomenta las siguientes líneas:

# from fastapi import Depends
# from sqlalchemy.orm import Session

# from database import get_db
# from repositories.category import CategoryRepository
# from services.category import CategoryService


# def get_category_repository(
#     db: Session = Depends(get_db)
# ) -> CategoryRepository:
#     """
#     Crea CategoryRepository con sesión de DB.
#     
#     Args:
#         db: Sesión inyectada por FastAPI
#         
#     Returns:
#         CategoryRepository configurado
#     """
#     return CategoryRepository(db)


# def get_category_service(
#     repo: CategoryRepository = Depends(get_category_repository)
# ) -> CategoryService:
#     """
#     Crea CategoryService con su repository.
#     
#     Args:
#         repo: Repository inyectado por FastAPI
#         
#     Returns:
#         CategoryService configurado
#     """
#     return CategoryService(repo)
