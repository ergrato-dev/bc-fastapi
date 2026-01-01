# 📦 Proyecto Semana 07: Task Manager API

## 🎯 Objetivo

Construir una **API de gestión de tareas** aplicando el **patrón Repository** y **Unit of Work** para separar la lógica de acceso a datos.

---

## 📋 Descripción

Crearás una API REST completa para gestionar tareas con usuarios, implementando:

- **BaseRepository genérico** con operaciones CRUD reutilizables
- **Repositorios específicos** (UserRepository, TaskRepository)
- **Unit of Work** para coordinar transacciones
- **Services** que usan repositorios (no acceden directamente a DB)
- **Tests con Fake Repositories**

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                      FastAPI Router                      │
│                   (HTTP endpoints)                       │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                       Services                           │
│              (Lógica de negocio)                        │
│         UserService, TaskService                         │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    Unit of Work                          │
│            (Coordina transacciones)                      │
│    ┌─────────────────┬─────────────────┐                │
│    │  UserRepository │  TaskRepository │                │
│    └─────────────────┴─────────────────┘                │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                      Database                            │
│                    (SQLite/PostgreSQL)                   │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Estructura del Proyecto

```
starter/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── config.py            # Configuración
│   ├── database.py          # Conexión DB
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py          # Base model
│   │   ├── user.py          # User model
│   │   └── task.py          # Task model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py          # User schemas
│   │   └── task.py          # Task schemas
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── base.py          # BaseRepository[T]
│   │   ├── user.py          # UserRepository
│   │   └── task.py          # TaskRepository
│   ├── unit_of_work.py      # UnitOfWork
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user.py          # UserService
│   │   └── task.py          # TaskService
│   └── routers/
│       ├── __init__.py
│       ├── users.py         # /users endpoints
│       └── tasks.py         # /tasks endpoints
└── tests/
    ├── __init__.py
    ├── conftest.py          # Fixtures
    ├── fakes/
    │   ├── __init__.py
    │   └── repositories.py  # Fake repositories
    ├── test_user_service.py
    └── test_task_service.py
```

---

## 🚀 Funcionalidades

### Usuarios (`/users`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/users/` | Crear usuario |
| GET | `/users/` | Listar usuarios |
| GET | `/users/{id}` | Obtener usuario |
| PUT | `/users/{id}` | Actualizar usuario |
| DELETE | `/users/{id}` | Eliminar usuario |

### Tareas (`/tasks`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/tasks/` | Crear tarea |
| GET | `/tasks/` | Listar tareas (filtros) |
| GET | `/tasks/{id}` | Obtener tarea |
| PUT | `/tasks/{id}` | Actualizar tarea |
| DELETE | `/tasks/{id}` | Eliminar tarea |
| PATCH | `/tasks/{id}/complete` | Marcar completada |
| GET | `/users/{id}/tasks` | Tareas de usuario |

---

## 📝 Modelos

### User

```python
class User:
    id: int (PK)
    username: str (unique)
    email: str (unique)
    is_active: bool = True
    created_at: datetime
```

### Task

```python
class Task:
    id: int (PK)
    title: str
    description: str | None
    is_completed: bool = False
    priority: Priority (LOW, MEDIUM, HIGH)
    user_id: int (FK -> users.id)
    created_at: datetime
    completed_at: datetime | None
```

---

## ✅ Criterios de Evaluación

### Repositorios (30%)

- [ ] `BaseRepository[T]` genérico con CRUD
- [ ] `UserRepository` con métodos específicos
- [ ] `TaskRepository` con filtros y queries
- [ ] Uso correcto de `flush()` vs `commit()`

### Unit of Work (25%)

- [ ] Clase `UnitOfWork` con context manager
- [ ] Repositorios comparten misma sesión
- [ ] Commit/rollback coordinado
- [ ] Cleanup automático

### Services (25%)

- [ ] `UserService` con lógica de negocio
- [ ] `TaskService` con validaciones
- [ ] Inyección de dependencias (UoW)
- [ ] Manejo de errores apropiado

### Tests (20%)

- [ ] Fake repositories implementados
- [ ] Tests unitarios para UserService
- [ ] Tests unitarios para TaskService
- [ ] Cobertura de casos de error

---

## 🔧 Comandos

```bash
# Instalar dependencias
cd starter
uv sync

# Ejecutar API
uv run fastapi dev src/main.py

# Ejecutar tests
uv run pytest -v

# Ejecutar tests con cobertura
uv run pytest --cov=src --cov-report=html
```

---

## 📚 Recursos

- [Teoría 02: Repositorio Genérico](../1-teoria/02-repositorio-generico.md)
- [Teoría 04: Unit of Work](../1-teoria/04-unit-of-work.md)
- [Teoría 05: Testing con Repositories](../1-teoria/05-testing-con-repositories.md)
- [Práctica 04: Unit of Work](../2-practicas/04-unit-of-work/)

---

## ⏱️ Tiempo Estimado

- **Implementación**: 2-3 horas
- **Tests**: 1 hora
- **Total**: 3-4 horas

---

## 💡 Tips

1. **Empieza por los modelos** - Define bien la estructura de datos
2. **Implementa BaseRepository primero** - Reutiliza en repos específicos
3. **UoW antes que Services** - Los services dependen del UoW
4. **Tests al final** - Usa fakes para aislar la lógica
5. **Consulta las prácticas** - Tienen ejemplos de cada patrón
