"""
Base de Datos Simulada
======================

Datos en memoria para el proyecto.
"""

from datetime import datetime

# ============================================
# CATEGORÍAS
# ============================================

categories_db: dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Electronics",
        "description": "Electronic devices and accessories",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    2: {
        "id": 2,
        "name": "Books",
        "description": "Physical and digital books",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    3: {
        "id": 3,
        "name": "Clothing",
        "description": "Apparel and accessories",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    4: {
        "id": 4,
        "name": "Home & Garden",
        "description": "Home decor and garden supplies",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
}

next_category_id = 5

# ============================================
# PRODUCTOS
# ============================================

products_db: dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Laptop Pro 15",
        "description": "High-performance laptop with 16GB RAM",
        "price": 1299.99,
        "category_id": 1,
        "stock": 25,
        "tags": ["new", "featured", "bestseller"],
        "created_at": datetime(2024, 1, 15, 9, 0, 0)
    },
    2: {
        "id": 2,
        "name": "Wireless Mouse",
        "description": "Ergonomic wireless mouse with long battery",
        "price": 29.99,
        "category_id": 1,
        "stock": 150,
        "tags": ["sale", "popular"],
        "created_at": datetime(2024, 2, 1, 10, 0, 0)
    },
    3: {
        "id": 3,
        "name": "Python Crash Course",
        "description": "A hands-on, project-based introduction to programming",
        "price": 39.99,
        "category_id": 2,
        "stock": 75,
        "tags": ["bestseller", "programming"],
        "created_at": datetime(2024, 1, 20, 14, 0, 0)
    },
    4: {
        "id": 4,
        "name": "FastAPI Modern Guide",
        "description": "Complete guide to building APIs with FastAPI",
        "price": 49.99,
        "category_id": 2,
        "stock": 50,
        "tags": ["new", "programming", "web"],
        "created_at": datetime(2024, 3, 1, 8, 0, 0)
    },
    5: {
        "id": 5,
        "name": "Classic T-Shirt",
        "description": "100% cotton comfortable t-shirt",
        "price": 24.99,
        "category_id": 3,
        "stock": 200,
        "tags": ["popular", "basics"],
        "created_at": datetime(2024, 2, 15, 11, 0, 0)
    },
    6: {
        "id": 6,
        "name": "Desk Lamp LED",
        "description": "Adjustable LED desk lamp with dimmer",
        "price": 45.99,
        "category_id": 4,
        "stock": 80,
        "tags": ["new", "energy-efficient"],
        "created_at": datetime(2024, 2, 20, 16, 0, 0)
    },
    7: {
        "id": 7,
        "name": "Mechanical Keyboard",
        "description": "RGB mechanical keyboard with Cherry MX switches",
        "price": 149.99,
        "category_id": 1,
        "stock": 0,
        "tags": ["gaming", "premium"],
        "created_at": datetime(2024, 3, 5, 9, 0, 0)
    },
    8: {
        "id": 8,
        "name": "Garden Tools Set",
        "description": "Complete set of essential garden tools",
        "price": 79.99,
        "category_id": 4,
        "stock": 30,
        "tags": ["sale", "outdoor"],
        "created_at": datetime(2024, 3, 10, 10, 0, 0)
    },
}

next_product_id = 9


# ============================================
# HELPER FUNCTIONS
# ============================================

def get_next_category_id() -> int:
    """Obtener y incrementar ID de categoría"""
    global next_category_id
    current = next_category_id
    next_category_id += 1
    return current


def get_next_product_id() -> int:
    """Obtener y incrementar ID de producto"""
    global next_product_id
    current = next_product_id
    next_product_id += 1
    return current
