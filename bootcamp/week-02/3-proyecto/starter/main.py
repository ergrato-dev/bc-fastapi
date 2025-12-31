"""
Proyecto Semana 02: API de Gestión de Contactos
===============================================

Aplicación FastAPI principal.
Los endpoints ya están definidos, debes completar schemas.py

Ejecutar:
    docker compose up --build
    
Documentación: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, status, Query
from datetime import datetime

# TODO: Importar los schemas que crearás
from schemas import (
    ContactCreate,
    ContactUpdate,
    ContactResponse,
    ContactList,
)
from database import contacts_db, get_next_id, find_by_email

app = FastAPI(
    title="API de Gestión de Contactos",
    description="Proyecto Semana 02 - Pydantic v2",
    version="1.0.0",
)


# ============================================
# ENDPOINTS
# ============================================

@app.post(
    "/contacts",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Contacts"],
)
async def create_contact(contact: ContactCreate) -> ContactResponse:
    """
    Crear un nuevo contacto.
    
    - Valida que el email no exista
    - Normaliza teléfono, nombres y tags
    """
    # Verificar email único
    if find_by_email(contact.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Contact with email {contact.email} already exists"
        )
    
    # Crear contacto
    contact_id = get_next_id()
    new_contact = {
        "id": contact_id,
        **contact.model_dump(),
        "created_at": datetime.now(),
        "updated_at": None,
    }
    contacts_db[contact_id] = new_contact
    
    return new_contact


@app.get(
    "/contacts",
    response_model=ContactList,
    tags=["Contacts"],
)
async def list_contacts(
    page: int = Query(ge=1, default=1),
    per_page: int = Query(ge=1, le=100, default=10),
    favorite_only: bool = False,
) -> ContactList:
    """
    Listar contactos con paginación.
    
    - Soporta filtro por favoritos
    """
    # Filtrar
    contacts = list(contacts_db.values())
    if favorite_only:
        contacts = [c for c in contacts if c["is_favorite"]]
    
    # Paginar
    total = len(contacts)
    start = (page - 1) * per_page
    end = start + per_page
    items = contacts[start:end]
    
    return ContactList(
        items=items,
        total=total,
        page=page,
        per_page=per_page,
    )


@app.get(
    "/contacts/{contact_id}",
    response_model=ContactResponse,
    tags=["Contacts"],
)
async def get_contact(contact_id: int) -> ContactResponse:
    """Obtener contacto por ID."""
    if contact_id not in contacts_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    return contacts_db[contact_id]


@app.get(
    "/contacts/email/{email}",
    response_model=ContactResponse,
    tags=["Contacts"],
)
async def get_contact_by_email(email: str) -> ContactResponse:
    """Buscar contacto por email."""
    contact = find_by_email(email)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    return contact


@app.patch(
    "/contacts/{contact_id}",
    response_model=ContactResponse,
    tags=["Contacts"],
)
async def update_contact(
    contact_id: int,
    contact: ContactUpdate,
) -> ContactResponse:
    """
    Actualizar contacto parcialmente.
    
    - Solo actualiza campos enviados
    - Valida email único si se cambia
    """
    if contact_id not in contacts_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    
    # Obtener solo campos enviados
    update_data = contact.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update"
        )
    
    # Si se actualiza email, verificar que no exista
    if "email" in update_data:
        existing = find_by_email(update_data["email"])
        if existing and existing["id"] != contact_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Email {update_data['email']} already in use"
            )
    
    # Actualizar
    stored = contacts_db[contact_id]
    for key, value in update_data.items():
        stored[key] = value
    stored["updated_at"] = datetime.now()
    
    return stored


@app.delete(
    "/contacts/{contact_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Contacts"],
)
async def delete_contact(contact_id: int) -> None:
    """Eliminar contacto."""
    if contact_id not in contacts_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    del contacts_db[contact_id]


@app.post(
    "/contacts/{contact_id}/favorite",
    response_model=ContactResponse,
    tags=["Contacts"],
)
async def toggle_favorite(contact_id: int) -> ContactResponse:
    """Alternar estado de favorito."""
    if contact_id not in contacts_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    
    stored = contacts_db[contact_id]
    stored["is_favorite"] = not stored["is_favorite"]
    stored["updated_at"] = datetime.now()
    
    return stored


# ============================================
# HEALTH CHECK
# ============================================

@app.get("/", tags=["Health"])
async def root():
    """Health check."""
    return {
        "status": "ok",
        "message": "Contacts API running",
        "total_contacts": len(contacts_db),
    }
