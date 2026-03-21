# ⚠️ Ejercicio 03: Manejo de Errores

## 🎯 Objetivo

Aprender a manejar errores de forma profesional usando HTTPException, exception handlers personalizados y formatos de error consistentes.

---

## 📋 Instrucciones

### Paso 1: HTTPException Básico

Aprende a lanzar errores HTTP controlados:

```python
from fastapi import HTTPException, status

if item_id not in items_db:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )
```

**Abre `starter/main.py`** y descomenta la sección del Paso 1.

---

### Paso 2: Excepciones Personalizadas

Crea tus propias excepciones para mejor organización:

```python
class NotFoundError(Exception):
    def __init__(self, resource: str, resource_id: int):
        self.resource = resource
        self.resource_id = resource_id

@app.exception_handler(NotFoundError)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": f"{exc.resource} {exc.resource_id} not found"}
    )
```

**Descomenta** la sección del Paso 2.

---

### Paso 3: Formato de Error Consistente

Define un modelo estándar para todos los errores:

```python
class ErrorResponse(BaseModel):
    success: bool = False
    error_code: str
    message: str
    timestamp: datetime
```

**Descomenta** la sección del Paso 3.

---

### Paso 4: Manejo de Errores de Validación

Personaliza los errores de validación de Pydantic:

```python
@app.exception_handler(RequestValidationError)
async def validation_handler(request, exc):
    errors = [{"field": e["loc"], "msg": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"errors": errors})
```

**Descomenta** la sección del Paso 4.

---

## 🧪 Verificación

1. Ejecuta el servidor:
   ```bash
   docker compose up --build
   ```

2. Prueba en http://localhost:8000/docs:
   - `GET /items/999` → Error 404 con mensaje personalizado
   - `POST /users` con email inválido → Error 422 formateado
   - `GET /users/999` → Error con formato consistente
   - `POST /products` con precio negativo → Validación personalizada

---

## ✅ Checklist

- [ ] HTTPException con mensajes descriptivos
- [ ] Excepciones personalizadas funcionan
- [ ] Formato de error es consistente
- [ ] Errores de validación tienen buen formato
- [ ] Errores 500 no exponen información sensible

---

[← Anterior: Status Codes](../02-ejercicio-status-codes/) | [Siguiente: Documentación →](../04-ejercicio-documentacion/)
