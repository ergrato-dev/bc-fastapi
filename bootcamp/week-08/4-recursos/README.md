# 📚 Recursos - Semana 08

## Arquitectura en Capas Completa

### 📖 Documentación Oficial

| Recurso | Descripción |
|---------|-------------|
| [FastAPI - Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) | Estructurar proyectos grandes |
| [FastAPI - Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) | Sistema de inyección de dependencias |
| [FastAPI - Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) | Manejo de errores y excepciones |
| [Pydantic - Model Config](https://docs.pydantic.dev/latest/concepts/config/) | Configuración de modelos |
| [SQLAlchemy - Session Basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) | Manejo de sesiones |

---

## 🎥 Videografía

### Arquitectura de Software

| Video | Canal | Duración |
|-------|-------|----------|
| [Clean Architecture with Python](https://www.youtube.com/watch?v=C7MRkqP5NRI) | ArjanCodes | 25 min |
| [Repository Pattern in Python](https://www.youtube.com/watch?v=9ymRLDfnDKg) | ArjanCodes | 20 min |
| [Dependency Injection in FastAPI](https://www.youtube.com/watch?v=0BVkgGVWTz4) | Pretty Printed | 15 min |

### FastAPI Avanzado

| Video | Canal | Duración |
|-------|-------|----------|
| [FastAPI Project Structure](https://www.youtube.com/watch?v=895e0H6HTNs) | Bitfumes | 30 min |
| [Exception Handling Best Practices](https://www.youtube.com/watch?v=rtJBfQpWGrI) | Tech With Tim | 18 min |

---

## 📕 Libros Gratuitos

### Arquitectura y Patrones

| Libro | Autor | Enlace |
|-------|-------|--------|
| Clean Architecture (resumen) | Robert C. Martin | [Refactoring Guru](https://refactoring.guru/design-patterns) |
| Patterns of Enterprise Application | Martin Fowler | [Catalog](https://martinfowler.com/eaaCatalog/) |

---

## 🔗 Webgrafía

### Artículos Recomendados

| Artículo | Tema |
|----------|------|
| [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html) | Patrón Repository |
| [Service Layer](https://martinfowler.com/eaaCatalog/serviceLayer.html) | Capa de servicios |
| [Data Transfer Object](https://martinfowler.com/eaaCatalog/dataTransferObject.html) | DTOs |
| [Layered Architecture](https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch01.html) | Arquitectura en capas |

### Blogs y Tutoriales

| Recurso | Descripción |
|---------|-------------|
| [TestDriven.io - FastAPI](https://testdriven.io/blog/topics/fastapi/) | Tutoriales avanzados |
| [Real Python - FastAPI](https://realpython.com/fastapi-python-web-apis/) | Guía completa |
| [Patrick Loeber - FastAPI](https://www.python-engineer.com/courses/fastapi-basics/) | Curso gratuito |

---

## 🛠️ Herramientas Útiles

| Herramienta | Uso |
|-------------|-----|
| [HTTPie](https://httpie.io/) | Cliente HTTP moderno |
| [Insomnia](https://insomnia.rest/) | Testing de APIs |
| [DB Browser for SQLite](https://sqlitebrowser.org/) | Visualizar base de datos |
| [Pydantic Plugin VSCode](https://marketplace.visualstudio.com/items?itemName=pedroafonseca.pydantic) | Autocompletado Pydantic |

---

## 📊 Diagramas de Referencia

### Flujo de Capas

```
┌─────────────────────────────────────────────────────┐
│                   PRESENTATION                       │
│              (Routers / Controllers)                 │
│         Recibe HTTP → Valida → Responde             │
└─────────────────────┬───────────────────────────────┘
                      │ DTOs
┌─────────────────────▼───────────────────────────────┐
│                   APPLICATION                        │
│                   (Services)                         │
│         Orquesta → Lógica de Negocio               │
└─────────────────────┬───────────────────────────────┘
                      │ Entities
┌─────────────────────▼───────────────────────────────┐
│                  DATA ACCESS                         │
│                 (Repositories)                       │
│         Abstrae → Persistencia                      │
└─────────────────────┬───────────────────────────────┘
                      │ SQL
┌─────────────────────▼───────────────────────────────┐
│                   DATABASE                           │
│              (SQLite / PostgreSQL)                   │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Próximos Pasos

Después de dominar la arquitectura en capas, explora:

1. **Semana 09**: Arquitectura Hexagonal (Ports & Adapters)
2. **Testing**: Pruebas unitarias por capa
3. **Async**: Repositories y Services asíncronos
4. **Caching**: Redis para optimización

---

## 📝 Notas del Instructor

- El proyecto E-Commerce consolida todos los conceptos
- Enfatizar la separación de responsabilidades
- El OrderService es el mejor ejemplo de orquestación
- Los exception handlers centralizan el manejo de errores
