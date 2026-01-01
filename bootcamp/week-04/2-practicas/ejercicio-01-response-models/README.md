# 📤 Ejercicio 01: Response Models

## 🎯 Objetivo

Aprender a definir modelos de respuesta tipados con `response_model` para garantizar consistencia y seguridad en las respuestas de la API.

---

## 📋 Instrucciones

### Paso 1: Modelo Base y Response

Aprende a separar modelos de entrada y salida:

```python
# El modelo UserResponse NO incluye password
# Aunque la función retorne un dict con password,
# response_model filtrará ese campo automáticamente

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    return {
        "id": 1,
        "email": user.email,
        "name": user.name,
        "password": user.password  # Será filtrado
    }
```

**Abre `starter/main.py`** y descomenta la sección del Paso 1.

---

### Paso 2: Response Model Exclude Unset

Aprende a omitir campos que no fueron establecidos:

```python
# Con response_model_exclude_unset=True
# Solo se envían los campos que fueron explícitamente establecidos
# Los campos con valores por defecto NO aparecen si no se establecieron

@app.get("/items/{item_id}", response_model_exclude_unset=True)
async def get_item(item_id: int):
    return items_db.get(item_id)  # Solo campos establecidos
```

**Descomenta** la sección del Paso 2.

---

### Paso 3: Lista de Modelos

Aprende a retornar listas tipadas:

```python
# response_model=list[Item] garantiza que cada elemento
# de la lista cumpla con el schema Item

@app.get("/items", response_model=list[Item])
async def list_items():
    return list(items_db.values())
```

**Descomenta** la sección del Paso 3.

---

### Paso 4: Respuesta con Paginación

Crea modelos para respuestas paginadas:

```python
class PaginatedResponse(BaseModel):
    items: list[Item]
    total: int
    page: int
    per_page: int
    pages: int

@app.get("/items/paginated", response_model=PaginatedResponse)
async def list_paginated(page: int = 1, per_page: int = 10):
    # ...
```

**Descomenta** la sección del Paso 4.

---

### Paso 5: Modelos con Alias

Usa alias para nombres diferentes en JSON:

```python
class ProductResponse(BaseModel):
    product_id: int = Field(..., alias="productId")
    product_name: str = Field(..., alias="productName")
    
    model_config = {"populate_by_name": True}
```

**Descomenta** la sección del Paso 5.

---

## 🧪 Verificación

1. Ejecuta el servidor:
   ```bash
   docker compose up --build
   ```

2. Prueba en http://localhost:8000/docs:
   - `POST /users` - Verifica que password NO aparece en respuesta
   - `GET /items/1` - Solo campos establecidos
   - `GET /items` - Lista de items
   - `GET /items/paginated` - Respuesta paginada
   - `GET /products/1` - Campos con alias (camelCase)

---

## ✅ Checklist

- [ ] `response_model` filtra campos sensibles
- [ ] `response_model_exclude_unset` omite campos no establecidos
- [ ] `list[Model]` para listas tipadas
- [ ] Modelo de paginación funcional
- [ ] Alias funcionan correctamente

---

[← Volver a Prácticas](../README.md) | [Siguiente: Status Codes →](../ejercicio-02-status-codes/)
