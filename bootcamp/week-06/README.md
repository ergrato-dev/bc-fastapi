# 📚 Semana 06: Relaciones en SQLAlchemy + Service Layer

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Implementar relaciones uno a muchos (1:N) entre modelos
- ✅ Implementar relaciones muchos a muchos (N:M) con tablas asociativas
- ✅ Realizar queries eficientes con joins y eager/lazy loading
- ✅ Entender el patrón Service Layer y su propósito
- ✅ Separar lógica de negocio de los endpoints (routers)
- ✅ Estructurar proyectos FastAPI con capas de responsabilidad

---

## 📋 Contenidos

### 1. Teoría

| # | Tema | Archivo |
|---|------|---------|
| 01 | Relaciones Uno a Muchos (1:N) | [01-relaciones-uno-a-muchos.md](1-teoria/01-relaciones-uno-a-muchos.md) |
| 02 | Relaciones Muchos a Muchos (N:M) | [02-relaciones-muchos-a-muchos.md](1-teoria/02-relaciones-muchos-a-muchos.md) |
| 03 | Queries con Relaciones | [03-queries-con-relaciones.md](1-teoria/03-queries-con-relaciones.md) |
| 04 | Introducción al Service Layer | [04-introduccion-service-layer.md](1-teoria/04-introduccion-service-layer.md) |
| 05 | Implementando Servicios | [05-implementando-servicios.md](1-teoria/05-implementando-servicios.md) |

### 2. Prácticas

| # | Ejercicio | Duración |
|---|-----------|----------|
| 01 | [Relación 1:N - Author → Posts](2-practicas/ejercicio-01-relacion-uno-a-muchos/) | 40 min |
| 02 | [Relación N:M - Posts ↔ Tags](2-practicas/ejercicio-02-relacion-muchos-a-muchos/) | 40 min |
| 03 | [Queries con Relaciones](2-practicas/ejercicio-03-queries-relaciones/) | 35 min |
| 04 | [Refactorizar a Services](2-practicas/ejercicio-04-service-layer/) | 45 min |

### 3. Proyecto

**Blog API con Service Layer** - API completa para un blog con:
- Authors, Posts y Tags
- Relaciones 1:N y N:M
- Arquitectura de capas (Routers → Services → Models)

[📁 Ver proyecto](3-proyecto/)

---

## 🏗️ Arquitectura de Esta Semana

Esta semana introducimos el **Service Layer**:

```
┌─────────────────────────────────────────────────────────┐
│                      ANTES (Week-05)                    │
├─────────────────────────────────────────────────────────┤
│   Router/Endpoint                                       │
│   ├── Validación (Pydantic)                            │
│   ├── Lógica de negocio     ← Todo mezclado            │
│   ├── Acceso a DB                                       │
│   └── Response                                          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                      AHORA (Week-06)                    │
├─────────────────────────────────────────────────────────┤
│   Router/Endpoint                                       │
│   ├── Validación (Pydantic)                            │
│   └── Llama a Service                                   │
│                    ↓                                    │
│   Service                                               │
│   ├── Lógica de negocio     ← Separado                 │
│   └── Acceso a DB                                       │
└─────────────────────────────────────────────────────────┘
```

### Estructura de archivos

```
src/
├── main.py              # FastAPI app
├── database.py          # Engine, Session
├── routers/             # ← Endpoints HTTP
│   ├── __init__.py
│   ├── authors.py
│   └── posts.py
├── services/            # ← NUEVO: Lógica de negocio
│   ├── __init__.py
│   ├── author_service.py
│   └── post_service.py
├── models/              # SQLAlchemy Models
│   ├── __init__.py
│   ├── author.py
│   └── post.py
└── schemas/             # Pydantic Schemas
    ├── __init__.py
    ├── author.py
    └── post.py
```

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| Teoría (5 temas) | 2 horas |
| Prácticas (4 ejercicios) | 2.5 horas |
| Proyecto | 1.5 horas |
| **Total** | **6 horas** |

---

## 📚 Requisitos Previos

- ✅ Week-05: SQLAlchemy ORM básico
- ✅ CRUD completo con FastAPI
- ✅ Pydantic schemas
- ✅ Dependency Injection (`Depends`)

---

## 📦 Entregables

1. **Ejercicios completados**: 4 ejercicios con código funcional
2. **Proyecto Blog API**: API con relaciones y services implementados
3. **Tests básicos**: Endpoints probados con Swagger

---

## 🔗 Navegación

| ← Anterior | Actual | Siguiente → |
|------------|--------|-------------|
| [Semana 05: SQLAlchemy ORM](../week-05/README.md) | **Semana 06** | [Semana 07: Repository Pattern](../week-07/README.md) |

---

## 📖 Recursos

- [SQLAlchemy Relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html)
- [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Service Layer Pattern](https://martinfowler.com/eaaCatalog/serviceLayer.html)
