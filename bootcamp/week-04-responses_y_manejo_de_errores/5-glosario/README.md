# 📖 Glosario - Semana 04

## Responses y Manejo de Errores

Términos técnicos clave de esta semana, ordenados alfabéticamente.

---

## A

### API (Application Programming Interface)
Interfaz que permite la comunicación entre aplicaciones. En este contexto, una API REST que expone endpoints HTTP.

---

## B

### Background Task
Tarea que se ejecuta después de enviar la respuesta al cliente. Útil para operaciones que no necesitan bloquear la respuesta.

```python
from fastapi import BackgroundTasks

@app.post("/items")
async def create(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email)
    return {"status": "created"}
```

---

## C

### Content-Type
Header HTTP que indica el tipo de contenido de la respuesta. Ejemplos: `application/json`, `text/html`, `text/plain`.

---

## D

### Deprecation
Proceso de marcar un endpoint como obsoleto antes de eliminarlo. Se indica con el parámetro `deprecated=True`.

```python
@app.get("/old-endpoint", deprecated=True)
async def old_endpoint():
    pass
```

---

## E

### Exception Handler
Función que captura excepciones específicas y las convierte en respuestas HTTP consistentes.

```python
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(status_code=400, content={"error": str(exc)})
```

### exclude_unset
Opción de response_model que excluye campos no establecidos explícitamente en la respuesta.

---

## F

### FileResponse
Clase para enviar archivos como respuesta HTTP, con soporte para descarga y streaming.

```python
from fastapi.responses import FileResponse
return FileResponse("archivo.pdf", filename="descarga.pdf")
```

---

## H

### HTTPException
Excepción de FastAPI para retornar errores HTTP con código de estado y mensaje.

```python
from fastapi import HTTPException
raise HTTPException(status_code=404, detail="Not found")
```

### Header
Metadatos enviados en requests/responses HTTP. Ejemplos: `Content-Type`, `Authorization`, `X-Custom-Header`.

---

## J

### JSONResponse
Respuesta HTTP con contenido JSON. Es el tipo de respuesta por defecto en FastAPI.

```python
from fastapi.responses import JSONResponse
return JSONResponse(content={"key": "value"}, status_code=200)
```

---

## M

### Media Type
Identificador del formato de datos (MIME type). Ejemplos: `application/json`, `image/png`, `text/csv`.

---

## O

### OpenAPI
Especificación estándar para describir APIs REST. FastAPI genera documentación OpenAPI automáticamente.

---

## P

### Paginación
Técnica para dividir resultados en páginas. Se implementa con parámetros `skip` (offset) y `limit`.

```python
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return items[skip:skip + limit]
```

---

## R

### RedirectResponse
Respuesta que redirige al cliente a otra URL.

```python
from fastapi.responses import RedirectResponse
return RedirectResponse(url="/new-location", status_code=307)
```

### response_model
Parámetro del decorador que define el schema Pydantic para validar y serializar la respuesta.

```python
@app.get("/users/{id}", response_model=UserResponse)
async def get_user(id: int):
    return user
```

### responses
Parámetro para documentar múltiples códigos de respuesta en OpenAPI.

---

## S

### Status Code
Código numérico que indica el resultado de una petición HTTP:
- **2xx**: Éxito (200, 201, 204)
- **4xx**: Error del cliente (400, 401, 403, 404, 422)
- **5xx**: Error del servidor (500, 503)

### StreamingResponse
Respuesta que envía datos en chunks, útil para archivos grandes o datos en tiempo real.

```python
from fastapi.responses import StreamingResponse

def generate():
    for i in range(10):
        yield f"chunk {i}\n"

return StreamingResponse(generate(), media_type="text/plain")
```

### Swagger UI
Interfaz web interactiva para explorar y probar APIs. Accesible en `/docs` por defecto.

---

## T

### Tags
Etiquetas para agrupar endpoints relacionados en la documentación OpenAPI.

```python
@app.get("/users", tags=["users"])
async def list_users():
    pass
```

---

## V

### Validation Error
Error 422 que ocurre cuando los datos de entrada no cumplen las validaciones de Pydantic.

---

## Códigos HTTP Comunes

| Código | Nombre | Uso |
|--------|--------|-----|
| 200 | OK | Éxito general |
| 201 | Created | Recurso creado |
| 204 | No Content | Éxito sin cuerpo |
| 400 | Bad Request | Error en la petición |
| 401 | Unauthorized | Sin autenticación |
| 403 | Forbidden | Sin autorización |
| 404 | Not Found | Recurso no existe |
| 409 | Conflict | Conflicto (duplicado) |
| 422 | Unprocessable Entity | Error de validación |
| 500 | Internal Server Error | Error del servidor |
| 503 | Service Unavailable | Servicio no disponible |

---

[← Recursos](../4-recursos/) | [Volver a Semana 04 →](../README.md)
