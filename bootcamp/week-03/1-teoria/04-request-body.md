# 📦 Request Body y Combinación de Parámetros

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Combinar path, query y body parameters
- ✅ Usar Body() para configuración avanzada
- ✅ Trabajar con Form data
- ✅ Manejar File uploads
- ✅ Entender la prioridad de parámetros

---

## 📚 Contenido

### 1. Combinando Tipos de Parámetros

FastAPI distingue automáticamente entre diferentes fuentes:

```python
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class ItemUpdate(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.put("/items/{item_id}")
async def update_item(
    # Path parameter - de la URL
    item_id: int = Path(..., gt=0),
    
    # Query parameters - después de ?
    notify: bool = Query(default=False),
    
    # Body - del JSON en el request
    item: ItemUpdate = ...
):
    """
    PUT /items/42?notify=true
    Body: {"name": "New Name", "price": 99.99}
    
    FastAPI detecta automáticamente:
    - item_id → path (está en la ruta)
    - notify → query (tipo simple, no en ruta)
    - item → body (modelo Pydantic)
    """
    return {
        "item_id": item_id,
        "notify": notify,
        "item": item.model_dump()
    }
```

#### Reglas de Detección Automática

| Tipo de Parámetro | FastAPI lo detecta cuando... |
|-------------------|------------------------------|
| **Path** | Nombre aparece en la ruta `{param}` |
| **Query** | Tipo simple (int, str, bool, float) no en ruta |
| **Body** | Modelo Pydantic |

---

### 2. Body() para Configuración

Usa `Body()` para ajustar el comportamiento del body:

```python
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

# Body con embed=True
@app.post("/items")
async def create_item(
    item: Item = Body(..., embed=True)
):
    """
    Sin embed=True, espera:
    {"name": "...", "price": ...}
    
    Con embed=True, espera:
    {"item": {"name": "...", "price": ...}}
    """
    return item

# Múltiples bodies
class User(BaseModel):
    username: str
    email: str

@app.post("/orders")
async def create_order(
    item: Item,
    user: User
):
    """
    Espera ambos modelos en el body:
    {
        "item": {"name": "...", "price": ...},
        "user": {"username": "...", "email": "..."}
    }
    """
    return {"item": item, "user": user}
```

#### Body con Valores Singulares

```python
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    # Valor singular en el body
    importance: int = Body(
        ...,
        gt=0,
        le=10,
        description="Priority level (1-10)"
    )
):
    """
    Espera:
    {
        "item": {"name": "...", "price": ...},
        "importance": 5
    }
    """
    return {
        "item_id": item_id,
        "item": item,
        "importance": importance
    }
```

---

### 3. Form Data

Para datos de formularios HTML (`application/x-www-form-urlencoded`):

```python
from fastapi import FastAPI, Form

app = FastAPI()

# Formulario de login típico
@app.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(..., min_length=8)
):
    """
    Recibe datos de formulario, no JSON.
    
    Content-Type: application/x-www-form-urlencoded
    Body: username=john&password=secret123
    """
    return {"username": username, "logged_in": True}

# Formulario con campos opcionales
@app.post("/contact")
async def contact_form(
    name: str = Form(..., min_length=2),
    email: str = Form(...),
    message: str = Form(..., min_length=10),
    subscribe: bool = Form(default=False)
):
    return {
        "name": name,
        "email": email,
        "message": message,
        "subscribed": subscribe
    }
```

> ⚠️ **Importante**: Para usar `Form`, necesitas instalar `python-multipart`:
> ```bash
> uv add python-multipart
> ```

---

### 4. File Uploads

Para subir archivos:

```python
from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()

# Upload simple con bytes
@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File(description="File as bytes")]
):
    """
    Lee el archivo completo en memoria.
    Útil para archivos pequeños.
    """
    return {"file_size": len(file)}

# Upload con UploadFile (recomendado)
@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile
):
    """
    UploadFile es más eficiente:
    - Usa spooled file (disco para archivos grandes)
    - Acceso a metadatos
    - Operaciones async
    """
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size
    }

# Múltiples archivos
@app.post("/uploadfiles/")
async def create_upload_files(
    files: list[UploadFile]
):
    """
    Subir múltiples archivos a la vez.
    """
    return {
        "filenames": [file.filename for file in files],
        "count": len(files)
    }
```

#### UploadFile: Propiedades y Métodos

```python
from fastapi import FastAPI, UploadFile, HTTPException
import aiofiles

app = FastAPI()

ALLOWED_TYPES = ["image/jpeg", "image/png", "image/gif"]
MAX_SIZE = 5 * 1024 * 1024  # 5MB

@app.post("/upload/image")
async def upload_image(file: UploadFile):
    # Validar tipo de archivo
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"File type not allowed. Allowed: {ALLOWED_TYPES}"
        )
    
    # Leer contenido
    content = await file.read()
    
    # Validar tamaño
    if len(content) > MAX_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max size: {MAX_SIZE} bytes"
        )
    
    # Guardar archivo
    file_path = f"uploads/{file.filename}"
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(content)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "saved_to": file_path
    }

# Métodos de UploadFile
@app.post("/upload/process")
async def process_file(file: UploadFile):
    # Leer todo el contenido
    content = await file.read()
    
    # Volver al inicio del archivo
    await file.seek(0)
    
    # Leer por chunks (para archivos grandes)
    chunks = []
    while chunk := await file.read(1024):  # 1KB chunks
        chunks.append(chunk)
    
    # Cerrar el archivo
    await file.close()
    
    return {"processed": True}
```

---

### 5. Combinando Form y File

```python
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post("/products")
async def create_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(..., gt=0),
    image: UploadFile = File(...)
):
    """
    Crear producto con imagen.
    Content-Type: multipart/form-data
    """
    return {
        "name": name,
        "description": description,
        "price": price,
        "image_filename": image.filename
    }

# Con imagen opcional
@app.post("/profiles")
async def create_profile(
    username: str = Form(...),
    bio: str = Form(default=""),
    avatar: UploadFile | None = File(default=None)
):
    result = {
        "username": username,
        "bio": bio,
        "has_avatar": avatar is not None
    }
    
    if avatar:
        result["avatar_name"] = avatar.filename
    
    return result
```

---

### 6. Ejemplo Completo: API de Productos

```python
from fastapi import FastAPI, Path, Query, Body, File, Form, UploadFile, HTTPException
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

# Enums
class Category(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    books = "books"

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

# Schemas
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(..., gt=0)
    category: Category

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    category: Category | None = None

# Base de datos simulada
products_db: dict[int, dict] = {}
next_id = 1

# CREATE - POST con body JSON
@app.post("/products", status_code=201)
async def create_product(product: ProductCreate):
    global next_id
    product_dict = product.model_dump()
    product_dict["id"] = next_id
    products_db[next_id] = product_dict
    next_id += 1
    return product_dict

# READ - GET con path y query params
@app.get("/products")
async def list_products(
    category: Category | None = Query(default=None),
    min_price: float | None = Query(default=None, ge=0),
    max_price: float | None = Query(default=None, ge=0),
    search: str | None = Query(default=None, min_length=2),
    sort_by: str = Query(default="name"),
    order: SortOrder = Query(default=SortOrder.asc),
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=50)
):
    # Filtrar
    result = list(products_db.values())
    
    if category:
        result = [p for p in result if p["category"] == category]
    if min_price is not None:
        result = [p for p in result if p["price"] >= min_price]
    if max_price is not None:
        result = [p for p in result if p["price"] <= max_price]
    if search:
        result = [p for p in result if search.lower() in p["name"].lower()]
    
    # Ordenar
    if sort_by in ["name", "price"]:
        result.sort(key=lambda x: x[sort_by], reverse=(order == SortOrder.desc))
    
    # Paginar
    total = len(result)
    start = (page - 1) * per_page
    result = result[start:start + per_page]
    
    return {
        "products": result,
        "total": total,
        "page": page,
        "per_page": per_page
    }

# READ ONE - GET con path param
@app.get("/products/{product_id}")
async def get_product(
    product_id: int = Path(..., gt=0)
):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

# UPDATE - PATCH con path + body
@app.patch("/products/{product_id}")
async def update_product(
    product_id: int = Path(..., gt=0),
    product: ProductUpdate = ...
):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_data = product.model_dump(exclude_unset=True)
    products_db[product_id].update(update_data)
    
    return products_db[product_id]

# DELETE - DELETE con path param
@app.delete("/products/{product_id}", status_code=204)
async def delete_product(
    product_id: int = Path(..., gt=0)
):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    del products_db[product_id]
    return None

# UPLOAD IMAGE - Form + File
@app.post("/products/{product_id}/image")
async def upload_product_image(
    product_id: int = Path(..., gt=0),
    image: UploadFile = File(...),
    alt_text: str = Form(default="")
):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Validar tipo
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Simular guardado
    products_db[product_id]["image"] = {
        "filename": image.filename,
        "alt_text": alt_text
    }
    
    return {
        "message": "Image uploaded",
        "product_id": product_id,
        "image": products_db[product_id]["image"]
    }
```

---

## 📝 Resumen

| Fuente | Cómo usar | Ejemplo |
|--------|-----------|---------|
| **Path** | En la ruta | `{item_id}` |
| **Query** | Tipo simple | `skip: int = 0` |
| **Body** | Modelo Pydantic | `item: Item` |
| **Form** | `Form()` | `username: str = Form(...)` |
| **File** | `File()` / `UploadFile` | `file: UploadFile` |

---

## ✅ Checklist de Verificación

- [ ] Combinar path, query y body
- [ ] Usar Body() con embed
- [ ] Manejar Form data
- [ ] Subir archivos con UploadFile
- [ ] Combinar Form y File
- [ ] Validar archivos (tipo, tamaño)

---

## 🔗 Recursos Adicionales

- [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI Request Files](https://fastapi.tiangolo.com/tutorial/request-files/)
- [FastAPI Form Data](https://fastapi.tiangolo.com/tutorial/request-forms/)

---

[← Query Parameters](03-query-parameters.md) | [Parámetros Avanzados →](05-parametros-avanzados.md)
