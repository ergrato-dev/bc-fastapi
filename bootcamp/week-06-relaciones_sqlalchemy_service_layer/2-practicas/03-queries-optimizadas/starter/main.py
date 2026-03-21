# ============================================
# Práctica 03: Queries Optimizadas
# ============================================
print("=== Práctica 03: Queries Optimizadas ===\n")

import time
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, joinedload, selectinload

from models import Base, Author, Post, Tag

# Configurar base de datos
engine = create_engine("sqlite:///./blog_queries.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

# Crear tablas
Base.metadata.create_all(bind=engine)


# ============================================
# Setup: Crear datos de prueba
# ============================================
def setup_test_data():
    """Crea datos de prueba para las queries"""
    db = SessionLocal()
    
    if db.execute(select(Author)).first():
        print("⚠️  Datos ya existen\n")
        db.close()
        return
    
    # Crear autores
    authors = [
        Author(name="Alice Smith", email="alice@example.com"),
        Author(name="Bob Jones", email="bob@example.com"),
        Author(name="Carol White", email="carol@example.com"),
    ]
    db.add_all(authors)
    db.commit()
    
    # Crear tags
    tags = [Tag(name=n) for n in ["python", "fastapi", "sqlalchemy", "docker", "testing"]]
    db.add_all(tags)
    db.commit()
    
    # Crear posts con tags
    python, fastapi, sqlalchemy, docker, testing = tags
    
    posts = [
        Post(title="FastAPI Intro", content="...", author=authors[0], tags=[python, fastapi]),
        Post(title="SQLAlchemy Tips", content="...", author=authors[0], tags=[python, sqlalchemy]),
        Post(title="Docker Guide", content="...", author=authors[1], tags=[docker, python]),
        Post(title="Testing in Python", content="...", author=authors[1], tags=[python, testing]),
        Post(title="Advanced FastAPI", content="...", author=authors[2], tags=[fastapi, python, docker]),
    ]
    db.add_all(posts)
    db.commit()
    
    print("✅ Datos de prueba creados\n")
    db.close()

setup_test_data()


# ============================================
# PASO 1: El Problema N+1
# ============================================
# Descomenta la siguiente función y su llamada:

# def demonstrate_n_plus_1():
#     """
#     Demuestra el problema N+1.
#     Observa los logs SQL - verás muchas queries.
#     """
#     print("\n--- PROBLEMA N+1 ---")
#     print("Observa cuántas queries se ejecutan:\n")
#     
#     db = SessionLocal()
#     
#     # Query 1: Obtener todos los posts
#     posts = db.execute(select(Post)).scalars().all()
#     
#     # N queries adicionales (1 por cada post para cargar author)
#     for post in posts:
#         print(f"  {post.title} by {post.author.name}")
#     
#     db.close()
#     print("\n❌ Problema: Se ejecutaron N+1 queries!")
# 
# demonstrate_n_plus_1()


# ============================================
# PASO 2: Solución con joinedload()
# ============================================
# Descomenta la siguiente función y su llamada:

# def optimized_with_joinedload():
#     """
#     Usa JOIN para cargar autor en UNA sola query.
#     joinedload() es ideal para relaciones "to-one" (muchos a uno).
#     """
#     print("\n--- SOLUCIÓN: joinedload() ---")
#     print("Ahora solo 1 query con JOIN:\n")
#     
#     db = SessionLocal()
#     
#     stmt = (
#         select(Post)
#         .options(joinedload(Post.author))
#     )
#     # .unique() es necesario con joinedload para evitar duplicados
#     posts = db.execute(stmt).scalars().unique().all()
#     
#     for post in posts:
#         print(f"  {post.title} by {post.author.name}")
#     
#     db.close()
#     print("\n✅ Solo 1 query ejecutada!")
# 
# optimized_with_joinedload()


# ============================================
# PASO 3: selectinload() para colecciones
# ============================================
# Descomenta la siguiente función y su llamada:

# def load_with_selectinload():
#     """
#     selectinload() es mejor para relaciones "to-many" (uno a muchos, N:M).
#     Ejecuta 2 queries: una para posts, otra para tags con WHERE IN.
#     """
#     print("\n--- selectinload() para colecciones ---")
#     
#     db = SessionLocal()
#     
#     stmt = (
#         select(Post)
#         .options(
#             joinedload(Post.author),      # JOIN para el autor (1)
#             selectinload(Post.tags)       # SELECT IN para tags (lista)
#         )
#     )
#     posts = db.execute(stmt).scalars().unique().all()
#     
#     print("Posts con autor y tags:")
#     for post in posts:
#         tag_names = ", ".join(t.name for t in post.tags)
#         print(f"  {post.title} by {post.author.name}")
#         print(f"      Tags: [{tag_names}]")
#     
#     db.close()
# 
# load_with_selectinload()


# ============================================
# PASO 4: Filtrar por Relación
# ============================================
# Descomenta la siguiente función y su llamada:

# def filter_by_relation():
#     """
#     Para FILTRAR por campos de una relación,
#     necesitas un JOIN explícito (no options).
#     """
#     print("\n--- Filtrar por relación ---")
#     
#     db = SessionLocal()
#     
#     # Posts que tienen el tag "python"
#     stmt = (
#         select(Post)
#         .join(Post.tags)                    # JOIN explícito para filtrar
#         .where(Tag.name == "python")
#         .options(
#             joinedload(Post.author),
#             selectinload(Post.tags)
#         )
#     )
#     posts = db.execute(stmt).scalars().unique().all()
#     
#     print(f"Posts con tag 'python':")
#     for post in posts:
#         print(f"  - {post.title}")
#     
#     # Posts de un autor específico
#     print(f"\nPosts de Alice:")
#     stmt = (
#         select(Post)
#         .join(Post.author)
#         .where(Author.name == "Alice Smith")
#     )
#     posts = db.execute(stmt).scalars().all()
#     for post in posts:
#         print(f"  - {post.title}")
#     
#     db.close()
# 
# filter_by_relation()


# ============================================
# PASO 5: Ordenar por Relación
# ============================================
# Descomenta la siguiente función y su llamada:

# def order_by_relation():
#     """
#     Para ORDENAR por campos de una relación,
#     también necesitas JOIN explícito.
#     """
#     print("\n--- Ordenar por relación ---")
#     
#     db = SessionLocal()
#     
#     # Ordenar posts por nombre del autor
#     stmt = (
#         select(Post)
#         .join(Post.author)
#         .order_by(Author.name, Post.title)
#         .options(joinedload(Post.author))
#     )
#     posts = db.execute(stmt).scalars().unique().all()
#     
#     print("Posts ordenados por autor:")
#     for post in posts:
#         print(f"  {post.author.name}: {post.title}")
#     
#     db.close()
# 
# order_by_relation()


# ============================================
# PASO 6: Agregaciones y Stats
# ============================================
# Descomenta la siguiente función y su llamada:

# def author_stats():
#     """
#     Queries con agregaciones (COUNT, SUM, etc.)
#     """
#     print("\n--- Estadísticas ---")
#     
#     db = SessionLocal()
#     
#     # Posts por autor
#     stmt = (
#         select(
#             Author.name,
#             func.count(Post.id).label("post_count")
#         )
#         .join(Author.posts)
#         .group_by(Author.id)
#         .order_by(func.count(Post.id).desc())
#     )
#     
#     results = db.execute(stmt).all()
#     
#     print("Posts por autor:")
#     for name, count in results:
#         print(f"  - {name}: {count} posts")
#     
#     # Tags más usados
#     stmt = (
#         select(
#             Tag.name,
#             func.count(Post.id).label("usage_count")
#         )
#         .join(Tag.posts)
#         .group_by(Tag.id)
#         .order_by(func.count(Post.id).desc())
#         .limit(3)
#     )
#     
#     results = db.execute(stmt).all()
#     
#     print("\nTop 3 tags más usados:")
#     for name, count in results:
#         print(f"  - {name}: {count} posts")
#     
#     db.close()
# 
# author_stats()


# ============================================
# PASO 7: Comparar Rendimiento
# ============================================
# Descomenta la siguiente función y su llamada:

# def compare_performance():
#     """
#     Compara tiempo de ejecución con y sin eager loading.
#     La diferencia es más notable con más datos.
#     """
#     print("\n--- Comparación de rendimiento ---")
#     
#     db = SessionLocal()
#     
#     # Sin optimización (lazy loading)
#     start = time.time()
#     posts = db.execute(select(Post)).scalars().all()
#     for post in posts:
#         _ = post.author.name
#         _ = [t.name for t in post.tags]
#     lazy_time = time.time() - start
#     
#     # Con optimización (eager loading)
#     start = time.time()
#     stmt = select(Post).options(
#         joinedload(Post.author),
#         selectinload(Post.tags)
#     )
#     posts = db.execute(stmt).scalars().unique().all()
#     for post in posts:
#         _ = post.author.name
#         _ = [t.name for t in post.tags]
#     eager_time = time.time() - start
#     
#     print(f"⏱️  Lazy loading:  {lazy_time:.6f}s")
#     print(f"⏱️  Eager loading: {eager_time:.6f}s")
#     print(f"📈 Diferencia: {((lazy_time - eager_time) / lazy_time * 100):.1f}% más rápido")
#     
#     db.close()
# 
# compare_performance()


# ============================================
# RETO EXTRA
# ============================================

# def reto_posts_sin_tags():
#     """Posts que NO tienen tags"""
#     db = SessionLocal()
#     
#     stmt = (
#         select(Post)
#         .outerjoin(Post.tags)
#         .where(Tag.id.is_(None))
#     )
#     posts = db.execute(stmt).scalars().all()
#     
#     print(f"\nPosts sin tags: {len(posts)}")
#     db.close()
# 
# reto_posts_sin_tags()


print("\n=== Fin de la Práctica 03 ===")
