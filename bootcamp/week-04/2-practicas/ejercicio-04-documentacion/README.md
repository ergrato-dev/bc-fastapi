# 📖 Ejercicio 04: Documentación OpenAPI

## 🎯 Objetivo

Aprender a documentar APIs de forma profesional usando OpenAPI, Swagger UI y ReDoc con ejemplos, descripciones y tags.

---

## 📋 Instrucciones

### Paso 1: Metadata de la API

Configura información general de la API:

```python
app = FastAPI(
    title="Mi API",
    description="Descripción completa con **markdown**",
    version="1.0.0",
    contact={"name": "Dev", "email": "dev@example.com"},
    license_info={"name": "MIT"}
)
```

**Abre `starter/main.py`** y descomenta la sección del Paso 1.

---

### Paso 2: Tags para Agrupar Endpoints

Organiza endpoints en categorías:

```python
tags_metadata = [
    {"name": "users", "description": "Operaciones de usuarios"},
    {"name": "items", "description": "Gestión de items"}
]

@app.get("/users", tags=["users"])
async def list_users():
    pass
```

**Descomenta** la sección del Paso 2.

---

### Paso 3: Documentar Endpoints

Añade descripciones y ejemplos:

```python
@app.get(
    "/items/{item_id}",
    summary="Obtener item",
    description="Descripción detallada del endpoint",
    response_description="El item solicitado"
)
async def get_item(item_id: int):
    """Docstring también aparece en docs."""
    pass
```

**Descomenta** la sección del Paso 3.

---

### Paso 4: Ejemplos en Schemas

Incluye ejemplos realistas en los modelos:

```python
class User(BaseModel):
    name: str = Field(..., example="John Doe")
    
    model_config = {
        "json_schema_extra": {
            "example": {"name": "John", "email": "john@example.com"}
        }
    }
```

**Descomenta** la sección del Paso 4.

---

### Paso 5: Documentar Múltiples Responses

Documenta todos los códigos de respuesta posibles:

```python
@app.get(
    "/items/{id}",
    responses={
        200: {"description": "Item encontrado"},
        404: {"description": "No encontrado", "model": ErrorModel}
    }
)
```

**Descomenta** la sección del Paso 5.

---

## 🧪 Verificación

1. Ejecuta el servidor:
   ```bash
   docker compose up --build
   ```

2. Revisa la documentación:
   - **Swagger UI**: http://localhost:8000/docs
   - **ReDoc**: http://localhost:8000/redoc

3. Verifica:
   - Título y descripción de la API
   - Tags agrupando endpoints
   - Descripciones en cada endpoint
   - Ejemplos en "Try it out"
   - Múltiples responses documentados

---

## ✅ Checklist

- [ ] Metadata de API configurada
- [ ] Tags organizan los endpoints
- [ ] Endpoints tienen summary y description
- [ ] Schemas incluyen ejemplos
- [ ] Responses múltiples documentados
- [ ] Swagger UI muestra todo correctamente

---

[← Anterior: Errores](../ejercicio-03-errores/) | [Volver a Prácticas →](../README.md)
