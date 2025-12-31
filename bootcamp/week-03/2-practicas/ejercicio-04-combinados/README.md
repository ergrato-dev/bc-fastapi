# 🔀 Ejercicio 04: Parámetros Combinados

## 🎯 Objetivos

- Combinar path, query y body parameters
- Usar Header() y Cookie()
- Crear dependencias reutilizables
- Aplicar autenticación básica

---

## 📋 Instrucciones

### Paso 1: Configurar el Proyecto

```bash
cd starter
docker compose up --build
```

Abre http://localhost:8000/docs para ver Swagger UI.

---

### Paso 2: Combinar Path y Query

Usa ambos tipos en el mismo endpoint.

**Abre `starter/main.py`** y descomenta la sección del Paso 2.

```python
@app.get("/users/{user_id}/posts")
async def get_user_posts(
    user_id: int = Path(..., gt=0),
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=50)
):
    return {"user_id": user_id, "page": page}
```

---

### Paso 3: Path, Query y Body

Tres fuentes de parámetros.

**Descomenta** la sección del Paso 3.

```python
@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., gt=0),          # De la URL
    notify: bool = Query(default=False),      # Query string
    item: ItemUpdate = ...                    # Body JSON
):
    return {"item_id": item_id, "notify": notify, "item": item}
```

---

### Paso 4: Headers

Leer encabezados HTTP.

**Descomenta** la sección del Paso 4.

```python
from fastapi import Header

@app.get("/info")
async def get_info(
    user_agent: str | None = Header(default=None),
    x_token: str | None = Header(default=None)
):
    return {"user_agent": user_agent, "token": x_token}
```

---

### Paso 5: Cookies

Leer cookies del cliente.

**Descomenta** la sección del Paso 5.

```python
from fastapi import Cookie

@app.get("/session")
async def get_session(
    session_id: str | None = Cookie(default=None)
):
    return {"session_id": session_id}
```

---

### Paso 6: Dependencias Reutilizables

Crea lógica compartida entre endpoints.

**Descomenta** la sección del Paso 6.

```python
from fastapi import Depends

async def pagination_params(
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=50)
):
    return {"page": page, "per_page": per_page}

@app.get("/items")
async def list_items(pagination: dict = Depends(pagination_params)):
    return pagination
```

---

### Paso 7: Autenticación con Dependencias

Protege endpoints con autenticación.

**Descomenta** la sección del Paso 7.

```python
async def get_current_user(
    authorization: str = Header(...)
) -> dict:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401)
    # ... verificar token
    return {"user_id": 1, "role": "user"}

@app.get("/me")
async def get_me(user: dict = Depends(get_current_user)):
    return user
```

---

## ✅ Checklist de Verificación

- [ ] Path + Query funcionan juntos
- [ ] Path + Query + Body funcionan
- [ ] Headers se leen correctamente
- [ ] Cookies se leen correctamente
- [ ] Dependencias se reutilizan
- [ ] Autenticación protege endpoints

---

## 🔗 Navegación

[← Ejercicio 03](../ejercicio-03-query-params/) | [Volver a Prácticas →](../README.md)
