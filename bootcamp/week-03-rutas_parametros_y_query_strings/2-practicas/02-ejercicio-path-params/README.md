# 🔗 Ejercicio 02: Path Parameters con Validación

## 🎯 Objetivos

- Usar Path() para validación de parámetros
- Aplicar restricciones numéricas (gt, ge, lt, le)
- Usar Enum para valores fijos
- Capturar rutas con `/`

---

## 📋 Instrucciones

### Paso 1: Configurar el Proyecto

```bash
cd starter
docker compose up --build
```

Abre http://localhost:8000/docs para ver Swagger UI.

---

### Paso 2: Path Parameters Tipados

FastAPI convierte automáticamente los tipos.

**Abre `starter/main.py`** y descomenta la sección del Paso 2.

```python
@app.get("/items/{item_id}")
async def get_item(item_id: int):  # Convierte a int
    return {"item_id": item_id}
```

✅ **Prueba**:
- `/items/42` → `{"item_id": 42}` ✅
- `/items/abc` → Error 422 ✅

---

### Paso 3: Validación con Path()

Agrega restricciones y documentación.

**Descomenta** la sección del Paso 3.

```python
from fastapi import Path

@app.get("/products/{product_id}")
async def get_product(
    product_id: int = Path(
        ...,
        gt=0,        # Mayor que 0
        le=10000,    # Menor o igual a 10000
        title="Product ID",
        description="Unique product identifier"
    )
):
    return {"product_id": product_id}
```

✅ **Prueba**:
- `/products/0` → Error 422 (gt=0)
- `/products/10001` → Error 422 (le=10000)

---

### Paso 4: Validación de Strings

Aplica min_length, max_length y pattern.

**Descomenta** la sección del Paso 4.

```python
@app.get("/users/{username}")
async def get_user(
    username: str = Path(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"  # Solo alfanuméricos
    )
):
    return {"username": username}
```

✅ **Prueba**:
- `/users/ab` → Error (muy corto)
- `/users/john@doe` → Error (carácter inválido)

---

### Paso 5: Enum para Valores Fijos

Restringe a valores predefinidos.

**Descomenta** la sección del Paso 5.

```python
from enum import Enum

class Status(str, Enum):
    pending = "pending"
    active = "active"
    completed = "completed"

@app.get("/orders/{status}")
async def get_orders_by_status(status: Status):
    return {"status": status.value}
```

✅ **Prueba**: Swagger muestra dropdown con opciones.

---

### Paso 6: Múltiples Path Parameters

Combina varios parámetros en la ruta.

**Descomenta** la sección del Paso 6.

```python
@app.get("/users/{user_id}/posts/{post_id}")
async def get_user_post(
    user_id: int = Path(..., gt=0),
    post_id: int = Path(..., gt=0)
):
    return {"user_id": user_id, "post_id": post_id}
```

---

### Paso 7: Capturar Rutas con /

Usa `:path` para rutas de archivos.

**Descomenta** la sección del Paso 7.

```python
@app.get("/files/{file_path:path}")
async def get_file(file_path: str):
    return {"file_path": file_path}
```

✅ **Prueba**: `/files/docs/images/photo.png` funciona.

---

## ✅ Checklist de Verificación

- [ ] Tipos se convierten automáticamente
- [ ] Path() valida números (gt, le, etc.)
- [ ] Path() valida strings (min_length, pattern)
- [ ] Enum restringe a valores válidos
- [ ] Múltiples path params funcionan
- [ ] :path captura rutas con /

---

## 🔗 Navegación

[← Ejercicio 01](../01-ejercicio-rutas/) | [Ejercicio 03 →](../03-ejercicio-query-params/)
