# 🔍 Ejercicio 03: Query Parameters - Filtrado y Paginación

## 🎯 Objetivos

- Usar Query() para validación
- Implementar filtrado por múltiples criterios
- Crear paginación reutilizable
- Trabajar con listas de valores

---

## 📋 Instrucciones

### Paso 1: Configurar el Proyecto

```bash
cd starter
docker compose up --build
```

Abre http://localhost:8000/docs para ver Swagger UI.

---

### Paso 2: Query Parameters Básicos

Parámetros opcionales con valores por defecto.

**Abre `starter/main.py`** y descomenta la sección del Paso 2.

```python
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

✅ **Prueba**:
- `/items` → skip=0, limit=10
- `/items?skip=5&limit=20` → skip=5, limit=20

---

### Paso 3: Validación con Query()

Agrega restricciones y documentación.

**Descomenta** la sección del Paso 3.

```python
from fastapi import Query

@app.get("/products")
async def list_products(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100)
):
    return {"skip": skip, "limit": limit}
```

✅ **Prueba**: `limit=200` genera error 422.

---

### Paso 4: Filtrado

Parámetros opcionales para filtrar.

**Descomenta** la sección del Paso 4.

```python
@app.get("/products")
async def list_products(
    category: str | None = Query(default=None),
    min_price: float | None = Query(default=None, ge=0),
    max_price: float | None = Query(default=None, ge=0),
    search: str | None = Query(default=None, min_length=2)
):
    filters = {}
    if category:
        filters["category"] = category
    # ... aplicar filtros
```

---

### Paso 5: Paginación Completa

Retorna metadatos de paginación.

**Descomenta** la sección del Paso 5.

```python
@app.get("/products")
async def list_products(
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=50)
):
    offset = (page - 1) * per_page
    return {
        "page": page,
        "per_page": per_page,
        "total": 100,
        "pages": 10
    }
```

---

### Paso 6: Listas de Valores

Acepta múltiples valores del mismo parámetro.

**Descomenta** la sección del Paso 6.

```python
@app.get("/items")
async def list_items(
    tags: list[str] = Query(default=[])
):
    return {"tags": tags}
```

✅ **Prueba**: `/items?tags=new&tags=sale&tags=featured`

---

### Paso 7: Ordenamiento

Combina filtrado con ordenamiento.

**Descomenta** la sección del Paso 7.

```python
class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

@app.get("/products")
async def list_products(
    sort_by: str = Query(default="name"),
    order: SortOrder = Query(default=SortOrder.asc)
):
    return {"sort_by": sort_by, "order": order}
```

---

## ✅ Checklist de Verificación

- [ ] Query params con defaults funcionan
- [ ] Query() valida rangos numéricos
- [ ] Filtros opcionales se aplican correctamente
- [ ] Paginación retorna metadatos
- [ ] Listas de valores se reciben como array
- [ ] Ordenamiento con Enum funciona

---

## 🔗 Navegación

[← Ejercicio 02](../02-ejercicio-path-params/) | [Ejercicio 04 →](../04-ejercicio-combinados/)
