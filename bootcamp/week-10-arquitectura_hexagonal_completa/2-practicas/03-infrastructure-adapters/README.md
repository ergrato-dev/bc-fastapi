# 🔧 Práctica 03: Infrastructure Adapters

## 📋 Descripción

En esta práctica aprenderás a implementar **Infrastructure Adapters** que conectan la aplicación con el mundo exterior. Crearás tanto Driving Adapters (API REST) como Driven Adapters (Repositories).

---

## 🎯 Objetivos

- Implementar Driven Adapters (Repositories en memoria)
- Crear Driving Adapters (API REST con FastAPI)
- Mapear entre schemas de API y DTOs
- Manejar errores y traducirlos a HTTP
- Configurar la aplicación con Pydantic Settings

---

## 📁 Estructura del Ejercicio

```
03-infrastructure-adapters/
├── README.md
└── starter/
    ├── pyproject.toml
    └── src/
        ├── __init__.py
        ├── domain/                 # Copiado de práctica 01
        ├── application/            # Copiado de práctica 02
        └── infrastructure/
            ├── __init__.py
            ├── config.py
            ├── persistence/
            │   ├── __init__.py
            │   ├── task_repository.py
            │   └── project_repository.py
            └── api/
                ├── __init__.py
                ├── schemas/
                │   ├── __init__.py
                │   └── task_schemas.py
                ├── routers/
                │   ├── __init__.py
                │   └── tasks.py
                └── error_handlers.py
```

---

## ⏱️ Duración Estimada

45 minutos

---

## ✅ Criterios de Éxito

- [ ] InMemoryTaskRepository implementa el Port
- [ ] TaskResponse es un Pydantic model para la API
- [ ] El router traduce errores de dominio a HTTP
- [ ] Settings usa Pydantic Settings con .env
