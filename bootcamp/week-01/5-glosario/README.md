# 📚 Glosario - Semana 1

Términos clave de la Semana 1: Introducción a Python Moderno y FastAPI.

---

## A

### API (Application Programming Interface)
Conjunto de reglas y protocolos que permiten que diferentes aplicaciones se comuniquen entre sí. En este bootcamp, construimos APIs REST.

```python
# Una API en FastAPI
@app.get("/users")
async def get_users():
    return [{"id": 1, "name": "Juan"}]
```

### ASGI (Asynchronous Server Gateway Interface)
Estándar de Python para servidores web asíncronos. FastAPI usa ASGI a través de Uvicorn.

### Async/Await
Palabras clave de Python para programación asíncrona.

```python
async def fetch_data():
    await asyncio.sleep(1)  # No bloquea
    return "data"
```

---

## C

### Container (Contenedor)
Unidad de software que empaqueta código y dependencias para ejecutarse de forma aislada. Docker crea contenedores.

### Coroutine (Corrutina)
Función definida con `async def` que puede pausarse y reanudarse.

---

## D

### Decorator (Decorador)
Función que modifica el comportamiento de otra función. FastAPI los usa para definir rutas.

```python
@app.get("/")  # @app.get es un decorador
async def root():
    return {"message": "Hello"}
```

### Docker
Plataforma para crear, ejecutar y gestionar contenedores.

### Docker Compose
Herramienta para definir y ejecutar aplicaciones multi-contenedor.

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "8000:8000"
```

---

## E

### Endpoint
URL específica de una API que realiza una acción. Ej: `GET /users`, `POST /users`.

### Event Loop
Mecanismo que gestiona la ejecución de código asíncrono en Python.

---

## F

### FastAPI
Framework web moderno de Python para construir APIs, basado en type hints y ASGI.

---

## H

### HTTP Methods (Métodos HTTP)
Verbos que indican la acción a realizar: GET (obtener), POST (crear), PUT (actualizar), DELETE (eliminar).

---

## J

### JSON (JavaScript Object Notation)
Formato de texto para intercambio de datos. FastAPI lo usa por defecto.

```json
{"name": "Juan", "age": 25}
```

---

## O

### OpenAPI
Especificación estándar para describir APIs REST. FastAPI genera documentación OpenAPI automáticamente.

---

## P

### Path Parameter (Parámetro de Ruta)
Variable en la URL de un endpoint.

```python
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id}
```

### Pydantic
Librería de validación de datos usando type hints. FastAPI la usa internamente.

---

## Q

### Query Parameter (Parámetro de Consulta)
Parámetro opcional en la URL después del `?`.

```python
# /items?skip=0&limit=10
@app.get("/items")
async def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

---

## R

### REST (Representational State Transfer)
Estilo de arquitectura para APIs web que usa HTTP y recursos identificados por URLs.

### Route (Ruta)
Asociación entre una URL y una función que la maneja.

---

## S

### Schema
Definición de la estructura de datos. En FastAPI, usamos Pydantic para definir schemas.

### Swagger UI
Interfaz web interactiva para probar APIs. FastAPI la genera en `/docs`.

---

## T

### Type Hint (Anotación de Tipo)
Sintaxis de Python para indicar el tipo esperado de variables y retornos.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

---

## U

### Uvicorn
Servidor ASGI de alto rendimiento para aplicaciones Python async.

```bash
uvicorn main:app --reload
```

---

## V

### Validation (Validación)
Proceso de verificar que los datos cumplen con reglas definidas. FastAPI valida automáticamente usando type hints.

---

> 📖 **Tip**: Revisa este glosario cuando encuentres un término desconocido en la documentación o código.
