# 📋 Práctica 02: Application Services

## 📋 Descripción

En esta práctica aprenderás a crear el **Application Layer** con Use Cases, DTOs y Application Services. Esta capa orquesta el dominio sin contener lógica de negocio.

---

## 🎯 Objetivos

- Implementar Use Cases para cada operación
- Crear Commands y Queries inmutables
- Diseñar DTOs de entrada y salida
- Usar Application Services como fachada
- Manejar errores de aplicación

---

## 📁 Estructura del Ejercicio

```
02-application-services/
├── README.md
└── starter/
    ├── pyproject.toml
    └── src/
        ├── __init__.py
        ├── domain/                    # Copiado de práctica 01
        │   └── ...
        └── application/
            ├── __init__.py
            ├── use_cases/
            │   ├── __init__.py
            │   ├── create_task.py
            │   ├── assign_task.py
            │   ├── complete_task.py
            │   └── get_tasks.py
            ├── dtos/
            │   ├── __init__.py
            │   └── task_dtos.py
            ├── services/
            │   ├── __init__.py
            │   └── task_service.py
            └── exceptions.py
```

---

## ⏱️ Duración Estimada

45 minutos

---

## ✅ Criterios de Éxito

- [ ] CreateTaskCommand es inmutable (frozen=True)
- [ ] CreateTaskUseCase orquesta sin lógica de negocio
- [ ] TaskDTO tiene factory method from_entity()
- [ ] TaskService agrupa use cases relacionados
- [ ] ApplicationError es distinta de DomainError
