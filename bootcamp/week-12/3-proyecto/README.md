# 🧪 Proyecto: Test Suite Completo

## 📋 Descripción

En este proyecto crearás una **suite de tests completa** para una API de gestión de tareas (Task Manager). La API ya está implementada, tu trabajo es escribir los tests que garanticen su correcto funcionamiento.

---

## 🎯 Objetivos

- Implementar tests unitarios para services
- Implementar tests de integración para endpoints
- Crear fixtures reutilizables en conftest.py
- Usar mocking para dependencias externas
- Alcanzar >80% de cobertura de código

---

## 📁 Estructura del Proyecto

```
3-proyecto/
├── README.md
├── starter/                    # 👈 Tu código aquí
│   ├── pyproject.toml
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py            # API FastAPI (ya implementada)
│   │   ├── database.py        # Configuración BD
│   │   ├── models.py          # Modelos SQLAlchemy
│   │   ├── schemas.py         # Schemas Pydantic
│   │   ├── services.py        # Lógica de negocio
│   │   ├── auth.py            # Autenticación
│   │   └── notifications.py   # Servicio de notificaciones
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py        # TODO: Crear fixtures
│       ├── unit/
│       │   ├── __init__.py
│       │   └── test_services.py   # TODO: Tests unitarios
│       └── integration/
│           ├── __init__.py
│           └── test_api.py        # TODO: Tests de integración
└── solution/                   # Solución (solo instructores)
```

---

## 🚀 Instrucciones

### Paso 1: Configurar el proyecto

```bash
cd starter
uv sync
```

### Paso 2: Explorar la API

Revisa los archivos en `src/` para entender la API:

- **main.py**: Endpoints de la API
- **models.py**: Modelos Task y User
- **services.py**: Lógica de negocio (TaskService)
- **notifications.py**: Servicio de notificaciones (mockear)

### Paso 3: Implementar fixtures (conftest.py)

Crea las fixtures necesarias:

- `db_session`: Sesión de BD de prueba
- `client`: TestClient con BD override
- `test_user`: Usuario de prueba
- `auth_headers`: Headers con token
- `test_task`: Tarea de prueba

### Paso 4: Implementar tests unitarios

En `tests/unit/test_services.py`:

- Tests para `TaskService.create_task()`
- Tests para `TaskService.get_tasks()`
- Tests para `TaskService.update_task()`
- Tests para `TaskService.complete_task()`
- Tests para `TaskService.delete_task()`

### Paso 5: Implementar tests de integración

En `tests/integration/test_api.py`:

- Tests para todos los endpoints CRUD
- Tests de autenticación
- Tests de permisos (solo dueño puede modificar)
- Tests de errores (404, 422, 401, 403)

### Paso 6: Verificar cobertura

```bash
uv run pytest --cov=src --cov-report=html --cov-fail-under=80
```

---

## 📊 API Endpoints

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/auth/register` | Registrar usuario | No |
| POST | `/auth/token` | Login | No |
| GET | `/users/me` | Usuario actual | Sí |
| GET | `/tasks/` | Listar tareas | Sí |
| POST | `/tasks/` | Crear tarea | Sí |
| GET | `/tasks/{id}` | Obtener tarea | Sí |
| PUT | `/tasks/{id}` | Actualizar tarea | Sí |
| PATCH | `/tasks/{id}/complete` | Marcar completada | Sí |
| DELETE | `/tasks/{id}` | Eliminar tarea | Sí |

---

## ✅ Criterios de Evaluación

### Tests Requeridos (mínimo)

- [ ] 5+ tests unitarios para TaskService
- [ ] 10+ tests de integración para endpoints
- [ ] Tests de autenticación (401)
- [ ] Tests de permisos (403)
- [ ] Tests de validación (422)
- [ ] Tests de not found (404)

### Calidad

- [ ] Fixtures organizadas en conftest.py
- [ ] Mocking de NotificationService
- [ ] Nombres descriptivos de tests
- [ ] Sin código duplicado (DRY)

### Cobertura

- [ ] >80% cobertura total
- [ ] 100% cobertura de services.py
- [ ] Reporte HTML generado

---

## 📝 Entregables

1. `tests/conftest.py` con fixtures
2. `tests/unit/test_services.py` con tests unitarios
3. `tests/integration/test_api.py` con tests de integración
4. Screenshot de cobertura >80%

---

## ⏱️ Tiempo Estimado

90 minutos
