# 🔨 Práctica 01: Primer Repositorio

## 🎯 Objetivo

Crear tu primer repositorio separando el acceso a datos del service.

---

## 📋 Contexto

Partimos de un service que accede directamente a SQLAlchemy (como en Week-06) y lo refactorizamos para usar un repositorio.

---

## 📝 Instrucciones

### Paso 1: Revisar el código inicial

Abre `starter/main.py` y observa cómo el service accede directamente a la base de datos.

### Paso 2: Crear el repositorio

En `starter/repositories.py`, descomenta el código del `ProductRepository`.

### Paso 3: Refactorizar el service

En `starter/services.py`, descomenta el código que usa el repositorio en lugar de acceder directamente a SQLAlchemy.

### Paso 4: Actualizar el endpoint

En `starter/main.py`, descomenta el código que inyecta el repositorio.

### Paso 5: Probar

```bash
cd starter
uv run fastapi dev main.py
```

Visita http://localhost:8000/docs y prueba los endpoints.

---

## ✅ Resultado Esperado

- Service NO tiene imports de SQLAlchemy
- Repository maneja todas las operaciones de BD
- Endpoints funcionan igual que antes

---

## 🔗 Archivos

- `starter/models.py` - Modelo Product
- `starter/repositories.py` - ProductRepository (descomentar)
- `starter/services.py` - ProductService refactorizado
- `starter/main.py` - Endpoints actualizados
