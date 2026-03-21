# ============================================
# Práctica 01: Relación Uno a Muchos
# ============================================
print("=== Práctica 01: Relación 1:N ===\n")

from sqlalchemy import select


# ============================================
# PASO 4: Crear las Tablas
# ============================================
# Descomenta las siguientes líneas:

# from database import engine, Base
# from models import Author, Post
# 
# # Crear todas las tablas en la base de datos
# Base.metadata.create_all(bind=engine)
# print("✅ Tablas creadas correctamente\n")


# ============================================
# PASO 5: Insertar Datos
# ============================================
# Descomenta la siguiente función y su llamada:

# from database import SessionLocal
# 
# def create_sample_data():
#     """Crea datos de ejemplo: un autor con dos posts"""
#     db = SessionLocal()
#     
#     # Verificar si ya hay datos
#     existing = db.execute(select(Author)).first()
#     if existing:
#         print("⚠️  Ya existen datos en la base de datos")
#         db.close()
#         return
#     
#     # Crear autor
#     author = Author(name="John Doe", email="john@example.com")
#     db.add(author)
#     db.commit()
#     db.refresh(author)  # Obtener el ID asignado
#     print(f"✅ Autor creado: {author.name} (ID: {author.id})")
#     
#     # Crear posts para el autor
#     # Método 1: Usando author_id (FK directamente)
#     post1 = Post(
#         title="Intro to FastAPI",
#         content="FastAPI es un framework moderno para crear APIs...",
#         author_id=author.id
#     )
#     
#     # Método 2: Usando la relación (también válido)
#     post2 = Post(
#         title="SQLAlchemy 2.0 Guide",
#         content="SQLAlchemy 2.0 trae muchas mejoras...",
#         author=author  # Asigna directamente el objeto
#     )
#     
#     db.add_all([post1, post2])
#     db.commit()
#     print(f"✅ Posts creados: {post1.title}, {post2.title}\n")
#     
#     db.close()
# 
# # Llamar a la función
# create_sample_data()


# ============================================
# PASO 6: Consultar Relaciones
# ============================================
# Descomenta la siguiente función y su llamada:

# def query_relationships():
#     """Demuestra cómo navegar las relaciones"""
#     db = SessionLocal()
#     
#     # -----------------------------------------
#     # Acceder de Author → Posts (1 a muchos)
#     # -----------------------------------------
#     author = db.execute(
#         select(Author).where(Author.email == "john@example.com")
#     ).scalar_one()
#     
#     print(f"📝 Posts de {author.name}:")
#     for post in author.posts:  # Acceso via relación ORM
#         print(f"   - {post.title}")
#     
#     # -----------------------------------------
#     # Acceder de Post → Author (muchos a 1)
#     # -----------------------------------------
#     post = db.execute(select(Post).limit(1)).scalar()
#     print(f"\n👤 Autor del post '{post.title}': {post.author.name}")
#     
#     # -----------------------------------------
#     # Contar posts por autor
#     # -----------------------------------------
#     print(f"\n📊 Total de posts de {author.name}: {len(author.posts)}")
#     
#     db.close()
# 
# # Llamar a la función
# query_relationships()


# ============================================
# RETO EXTRA (opcional)
# ============================================
# Descomenta para intentar el reto:

# def reto_extra():
#     """
#     Reto: Crear otro autor con 3 posts y mostrar estadísticas
#     """
#     db = SessionLocal()
#     
#     # 1. Crear segundo autor
#     # author2 = Author(name="Jane Smith", email="jane@example.com")
#     # db.add(author2)
#     # db.commit()
#     
#     # 2. Crear 3 posts para Jane
#     # posts = [
#     #     Post(title="Post 1", content="...", author=author2),
#     #     Post(title="Post 2", content="...", author=author2),
#     #     Post(title="Post 3", content="...", author=author2),
#     # ]
#     # db.add_all(posts)
#     # db.commit()
#     
#     # 3. Listar todos los autores con cantidad de posts
#     # authors = db.execute(select(Author)).scalars().all()
#     # print("\n📊 Estadísticas de autores:")
#     # for author in authors:
#     #     print(f"   - {author.name}: {len(author.posts)} posts")
#     
#     db.close()
# 
# reto_extra()


print("\n=== Fin de la Práctica 01 ===")
