# 🚀 Proyecto Semana 04: Task Manager API

## 📋 Descripción

Construirás una **API REST completa** para gestión de tareas aplicando todo lo aprendido sobre responses, status codes, manejo de errores y documentación OpenAPI.

---

## 🎯 Objetivos

Al completar este proyecto serás capaz de:

- ✅ Diseñar response models que protejan datos sensibles
- ✅ Usar status codes HTTP correctos para cada operación
- ✅ Implementar manejo de errores consistente y profesional
- ✅ Documentar APIs con OpenAPI de forma completa
- ✅ Crear una API lista para producción

---

## 📚 Requisitos Previos

- Completar ejercicios 01-04 de esta semana
- Entender response_model y sus opciones
- Conocer status codes HTTP
- Saber usar HTTPException y exception handlers

---

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md          # Este archivo
├── starter/           # Código inicial (tu punto de partida)
│   ├── main.py        # Archivo principal con TODOs
│   ├── models.py      # Schemas Pydantic
│   ├── database.py    # Simulación de base de datos
│   ├── exceptions.py  # Excepciones personalizadas
│   ├── pyproject.toml
│   ├── Dockerfile
│   └── docker-compose.yml
└── solution/          # Solución completa (solo instructores)
```

---

## 📝 Requerimientos Funcionales

### Entidades

**Task (Tarea)**
- `id`: int (auto-generado)
- `title`: str (2-100 caracteres)
- `description`: str | None (máx 500 caracteres)
- `status`: enum (pending, in_progress, completed)
- `priority`: enum (low, medium, high)
- `created_at`: datetime
- `updated_at`: datetime | None
- `completed_at`: datetime | None

### Endpoints Requeridos

| Método | Endpoint | Descripción | Status Code |
|--------|----------|-------------|-------------|
| GET | `/tasks` | Listar tareas (con filtros) | 200 |
| GET | `/tasks/{id}` | Obtener tarea por ID | 200 / 404 |
| POST | `/tasks` | Crear nueva tarea | 201 |
| PUT | `/tasks/{id}` | Actualizar tarea completa | 200 / 404 |
| PATCH | `/tasks/{id}/status` | Cambiar solo el status | 200 / 404 / 400 |
| DELETE | `/tasks/{id}` | Eliminar tarea | 204 / 404 |
| GET | `/tasks/stats` | Estadísticas de tareas | 200 |

### Filtros para GET /tasks

- `status`: filtrar por estado
- `priority`: filtrar por prioridad
- `skip`: paginación (offset)
- `limit`: paginación (máximo 100)

---

## 🔒 Response Models

Debes crear schemas separados para:

1. **TaskCreate**: Para crear tareas (sin id, timestamps)
2. **TaskUpdate**: Para actualizar (todos opcionales)
3. **TaskResponse**: Para respuestas (sin campos internos)
4. **TaskListResponse**: Para listados con paginación
5. **TaskStats**: Para estadísticas

---

## ⚠️ Manejo de Errores

Implementa errores consistentes con este formato:

```json
{
    "error": {
        "code": "TASK_NOT_FOUND",
        "message": "Task with id 99 not found",
        "details": null
    }
}
```

### Códigos de Error Requeridos

| Código | HTTP Status | Descripción |
|--------|-------------|-------------|
| `TASK_NOT_FOUND` | 404 | Tarea no existe |
| `INVALID_STATUS_TRANSITION` | 400 | Transición de estado inválida |
| `VALIDATION_ERROR` | 422 | Error de validación |
| `DUPLICATE_TASK` | 409 | Tarea duplicada (mismo título) |

### Reglas de Negocio

- No se puede pasar de `pending` a `completed` directamente
- No se puede volver a `pending` desde `completed`
- Al completar, se registra `completed_at`

---

## 📖 Documentación OpenAPI

Tu API debe incluir:

- ✅ Título, descripción y versión
- ✅ Tags para agrupar endpoints
- ✅ Descripciones en cada endpoint
- ✅ Ejemplos en schemas
- ✅ Múltiples responses documentados (200, 404, 422, etc.)

---

## 🧪 Casos de Prueba

Verifica estos escenarios:

### Crear Tarea
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "priority": "high"}'
# Esperado: 201 Created
```

### Obtener Tarea Inexistente
```bash
curl http://localhost:8000/tasks/999
# Esperado: 404 con error TASK_NOT_FOUND
```

### Transición Inválida
```bash
# Intentar pasar de pending a completed
curl -X PATCH http://localhost:8000/tasks/1/status \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
# Esperado: 400 con error INVALID_STATUS_TRANSITION
```

### Listar con Filtros
```bash
curl "http://localhost:8000/tasks?status=pending&priority=high&limit=10"
# Esperado: 200 con lista paginada
```

---

## 🚀 Ejecución

```bash
cd starter
docker compose up --build
```

Accede a:
- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📊 Rúbrica de Evaluación

| Criterio | Puntos |
|----------|--------|
| CRUD completo funcional | 20 |
| Response models correctos | 15 |
| Status codes apropiados | 15 |
| Manejo de errores consistente | 20 |
| Documentación OpenAPI completa | 15 |
| Reglas de negocio implementadas | 10 |
| Código limpio y organizado | 5 |
| **Total** | **100** |

**Mínimo para aprobar**: 70 puntos

---

## 💡 Consejos

1. Empieza por los schemas Pydantic
2. Implementa el CRUD básico primero
3. Agrega el manejo de errores después
4. Documenta mientras desarrollas
5. Prueba cada endpoint con Swagger UI

---

## 📚 Recursos

- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## ✅ Checklist de Entrega

- [ ] Todos los endpoints funcionan
- [ ] Status codes correctos
- [ ] Errores con formato consistente
- [ ] Reglas de negocio implementadas
- [ ] Documentación OpenAPI completa
- [ ] Docker funcional
- [ ] Código comentado

---

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
