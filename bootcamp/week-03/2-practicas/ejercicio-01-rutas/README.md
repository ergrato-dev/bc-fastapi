# 🛣️ Ejercicio 01: Rutas CRUD Básicas

## 🎯 Objetivos

- Crear rutas con diferentes métodos HTTP
- Usar status codes apropiados
- Organizar rutas con APIRouter
- Entender el orden de rutas

---

## 📋 Instrucciones

### Paso 1: Configurar el Proyecto

```bash
cd starter
docker compose up --build
```

Abre http://localhost:8000/docs para ver Swagger UI.

---

### Paso 2: Crear Rutas GET

El método GET se usa para obtener recursos.

**Abre `starter/main.py`** y descomenta la sección del Paso 2.

```python
# Ejemplo de GET
@app.get("/items")
async def list_items():
    return [{"id": 1, "name": "Item 1"}]

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"id": item_id, "name": f"Item {item_id}"}
```

✅ **Verifica**: GET `/items` y GET `/items/1` funcionan en Swagger.

---

### Paso 3: Crear Rutas POST

POST se usa para crear nuevos recursos.

**Descomenta** la sección del Paso 3 en `main.py`.

```python
# status_code=201 indica "Created"
@app.post("/items", status_code=201)
async def create_item(item: dict):
    return {"id": 1, **item}
```

✅ **Verifica**: POST `/items` retorna status 201.

---

### Paso 4: Crear Rutas PUT y PATCH

- PUT: Reemplaza el recurso completo
- PATCH: Actualiza parcialmente

**Descomenta** la sección del Paso 4.

```python
@app.put("/items/{item_id}")
async def replace_item(item_id: int, item: dict):
    return {"id": item_id, **item}

@app.patch("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"id": item_id, "updated": True, **item}
```

---

### Paso 5: Crear Ruta DELETE

DELETE elimina recursos. Usa status 204 (No Content).

**Descomenta** la sección del Paso 5.

```python
@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    return None  # 204 no retorna body
```

---

### Paso 6: Orden de Rutas

Las rutas fijas deben ir ANTES de las dinámicas.

**Descomenta** la sección del Paso 6.

```python
# ✅ CORRECTO: ruta fija primero
@app.get("/users/me")
async def get_current_user():
    return {"user": "current"}

# Después la ruta dinámica
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}
```

✅ **Verifica**: `/users/me` no interpreta "me" como user_id.

---

### Paso 7: Usar APIRouter

Organiza rutas en módulos separados.

**Descomenta** la sección del Paso 7.

```python
from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
async def list_products():
    return []

# En main.py
app.include_router(router)
```

---

## ✅ Checklist de Verificación

- [ ] GET retorna lista y elemento individual
- [ ] POST retorna 201 Created
- [ ] PUT y PATCH actualizan correctamente
- [ ] DELETE retorna 204 No Content
- [ ] Rutas fijas funcionan antes que dinámicas
- [ ] APIRouter organiza las rutas

---

## 🔗 Navegación

[← Volver a Prácticas](../README.md) | [Ejercicio 02 →](../ejercicio-02-path-params/)
