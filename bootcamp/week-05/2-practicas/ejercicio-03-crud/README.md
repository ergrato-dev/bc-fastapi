# 🔄 Ejercicio 03: Operaciones CRUD

## 🎯 Objetivo

Dominar las operaciones Create, Read, Update y Delete con SQLAlchemy 2.0.

**Duración estimada:** 45 minutos

---

## 📋 Pasos

### Paso 1: Setup con Modelo Task

Modelo de tareas para practicar CRUD:

```python
class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    completed: Mapped[bool] = mapped_column(default=False)
    priority: Mapped[int] = mapped_column(default=1)
```

**Abre `starter/main.py`** y descomenta la sección del Paso 1.

---

### Paso 2: CREATE - Crear Registros

Insertar nuevos registros:

```python
# Un registro
task = Task(title="Learn SQLAlchemy")
session.add(task)
session.commit()

# Múltiples registros
tasks = [Task(title="Task 1"), Task(title="Task 2")]
session.add_all(tasks)
session.commit()
```

**Descomenta** la sección del Paso 2.

---

### Paso 3: READ - Obtener por ID

Usar `session.get()` para buscar por primary key:

```python
task = session.get(Task, 1)  # Busca task con id=1
if task:
    print(f"Encontrado: {task.title}")
```

**Descomenta** la sección del Paso 3.

---

### Paso 4: READ - Listar con Filtros

Usar `select()` para queries complejas:

```python
from sqlalchemy import select

# Todas las tareas
stmt = select(Task)
tasks = session.execute(stmt).scalars().all()

# Con filtro
stmt = select(Task).where(Task.completed == False)
pending = session.execute(stmt).scalars().all()
```

**Descomenta** la sección del Paso 4.

---

### Paso 5: READ - Ordenar y Paginar

```python
from sqlalchemy import select, desc

# Ordenar por prioridad descendente
stmt = select(Task).order_by(desc(Task.priority))

# Paginar: skip 0, limit 5
stmt = select(Task).offset(0).limit(5)
```

**Descomenta** la sección del Paso 5.

---

### Paso 6: UPDATE - Modificar Registros

```python
# Obtener y modificar
task = session.get(Task, 1)
task.completed = True
task.priority = 5
session.commit()
```

**Descomenta** la sección del Paso 6.

---

### Paso 7: DELETE - Eliminar Registros

```python
task = session.get(Task, 1)
session.delete(task)
session.commit()
```

**Descomenta** la sección del Paso 7.

---

## ▶️ Ejecutar

```bash
uv run python starter/main.py
```

**Salida esperada:**
```
=== Paso 1: Setup completado ===
=== Paso 2: CREATE ===
Creada: Task(id=1, title='Learn SQLAlchemy')
Creadas 3 tareas adicionales
=== Paso 3: READ por ID ===
Por ID: Task(id=1, title='Learn SQLAlchemy')
=== Paso 4: READ con filtros ===
Todas: 4 tareas
Pendientes: 4 tareas
Alta prioridad: 1 tareas
=== Paso 5: READ ordenar y paginar ===
Ordenadas por prioridad: [...]
Página 1 (2 items): [...]
=== Paso 6: UPDATE ===
Actualizada: Task(id=1, completed=True, priority=10)
=== Paso 7: DELETE ===
Eliminada tarea id=4
Tareas restantes: 3
```

---

## ✅ Verificación

- [ ] CREATE: Puedo crear uno y múltiples registros
- [ ] READ: Puedo buscar por ID con `session.get()`
- [ ] READ: Puedo filtrar con `select().where()`
- [ ] UPDATE: Puedo modificar atributos y hacer commit
- [ ] DELETE: Puedo eliminar registros con `session.delete()`

---

## 🧠 Métodos Clave

| Operación | Código SQLAlchemy 2.0 |
|-----------|----------------------|
| Create one | `session.add(obj)` |
| Create many | `session.add_all([...])` |
| Read by ID | `session.get(Model, id)` |
| Read all | `session.execute(select(Model)).scalars().all()` |
| Read filter | `select(Model).where(...)` |
| Update | `obj.attr = value` + `commit()` |
| Delete | `session.delete(obj)` + `commit()` |

---

[← Anterior: Modelos](../ejercicio-02-modelos/) | [Siguiente: FastAPI + DB →](../ejercicio-04-fastapi-db/)
