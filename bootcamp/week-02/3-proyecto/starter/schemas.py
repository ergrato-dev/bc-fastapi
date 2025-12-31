"""
Schemas Pydantic para la API de Contactos
=========================================

TODO: Implementar los schemas según las especificaciones del proyecto.

Schemas requeridos:
- ContactBase: Campos comunes
- ContactCreate: Para POST (con validadores)
- ContactUpdate: Para PATCH (todos opcionales)
- ContactResponse: Para respuestas
- ContactList: Lista paginada
"""

from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator
from datetime import datetime
import re


# ============================================
# TODO 1: ContactBase
# Campos comunes para todos los schemas de contacto
# ============================================

class ContactBase(BaseModel):
    """
    Campos comunes para contactos.
    
    Campos:
    - first_name: str (2-50 caracteres)
    - last_name: str (2-50 caracteres)
    - email: EmailStr
    - phone: str
    - company: str | None = None
    - tags: list[str] (máximo 5, default: [])
    - is_favorite: bool = False
    """
    # TODO: Definir los campos con sus validaciones usando Field()
    pass


# ============================================
# TODO 2: ContactCreate
# Schema para crear contactos (POST)
# Incluye validadores para normalizar datos
# ============================================

class ContactCreate(ContactBase):
    """
    Schema para crear un contacto.
    
    Validadores requeridos:
    1. normalize_names: Capitalizar first_name y last_name
    2. normalize_phone: Convertir a formato +52 XXX XXX XXXX
    3. normalize_tags: Minúsculas, sin duplicados, máximo 5
    """
    
    # TODO: Implementar @field_validator para first_name y last_name
    # - Quitar espacios al inicio/final
    # - Capitalizar (title())
    # - Validar longitud mínima 2
    
    # TODO: Implementar @field_validator para phone (mode="before")
    # - Extraer solo dígitos
    # - Si tiene 10 dígitos, formatear como +52 XXX XXX XXXX
    # - Si tiene 12 dígitos y empieza con 52, formatear igual
    # - Si no, lanzar ValueError
    
    # TODO: Implementar @field_validator para tags
    # - Convertir a minúsculas
    # - Eliminar duplicados
    # - Limitar a máximo 5
    pass


# ============================================
# TODO 3: ContactUpdate
# Schema para actualizar contactos (PATCH)
# Todos los campos son opcionales
# ============================================

class ContactUpdate(BaseModel):
    """
    Schema para actualizar contacto parcialmente.
    
    Todos los campos son opcionales (None por defecto).
    Incluir los mismos validadores que ContactCreate.
    """
    # TODO: Definir campos opcionales (str | None = None, etc.)
    # TODO: Copiar validadores de ContactCreate (adaptados para valores None)
    pass


# ============================================
# TODO 4: ContactResponse
# Schema para respuestas (incluye id y timestamps)
# ============================================

class ContactResponse(ContactBase):
    """
    Schema para respuestas de contacto.
    
    Campos adicionales:
    - id: int
    - created_at: datetime
    - updated_at: datetime | None
    
    Configuración:
    - from_attributes=True (para compatibilidad con ORM)
    """
    model_config = ConfigDict(from_attributes=True)
    
    # TODO: Agregar campos id, created_at, updated_at
    pass


# ============================================
# TODO 5: ContactList
# Schema para lista paginada
# ============================================

class ContactList(BaseModel):
    """
    Schema para lista paginada de contactos.
    
    Campos:
    - items: list[ContactResponse]
    - total: int
    - page: int
    - per_page: int
    """
    # TODO: Definir los campos para paginación
    pass
