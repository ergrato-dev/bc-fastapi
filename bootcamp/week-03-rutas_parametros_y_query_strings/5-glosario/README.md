cd cd# 📖 Glosario - Semana 03

## A

### API (Application Programming Interface)
Interfaz que permite la comunicación entre diferentes aplicaciones. REST APIs usan HTTP para intercambiar datos.

### APIRouter
Clase de FastAPI para organizar rutas en módulos separados, facilitando la estructura de proyectos grandes.

```python
from fastapi import APIRouter
router = APIRouter(prefix="/users", tags=["Users"])
```

---

## B

### Body
Contenido del mensaje HTTP, generalmente en formato JSON. Se usa para enviar datos en POST, PUT y PATCH.

```python
@app.post("/items")
async def create(item: Item):  # item viene del body
    pass
```

---

## C

### Cookie
Pequeño archivo almacenado en el navegador del cliente. Se usa para sesiones y preferencias.

```python
from fastapi import Cookie

@app.get("/items")
async def read(session_id: str = Cookie(None)):
    pass
```

### CRUD
Acrónimo de Create, Read, Update, Delete - las cuatro operaciones básicas de persistencia de datos.

---

## D

### DELETE
Método HTTP para eliminar recursos. Típicamente retorna 204 No Content.

### Depends
Función de FastAPI para inyección de dependencias.

```python
from fastapi import Depends

async def get_db():
    return database

@app.get("/items")
async def read(db = Depends(get_db)):
    pass
```

---

## E

### Endpoint
URL específica de una API que realiza una acción determinada. Ejemplo: `GET /users/123`.

### Enum
Tipo de dato que define un conjunto fijo de valores permitidos.

```python
from enum import Enum

class Status(str, Enum):
    active = "active"
    inactive = "inactive"
```

---

## F

### Form Data
Datos enviados desde formularios HTML con Content-Type `application/x-www-form-urlencoded`.

```python
from fastapi import Form

@app.post("/login")
async def login(username: str = Form(...)):
    pass
```

---

## G

### GET
Método HTTP para obtener recursos. No debe modificar datos en el servidor.

---

## H

### Header
Metadatos enviados con la request/response HTTP. Incluyen información como Content-Type, Authorization, etc.

```python
from fastapi import Header

@app.get("/items")
async def read(user_agent: str = Header(None)):
    pass
```

### HTTP Methods
Verbos que indican la acción a realizar: GET, POST, PUT, PATCH, DELETE, etc.

---

## I

### Idempotente
Operación que produce el mismo resultado sin importar cuántas veces se ejecute. GET, PUT y DELETE son idempotentes.

---

## P

### Pagination
Técnica para dividir grandes conjuntos de datos en páginas más pequeñas.

```python
@app.get("/items")
async def list(page: int = 1, per_page: int = 10):
    pass
```

### PATCH
Método HTTP para actualización parcial de recursos.

### Path
1. Ruta URL de un endpoint
2. Función de FastAPI para validar path parameters

```python
from fastapi import Path

@app.get("/items/{id}")
async def read(id: int = Path(..., gt=0)):
    pass
```

### Path Parameter
Variable en la URL que identifica un recurso específico.

```
/users/{user_id}  →  user_id es un path parameter
```

### POST
Método HTTP para crear nuevos recursos.

### PUT
Método HTTP para reemplazar completamente un recurso.

---

## Q

### Query
Función de FastAPI para validar query parameters.

```python
from fastapi import Query

@app.get("/items")
async def list(skip: int = Query(0, ge=0)):
    pass
```

### Query Parameter
Parámetros después de `?` en la URL para filtrar o modificar la respuesta.

```
/items?skip=10&limit=5  →  skip y limit son query params
```

### Query String
Parte de la URL después de `?` que contiene los query parameters.

---

## R

### REST (Representational State Transfer)
Estilo arquitectónico para diseñar APIs web usando recursos y métodos HTTP.

### Router
Componente que dirige las requests a los handlers apropiados según la URL y método.

---

## S

### Status Code
Código numérico que indica el resultado de una request HTTP.

| Código | Significado |
|--------|-------------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 404 | Not Found |
| 422 | Unprocessable Entity |

### Sorting
Ordenamiento de resultados según uno o más campos.

---

## U

### URI (Uniform Resource Identifier)
Identificador único de un recurso. Las URLs son un tipo de URI.

### URL (Uniform Resource Locator)
Dirección completa de un recurso web, incluyendo protocolo, dominio y path.

---

## V

### Validation
Proceso de verificar que los datos cumplen con reglas específicas antes de procesarlos.

```python
from fastapi import Query

limit: int = Query(..., ge=1, le=100)  # Entre 1 y 100
```

---

[← Volver a Week-03](../README.md)
