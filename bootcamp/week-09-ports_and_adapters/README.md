# 📦 Semana 09: Ports & Adapters (Inversión de Dependencias)

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Comprender el patrón Ports & Adapters y su propósito
- ✅ Implementar interfaces (protocols) en Python para definir contratos
- ✅ Aplicar el Principio de Inversión de Dependencias (DIP)
- ✅ Separar la lógica de negocio de los detalles de infraestructura
- ✅ Crear adapters intercambiables para diferentes implementaciones
- ✅ Facilitar el testing mediante inyección de dependencias
- ✅ Preparar el código para la arquitectura hexagonal completa

---

## 📚 Requisitos Previos

Antes de comenzar esta semana, debes:

- ✅ Haber completado la **Semana 08** (Arquitectura en Capas Completa)
- ✅ Dominar el patrón Repository y Service Layer
- ✅ Entender DTOs y mappers
- ✅ Conocer el sistema de dependencias de FastAPI
- ✅ Familiaridad con type hints y genéricos en Python

---

## 🗂️ Estructura de la Semana

```
week-09-ports_and_adapters/
├── README.md                      # Este archivo
├── rubrica-evaluacion.md          # Criterios de evaluación
├── 0-assets/                      # Diagramas y recursos visuales
│   ├── 01-ports-adapters-pattern.svg
│   ├── 02-dependency-inversion.svg
│   ├── 03-protocols-interfaces.svg
│   ├── 04-adapters-implementations.svg
│   └── 05-testing-with-ports.svg
├── 1-teoria/                      # Material teórico
│   ├── 01-introduccion-ports-adapters.md
│   ├── 02-protocols-python.md
│   ├── 03-dependency-inversion-principle.md
│   ├── 04-implementando-adapters.md
│   └── 05-testing-estrategias.md
├── 2-practicas/                   # Ejercicios guiados
│   ├── 01-definir-ports/
│   ├── 02-crear-adapters/
│   ├── 03-inyeccion-dependencias/
│   └── 04-testing-con-mocks/
├── 3-proyecto/                    # Proyecto integrador
│   ├── README.md
│   └── starter/
├── 4-recursos/                    # Material complementario
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/                    # Términos clave
    └── README.md
```

---

## 📝 Contenidos

### 1. Teoría (1-teoria/)

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-introduccion-ports-adapters.md](1-teoria/01-introduccion-ports-adapters.md) | Patrón Ports & Adapters | 25 min |
| [02-protocols-python.md](1-teoria/02-protocols-python.md) | Protocols en Python | 25 min |
| [03-dependency-inversion-principle.md](1-teoria/03-dependency-inversion-principle.md) | Principio de Inversión de Dependencias | 20 min |
| [04-implementando-adapters.md](1-teoria/04-implementando-adapters.md) | Implementación de Adapters | 25 min |
| [05-testing-estrategias.md](1-teoria/05-testing-estrategias.md) | Estrategias de Testing | 20 min |

### 2. Prácticas (2-practicas/)

| Práctica | Tema | Duración |
|----------|------|----------|
| [01-definir-ports](2-practicas/01-definir-ports/) | Definir Ports con Protocols | 40 min |
| [02-crear-adapters](2-practicas/02-crear-adapters/) | Crear Adapters concretos | 45 min |
| [03-inyeccion-dependencias](2-practicas/03-inyeccion-dependencias/) | Inyección de Dependencias avanzada | 40 min |
| [04-testing-con-mocks](2-practicas/04-testing-con-mocks/) | Testing con Fake Adapters | 45 min |

### 3. Proyecto (3-proyecto/)

| Proyecto | Descripción | Duración |
|----------|-------------|----------|
| [Notification Service](3-proyecto/) | Sistema de notificaciones multi-canal | 2 horas |

---

## ⏱️ Distribución del Tiempo (6 horas)

```
┌─────────────────────────────────────────────────────────────┐
│                    SEMANA 09 - 6 HORAS                      │
├─────────────────────────────────────────────────────────────┤
│  Teoría (2h)          ████████████░░░░░░░░░░░░░░░░░░  33%  │
│  Prácticas (2.75h)    ░░░░░░░░░░░░████████████████░░░  46%  │
│  Proyecto (1.25h)     ░░░░░░░░░░░░░░░░░░░░░░░░░░░████  21%  │
└─────────────────────────────────────────────────────────────┘
```

### Distribución Recomendada

| Día | Actividad | Tiempo |
|-----|-----------|--------|
| Día 1 | Teoría 01-03 + Práctica 01 | 2h |
| Día 2 | Teoría 04-05 + Práctica 02 | 2h |
| Día 3 | Prácticas 03-04 | 1.5h |
| Día 4 | Proyecto | 0.5h |

---

## 🔑 Conceptos Clave

### ¿Qué es Ports & Adapters?

```
┌──────────────────────────────────────────────────────────────┐
│                      APLICACIÓN                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                   DOMINIO/NEGOCIO                      │  │
│  │              (Lógica de negocio pura)                  │  │
│  └────────────────────────────────────────────────────────┘  │
│           ▲                                    ▲              │
│           │ PORT                               │ PORT         │
│           │ (interface)                        │ (interface)  │
│           │                                    │              │
│  ┌────────┴────────┐                ┌─────────┴─────────┐    │
│  │  ADAPTER        │                │   ADAPTER         │    │
│  │  (SQLAlchemy)   │                │   (Email SMTP)    │    │
│  └─────────────────┘                └───────────────────┘    │
│           │                                    │              │
│           ▼                                    ▼              │
│      PostgreSQL                          Servidor SMTP       │
└──────────────────────────────────────────────────────────────┘
```

### Ports (Interfaces)

```python
from typing import Protocol

class UserRepository(Protocol):
    """Port: define el contrato para acceso a usuarios"""
    
    async def get_by_id(self, user_id: int) -> User | None: ...
    async def save(self, user: User) -> User: ...
    async def delete(self, user_id: int) -> bool: ...
```

### Adapters (Implementaciones)

```python
class SQLAlchemyUserRepository:
    """Adapter: implementación con SQLAlchemy"""
    
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, user_id: int) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        return result.scalar_one_or_none()
    
    # ... más métodos
```

### Inversión de Dependencias

```python
# ❌ ANTES: Dependencia directa (acoplamiento)
class UserService:
    def __init__(self):
        self.repo = SQLAlchemyUserRepository()  # Acoplado!

# ✅ DESPUÉS: Depende de abstracción (desacoplado)
class UserService:
    def __init__(self, repo: UserRepository):  # Protocol!
        self.repo = repo
```

---

## 📌 Entregable

**Proyecto: [Notification Service](3-proyecto/)**

Sistema de notificaciones multi-canal funcionando con:

- [ ] Ports definidos para todos los canales
- [ ] Adapters: Email, SMS, Push, Webhook
- [ ] Service layer usando ports (no adapters directos)
- [ ] Tests con fake adapters
- [ ] API REST funcionando

---

## 🔗 Navegación

| ← Anterior | Inicio | Siguiente → |
|:-----------|:------:|------------:|
| [Semana 08: Arquitectura en Capas](../week-08-arquitectura_en_capas_completa/README.md) | [Índice](../../README.md) | [Semana 10: Hexagonal Completo](../week-10-arquitectura_hexagonal_completa/README.md) |

---

## 📚 Recursos Adicionales

- [Documentación oficial de Python - Protocols](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [FastAPI - Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Clean Architecture - Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Hexagonal Architecture - Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)

---

## ✅ Checklist de la Semana

Antes de avanzar a la semana 10, verifica:

- [ ] Entiendo la diferencia entre Port y Adapter
- [ ] Puedo definir Protocols en Python
- [ ] Comprendo el Principio de Inversión de Dependencias
- [ ] Sé crear adapters intercambiables
- [ ] Puedo testear usando fake adapters
- [ ] Mi código de negocio no depende de infraestructura
- [ ] El proyecto Notification Service funciona correctamente

---

_Semana 09 de 16 | Nivel: Intermedio | Arquitectura: Ports & Adapters_
