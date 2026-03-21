"""
============================================
PRÁCTICA 02: Optimización de API
Archivo: optimize_endpoints.py
============================================

Técnicas adicionales para optimizar endpoints de FastAPI.
"""

# ============================================
# PASO 1: Compresión de respuestas
# ============================================
print("--- Paso 1: Compresión gzip ---")

COMPRESSION = """
# Habilita compresión para reducir tamaño de respuestas

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# Comprimir respuestas > 500 bytes
app.add_middleware(GZipMiddleware, minimum_size=500)

# Las respuestas JSON grandes se comprimirán automáticamente
# Típicamente 60-80% de reducción en tamaño

# Verificar en headers de response:
# Content-Encoding: gzip
"""
print(COMPRESSION)


# ============================================
# PASO 2: Paginación eficiente
# ============================================
print("\n--- Paso 2: Paginación eficiente ---")

PAGINATION = """
# Implementa paginación cursor-based para grandes datasets

from fastapi import Query
from pydantic import BaseModel
from sqlalchemy import select
from typing import Generic, TypeVar

T = TypeVar("T")

class CursorPagination(BaseModel):
    '''Paginación basada en cursor (más eficiente que offset).'''
    
    cursor: str | None = None  # ID del último elemento
    limit: int = 20

class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    next_cursor: str | None
    has_more: bool

# ❌ MAL - Offset pagination (lento para páginas altas)
async def list_items_offset(
    db: AsyncSession,
    page: int = 1,
    per_page: int = 20
):
    # OFFSET es lento porque DB debe contar N filas
    offset = (page - 1) * per_page
    query = select(Item).offset(offset).limit(per_page)
    # Página 1000 = DB cuenta 20,000 filas antes de retornar
    return await db.execute(query)

# ✅ BIEN - Cursor pagination (consistente en velocidad)
async def list_items_cursor(
    db: AsyncSession,
    cursor: str | None = None,
    limit: int = 20
) -> PaginatedResponse:
    query = select(Item).order_by(Item.id)
    
    if cursor:
        # Usar índice directamente, no cuenta filas
        query = query.where(Item.id > int(cursor))
    
    query = query.limit(limit + 1)  # +1 para saber si hay más
    result = await db.execute(query)
    items = result.scalars().all()
    
    has_more = len(items) > limit
    if has_more:
        items = items[:limit]
    
    return PaginatedResponse(
        items=items,
        next_cursor=str(items[-1].id) if items else None,
        has_more=has_more
    )

# Endpoint:
@router.get("/items", response_model=PaginatedResponse[ItemResponse])
async def list_items(
    cursor: str | None = Query(None, description="Cursor para paginación"),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    return await list_items_cursor(db, cursor, limit)
"""
print(PAGINATION)


# ============================================
# PASO 3: Selección de campos
# ============================================
print("\n--- Paso 3: Selección de campos (sparse fieldsets) ---")

FIELD_SELECTION = """
# Permite al cliente solicitar solo los campos que necesita

from fastapi import Query
from sqlalchemy import select
from sqlalchemy.orm import load_only

@router.get("/users")
async def list_users(
    fields: str | None = Query(
        None, 
        description="Campos a incluir, separados por coma",
        examples=["id,name,email"]
    ),
    db: AsyncSession = Depends(get_db)
):
    query = select(User)
    
    if fields:
        # Cargar solo campos solicitados
        field_list = [f.strip() for f in fields.split(",")]
        valid_fields = {"id", "name", "email", "created_at"}  # Whitelist
        
        selected = [
            getattr(User, f) 
            for f in field_list 
            if f in valid_fields
        ]
        
        if selected:
            query = query.options(load_only(*selected))
    
    result = await db.execute(query)
    users = result.scalars().all()
    
    # Retornar solo campos solicitados
    if fields:
        field_list = [f.strip() for f in fields.split(",")]
        return [
            {f: getattr(u, f) for f in field_list if hasattr(u, f)}
            for u in users
        ]
    
    return users

# Uso:
# GET /users?fields=id,name
# Retorna: [{"id": 1, "name": "John"}, ...]
# En lugar de todos los campos
"""
print(FIELD_SELECTION)


# ============================================
# PASO 4: Background tasks para operaciones lentas
# ============================================
print("\n--- Paso 4: Background tasks ---")

BACKGROUND_TASKS = """
# Mueve operaciones lentas a background

from fastapi import BackgroundTasks

# Función que se ejecuta en background
async def send_welcome_email(email: str, name: str):
    # Operación lenta (envío de email)
    await email_service.send(
        to=email,
        subject="Bienvenido!",
        body=f"Hola {name}, gracias por registrarte."
    )

async def update_analytics(user_id: int, action: str):
    # Actualizar stats en background
    await analytics.track(user_id, action)

@router.post("/users", status_code=201)
async def create_user(
    user: UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    # Crear usuario (rápido)
    new_user = User(**user.model_dump())
    db.add(new_user)
    await db.commit()
    
    # Tareas lentas en background (no bloquean response)
    background_tasks.add_task(send_welcome_email, user.email, user.name)
    background_tasks.add_task(update_analytics, new_user.id, "signup")
    
    # Response inmediato
    return new_user

# Para tareas más complejas, considera Celery o ARQ
"""
print(BACKGROUND_TASKS)


# ============================================
# PASO 5: Bulk operations
# ============================================
print("\n--- Paso 5: Operaciones en bulk ---")

BULK_OPERATIONS = """
# Agrupa operaciones para reducir round-trips a DB

from sqlalchemy import insert, update, delete

# ❌ MAL - Una query por item
async def create_items_slow(items: list[ItemCreate], db: AsyncSession):
    for item in items:
        new_item = Item(**item.model_dump())
        db.add(new_item)
        await db.commit()  # Commit por cada item = N queries

# ✅ BIEN - Una query para todos
async def create_items_fast(items: list[ItemCreate], db: AsyncSession):
    # Insert bulk
    stmt = insert(Item).values([item.model_dump() for item in items])
    await db.execute(stmt)
    await db.commit()  # Un solo commit

# Bulk update
async def mark_items_as_processed(item_ids: list[int], db: AsyncSession):
    stmt = (
        update(Item)
        .where(Item.id.in_(item_ids))
        .values(processed=True, processed_at=datetime.utcnow())
    )
    await db.execute(stmt)
    await db.commit()

# Bulk delete
async def delete_old_items(days: int, db: AsyncSession):
    cutoff = datetime.utcnow() - timedelta(days=days)
    stmt = delete(Item).where(Item.created_at < cutoff)
    result = await db.execute(stmt)
    await db.commit()
    return result.rowcount

# Endpoint de bulk:
@router.post("/items/bulk", status_code=201)
async def create_items_bulk(
    items: list[ItemCreate],
    db: AsyncSession = Depends(get_db)
):
    if len(items) > 100:
        raise HTTPException(400, "Maximum 100 items per request")
    
    await create_items_fast(items, db)
    return {"created": len(items)}
"""
print(BULK_OPERATIONS)


# ============================================
# PASO 6: Response streaming
# ============================================
print("\n--- Paso 6: Streaming para respuestas grandes ---")

STREAMING = """
# Para respuestas muy grandes, usa streaming

from fastapi.responses import StreamingResponse
import csv
from io import StringIO

async def generate_csv_rows(db: AsyncSession):
    '''Generator que produce filas de CSV.'''
    # Header
    yield "id,name,email,created_at\\n"
    
    # Procesar en batches
    offset = 0
    batch_size = 1000
    
    while True:
        query = select(User).offset(offset).limit(batch_size)
        result = await db.execute(query)
        users = result.scalars().all()
        
        if not users:
            break
        
        for user in users:
            yield f"{user.id},{user.name},{user.email},{user.created_at}\\n"
        
        offset += batch_size

@router.get("/users/export")
async def export_users_csv(db: AsyncSession = Depends(get_db)):
    '''Exporta usuarios como CSV usando streaming.'''
    return StreamingResponse(
        generate_csv_rows(db),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=users.csv"}
    )

# Beneficios:
# - No carga todo en memoria
# - El cliente recibe datos incrementalmente
# - Funciona para millones de registros
"""
print(STREAMING)


# ============================================
# RESUMEN DE OPTIMIZACIONES
# ============================================
print("\n" + "="*50)
print("📊 CHECKLIST DE OPTIMIZACIÓN")
print("="*50)
print("""
□ Compresión gzip habilitada
□ N+1 queries eliminados (selectinload/joinedload)
□ Paginación en todos los listados
□ Cache implementado para datos frecuentes
□ Índices en campos de búsqueda/filtro
□ Background tasks para operaciones lentas
□ Bulk operations para múltiples writes
□ Streaming para exports grandes
□ Selección de campos (sparse fieldsets)
□ Query logging para monitoreo

Métricas objetivo:
• Response time p95 < 200ms
• Queries por request < 5
• Cache hit rate > 80%
• No queries > 100ms
""")
