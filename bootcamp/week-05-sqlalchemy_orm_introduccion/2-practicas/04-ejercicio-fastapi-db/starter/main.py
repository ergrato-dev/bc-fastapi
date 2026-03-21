"""
Ejercicio 04: FastAPI + Database
================================
Integra SQLAlchemy con FastAPI para crear una API CRUD completa.

Instrucciones:
1. Lee cada sección
2. Descomenta el código paso a paso
3. Ejecuta: uv run fastapi dev main.py
4. Abre: http://localhost:8000/docs
"""

# ============================================
# PASO 1: Imports
# ============================================

# Descomenta las siguientes líneas:
# from datetime import datetime
# from fastapi import FastAPI, Depends, HTTPException, status
# from pydantic import BaseModel, Field, ConfigDict
# from sqlalchemy import create_engine, String, Text, select, desc
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session


# ============================================
# PASO 2: Configuración de Base de Datos
# ============================================

# Engine conecta a SQLite
# SessionLocal es la fábrica de sesiones

# Descomenta las siguientes líneas:
# engine = create_engine(
#     "sqlite:///./notes.db",
#     connect_args={"check_same_thread": False}  # Necesario para SQLite + FastAPI
# )
#
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
#
# class Base(DeclarativeBase):
#     pass


# ============================================
# PASO 3: Modelo SQLAlchemy
# ============================================

# Note es la tabla en la base de datos

# Descomenta las siguientes líneas:
# class Note(Base):
#     __tablename__ = "notes"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(100))
#     content: Mapped[str] = mapped_column(Text)
#     created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


# ============================================
# PASO 4: Schemas Pydantic
# ============================================

# Schemas para validación de entrada/salida
# - NoteCreate: valida POST body
# - NoteUpdate: valida PUT body (campos opcionales)
# - NoteResponse: formato de respuesta

# Descomenta las siguientes líneas:
# class NoteCreate(BaseModel):
#     """Schema para crear nota"""
#     title: str = Field(..., min_length=1, max_length=100)
#     content: str = Field(..., min_length=1)
#
# class NoteUpdate(BaseModel):
#     """Schema para actualizar nota (campos opcionales)"""
#     title: str | None = Field(None, min_length=1, max_length=100)
#     content: str | None = Field(None, min_length=1)
#
# class NoteResponse(BaseModel):
#     """Schema de respuesta"""
#     id: int
#     title: str
#     content: str
#     created_at: datetime
#     
#     # Permite crear NoteResponse desde objeto SQLAlchemy
#     model_config = ConfigDict(from_attributes=True)


# ============================================
# PASO 5: Dependency get_db
# ============================================

# get_db() provee una sesión de DB a cada request
# El 'finally' garantiza que la sesión se cierre

# Descomenta las siguientes líneas:
# def get_db():
#     """Dependency que provee sesión de base de datos"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# ============================================
# CREAR APP Y TABLAS
# ============================================

# Descomenta las siguientes líneas:
# # Crear tablas al iniciar
# Base.metadata.create_all(bind=engine)
#
# app = FastAPI(
#     title="Notes API",
#     description="API CRUD para notas con SQLAlchemy",
#     version="1.0.0"
# )


# ============================================
# PASO 6: Endpoint CREATE
# ============================================

# POST /notes - Crear nueva nota
# - Recibe NoteCreate (validado por Pydantic)
# - Usa db de Depends(get_db)
# - Retorna NoteResponse

# Descomenta las siguientes líneas:
# @app.post(
#     "/notes",
#     response_model=NoteResponse,
#     status_code=status.HTTP_201_CREATED,
#     tags=["notes"]
# )
# def create_note(note: NoteCreate, db: Session = Depends(get_db)):
#     """Crea una nueva nota"""
#     db_note = Note(
#         title=note.title,
#         content=note.content
#     )
#     db.add(db_note)
#     db.commit()
#     db.refresh(db_note)
#     return db_note


# ============================================
# PASO 7: Endpoints READ
# ============================================

# GET /notes - Listar todas las notas
# GET /notes/{id} - Obtener una nota por ID

# Descomenta las siguientes líneas:
# @app.get(
#     "/notes",
#     response_model=list[NoteResponse],
#     tags=["notes"]
# )
# def list_notes(
#     skip: int = 0,
#     limit: int = 10,
#     db: Session = Depends(get_db)
# ):
#     """Lista todas las notas con paginación"""
#     stmt = select(Note).order_by(desc(Note.created_at)).offset(skip).limit(limit)
#     notes = db.execute(stmt).scalars().all()
#     return notes
#
#
# @app.get(
#     "/notes/{note_id}",
#     response_model=NoteResponse,
#     tags=["notes"]
# )
# def get_note(note_id: int, db: Session = Depends(get_db)):
#     """Obtiene una nota por ID"""
#     note = db.get(Note, note_id)
#     
#     if not note:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Note with id {note_id} not found"
#         )
#     
#     return note


# ============================================
# PASO 8: Endpoints UPDATE y DELETE
# ============================================

# PUT /notes/{id} - Actualizar nota
# DELETE /notes/{id} - Eliminar nota

# Descomenta las siguientes líneas:
# @app.put(
#     "/notes/{note_id}",
#     response_model=NoteResponse,
#     tags=["notes"]
# )
# def update_note(
#     note_id: int,
#     note_data: NoteUpdate,
#     db: Session = Depends(get_db)
# ):
#     """Actualiza una nota existente"""
#     note = db.get(Note, note_id)
#     
#     if not note:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Note with id {note_id} not found"
#         )
#     
#     # Actualizar solo campos proporcionados
#     update_data = note_data.model_dump(exclude_unset=True)
#     for key, value in update_data.items():
#         setattr(note, key, value)
#     
#     db.commit()
#     db.refresh(note)
#     return note
#
#
# @app.delete(
#     "/notes/{note_id}",
#     status_code=status.HTTP_204_NO_CONTENT,
#     tags=["notes"]
# )
# def delete_note(note_id: int, db: Session = Depends(get_db)):
#     """Elimina una nota"""
#     note = db.get(Note, note_id)
#     
#     if not note:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Note with id {note_id} not found"
#         )
#     
#     db.delete(note)
#     db.commit()
#     return None


# ============================================
# HEALTH CHECK
# ============================================

# Descomenta las siguientes líneas:
# @app.get("/health", tags=["health"])
# def health_check():
#     """Verifica que la API está funcionando"""
#     return {"status": "healthy", "database": "sqlite"}


# ============================================
# RESUMEN
# ============================================
print("""
FastAPI + SQLAlchemy Integration
================================

Estructura típica:
1. database.py  → Engine, SessionLocal, Base
2. models.py    → Modelos SQLAlchemy (tablas)
3. schemas.py   → Schemas Pydantic (validación)
4. main.py      → App FastAPI con endpoints

Flujo de un request:
Request → Pydantic valida → Endpoint → SQLAlchemy → DB
                                            ↓
Response ← Pydantic serializa ← Endpoint ← SQLAlchemy

Dependency Injection:
def get_db():
    db = SessionLocal()
    try:
        yield db      # FastAPI usa la sesión
    finally:
        db.close()    # Se cierra al terminar

Ejecutar:
  uv run fastapi dev main.py
  
Abrir docs:
  http://localhost:8000/docs
""")
