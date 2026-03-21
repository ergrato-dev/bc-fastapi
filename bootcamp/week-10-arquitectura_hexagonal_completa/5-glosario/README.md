# 📖 Glosario - Semana 10: Arquitectura Hexagonal

## A

### Adapter (Adaptador)
Implementación concreta de un puerto. Traduce entre el mundo externo y el dominio. Ejemplos: `InMemoryTaskRepository`, `FastAPIRouter`.

### Application Layer (Capa de Aplicación)
Capa que orquesta los casos de uso. Coordina entidades del dominio pero no contiene lógica de negocio. Contiene Services, Commands, Queries y DTOs.

### Application Service
Clase que implementa un caso de uso específico. Recibe Commands/Queries y retorna DTOs. No contiene lógica de negocio, solo orquestación.

---

## B

### Bounded Context
Límite conceptual donde un modelo de dominio es válido y consistente. Cada bounded context puede tener su propia arquitectura hexagonal.

### Business Logic
Ver **Domain Logic**.

---

## C

### Clean Architecture
Arquitectura propuesta por Robert C. Martin que organiza el código en capas concéntricas con dependencias hacia el centro.

### Command
Objeto inmutable que representa una intención de cambio en el sistema. Ejemplo: `CreateTaskCommand`, `AssignTaskCommand`.

### Composition Root
Punto único donde se ensamblan todas las dependencias de la aplicación. En FastAPI típicamente es `main.py`.

---

## D

### Dependency Injection (DI)
Patrón donde las dependencias se pasan desde fuera en lugar de crearse internamente. Permite desacoplamiento y testeo.

### Dependency Inversion Principle (DIP)
Principio SOLID: los módulos de alto nivel no deben depender de módulos de bajo nivel; ambos deben depender de abstracciones.

### Domain
El núcleo del negocio. Contiene entidades, value objects, reglas de negocio y puertos.

### Domain Error
Excepción que representa una violación de reglas de negocio. Es independiente de la infraestructura.

### Domain Layer (Capa de Dominio)
Capa central de la arquitectura hexagonal. Contiene la lógica de negocio pura, sin dependencias externas.

### Domain Logic
Reglas y comportamientos del negocio. Debe estar encapsulada en entidades y domain services.

### Domain Service
Servicio que contiene lógica de negocio que no pertenece naturalmente a una entidad específica.

### Driven Adapter (Adaptador Secundario)
Adaptador que el dominio "conduce" para acceder a recursos externos. Ejemplo: repositorios de base de datos.

### Driving Adapter (Adaptador Primario)
Adaptador que "conduce" al dominio. Inicia las acciones. Ejemplo: controladores HTTP, CLI.

### DTO (Data Transfer Object)
Objeto simple para transferir datos entre capas. No contiene lógica de negocio.

---

## E

### Entity (Entidad)
Objeto del dominio con identidad única y ciclo de vida. Se distingue por su ID, no por sus atributos. Ejemplo: `Task`, `User`.

---

## F

### Factory Method
Patrón de diseño donde un método estático crea instancias de una clase. Ejemplo: `Task.create()`.

---

## H

### Hexagonal Architecture
Arquitectura de software propuesta por Alistair Cockburn. Organiza el código con el dominio en el centro, aislado mediante puertos y adaptadores.

---

## I

### Infrastructure Layer (Capa de Infraestructura)
Capa externa que implementa los puertos. Contiene adaptadores, frameworks, bases de datos y servicios externos.

### Inversion of Control (IoC)
Principio donde el control del flujo se invierte. El framework llama a tu código, no al revés.

---

## L

### Layered Architecture
Arquitectura tradicional en capas (presentación, negocio, datos). La arquitectura hexagonal es una evolución de este concepto.

---

## O

### Onion Architecture
Arquitectura similar a la hexagonal, propuesta por Jeffrey Palermo. Usa capas concéntricas como una cebolla.

---

## P

### Port (Puerto)
Interfaz que define cómo el dominio interactúa con el exterior. En Python se implementa con `Protocol`. No depende de tecnología específica.

### Ports and Adapters
Nombre alternativo para Arquitectura Hexagonal. Enfatiza los conceptos clave de la arquitectura.

### Protocol (Python)
Mecanismo de Python para definir interfaces mediante structural subtyping. Base para implementar puertos.

---

## Q

### Query
Objeto inmutable que representa una petición de datos sin modificar el estado. Ejemplo: `GetTaskQuery`, `ListTasksQuery`.

---

## R

### Repository Pattern
Patrón que abstrae el acceso a datos detrás de una interfaz similar a una colección. Permite intercambiar implementaciones de persistencia.

### Rich Domain Model
Modelo de dominio donde las entidades contienen tanto datos como comportamiento. Opuesto a Anemic Domain Model.

---

## S

### Service Layer
Capa de servicios que coordina operaciones del dominio. En arquitectura hexagonal corresponde a la Application Layer.

### Singleton
Patrón que garantiza una única instancia de una clase. En Python se puede implementar con `@lru_cache`.

### Structural Subtyping
Sistema de tipos donde la compatibilidad se determina por la estructura, no por herencia explícita. Base de Protocol en Python.

---

## U

### Use Case
Operación específica del sistema que representa un flujo de negocio completo. Se implementa en la Application Layer.

---

## V

### Value Object
Objeto del dominio sin identidad, definido solo por sus atributos. Es inmutable y se compara por valor. Ejemplo: `TaskStatus`, `Priority`.

---

## Diagrama de Relaciones

```
┌─────────────────────────────────────────────────────────────┐
│                    INFRASTRUCTURE                            │
│  ┌─────────────┐                      ┌─────────────┐       │
│  │   Driving   │                      │   Driven    │       │
│  │  Adapters   │                      │  Adapters   │       │
│  │  (API REST) │                      │ (Database)  │       │
│  └──────┬──────┘                      └──────┬──────┘       │
│         │                                    │              │
│         ▼                                    ▼              │
│  ┌─────────────────────────────────────────────────┐       │
│  │                   PORTS                          │       │
│  │        (Protocol interfaces)                     │       │
│  └─────────────────────────────────────────────────┘       │
│                          │                                  │
├──────────────────────────┼──────────────────────────────────┤
│                          ▼                                  │
│  ┌─────────────────────────────────────────────────┐       │
│  │              APPLICATION LAYER                   │       │
│  │    Commands │ Queries │ DTOs │ Services          │       │
│  └─────────────────────────────────────────────────┘       │
│                          │                                  │
│                          ▼                                  │
│  ┌─────────────────────────────────────────────────┐       │
│  │               DOMAIN LAYER                       │       │
│  │    Entities │ Value Objects │ Domain Services    │       │
│  └─────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

---

_Glosario actualizado: Diciembre 2025_
