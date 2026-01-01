# ============================================
# Script de prueba
# ============================================
"""
Ejecuta este script para probar los repositorios.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Product, Category
# from base_repository import BaseRepository  # ← Descomentar
# from repositories import ProductRepository, CategoryRepository  # ← Descomentar

# Setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Crear tablas
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def main():
    """Prueba los repositorios"""
    db = SessionLocal()
    
    try:
        print("\n" + "="*50)
        print("PRUEBA DE REPOSITORIOS GENÉRICOS")
        print("="*50)
        
        # ============================================
        # Descomenta para probar:
        # ============================================
        
        # # Crear repositorios
        # category_repo = CategoryRepository(db)
        # product_repo = ProductRepository(db)
        # 
        # # --- Crear categorías ---
        # print("\n--- Creando categorías ---")
        # electronics = Category(name="Electronics", description="Electronic devices")
        # category_repo.add(electronics)
        # 
        # clothing = Category(name="Clothing", description="Apparel")
        # category_repo.add(clothing)
        # 
        # db.commit()
        # print(f"Categorías creadas: {category_repo.count()}")
        # 
        # # --- Crear productos ---
        # print("\n--- Creando productos ---")
        # products = [
        #     Product(name="Laptop", price=999.99, stock=10, category_id=electronics.id),
        #     Product(name="Phone", price=599.99, stock=25, category_id=electronics.id),
        #     Product(name="T-Shirt", price=29.99, stock=100, category_id=clothing.id),
        #     Product(name="Jeans", price=79.99, stock=50, category_id=clothing.id),
        # ]
        # product_repo.add_many(products)
        # db.commit()
        # print(f"Productos creados: {product_repo.count()}")
        # 
        # # --- Probar métodos genéricos (heredados) ---
        # print("\n--- Métodos genéricos de BaseRepository ---")
        # 
        # # get_by_id
        # product = product_repo.get_by_id(1)
        # print(f"get_by_id(1): {product}")
        # 
        # # get_all con paginación
        # all_products = product_repo.get_all(skip=0, limit=2)
        # print(f"get_all(limit=2): {len(all_products)} productos")
        # 
        # # exists
        # print(f"exists(1): {product_repo.exists(1)}")
        # print(f"exists(999): {product_repo.exists(999)}")
        # 
        # # filter_by
        # electronics_products = product_repo.filter_by(category_id=electronics.id)
        # print(f"filter_by(category_id={electronics.id}): {len(electronics_products)} productos")
        # 
        # # --- Probar métodos específicos ---
        # print("\n--- Métodos específicos de ProductRepository ---")
        # 
        # # get_by_category
        # by_category = product_repo.get_by_category(electronics.id)
        # print(f"get_by_category: {[p.name for p in by_category]}")
        # 
        # # get_in_stock
        # in_stock = product_repo.get_in_stock()
        # print(f"get_in_stock: {len(in_stock)} productos")
        # 
        # # search_by_name
        # found = product_repo.search_by_name("shirt")
        # print(f"search_by_name('shirt'): {[p.name for p in found]}")
        # 
        # # --- Probar CategoryRepository ---
        # print("\n--- Métodos específicos de CategoryRepository ---")
        # 
        # # get_by_name
        # cat = category_repo.get_by_name("Electronics")
        # print(f"get_by_name('Electronics'): {cat}")
        # 
        # # get_with_products (eager loading)
        # cat_with_products = category_repo.get_with_products(electronics.id)
        # print(f"get_with_products: {cat_with_products.name} tiene {len(cat_with_products.products)} productos")
        # 
        # # name_exists
        # print(f"name_exists('Electronics'): {category_repo.name_exists('Electronics')}")
        # print(f"name_exists('Food'): {category_repo.name_exists('Food')}")
        # 
        # # --- Eliminar ---
        # print("\n--- Eliminando ---")
        # deleted = product_repo.delete_by_id(1)
        # db.commit()
        # print(f"delete_by_id(1): {deleted}")
        # print(f"Productos restantes: {product_repo.count()}")
        
        print("\n✅ Descomentar código en main.py y repositories.py para probar")
        print("="*50)
        
    finally:
        db.close()


if __name__ == "__main__":
    main()
