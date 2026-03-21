# ============================================
# Práctica 02: Relación Muchos a Muchos
# ============================================
print("=== Práctica 02: Relación N:M ===\n")

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from models import Base, Author, Post, Tag, post_tags

# Configurar base de datos
engine = create_engine("sqlite:///./blog_nm.db", echo=True)
SessionLocal = sessionmaker(bind=engine)


# ============================================
# PASO 4: Crear las Tablas
# ============================================
# Descomenta las siguientes líneas:

# Base.metadata.create_all(bind=engine)
# print("✅ Tablas creadas (incluyendo post_tags)\n")


# ============================================
# Crear datos base (Author y Post)
# ============================================
def create_base_data():
    """Crea un autor con posts para trabajar"""
    db = SessionLocal()
    
    # Verificar si ya hay datos
    if db.execute(select(Author)).first():
        print("⚠️  Datos base ya existen")
        db.close()
        return
    
    author = Author(name="John Doe", email="john@example.com")
    db.add(author)
    db.commit()
    
    posts = [
        Post(title="Intro to FastAPI", content="...", author=author),
        Post(title="SQLAlchemy Guide", content="...", author=author),
        Post(title="Python Tips", content="...", author=author),
    ]
    db.add_all(posts)
    db.commit()
    
    print(f"✅ Autor '{author.name}' creado con {len(posts)} posts\n")
    db.close()

# Descomenta para ejecutar:
# create_base_data()


# ============================================
# PASO 5: Crear Tags
# ============================================
# Descomenta la siguiente función y su llamada:

# def create_tags():
#     """Crea tags de ejemplo"""
#     db = SessionLocal()
#     
#     # Verificar si ya hay tags
#     if db.execute(select(Tag)).first():
#         print("⚠️  Tags ya existen")
#         db.close()
#         return
#     
#     tag_names = ["python", "fastapi", "sqlalchemy", "tutorial", "backend"]
#     
#     for name in tag_names:
#         tag = Tag(name=name)
#         db.add(tag)
#     
#     db.commit()
#     print(f"✅ Tags creados: {tag_names}\n")
#     db.close()
# 
# create_tags()


# ============================================
# PASO 6: Asignar Tags a Posts
# ============================================
# Descomenta la siguiente función y su llamada:

# def assign_tags_to_posts():
#     """Asigna tags a los posts existentes"""
#     db = SessionLocal()
#     
#     # Obtener posts
#     posts = db.execute(select(Post)).scalars().all()
#     
#     # Obtener tags
#     python = db.execute(select(Tag).where(Tag.name == "python")).scalar()
#     fastapi = db.execute(select(Tag).where(Tag.name == "fastapi")).scalar()
#     sqlalchemy = db.execute(select(Tag).where(Tag.name == "sqlalchemy")).scalar()
#     tutorial = db.execute(select(Tag).where(Tag.name == "tutorial")).scalar()
#     
#     # Asignar tags (como listas normales)
#     if posts[0].tags == []:  # Solo si no tiene tags
#         posts[0].tags = [python, fastapi, tutorial]  # Intro to FastAPI
#         posts[1].tags = [python, sqlalchemy]         # SQLAlchemy Guide
#         posts[2].tags = [python, tutorial]           # Python Tips
#         
#         db.commit()
#         print("✅ Tags asignados a posts:")
#         for post in posts:
#             tags = [t.name for t in post.tags]
#             print(f"   - '{post.title}': {tags}")
#     else:
#         print("⚠️  Posts ya tienen tags asignados")
#     
#     db.close()
# 
# assign_tags_to_posts()


# ============================================
# PASO 7: Consultar Relaciones N:M
# ============================================
# Descomenta la siguiente función y su llamada:

# def query_many_to_many():
#     """Demuestra queries en relaciones N:M"""
#     db = SessionLocal()
#     
#     # -----------------------------------------
#     # Desde Tag → Posts
#     # -----------------------------------------
#     python_tag = db.execute(
#         select(Tag).where(Tag.name == "python")
#     ).scalar()
#     
#     print(f"\n📝 Posts con tag '{python_tag.name}':")
#     for post in python_tag.posts:
#         print(f"   - {post.title}")
#     
#     # -----------------------------------------
#     # Desde Post → Tags
#     # -----------------------------------------
#     post = db.execute(
#         select(Post).where(Post.title.contains("FastAPI"))
#     ).scalar()
#     
#     print(f"\n🏷️ Tags del post '{post.title}':")
#     for tag in post.tags:
#         print(f"   - {tag.name}")
#     
#     # -----------------------------------------
#     # Posts con tag específico usando JOIN
#     # -----------------------------------------
#     print(f"\n🔍 Query con JOIN (posts con 'tutorial'):")
#     stmt = (
#         select(Post)
#         .join(Post.tags)
#         .where(Tag.name == "tutorial")
#     )
#     results = db.execute(stmt).scalars().all()
#     for post in results:
#         print(f"   - {post.title}")
#     
#     db.close()
# 
# query_many_to_many()


# ============================================
# PASO 8: Agregar/Eliminar Tags
# ============================================
# Descomenta la siguiente función y su llamada:

# def manage_tags():
#     """Demuestra agregar y eliminar tags"""
#     db = SessionLocal()
#     
#     # Obtener un post
#     post = db.execute(
#         select(Post).where(Post.title.contains("Python"))
#     ).scalar()
#     
#     print(f"\n🏷️ Tags actuales de '{post.title}': {[t.name for t in post.tags]}")
#     
#     # -----------------------------------------
#     # Agregar un tag
#     # -----------------------------------------
#     backend = db.execute(select(Tag).where(Tag.name == "backend")).scalar()
#     
#     if backend not in post.tags:
#         post.tags.append(backend)
#         print(f"✅ Tag 'backend' AGREGADO")
#     
#     # -----------------------------------------
#     # Eliminar un tag
#     # -----------------------------------------
#     for tag in post.tags[:]:  # Copia para iterar y modificar
#         if tag.name == "tutorial":
#             post.tags.remove(tag)
#             print(f"❌ Tag 'tutorial' ELIMINADO")
#             break
#     
#     db.commit()
#     
#     # Verificar cambios
#     db.refresh(post)
#     print(f"🏷️ Tags finales: {[t.name for t in post.tags]}")
#     
#     db.close()
# 
# manage_tags()


# ============================================
# RETO EXTRA (opcional)
# ============================================

# def get_or_create_tag(db, name: str):
#     """Obtiene un tag o lo crea si no existe"""
#     tag = db.execute(select(Tag).where(Tag.name == name)).scalar()
#     if not tag:
#         tag = Tag(name=name)
#         db.add(tag)
#         db.flush()  # Obtiene ID sin commit
#     return tag
# 
# def count_posts_per_tag():
#     """Cuenta posts por tag"""
#     db = SessionLocal()
#     
#     tags = db.execute(select(Tag)).scalars().all()
#     
#     print("\n📊 Posts por tag:")
#     for tag in tags:
#         print(f"   - {tag.name}: {len(tag.posts)} posts")
#     
#     db.close()
# 
# count_posts_per_tag()


print("\n=== Fin de la Práctica 02 ===")
