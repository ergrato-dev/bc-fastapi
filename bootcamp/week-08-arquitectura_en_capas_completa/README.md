# 📘 Semana 07: Arquitectura en Capas Completa

## 🎯 Objetivos de la Semana

Al finalizar esta semana, serás capaz de:

- ✅ Consolidar la arquitectura Router → Service → Repository
- ✅ Implementar DTOs (Data Transfer Objects) para cada capa
- ✅ Aplicar el principio de separación de responsabilidades
- ✅ Manejar errores de forma estructurada por capas
- ✅ Crear factories y builders para objetos complejos
- ✅ Entender el flujo de datos entre capas

---

## 📋 Contenidos

### 1. Teoría

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-arquitectura-capas.md](1-teoria/01-arquitectura-capas.md) | Arquitectura en capas MVC | 25 min |
| [02-dtos-mappers.md](1-teoria/02-dtos-mappers.md) | DTOs y Mappers entre capas | 25 min |
| [03-manejo-errores-capas.md](1-teoria/03-manejo-errores-capas.md) | Errores estructurados por capa | 20 min |
| [04-factories-builders.md](1-teoria/04-factories-builders.md) | Patrones Factory y Builder | 20 min |
| [05-flujo-datos.md](1-teoria/05-flujo-datos.md) | Flujo completo Request → Response | 20 min |

### 2. Prácticas

| Práctica | Tema | Duración |
|----------|------|----------|
| [01-estructura-capas](2-practicas/01-estructura-capas/) | Organización de proyecto en capas | 30 min |
| [02-dtos-conversiones](2-practicas/02-dtos-conversiones/) | DTOs y conversiones | 30 min |
| [03-error-handling](2-practicas/03-error-handling/) | Manejo de errores por capa | 30 min |
| [04-flujo-completo](2-practicas/04-flujo-completo/) | Flujo Request → Response | 30 min |

### 3. Proyecto

| Proyecto | Descripción | Duración |
|----------|-------------|----------|
| [E-Commerce API](3-proyecto/) | API completa con arquitectura en capas | 3-4 horas |

---

## 🏗️ Arquitectura de la Semana

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                            │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    Routers (FastAPI)                     │    │
│  │         HTTP Request/Response, Validación                │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────┬───────────────────────────────────┘
                              │ DTOs
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                      Services                            │    │
│  │         Lógica de Negocio, Orquestación                 │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────┬───────────────────────────────────┘
                              │ Entities
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DATA ACCESS LAYER                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    Repositories                          │    │
│  │         Acceso a Datos, Persistencia                    │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────┬───────────────────────────────────┘
                              │ SQL
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATABASE                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Requisitos Previos

- ✅ Week-05: SQLAlchemy básico
- ✅ Week-06: Service Layer
- ✅ Week-07: Repository Pattern y Unit of Work

---

## ⏱️ Distribución del Tiempo (6 horas)

| Actividad | Tiempo |
|-----------|--------|
| Teoría | 2 horas |
| Prácticas | 2 horas |
| Proyecto | 2 horas |

---

## 📌 Entregable

**Proyecto: [E-Commerce API](3-proyecto/)**

API de e-commerce funcionando con arquitectura MVC completa:

- [ ] Presentation Layer (routers + schemas)
- [ ] Application Layer (services)
- [ ] Data Access Layer (repositories)
- [ ] DTOs y mappers implementados

---

## 📌 Conceptos Clave

- **Presentation Layer**: Maneja HTTP, serialización, validación de entrada
- **Application Layer**: Lógica de negocio, casos de uso, orquestación
- **Data Access Layer**: Persistencia, queries, transacciones
- **DTO (Data Transfer Object)**: Objetos para transferir datos entre capas
- **Mapper**: Convierte entre DTOs y entidades

---

## 🔗 Navegación

| Anterior | Siguiente |
|----------|-----------|
| [← Semana 07: Repository Pattern](../week-07-repository_pattern/README.md) | [Semana 09: Ports & Adapters →](../week-09-ports_and_adapters/README.md) |
