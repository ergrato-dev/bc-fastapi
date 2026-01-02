# router.py
"""
Router de usuarios con endpoints protegidos.

Este módulo demuestra cómo proteger endpoints usando
dependencias de autenticación y autorización.
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from src.auth.dependencies import (
    get_current_user,
    get_current_active_user,
    require_role,
)


router = APIRouter(tags=["Users"])


# ============================================
# PASO 4: Endpoint protegido básico
# ============================================
print("--- Paso 4: Endpoint /users/me ---")

@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[dict, Depends(get_current_active_user)]
):
    """
    Retorna los datos del usuario autenticado.
    
    Este endpoint requiere un token válido.
    Usa get_current_active_user para asegurar que el usuario esté activo.
    
    El usuario se obtiene automáticamente del token JWT.
    """
    # Filtrar datos sensibles antes de retornar
    return {
        "id": current_user["id"],
        "email": current_user["email"],
        "full_name": current_user["full_name"],
        "role": current_user["role"],
        "is_active": current_user["is_active"],
    }


# ============================================
# PASO 5: Endpoint con rol específico
# ============================================
print("--- Paso 5: Endpoint /admin/dashboard ---")

# Descomenta las siguientes líneas:

# @router.get("/admin/dashboard")
# async def admin_dashboard(
#     admin: Annotated[dict, Depends(require_role("admin"))]
# ):
#     """
#     Panel de administración - Solo para admins.
#     
#     Este endpoint usa require_role("admin") para verificar
#     que el usuario tenga el rol de administrador.
#     """
#     return {
#         "message": f"Welcome, {admin['full_name']}!",
#         "role": admin["role"],
#         "admin_features": [
#             "View all users",
#             "Manage permissions",
#             "View system logs",
#         ],
#     }


# ============================================
# PASO 6: Endpoint para cualquier usuario autenticado
# ============================================
print("--- Paso 6: Endpoint /users/profile ---")

# @router.get("/users/profile")
# async def get_user_profile(
#     user: Annotated[dict, Depends(get_current_user)]
# ):
#     """
#     Perfil del usuario (incluso si está inactivo).
#     
#     A diferencia de /users/me, este endpoint usa get_current_user
#     directamente, permitiendo acceso incluso a usuarios inactivos.
#     """
#     return {
#         "email": user["email"],
#         "full_name": user["full_name"],
#         "status": "active" if user["is_active"] else "inactive",
#     }
