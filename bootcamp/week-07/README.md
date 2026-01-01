# 📘 Semana 07: Repository Pattern

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Entender el **Repository Pattern** y su propósito
- ✅ Separar el **acceso a datos** de la **lógica de negocio**
- ✅ Implementar **repositorios genéricos** reutilizables
- ✅ Aplicar el patrón **Unit of Work** para transacciones
- ✅ Facilitar el **testing** con repositorios mock
- ✅ Evolucionar la arquitectura: Router → Service → **Repository**

---

## 📋 Contexto Arquitectónico

### Evolución del Bootcamp

```
Semana 05: Monolítico      → Todo en endpoints
Semana 06: + Service Layer → Lógica separada
Semana 07: + Repository    → Acceso a datos separado  ← ESTAMOS AQUÍ
Semana 08: MVC Completo    → Arquitectura por capas
```

### Arquitectura Actual (Semana 07)

```
┌─────────────────────────────────────────────────────┐
│                    HTTP Request                      │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│              📡 Router Layer (HTTP)                  │
│         Validación HTTP, respuestas, status         │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│              ⚙️ Service Layer (Lógica)              │
│      Reglas de negocio, validaciones, orquestación  │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│           🗄️ Repository Layer (Datos)        ← NEW  │
│        CRUD, queries, abstracción de BD             │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│                   💾 Database                        │
└─────────────────────────────────────────────────────┘
```

---

## 📚 Requisitos Previos

Antes de comenzar, asegúrate de:

- ✅ Haber completado la **Semana 06** (Service Layer)
- ✅ Entender relaciones SQLAlchemy (1:N, N:M)
- ✅ Conocer el patrón Service Layer
- ✅ Saber usar `Depends()` de FastAPI

---

## 🗂️ Estructura de la Semana

```
week-07/
├── README.md                          # Este archivo
├── rubrica-evaluacion.md              # Criterios de evaluación
├── 0-assets/                          # Diagramas SVG
│   ├── 01-repository-pattern.svg
│   ├── 02-capas-arquitectura.svg
│   └── 03-unit-of-work.svg
├── 1-teoria/
│   ├── 01-introduccion-repository-pattern.md
│   ├── 02-repositorio-generico.md
│   ├── 03-repositorios-especificos.md
│   ├── 04-unit-of-work.md
│   └── 05-testing-con-repositories.md
├── 2-practicas/
│   ├── 01-primer-repositorio/
│   ├── 02-repositorio-generico/
│   ├── 03-integracion-service-repository/
│   └── 04-unit-of-work/
├── 3-proyecto/
│   ├── README.md
│   ├── starter/                       # Código inicial
│   └── solution/                      # Solución (oculta)
├── 4-recursos/
│   └── README.md
└── 5-glosario/
    └── README.md
```

---

## 📝 Contenidos

### 1️⃣ Teoría

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-introduccion-repository-pattern.md](1-teoria/01-introduccion-repository-pattern.md) | Qué es y por qué usar Repository | 20 min |
| [02-repositorio-generico.md](1-teoria/02-repositorio-generico.md) | Implementación de BaseRepository | 25 min |
| [03-repositorios-especificos.md](1-teoria/03-repositorios-especificos.md) | Repositorios con métodos custom | 20 min |
| [04-unit-of-work.md](1-teoria/04-unit-of-work.md) | Patrón Unit of Work | 25 min |
| [05-testing-con-repositories.md](1-teoria/05-testing-con-repositories.md) | Testing con mocks y fakes | 20 min |

### 2️⃣ Prácticas

| Práctica | Tema | Duración |
|----------|------|----------|
| [01-primer-repositorio](2-practicas/01-primer-repositorio/) | Crear repositorio básico | 30 min |
| [02-repositorio-generico](2-practicas/02-repositorio-generico/) | Implementar BaseRepository | 35 min |
| [03-integracion-service-repository](2-practicas/03-integracion-service-repository/) | Conectar Service con Repository | 30 min |
| [04-unit-of-work](2-practicas/04-unit-of-work/) | Implementar Unit of Work | 35 min |

### 3️⃣ Proyecto

| Proyecto | Descripción | Duración |
|----------|-------------|----------|
| [Task Manager API](3-proyecto/) | API de gestión de tareas con Repository Pattern | 2 horas |

---

## ⏱️ Distribución del Tiempo (6 horas)

| Actividad | Tiempo |
|-----------|--------|
| 📚 Teoría | 1.5 h |
| 🔨 Prácticas | 2.5 h |
| 🚀 Proyecto | 2 h |

---

## 🎯 Competencias a Desarrollar

### Técnicas

- Implementar el patrón Repository en Python
- Crear repositorios genéricos con tipado estricto
- Aplicar Unit of Work para transacciones
- Escribir tests con repositorios mock

### Arquitectónicas

- Separar responsabilidades por capas
- Diseñar interfaces para abstracción
- Facilitar el testing mediante inyección de dependencias

---

## 📌 Entregables

1. **Prácticas completadas** (código descomentado y funcionando)
2. **Proyecto Task Manager** con:
   - BaseRepository genérico
   - TaskRepository y UserRepository
   - TaskService usando repositorios
   - Tests unitarios básicos

---

## 🔗 Navegación

| ← Anterior | Inicio | Siguiente → |
|:-----------|:------:|------------:|
| [Semana 06: Relaciones SQLAlchemy](../week-06/README.md) | [Bootcamp](../../README.md) | [Semana 08: MVC Completo](../week-08/README.md) |

---

## 💡 Tip de la Semana

> **"Un repositorio es como un bibliotecario"**: no necesitas saber cómo está organizada la biblioteca internamente, solo le pides el libro que necesitas y él sabe dónde encontrarlo.

---

## 📚 Referencias Rápidas

- [Repository Pattern - Martin Fowler](https://martinfowler.com/eaaCatalog/repository.html)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/tutorial.html)
- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
