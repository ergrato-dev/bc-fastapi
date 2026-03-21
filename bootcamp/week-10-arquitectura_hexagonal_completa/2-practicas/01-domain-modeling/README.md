# 🎯 Práctica 01: Domain Modeling

## 📋 Descripción

En esta práctica aprenderás a modelar el **Domain Layer** de una aplicación siguiendo los principios de Domain-Driven Design (DDD) táctico. Crearás entidades ricas con comportamiento, value objects inmutables y ports para abstraer dependencias externas.

---

## 🎯 Objetivos

- Crear entidades con identidad y comportamiento
- Implementar value objects inmutables
- Definir ports (interfaces) usando Protocol
- Encapsular reglas de negocio en el dominio
- Escribir excepciones de dominio expresivas

---

## 📁 Estructura del Ejercicio

```
01-domain-modeling/
├── README.md                 # Este archivo
└── starter/
    ├── pyproject.toml
    └── src/
        ├── __init__.py
        └── domain/
            ├── __init__.py
            ├── entities/
            │   ├── __init__.py
            │   ├── task.py
            │   └── project.py
            ├── value_objects/
            │   ├── __init__.py
            │   ├── task_status.py
            │   └── priority.py
            ├── ports/
            │   ├── __init__.py
            │   ├── task_repository.py
            │   └── project_repository.py
            └── exceptions.py
```

---

## 📝 Instrucciones

### Paso 1: Crear los Value Objects

Abre `starter/src/domain/value_objects/task_status.py` y descomenta el código:

```python
# Los value objects son inmutables y se comparan por valor
# TaskStatus representa los estados posibles de una tarea
```

### Paso 2: Crear la Entidad Task

Abre `starter/src/domain/entities/task.py` y descomenta el código:

```python
# La entidad Task tiene:
# - Identidad única (id)
# - Estado mutable controlado
# - Comportamiento que encapsula reglas de negocio
```

### Paso 3: Definir los Ports

Abre `starter/src/domain/ports/task_repository.py` y descomenta el código:

```python
# Los ports definen contratos usando Protocol
# El dominio dice QUÉ necesita, no CÓMO se implementa
```

### Paso 4: Crear Excepciones de Dominio

Abre `starter/src/domain/exceptions.py` y descomenta el código.

---

## ⏱️ Duración Estimada

45 minutos

---

## ✅ Criterios de Éxito

- [ ] TaskStatus es un Enum con los 4 estados
- [ ] Priority es un IntEnum ordenable
- [ ] Task tiene factory method `create()`
- [ ] Task tiene métodos `assign_to()`, `start()`, `complete()`
- [ ] Los métodos validan el estado antes de modificar
- [ ] TaskRepository es un Protocol con métodos CRUD
- [ ] Las excepciones expresan errores del dominio
