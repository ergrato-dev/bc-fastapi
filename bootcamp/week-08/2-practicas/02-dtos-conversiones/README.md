# 🔄 Práctica 02: DTOs y Conversiones

## 🎯 Objetivos

- Crear DTOs específicos para cada operación
- Implementar Mappers para conversiones
- Usar `model_validate` de Pydantic v2
- Separar completamente Entity de Response

---

## 📋 Descripción

En esta práctica aprenderás a crear diferentes DTOs para entrada y salida, implementando Mappers que convierten entre entidades SQLAlchemy y schemas Pydantic.

Trabajarás con la entidad `Product` que tiene más complejidad que `Category`.

---

## 📁 Estructura

```
starter/
├── main.py
├── database.py
├── models/
│   └── product.py           # Entity Product
├── schemas/
│   └── product.py           # DTOs: Create, Update, Response, Detail
├── mappers/
│   └── product.py           # ProductMapper
├── repositories/
│   └── product.py           # ProductRepository
├── services/
│   └── product.py           # ProductService con Mapper
└── routers/
    └── products.py          # Endpoints
```

---

## 🚀 Pasos

### Paso 1: Modelo Product

Abre `starter/models/product.py` y observa la entidad Product con campos que NO queremos exponer (como `cost_price`, `internal_notes`).

### Paso 2: DTOs Específicos

Abre `starter/schemas/product.py` y descomenta:

- `ProductCreate` - campos para crear (sin ID, sin timestamps)
- `ProductUpdate` - campos opcionales para PATCH
- `ProductResponse` - campos públicos (sin cost_price)
- `ProductDetail` - respuesta extendida con más info

### Paso 3: Mapper

Abre `starter/mappers/product.py` y descomenta:

- `to_entity()` - DTO → Entity
- `to_response()` - Entity → Response DTO
- `update_entity()` - Aplica Update DTO a Entity

### Paso 4: Service con Mapper

Abre `starter/services/product.py` y descomenta el uso del Mapper en cada operación.

### Paso 5: Router

Abre `starter/routers/products.py` y descomenta los endpoints.

---

## 📊 Flujo de Conversiones

```
POST /products/
     │
     │  JSON Input
     ▼
┌─────────────────┐
│  ProductCreate  │  ← Pydantic valida input
└────────┬────────┘
         │
         │  Mapper.to_entity()
         ▼
┌─────────────────┐
│    Product      │  ← SQLAlchemy Entity
│   (Entity)      │
└────────┬────────┘
         │
         │  Repository.add()
         ▼
┌─────────────────┐
│    Product      │  ← Con ID generado
│  (con ID)       │
└────────┬────────┘
         │
         │  Mapper.to_response()
         ▼
┌─────────────────┐
│ ProductResponse │  ← Sin campos sensibles
└────────┬────────┘
         │
         │  FastAPI serializa
         ▼
    JSON Output
```

---

## ✅ Verificación

Ejecuta y prueba:

```bash
cd starter
uvicorn main:app --reload
```

1. **POST** `/products/` - Crea producto (no envíes `cost_price` en response)
2. **GET** `/products/{id}` - Verifica que `cost_price` NO aparece
3. **PATCH** `/products/{id}` - Actualiza solo algunos campos

---

## 🎯 Puntos Clave

- **ProductCreate**: Solo campos que el cliente puede enviar
- **ProductResponse**: Solo campos que el cliente puede ver
- **ProductUpdate**: Todos opcionales con `exclude_unset=True`
- **Mapper**: Centraliza toda la lógica de conversión
