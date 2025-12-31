# 🚀 Ejercicio 04: Primera API FastAPI

## 🎯 Objetivo

Crear tu primera API funcional con FastAPI, incluyendo diferentes tipos de endpoints.

**Duración estimada:** 30 minutos

---

## 📋 Requisitos Previos

- Haber completado los ejercicios anteriores
- Haber leído [Introducción a FastAPI](../../1-teoria/05-intro-fastapi.md)

---

## 📝 Instrucciones

### Paso 1: Crear la Aplicación

Crea la instancia de FastAPI con metadata:

```python
app = FastAPI(
    title="Mi API",
    description="Mi primera API con FastAPI",
    version="1.0.0",
)
```

**Abre `starter/main.py`** y descomenta el Paso 1.

---

### Paso 2: Endpoint GET Básico

El endpoint más simple retorna un diccionario:

```python
@app.get("/")
async def root():
    return {"message": "Hello"}
```

---

### Paso 3: Path Parameters

Captura valores de la URL:

```python
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}
```

---

### Paso 4: Query Parameters

Parámetros opcionales en la URL:

```python
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

---

### Paso 5: Ejecutar y Probar

```bash
# Copiar archivos al proyecto
cp starter/* ../ejercicio-01-setup/starter/src/

# Ejecutar
cd ../ejercicio-01-setup/starter
docker compose up --build
```

Prueba los endpoints:
- `http://localhost:8000/`
- `http://localhost:8000/docs`
- `http://localhost:8000/users/123`
- `http://localhost:8000/items?skip=0&limit=5`

---

## ✅ Checklist de Verificación

- [ ] La API arranca sin errores
- [ ] Puedes ver la documentación en `/docs`
- [ ] Los path parameters funcionan
- [ ] Los query parameters funcionan
- [ ] Entiendes la validación automática de tipos

---

## 🔗 Navegación

[← Anterior: Async](../ejercicio-03-async/) | [Volver a Prácticas](../README.md)
