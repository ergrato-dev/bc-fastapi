# 🔗 Path Parameters (Parámetros de Ruta)

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Definir path parameters con tipos específicos
- ✅ Validar parámetros con Path()
- ✅ Usar Enum para valores restringidos
- ✅ Manejar múltiples path parameters

---

## 📚 Contenido

![Anatomía de una URL](../0-assets/02-url-anatomy.svg)

### 1. Path Parameters Básicos

Los path parameters son variables en la URL que identifican recursos:

```python
from fastapi import FastAPI

app = FastAPI()

# Path parameter básico
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    El parámetro user_id se extrae de la URL.
    FastAPI convierte automáticamente a int.
    """
    return {"user_id": user_id}

# Múltiples path parameters
@app.get("/users/{user_id}/posts/{post_id}")
async def get_user_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

#### Conversión Automática de Tipos

```python
from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

# int - Convierte string a entero
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}  # /items/42 → {"item_id": 42}

# float - Convierte a decimal
@app.get("/prices/{price}")
async def get_price(price: float):
    return {"price": price}  # /prices/19.99 → {"price": 19.99}

# str - Mantiene como string (default)
@app.get("/files/{filename}")
async def get_file(filename: str):
    return {"filename": filename}

# UUID - Valida formato UUID
@app.get("/orders/{order_id}")
async def get_order(order_id: UUID):
    return {"order_id": str(order_id)}
    # /orders/550e8400-e29b-41d4-a716-446655440000 ✅
    # /orders/invalid-uuid ❌ Error 422
```

---

### 2. Validación con Path()

`Path()` permite agregar validaciones y metadatos:

```python
from fastapi import FastAPI, Path

app = FastAPI()

# Validación numérica
@app.get("/items/{item_id}")
async def get_item(
    item_id: int = Path(
        ...,  # ... significa requerido
        title="Item ID",
        description="The unique identifier of the item",
        gt=0,  # greater than 0
        le=10000,  # less than or equal to 10000
        examples=[1, 42, 100]
    )
):
    return {"item_id": item_id}

# Validación de string
@app.get("/users/{username}")
async def get_user(
    username: str = Path(
        ...,
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_]+$",  # Solo alfanuméricos y _
        examples=["john_doe", "alice123"]
    )
):
    return {"username": username}
```

#### Opciones de Validación Numérica

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `gt` | Greater than (mayor que) | `gt=0` |
| `ge` | Greater or equal (mayor o igual) | `ge=1` |
| `lt` | Less than (menor que) | `lt=100` |
| `le` | Less or equal (menor o igual) | `le=99` |

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/products/{product_id}/quantity/{qty}")
async def get_product_quantity(
    product_id: int = Path(..., gt=0, description="Product ID"),
    qty: int = Path(..., ge=1, le=100, description="Quantity (1-100)")
):
    return {
        "product_id": product_id,
        "quantity": qty
    }
```

---

### 3. Enum para Valores Restringidos

Usa `Enum` cuando el parámetro debe ser uno de varios valores fijos:

```python
from enum import Enum
from fastapi import FastAPI

# Definir Enum con valores permitidos
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Solo acepta: alexnet, resnet, lenet
    Otros valores devuelven 422
    """
    if model_name is ModelName.alexnet:
        return {"model": model_name, "message": "Deep Learning FTW!"}
    
    return {"model": model_name, "message": "Using a standard model"}

@app.get("/orders/{order_id}/status/{status}")
async def update_order_status(order_id: int, status: OrderStatus):
    return {
        "order_id": order_id,
        "new_status": status.value  # .value obtiene el string
    }
```

#### Beneficios de Enum

1. **Documentación automática** - Swagger muestra opciones válidas
2. **Validación automática** - Rechaza valores no definidos
3. **Autocompletado** - IDEs sugieren valores válidos
4. **Type safety** - El linter detecta errores

---

### 4. Rutas con Paths que Contienen /

Para aceptar paths completos (ej: rutas de archivos):

```python
from fastapi import FastAPI

app = FastAPI()

# Usando :path para capturar rutas completas
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    file_path puede contener /
    
    Ejemplos:
    - /files/document.txt
    - /files/folder/subfolder/image.png
    """
    return {"file_path": file_path}

# Sin :path, / en el path causaría 404
@app.get("/download/{filename}")  # Solo captura hasta el primer /
async def download_file(filename: str):
    return {"filename": filename}
```

---

### 5. Orden de Rutas

El orden importa cuando hay rutas similares:

```python
from fastapi import FastAPI

app = FastAPI()

# ⚠️ ORDEN CORRECTO

# 1. Rutas estáticas primero
@app.get("/users/me")
async def get_current_user():
    return {"user": "current"}

@app.get("/users/admin")
async def get_admin_user():
    return {"user": "admin"}

# 2. Rutas dinámicas después
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

# Si /users/{user_id} estuviera primero,
# /users/me interpretaría "me" como user_id
```

#### Ejemplo con Múltiples Niveles

```python
from fastapi import FastAPI

app = FastAPI()

# Específico → General

@app.get("/items/special/featured")
async def get_featured_items():
    return {"items": "featured"}

@app.get("/items/special/{category}")
async def get_special_by_category(category: str):
    return {"category": category}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
```

---

### 6. Alias para Path Parameters

Puedes usar un nombre diferente en la función:

```python
from fastapi import FastAPI, Path

app = FastAPI()

# El parámetro en URL es item-id (con guión)
# Pero en Python usamos item_id (con guión bajo)
@app.get("/items/{item-id}")
async def get_item(
    item_id: int = Path(..., alias="item-id")
):
    return {"item_id": item_id}

# También útil para palabras reservadas
@app.get("/classes/{class}")
async def get_class(
    class_name: str = Path(..., alias="class")
):
    return {"class": class_name}
```

---

### 7. Ejemplo Completo: CRUD con Path Parameters

```python
from fastapi import FastAPI, Path, HTTPException, status
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# Enums
class Category(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    books = "books"

# Schemas
class Product(BaseModel):
    name: str
    price: float
    category: Category

# Base de datos simulada
products_db: dict[int, dict] = {
    1: {"name": "Laptop", "price": 999.99, "category": "electronics"},
    2: {"name": "T-Shirt", "price": 29.99, "category": "clothing"},
}

# GET - Producto por ID
@app.get("/products/{product_id}")
async def get_product(
    product_id: int = Path(
        ...,
        gt=0,
        title="Product ID",
        description="Unique product identifier",
        examples=[1, 2]
    )
):
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found"
        )
    return products_db[product_id]

# GET - Productos por categoría
@app.get("/categories/{category}/products")
async def get_products_by_category(category: Category):
    filtered = {
        pid: product 
        for pid, product in products_db.items()
        if product["category"] == category.value
    }
    return {"category": category, "products": filtered}

# PUT - Actualizar producto
@app.put("/products/{product_id}")
async def update_product(
    product_id: int = Path(..., gt=0),
    product: Product = ...
):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    products_db[product_id] = product.model_dump()
    return {"message": "Updated", "product": products_db[product_id]}

# DELETE - Eliminar producto
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int = Path(..., gt=0)
):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    del products_db[product_id]
    return None
```

---

## 📝 Resumen

| Concepto | Uso |
|----------|-----|
| `{param}` | Definir path parameter |
| `param: int` | Tipado automático |
| `Path()` | Validación y metadatos |
| `Enum` | Valores restringidos |
| `:path` | Capturar rutas con / |
| `alias` | Nombre alternativo |

---

## ✅ Checklist de Verificación

- [ ] Definir path parameters tipados
- [ ] Usar Path() para validación numérica
- [ ] Crear Enums para valores fijos
- [ ] Ordenar rutas correctamente
- [ ] Manejar errores 404

---

## 🔗 Recursos Adicionales

- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Path Parameters Validation](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/)

---

[← Rutas Básicas](01-rutas-basicas.md) | [Query Parameters →](03-query-parameters.md)
