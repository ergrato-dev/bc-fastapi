# 📅 Semana 05: SQLAlchemy ORM - Introducción

## 🎯 Objetivos de la Semana

Al finalizar esta semana, serás capaz de:

- ✅ Entender qué es un ORM y sus beneficios
- ✅ Configurar SQLAlchemy 2.x con FastAPI
- ✅ Definir modelos de datos como clases Python
- ✅ Realizar operaciones CRUD con SQLAlchemy
- ✅ Integrar bases de datos en endpoints de FastAPI

---

## 📚 Contenido

### 1. Teoría

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-introduccion-orm.md](1-teoria/01-introduccion-orm.md) | ¿Qué es un ORM? SQLAlchemy vs SQL raw | 20 min |
| [02-configuracion-sqlalchemy.md](1-teoria/02-configuracion-sqlalchemy.md) | Engine, Session, Base declarativa | 25 min |
| [03-modelos-declarativos.md](1-teoria/03-modelos-declarativos.md) | Definir tablas como clases Python | 25 min |
| [04-operaciones-crud.md](1-teoria/04-operaciones-crud.md) | Create, Read, Update, Delete | 30 min |
| [05-integracion-fastapi.md](1-teoria/05-integracion-fastapi.md) | Dependency injection y sessions | 25 min |

### 2. Prácticas

| Ejercicio | Tema | Duración |
|-----------|------|----------|
| [ejercicio-01](2-practicas/ejercicio-01-configuracion/) | Configurar SQLAlchemy con SQLite | 30 min |
| [ejercicio-02](2-practicas/ejercicio-02-modelos/) | Crear modelos declarativos | 35 min |
| [ejercicio-03](2-practicas/ejercicio-03-crud/) | Operaciones CRUD básicas | 40 min |
| [ejercicio-04](2-practicas/ejercicio-04-fastapi-db/) | Integrar con FastAPI | 35 min |

### 3. Proyecto

| Proyecto | Descripción | Duración |
|----------|-------------|----------|
| [Library API](3-proyecto/) | API de biblioteca con libros y autores | 90 min |

---

## 🗂️ Estructura de la Semana

```
week-05/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
│   ├── 01-orm-concept.svg
│   ├── 02-sqlalchemy-architecture.svg
│   └── 03-crud-flow.svg
├── 1-teoria/
│   ├── 01-introduccion-orm.md
│   ├── 02-configuracion-sqlalchemy.md
│   ├── 03-modelos-declarativos.md
│   ├── 04-operaciones-crud.md
│   └── 05-integracion-fastapi.md
├── 2-practicas/
│   ├── README.md
│   ├── ejercicio-01-configuracion/
│   ├── ejercicio-02-modelos/
│   ├── ejercicio-03-crud/
│   └── ejercicio-04-fastapi-db/
├── 3-proyecto/
│   ├── README.md
│   ├── starter/
│   └── solution/
├── 4-recursos/
│   ├── README.md
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo | Porcentaje |
|-----------|--------|------------|
| Teoría | 2 horas | 33% |
| Prácticas | 2.5 horas | 42% |
| Proyecto | 1.5 horas | 25% |
| **Total** | **6 horas** | **100%** |

---

## 📋 Requisitos Previos

Antes de comenzar esta semana, debes:

- ✅ Completar Semana 04 (Responses y Manejo de Errores)
- ✅ Entender async/await en Python
- ✅ Conocer Pydantic para validación
- ✅ Saber crear endpoints en FastAPI

---

## 🔧 Herramientas de la Semana

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| SQLAlchemy | 2.0+ | ORM principal |
| SQLite | 3.47+ | Base de datos de desarrollo |
| aiosqlite | 0.20+ | Driver async para SQLite |

---

## 📌 Entregables

1. **Ejercicios completados** (4 ejercicios)
2. **Proyecto Library API** funcionando con:
   - CRUD de libros
   - CRUD de autores
   - Documentación OpenAPI
3. **Reflexión** sobre ventajas de usar ORM

---

## 🔗 Navegación

| ← Anterior | Actual | Siguiente → |
|------------|--------|-------------|
| [Semana 04: Responses y Errores](../week-04/) | **Semana 05** | [Semana 06: Relaciones](../week-06/) |

---

## 💡 Tip de la Semana

> **SQLAlchemy 2.0** introdujo un nuevo estilo "2.0" más pythónico y con mejor soporte para async. Este bootcamp usa exclusivamente el estilo moderno.

```python
# ✅ Estilo SQLAlchemy 2.0 (moderno)
from sqlalchemy import select
stmt = select(User).where(User.email == email)
result = session.execute(stmt)
user = result.scalar_one_or_none()

# ❌ Estilo legacy 1.x (NO usar)
user = session.query(User).filter_by(email=email).first()
```

---

## 📚 Recursos Rápidos

- [SQLAlchemy 2.0 Docs](https://docs.sqlalchemy.org/en/20/)
- [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [Pydantic + SQLAlchemy](https://docs.pydantic.dev/latest/concepts/models/#orm-mode)
