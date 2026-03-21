# 🚀 Práctica 03: Testing Endpoints FastAPI

## 🎯 Objetivo

Aprender a testear endpoints de FastAPI usando TestClient y httpx.

---

## 📋 Descripción

En esta práctica aprenderás a:

- Usar TestClient para tests síncronos
- Testear todos los métodos HTTP (GET, POST, PUT, DELETE)
- Override de dependencias (database)
- Testear autenticación y autorización
- Testear casos de error

---

## 📁 Estructura

```
03-testing-endpoints/
├── README.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py            # App FastAPI
│   ├── database.py        # Conexión a BD
│   ├── models.py          # Modelos SQLAlchemy
│   ├── schemas.py         # Schemas Pydantic
│   └── auth.py            # Autenticación
└── tests/
    ├── __init__.py
    ├── conftest.py        # Fixtures de FastAPI
    ├── test_items.py      # Tests de /items
    └── test_auth.py       # Tests de /auth
```

---

## 🚀 Instrucciones

### Paso 1: Configurar el proyecto

```bash
cd 03-testing-endpoints
uv sync
```

### Paso 2: Explorar la API

Abre `src/main.py` y revisa los endpoints disponibles.

### Paso 3: Escribir tests

Descomenta los tests en `tests/test_items.py` y `tests/test_auth.py`.

### Paso 4: Ejecutar tests

```bash
uv run pytest -v
uv run pytest --cov=src --cov-report=term-missing
```

---

## ✅ Criterios de Éxito

- [ ] Tests para CRUD completo de items
- [ ] Tests de endpoints protegidos
- [ ] Tests de errores (404, 422, 401)
- [ ] Cobertura > 80%

---

## ⏱️ Tiempo Estimado

35 minutos
