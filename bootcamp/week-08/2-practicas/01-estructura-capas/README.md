# 🏗️ Práctica 01: Estructura de Capas

## 🎯 Objetivos

- Crear la estructura de carpetas para arquitectura en capas
- Implementar las tres capas: Presentation, Application, Data Access
- Configurar las dependencias entre capas
- Verificar el flujo correcto de datos

---

## 📋 Descripción

En esta práctica crearás la estructura base de un proyecto con arquitectura en capas completa. Implementarás un CRUD simple de `Category` siguiendo el patrón **Router → Service → Repository**.

---

## 📁 Estructura del Proyecto

```
starter/
├── main.py                  # Punto de entrada
├── config.py                # Configuración
├── database.py              # Conexión a DB
├── models/
│   ├── __init__.py
│   └── category.py          # Entity Category
├── schemas/
│   ├── __init__.py
│   └── category.py          # DTOs Category
├── repositories/
│   ├── __init__.py
│   ├── base.py              # Repository base
│   └── category.py          # CategoryRepository
├── services/
│   ├── __init__.py
│   └── category.py          # CategoryService
├── routers/
│   ├── __init__.py
│   └── categories.py        # Endpoints
└── dependencies.py          # Inyección de dependencias
```

---

## 🚀 Pasos

### Paso 1: Configuración Base

Abre `starter/config.py` y descomenta el código de configuración con Pydantic Settings.

### Paso 2: Modelo de Datos

Abre `starter/models/category.py` y descomenta el modelo SQLAlchemy.

### Paso 3: DTOs (Schemas)

Abre `starter/schemas/category.py` y descomenta los schemas Pydantic:
- `CategoryCreate` - para crear
- `CategoryUpdate` - para actualizar
- `CategoryResponse` - para respuestas

### Paso 4: Repository

Abre `starter/repositories/category.py` y descomenta:
- La clase `CategoryRepository`
- Los métodos CRUD básicos

### Paso 5: Service

Abre `starter/services/category.py` y descomenta:
- La clase `CategoryService`
- La lógica de negocio

### Paso 6: Router

Abre `starter/routers/categories.py` y descomenta:
- Los endpoints CRUD
- La inyección de dependencias

### Paso 7: Dependencies

Abre `starter/dependencies.py` y descomenta las funciones de inyección.

### Paso 8: Main

Abre `starter/main.py` y descomenta la inclusión del router.

---

## ✅ Verificación

Ejecuta la aplicación:

```bash
cd starter
uvicorn main:app --reload
```

Prueba en `http://localhost:8000/docs`:

1. **POST /categories/** - Crear categoría
2. **GET /categories/** - Listar categorías
3. **GET /categories/{id}** - Obtener una
4. **PATCH /categories/{id}** - Actualizar
5. **DELETE /categories/{id}** - Eliminar

---

## 📊 Flujo de Datos

```
POST /categories/
     │
     ▼
┌─────────────┐    CategoryCreate    ┌─────────────┐
│   Router    │ ──────────────────▶  │   Service   │
│ (Presenta.) │                      │ (Aplicación)│
└─────────────┘                      └──────┬──────┘
                                            │
                                     Category (Entity)
                                            │
                                            ▼
                                     ┌─────────────┐
                                     │ Repository  │
                                     │(Data Access)│
                                     └──────┬──────┘
                                            │
                                            ▼
                                        DATABASE
```

---

## 🎯 Resultado Esperado

Al completar la práctica tendrás:

- ✅ Estructura de proyecto en capas
- ✅ CRUD completo de Category
- ✅ Separación clara de responsabilidades
- ✅ Inyección de dependencias funcionando
