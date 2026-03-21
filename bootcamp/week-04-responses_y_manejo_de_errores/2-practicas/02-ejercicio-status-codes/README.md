# 📊 Ejercicio 02: Status Codes

## 🎯 Objetivo

Aprender a usar los códigos de estado HTTP correctos para cada operación CRUD y situación de error.

---

## 📋 Instrucciones

### Paso 1: Códigos de Éxito Básicos

Aprende los códigos más comunes para operaciones exitosas:

```python
# 200 OK - Respuesta exitosa por defecto (GET, PUT, PATCH)
# 201 Created - Recurso creado exitosamente (POST)
# 204 No Content - Éxito sin body (DELETE)

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item

@app.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(id: int):
    return None
```

**Abre `starter/main.py`** y descomenta la sección del Paso 1.

---

### Paso 2: Códigos de Error del Cliente

Aprende a retornar errores 4xx apropiados:

```python
# 400 Bad Request - Datos inválidos
# 404 Not Found - Recurso no existe
# 409 Conflict - Conflicto (duplicado)

if item_id not in items_db:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item {item_id} not found"
    )
```

**Descomenta** la sección del Paso 2.

---

### Paso 3: Status Code Dinámico

Aprende a cambiar el status code en runtime:

```python
# PUT puede crear (201) o actualizar (200)
@app.put("/items/{item_id}")
async def upsert_item(item_id: int, item: Item, response: Response):
    if item_id in items_db:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_201_CREATED
    return item
```

**Descomenta** la sección del Paso 3.

---

### Paso 4: Documentar Responses en OpenAPI

Documenta todos los códigos posibles:

```python
@app.get(
    "/items/{item_id}",
    responses={
        200: {"description": "Item encontrado"},
        404: {"description": "Item no existe"}
    }
)
```

**Descomenta** la sección del Paso 4.

---

## 🧪 Verificación

1. Ejecuta el servidor:
   ```bash
   docker compose up --build
   ```

2. Prueba en http://localhost:8000/docs:
   - `POST /tasks` → Debe retornar **201 Created**
   - `GET /tasks/1` → **200 OK**
   - `GET /tasks/999` → **404 Not Found**
   - `DELETE /tasks/1` → **204 No Content**
   - `PUT /tasks/1` → **200 OK** (actualizar) o **201 Created** (crear)
   - `POST /users` con email duplicado → **409 Conflict**

---

## ✅ Checklist

- [ ] POST retorna 201 Created
- [ ] DELETE retorna 204 No Content
- [ ] Recurso no encontrado retorna 404
- [ ] Email duplicado retorna 409 Conflict
- [ ] PUT retorna 200 o 201 según corresponda
- [ ] Responses documentados en OpenAPI

---

[← Anterior: Response Models](../01-ejercicio-response-models/) | [Siguiente: Errores →](../03-ejercicio-errores/)
