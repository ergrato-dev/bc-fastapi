# 🔍 Query Parameters (Parámetros de Consulta)

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Definir query parameters opcionales y requeridos
- ✅ Establecer valores por defecto
- ✅ Validar con Query()
- ✅ Implementar paginación y filtrado
- ✅ Trabajar con listas de valores

---

## 📚 Contenido

### 1. Query Parameters Básicos

Los query parameters van después de `?` en la URL:

```
/items?skip=0&limit=10&search=laptop
```

```python
from fastapi import FastAPI

app = FastAPI()

# Query parameters con valores por defecto
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    """
    skip y limit son opcionales (tienen default).
    
    Ejemplos:
    - /items → skip=0, limit=10
    - /items?skip=5 → skip=5, limit=10
    - /items?limit=20 → skip=0, limit=20
    - /items?skip=10&limit=5 → skip=10, limit=5
    """
    return {"skip": skip, "limit": limit}

# Query parameter requerido (sin default)
@app.get("/search")
async def search(q: str):
    """
    q es REQUERIDO porque no tiene valor por defecto.
    
    - /search?q=laptop ✅
    - /search ❌ Error 422
    """
    return {"query": q}
```

---

### 2. Parámetros Opcionales con None

Usa `None` como default para parámetros verdaderamente opcionales:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
async def list_products(
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    in_stock: bool | None = None
):
    """
    Todos los parámetros son opcionales.
    Solo se aplican filtros si se proporcionan.
    """
    filters = {}
    
    if category:
        filters["category"] = category
    if min_price is not None:
        filters["min_price"] = min_price
    if max_price is not None:
        filters["max_price"] = max_price
    if in_stock is not None:
        filters["in_stock"] = in_stock
    
    return {"applied_filters": filters}
```

---

### 3. Validación con Query()

`Query()` agrega validación y documentación:

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def list_items(
    # String con validación
    q: str | None = Query(
        default=None,
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9\s]+$",
        title="Search Query",
        description="Search term for filtering items",
        examples=["laptop", "gaming mouse"]
    ),
    
    # Número con rango
    skip: int = Query(
        default=0,
        ge=0,
        description="Number of items to skip"
    ),
    
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Maximum items to return (1-100)"
    ),
    
    # Requerido explícitamente
    sort_by: str = Query(
        ...,  # ... = requerido
        description="Field to sort by"
    )
):
    return {
        "query": q,
        "skip": skip,
        "limit": limit,
        "sort_by": sort_by
    }
```

#### Opciones de Query()

| Parámetro | Descripción |
|-----------|-------------|
| `default` | Valor por defecto |
| `min_length` | Longitud mínima (strings) |
| `max_length` | Longitud máxima (strings) |
| `pattern` | Regex para validar (strings) |
| `gt`, `ge`, `lt`, `le` | Comparaciones numéricas |
| `title` | Título para documentación |
| `description` | Descripción en OpenAPI |
| `examples` | Ejemplos para Swagger |
| `deprecated` | Marcar como obsoleto |
| `alias` | Nombre alternativo en URL |

---

### 4. Listas de Valores

Para aceptar múltiples valores del mismo parámetro:

```python
from fastapi import FastAPI, Query

app = FastAPI()

# Lista de valores
@app.get("/items")
async def list_items(
    tags: list[str] = Query(
        default=[],
        description="Filter by tags"
    )
):
    """
    Acepta múltiples valores:
    /items?tags=electronics&tags=sale&tags=new
    
    Result: tags = ["electronics", "sale", "new"]
    """
    return {"tags": tags}

# Lista requerida con al menos un elemento
@app.get("/reports")
async def generate_report(
    ids: list[int] = Query(
        ...,  # Requerido
        min_length=1,  # Al menos un elemento
        description="IDs to include in report"
    )
):
    """
    /reports?ids=1&ids=2&ids=3
    """
    return {"ids": ids}

# Lista con valores por defecto
@app.get("/products")
async def list_products(
    categories: list[str] = Query(
        default=["all"],
        description="Categories to filter"
    )
):
    return {"categories": categories}
```

---

### 5. Paginación

Patrón común para paginar resultados:

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# Schema para respuesta paginada
class PaginatedResponse(BaseModel):
    items: list[dict]
    total: int
    page: int
    per_page: int
    pages: int
    has_next: bool
    has_prev: bool

# Base de datos simulada
fake_db = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]

@app.get("/items", response_model=PaginatedResponse)
async def list_items(
    page: int = Query(default=1, ge=1, description="Page number"),
    per_page: int = Query(default=10, ge=1, le=100, description="Items per page")
):
    """
    Paginación basada en página.
    
    - /items?page=1&per_page=10 → Items 1-10
    - /items?page=2&per_page=10 → Items 11-20
    """
    total = len(fake_db)
    pages = (total + per_page - 1) // per_page  # Ceiling division
    
    start = (page - 1) * per_page
    end = start + per_page
    items = fake_db[start:end]
    
    return PaginatedResponse(
        items=items,
        total=total,
        page=page,
        per_page=per_page,
        pages=pages,
        has_next=page < pages,
        has_prev=page > 1
    )
```

#### Paginación con Offset/Limit

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def list_items(
    offset: int = Query(default=0, ge=0, description="Number of items to skip"),
    limit: int = Query(default=20, ge=1, le=100, description="Number of items to return")
):
    """
    Paginación basada en offset.
    
    - /items?offset=0&limit=20 → Items 1-20
    - /items?offset=20&limit=20 → Items 21-40
    """
    items = fake_db[offset:offset + limit]
    
    return {
        "items": items,
        "offset": offset,
        "limit": limit,
        "total": len(fake_db)
    }
```

---

### 6. Filtrado y Ordenamiento

```python
from fastapi import FastAPI, Query
from enum import Enum

app = FastAPI()

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class SortField(str, Enum):
    name = "name"
    price = "price"
    created_at = "created_at"

# Base de datos simulada
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "electronics"},
    {"id": 2, "name": "Mouse", "price": 29.99, "category": "electronics"},
    {"id": 3, "name": "T-Shirt", "price": 19.99, "category": "clothing"},
    {"id": 4, "name": "Book", "price": 14.99, "category": "books"},
]

@app.get("/products")
async def list_products(
    # Filtros
    category: str | None = Query(default=None, description="Filter by category"),
    min_price: float | None = Query(default=None, ge=0, description="Minimum price"),
    max_price: float | None = Query(default=None, ge=0, description="Maximum price"),
    search: str | None = Query(default=None, min_length=2, description="Search in name"),
    
    # Ordenamiento
    sort_by: SortField = Query(default=SortField.name, description="Field to sort by"),
    order: SortOrder = Query(default=SortOrder.asc, description="Sort order"),
    
    # Paginación
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=50)
):
    """
    Filtrado, ordenamiento y paginación combinados.
    
    Ejemplos:
    - /products?category=electronics
    - /products?min_price=20&max_price=100
    - /products?search=laptop&sort_by=price&order=desc
    - /products?page=2&per_page=5
    """
    result = products.copy()
    
    # Aplicar filtros
    if category:
        result = [p for p in result if p["category"] == category]
    
    if min_price is not None:
        result = [p for p in result if p["price"] >= min_price]
    
    if max_price is not None:
        result = [p for p in result if p["price"] <= max_price]
    
    if search:
        result = [p for p in result if search.lower() in p["name"].lower()]
    
    # Ordenar
    reverse = order == SortOrder.desc
    result.sort(key=lambda x: x[sort_by.value], reverse=reverse)
    
    # Paginar
    total = len(result)
    start = (page - 1) * per_page
    end = start + per_page
    result = result[start:end]
    
    return {
        "products": result,
        "total": total,
        "page": page,
        "per_page": per_page,
        "filters": {
            "category": category,
            "min_price": min_price,
            "max_price": max_price,
            "search": search
        },
        "sorting": {
            "field": sort_by,
            "order": order
        }
    }
```

---

### 7. Alias y Deprecación

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def list_items(
    # Alias para nombres con guiones o caracteres especiales
    item_type: str | None = Query(
        default=None,
        alias="item-type",  # En URL: ?item-type=electronics
        description="Type of item"
    ),
    
    # Parámetro deprecado
    old_filter: str | None = Query(
        default=None,
        deprecated=True,  # Aparece tachado en docs
        description="DEPRECATED: Use 'category' instead"
    ),
    
    category: str | None = Query(default=None)
):
    return {
        "item_type": item_type,
        "category": category or old_filter
    }
```

---

### 8. Conversión de Booleanos

FastAPI convierte strings a booleanos automáticamente:

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def list_items(
    active: bool = Query(default=True),
    featured: bool | None = Query(default=None)
):
    """
    Valores que se convierten a True:
    - ?active=true
    - ?active=True
    - ?active=1
    - ?active=yes
    - ?active=on
    
    Valores que se convierten a False:
    - ?active=false
    - ?active=False
    - ?active=0
    - ?active=no
    - ?active=off
    """
    return {"active": active, "featured": featured}
```

---

## 📝 Resumen

| Concepto | Ejemplo |
|----------|---------|
| Opcional con default | `skip: int = 0` |
| Opcional None | `q: str \| None = None` |
| Requerido | `q: str` o `Query(...)` |
| Validación | `Query(min_length=3)` |
| Lista | `tags: list[str] = Query([])` |
| Paginación | `page`, `per_page` o `offset`, `limit` |
| Alias | `Query(alias="item-type")` |

---

## ✅ Checklist de Verificación

- [ ] Definir parámetros opcionales con defaults
- [ ] Usar Query() para validación
- [ ] Implementar paginación
- [ ] Implementar filtrado
- [ ] Implementar ordenamiento
- [ ] Trabajar con listas de valores

---

## 🔗 Recursos Adicionales

- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Query Parameters Validation](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)

---

[← Path Parameters](02-path-parameters.md) | [Request Body →](04-request-body.md)
