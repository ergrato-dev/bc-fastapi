# 🎯 Proyecto Semana 10: Task Management System

## 📋 Descripción

Construirás un **Sistema de Gestión de Tareas** completo usando **Arquitectura Hexagonal**. Este proyecto integra todos los conceptos aprendidos: Domain Layer, Application Layer, Infrastructure Layer y Composition Root.

---

## 🎯 Objetivos

- Implementar arquitectura hexagonal completa desde cero
- Crear entidades de dominio con comportamiento rico
- Definir puertos (interfaces) para inversión de dependencias
- Implementar casos de uso en la capa de aplicación
- Crear adaptadores de infraestructura (API REST, persistencia)
- Componer toda la aplicación en el Composition Root
- Escribir tests que demuestren la separación de capas

---

## 📁 Estructura del Proyecto

```
3-proyecto/
├── README.md
├── starter/                    # Código inicial (para el estudiante)
│   ├── pyproject.toml
│   ├── .env.example
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── src/
│       ├── main.py             # Entry point
│       ├── domain/             # Capa de dominio
│       │   ├── entities/       # Entidades
│       │   ├── value_objects/  # Value Objects
│       │   ├── ports/          # Interfaces (Protocol)
│       │   ├── services/       # Domain Services
│       │   └── exceptions.py   # Excepciones de dominio
│       ├── application/        # Capa de aplicación
│       │   ├── commands/       # Comandos (write)
│       │   ├── queries/        # Queries (read)
│       │   ├── dtos/           # Data Transfer Objects
│       │   └── services/       # Application Services
│       └── infrastructure/     # Capa de infraestructura
│           ├── config.py       # Configuración
│           ├── persistence/    # Adaptadores de persistencia
│           └── api/            # Adaptadores HTTP
│               ├── schemas/    # Pydantic schemas
│               ├── routers/    # FastAPI routers
│               ├── dependencies.py
│               └── main.py     # Composition Root
└── solution/                   # Solución completa (oculta)
```

---

## 🏗️ Modelo de Dominio

### Entidades

#### Task (Tarea)
```
Task
├── id: UUID (identidad)
├── title: str
├── description: str
├── status: TaskStatus (Value Object)
├── priority: Priority (Value Object)
├── project_id: UUID | None
├── assignee_id: UUID | None
├── due_date: datetime | None
├── created_at: datetime
└── updated_at: datetime

Comportamientos:
├── start() → cambiar a IN_PROGRESS
├── complete() → cambiar a COMPLETED
├── assign_to(user_id) → asignar usuario
└── set_due_date(date) → establecer fecha límite
```

#### Project (Proyecto)
```
Project
├── id: UUID (identidad)
├── name: str
├── description: str
├── owner_id: UUID
├── created_at: datetime
└── updated_at: datetime

Comportamientos:
└── add_task(task) → agregar tarea al proyecto
```

#### User (Usuario)
```
User
├── id: UUID (identidad)
├── email: str
├── name: str
├── created_at: datetime
└── is_active: bool
```

### Value Objects

- **TaskStatus**: PENDING, IN_PROGRESS, COMPLETED, CANCELLED
- **Priority**: LOW (1), MEDIUM (2), HIGH (3), URGENT (4)

---

## 📋 Casos de Uso a Implementar

### Tasks
1. **CreateTask** - Crear nueva tarea
2. **GetTask** - Obtener tarea por ID
3. **ListTasks** - Listar tareas (con filtros)
4. **StartTask** - Iniciar tarea
5. **CompleteTask** - Completar tarea
6. **AssignTask** - Asignar tarea a usuario
7. **DeleteTask** - Eliminar tarea

### Projects
1. **CreateProject** - Crear proyecto
2. **GetProject** - Obtener proyecto
3. **ListProjects** - Listar proyectos
4. **AddTaskToProject** - Agregar tarea a proyecto

### Users
1. **CreateUser** - Crear usuario
2. **GetUser** - Obtener usuario
3. **ListUsers** - Listar usuarios

---

## 🔌 Puertos (Interfaces)

```python
# Ports que debes implementar

class TaskRepository(Protocol):
    def save(self, task: Task) -> None: ...
    def find_by_id(self, id: UUID) -> Task | None: ...
    def find_all(self, filters: TaskFilters) -> list[Task]: ...
    def delete(self, id: UUID) -> bool: ...

class ProjectRepository(Protocol):
    def save(self, project: Project) -> None: ...
    def find_by_id(self, id: UUID) -> Project | None: ...
    def find_all(self) -> list[Project]: ...

class UserRepository(Protocol):
    def save(self, user: User) -> None: ...
    def find_by_id(self, id: UUID) -> User | None: ...
    def find_by_email(self, email: str) -> User | None: ...
```

---

## 🛠️ Endpoints API

### Tasks
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/v1/tasks` | Crear tarea |
| GET | `/api/v1/tasks` | Listar tareas |
| GET | `/api/v1/tasks/{id}` | Obtener tarea |
| PUT | `/api/v1/tasks/{id}/start` | Iniciar tarea |
| PUT | `/api/v1/tasks/{id}/complete` | Completar tarea |
| PUT | `/api/v1/tasks/{id}/assign` | Asignar tarea |
| DELETE | `/api/v1/tasks/{id}` | Eliminar tarea |

### Projects
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/v1/projects` | Crear proyecto |
| GET | `/api/v1/projects` | Listar proyectos |
| GET | `/api/v1/projects/{id}` | Obtener proyecto |
| POST | `/api/v1/projects/{id}/tasks` | Agregar tarea |

### Users
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/v1/users` | Crear usuario |
| GET | `/api/v1/users` | Listar usuarios |
| GET | `/api/v1/users/{id}` | Obtener usuario |

---

## ⏱️ Tiempo Estimado

| Fase | Tiempo |
|------|--------|
| Domain Layer | 45 min |
| Application Layer | 45 min |
| Infrastructure Layer | 60 min |
| Composition Root | 30 min |
| **Total** | **3 horas** |

---

## 📝 Instrucciones

### 1. Configurar Entorno

```bash
cd starter
cp .env.example .env
docker compose up -d
```

### 2. Implementar por Capas

**Orden recomendado:**

1. **Domain Layer** (de adentro hacia afuera)
   - Value Objects (TaskStatus, Priority)
   - Entities (Task, Project, User)
   - Ports (TaskRepository, ProjectRepository, UserRepository)
   - Exceptions

2. **Application Layer**
   - DTOs
   - Commands y Queries
   - Services (orquestradores)

3. **Infrastructure Layer**
   - Config (Settings)
   - Persistence adapters
   - API schemas
   - API routers
   - Error handlers

4. **Composition Root**
   - dependencies.py
   - main.py

### 3. Probar

```bash
# Ejecutar servidor
docker compose up

# Probar endpoints
curl http://localhost:8000/docs
```

---

## ✅ Criterios de Evaluación

### Conocimiento (30%)
- [ ] Explica la arquitectura hexagonal y sus beneficios
- [ ] Identifica correctamente cada capa y su responsabilidad
- [ ] Comprende la inversión de dependencias

### Desempeño (40%)
- [ ] Domain Layer implementado correctamente
- [ ] Application Layer con casos de uso funcionales
- [ ] Infrastructure Layer con adaptadores completos
- [ ] Composition Root ensamblando todo

### Producto (30%)
- [ ] API funcional con todos los endpoints
- [ ] Código limpio y bien organizado
- [ ] Tests básicos pasando

---

## 🎁 Bonus

- Implementar filtros avanzados en ListTasks
- Agregar validaciones de negocio en el dominio
- Implementar SQLite como segundo adaptador de persistencia
- Agregar tests de integración

---

## 📚 Recursos

- [Teoría: Arquitectura Hexagonal](../1-teoria/01-arquitectura-hexagonal-overview.md)
- [Práctica: Domain Modeling](../2-practicas/01-domain-modeling/)
- [Práctica: Wiring](../2-practicas/04-wiring-composition/)

---

_¡Éxito con tu proyecto! 🚀_
