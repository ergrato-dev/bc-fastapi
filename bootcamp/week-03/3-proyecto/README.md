# 🛒 Proyecto: API de Catálogo de Productos

## 📋 Descripción

Construirás una API completa para gestionar un catálogo de productos con categorías, incluyendo búsqueda avanzada, filtrado, paginación y ordenamiento.

---

## 🎯 Objetivos

- ✅ Implementar CRUD completo de productos y categorías
- ✅ Crear búsqueda y filtrado avanzado
- ✅ Implementar paginación con metadatos
- ✅ Aplicar ordenamiento flexible
- ✅ Combinar múltiples tipos de parámetros

---

## 📦 Requisitos Funcionales

### 1. Categorías

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/categories` | Listar todas las categorías |
| GET | `/categories/{id}` | Obtener una categoría |
| POST | `/categories` | Crear categoría |
| PUT | `/categories/{id}` | Actualizar categoría |
| DELETE | `/categories/{id}` | Eliminar categoría |

### 2. Productos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/products` | Listar productos con filtros |
| GET | `/products/{id}` | Obtener un producto |
| POST | `/products` | Crear producto |
| PUT | `/products/{id}` | Actualizar producto |
| PATCH | `/products/{id}` | Actualizar parcialmente |
| DELETE | `/products/{id}` | Eliminar producto |

### 3. Filtrado y Búsqueda

El endpoint `GET /products` debe soportar:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `search` | string | Buscar en nombre y descripción |
| `category_id` | int | Filtrar por categoría |
| `min_price` | float | Precio mínimo |
| `max_price` | float | Precio máximo |
| `in_stock` | bool | Solo productos en stock |
| `tags` | list[str] | Filtrar por tags |

### 4. Paginación

| Parámetro | Default | Descripción |
|-----------|---------|-------------|
| `page` | 1 | Número de página |
| `per_page` | 10 | Items por página (máx 50) |

Respuesta paginada:
```json
{
  "items": [...],
  "total": 100,
  "page": 1,
  "per_page": 10,
  "pages": 10,
  "has_next": true,
  "has_prev": false
}
```

### 5. Ordenamiento

| Parámetro | Valores | Default |
|-----------|---------|---------|
| `sort_by` | name, price, created_at | name |
| `order` | asc, desc | asc |

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py           # Punto de entrada
├── routers/
│   ├── __init__.py
│   ├── categories.py # Rutas de categorías
│   └── products.py   # Rutas de productos
├── schemas.py        # Modelos Pydantic
├── database.py       # Base de datos simulada
├── dependencies.py   # Dependencias reutilizables
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## 🚀 Ejecución

```bash
cd starter
docker compose up --build
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs

---

## 📝 Instrucciones

1. **Completa `schemas.py`**: Define los modelos Pydantic
2. **Completa `dependencies.py`**: Crea dependencias reutilizables
3. **Completa `routers/categories.py`**: Implementa CRUD de categorías
4. **Completa `routers/products.py`**: Implementa CRUD con filtros

### Schemas Requeridos

```python
# schemas.py
class CategoryCreate(BaseModel):
    name: str
    description: str | None = None

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    category_id: int
    stock: int = 0
    tags: list[str] = []
```

### Dependencias Requeridas

```python
# dependencies.py
class PaginationParams:
    # page, per_page, offset

class ProductFilters:
    # search, category_id, min_price, max_price, in_stock, tags

class SortingParams:
    # sort_by, order
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| CRUD de categorías funcional | 15 |
| CRUD de productos funcional | 20 |
| Búsqueda por texto | 10 |
| Filtros (categoría, precio, stock) | 15 |
| Filtro por múltiples tags | 10 |
| Paginación con metadatos | 15 |
| Ordenamiento | 10 |
| Documentación OpenAPI | 5 |
| **Total** | **100** |

---

## 🔗 Recursos

- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)

---

[← Volver a Week-03](../README.md)
