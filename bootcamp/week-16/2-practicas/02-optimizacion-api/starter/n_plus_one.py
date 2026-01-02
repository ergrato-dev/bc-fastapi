"""
============================================
PRÁCTICA 02: Optimización de API
Archivo: n_plus_one.py
============================================

El problema N+1 es uno de los más comunes en ORMs.
Ocurre cuando hacemos 1 query para obtener N registros,
y luego N queries adicionales para obtener datos relacionados.
"""

from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

# ============================================
# SETUP: Modelos de ejemplo
# ============================================
print("--- Setup: Modelos de ejemplo ---")

MODELS_EXAMPLE = """
# models/user.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(255), unique=True)
    
    # Relación 1:N con posts
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    # Relación N:1 con user
    author = relationship("User", back_populates="posts")
    
    # Relación N:M con tags
    tags = relationship("Tag", secondary="post_tags", back_populates="posts")

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    
    posts = relationship("Post", secondary="post_tags", back_populates="tags")
"""
print(MODELS_EXAMPLE)


# ============================================
# PASO 1: Identificar el problema N+1
# ============================================
print("\n--- Paso 1: El problema N+1 ---")

# ❌ MAL - Esto genera N+1 queries
N_PLUS_ONE_EXAMPLE = """
# Esta función genera 1 + N queries:
# 1 query: SELECT * FROM users
# N queries: SELECT * FROM posts WHERE author_id = ? (una por cada user)

async def get_users_with_posts_bad(db: AsyncSession):
    # Query 1: Obtener todos los usuarios
    result = await db.execute(select(User))
    users = result.scalars().all()
    
    response = []
    for user in users:
        # Query 2...N+1: Acceder a posts dispara una query por usuario
        # SQLAlchemy hace lazy loading por defecto
        user_data = {
            "id": user.id,
            "name": user.name,
            "posts": [{"id": p.id, "title": p.title} for p in user.posts]
            # ↑ Aquí ocurre la query adicional
        }
        response.append(user_data)
    
    return response

# Si hay 100 usuarios, esto ejecuta 101 queries!
# 1 (users) + 100 (posts por cada user) = 101 queries
"""
print(N_PLUS_ONE_EXAMPLE)


# ============================================
# PASO 2: Solución con selectinload
# ============================================
print("\n--- Paso 2: Solución con selectinload ---")

# ✅ BIEN - Usar selectinload para relaciones 1:N
SELECTINLOAD_EXAMPLE = """
# selectinload hace 2 queries en total:
# Query 1: SELECT * FROM users
# Query 2: SELECT * FROM posts WHERE author_id IN (1, 2, 3, ...)

async def get_users_with_posts_good(db: AsyncSession):
    # Eager loading con selectinload
    query = select(User).options(selectinload(User.posts))
    result = await db.execute(query)
    users = result.scalars().all()
    
    response = []
    for user in users:
        # Los posts ya están cargados, no hay query adicional
        user_data = {
            "id": user.id,
            "name": user.name,
            "posts": [{"id": p.id, "title": p.title} for p in user.posts]
        }
        response.append(user_data)
    
    return response

# Con 100 usuarios, esto ejecuta solo 2 queries!
# Mucho más eficiente que 101 queries
"""
print(SELECTINLOAD_EXAMPLE)


# ============================================
# PASO 3: Solución con joinedload
# ============================================
print("\n--- Paso 3: Solución con joinedload ---")

# ✅ BIEN - Usar joinedload para relaciones N:1
JOINEDLOAD_EXAMPLE = """
# joinedload hace 1 query con JOIN:
# SELECT posts.*, users.* FROM posts JOIN users ON ...

async def get_posts_with_author(db: AsyncSession):
    # Eager loading con joinedload (mejor para N:1)
    query = select(Post).options(joinedload(Post.author))
    result = await db.execute(query)
    posts = result.unique().scalars().all()
    
    response = []
    for post in posts:
        # El autor ya está cargado
        post_data = {
            "id": post.id,
            "title": post.title,
            "author_name": post.author.name  # Sin query adicional
        }
        response.append(post_data)
    
    return response

# IMPORTANTE: usar .unique() con joinedload para evitar duplicados
"""
print(JOINEDLOAD_EXAMPLE)


# ============================================
# PASO 4: Relaciones anidadas
# ============================================
print("\n--- Paso 4: Relaciones anidadas ---")

NESTED_EXAMPLE = """
# Para cargar relaciones anidadas (posts -> tags):
# Usamos selectinload encadenado

async def get_users_with_posts_and_tags(db: AsyncSession):
    query = (
        select(User)
        .options(
            selectinload(User.posts).selectinload(Post.tags)
        )
    )
    result = await db.execute(query)
    users = result.scalars().all()
    
    # Esto genera 3 queries:
    # 1. SELECT * FROM users
    # 2. SELECT * FROM posts WHERE author_id IN (...)
    # 3. SELECT * FROM tags JOIN post_tags WHERE post_id IN (...)
    
    return users

# También puedes combinar joinedload y selectinload:
async def get_posts_complete(db: AsyncSession):
    query = (
        select(Post)
        .options(
            joinedload(Post.author),         # JOIN para autor (N:1)
            selectinload(Post.tags),         # Subquery para tags (N:M)
            selectinload(Post.comments)      # Subquery para comments (1:N)
        )
    )
    result = await db.execute(query)
    return result.unique().scalars().all()
"""
print(NESTED_EXAMPLE)


# ============================================
# PASO 5: Cuándo usar cada uno
# ============================================
print("\n--- Paso 5: Cuándo usar cada estrategia ---")

WHEN_TO_USE = """
┌─────────────────┬───────────────────────────────────────────────────┐
│ Estrategia      │ Cuándo usar                                       │
├─────────────────┼───────────────────────────────────────────────────┤
│ selectinload    │ • Relaciones 1:N (user.posts)                     │
│                 │ • Relaciones N:M (post.tags)                      │
│                 │ • Cuando esperas muchos registros relacionados    │
│                 │ • Genera query IN(...) separada                   │
├─────────────────┼───────────────────────────────────────────────────┤
│ joinedload      │ • Relaciones N:1 (post.author)                    │
│                 │ • Cuando esperas un solo registro relacionado     │
│                 │ • Genera JOIN en la misma query                   │
│                 │ • Requiere .unique() para evitar duplicados       │
├─────────────────┼───────────────────────────────────────────────────┤
│ lazy (default)  │ • Cuando raramente accedes a la relación          │
│                 │ • Para relaciones opcionales                      │
│                 │ • ⚠️ Cuidado con N+1!                             │
├─────────────────┼───────────────────────────────────────────────────┤
│ subqueryload    │ • Similar a selectinload                          │
│                 │ • Usa subquery en lugar de IN                     │
│                 │ • Mejor para queries muy complejas                │
└─────────────────┴───────────────────────────────────────────────────┘
"""
print(WHEN_TO_USE)


# ============================================
# PASO 6: Detectar N+1 en tu proyecto
# ============================================
print("\n--- Paso 6: Cómo detectar N+1 en tu proyecto ---")

DETECTION = """
# 1. Habilita logging de SQL en SQLAlchemy
engine = create_async_engine(
    DATABASE_URL,
    echo=True  # Imprime todas las queries
)

# 2. Busca patrones sospechosos en logs:
#    - Muchas queries SELECT similares
#    - Queries que difieren solo en el ID
#    - Ráfagas de queries en endpoints de listado

# 3. Revisa endpoints que:
#    - Retornan listas de objetos
#    - Incluyen datos de relaciones
#    - Tienen bucles for sobre resultados de DB

# 4. Usa herramientas como:
#    - SQLAlchemy-Utils (query counter)
#    - nplusone library (auto-detection)
"""
print(DETECTION)


# ============================================
# EJERCICIO PRÁCTICO
# ============================================
print("\n" + "="*50)
print("📝 EJERCICIO: Optimiza tu proyecto")
print("="*50)
print("""
1. Habilita echo=True en tu engine de SQLAlchemy

2. Accede a un endpoint que liste datos con relaciones

3. Cuenta las queries en los logs

4. Si hay N+1, agrega selectinload o joinedload

5. Verifica que las queries se redujeron

Ejemplo de endpoint a revisar:
- GET /tasks (si incluye project o assignee)
- GET /users/{id}/tasks
- GET /projects/{id} (si incluye tasks)
""")
