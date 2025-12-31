# 🚀 Ejercicio 04: Integración con FastAPI

## 🎯 Objetivo

Aprender a integrar modelos Pydantic con FastAPI para validación automática y documentación.

---

## 📚 Conceptos Clave

- Request body con modelos Pydantic
- `response_model` para filtrar respuestas
- Patrón CRUD de schemas
- `model_dump(exclude_unset=True)` para updates parciales
- `from_attributes=True` para ORM

---

## 📝 Instrucciones

### Paso 1: Request Body Básico

FastAPI valida automáticamente el body con Pydantic:

```python
@app.post("/users")
async def create_user(user: UserCreate):
    # user ya está validado
    return {"message": f"User {user.name} created"}
```

**Descomenta y ejecuta** el Paso 1. Prueba en `/docs`.

---

### Paso 2: Response Model

`response_model` controla qué se envía al cliente:

```python
@app.get("/users/{id}", response_model=UserResponse)
async def get_user(id: int):
    # Aunque el modelo interno tenga password,
    # response_model lo excluye
    return user_in_db
```

**Descomenta y ejecuta** el Paso 2.

---

### Paso 3: Schemas CRUD

Patrón de schemas para APIs REST:

- `Base`: Campos comunes
- `Create`: Para POST (incluye password)
- `Update`: Para PATCH (todos opcionales)
- `Response`: Para GET (sin datos sensibles)

**Descomenta y ejecuta** el Paso 3.

---

### Paso 4: Updates Parciales

Usa `exclude_unset=True` para solo actualizar campos enviados:

```python
update_data = user_update.model_dump(exclude_unset=True)
```

**Descomenta y ejecuta** el Paso 4.

---

### Paso 5: Manejo de Errores

Personalizar respuestas de error de validación:

**Descomenta y ejecuta** el Paso 5.

---

## 🧪 Verificación

```bash
docker compose up --build
```

Visita http://localhost:8000/docs para probar los endpoints.

---

## 🎯 Reto Extra

Crea una API completa de productos con:
- `POST /products`: Crear producto
- `GET /products`: Listar productos con paginación
- `GET /products/{id}`: Obtener producto
- `PATCH /products/{id}`: Actualizar parcialmente
- `DELETE /products/{id}`: Eliminar producto

---

[← Anterior: Validadores](../ejercicio-03-validadores/) | [Ir al Proyecto →](../../3-proyecto/)
