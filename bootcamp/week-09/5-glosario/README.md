# 📖 Glosario - Semana 09

## Ports & Adapters (Inversión de Dependencias)

---

## A

### Adapter (Adaptador)
Implementación concreta de un Port. Traduce las operaciones definidas en el puerto a llamadas específicas de una tecnología o servicio externo.

```python
class EmailNotificationSender:
    """Adapter que implementa NotificationSender para email."""
    
    async def send(self, notification: Notification) -> bool:
        # Implementación específica para SMTP
        return await self._send_via_smtp(notification)
```

### Abstract Base Class (ABC)
Clase abstracta en Python que define una interfaz mediante herencia. Los Protocols son una alternativa más flexible basada en duck typing estructural.

---

## B

### Boundary (Frontera)
Límite entre capas de la arquitectura. Los Ports definen las fronteras entre el dominio y la infraestructura.

---

## C

### Clean Architecture
Arquitectura de software propuesta por Robert C. Martin que organiza el código en capas concéntricas, con las reglas de negocio en el centro.

### Composition Root
Punto de la aplicación donde se configuran y ensamblan todas las dependencias. En FastAPI, típicamente está en `dependencies.py`.

---

## D

### Dependency Injection (DI)
Técnica donde las dependencias de un objeto se proporcionan externamente en lugar de crearlas internamente.

```python
# Sin DI (acoplado)
class Service:
    def __init__(self):
        self.repo = MySQLRepository()  # Dependencia fija

# Con DI (desacoplado)
class Service:
    def __init__(self, repo: Repository):
        self.repo = repo  # Dependencia inyectada
```

### Dependency Inversion Principle (DIP)
Principio SOLID que establece:
1. Los módulos de alto nivel no deben depender de módulos de bajo nivel
2. Ambos deben depender de abstracciones

### Domain Layer
Capa central que contiene las entidades y reglas de negocio. No debe depender de ninguna otra capa.

### Driven Port (Puerto Secundario)
Puerto que el dominio usa para comunicarse con servicios externos (base de datos, email, etc.). También llamado "outbound port".

### Driving Port (Puerto Primario)
Puerto que expone la funcionalidad del dominio al mundo exterior (APIs, UI, CLI). También llamado "inbound port".

### Duck Typing
Filosofía de Python donde el tipo de un objeto se determina por sus métodos y propiedades, no por su clase. "If it walks like a duck and quacks like a duck, it's a duck."

---

## F

### Fake
Implementación simplificada de una dependencia usada en testing. A diferencia de un mock, tiene comportamiento funcional real.

```python
class FakeRepository:
    """Fake que almacena en memoria."""
    def __init__(self):
        self._data = {}
    
    async def save(self, entity):
        self._data[entity.id] = entity
        return entity
```

---

## H

### Hexagonal Architecture
Otro nombre para Ports & Adapters. Llamada así porque los diagramas originales mostraban la aplicación como un hexágono con puertos en cada lado.

---

## I

### Inversion of Control (IoC)
Principio donde el flujo de control se invierte: en lugar de que el código llame a frameworks, los frameworks llaman al código. DI es una forma de IoC.

### Interface Segregation
Principio SOLID que establece que los clientes no deben depender de interfaces que no usan. Los Protocols permiten definir interfaces pequeñas y específicas.

---

## L

### Liskov Substitution Principle
Principio SOLID que establece que los objetos de una clase derivada deben poder sustituir a objetos de la clase base sin alterar el comportamiento correcto.

---

## M

### Mock
Objeto que simula el comportamiento de una dependencia y permite verificar interacciones (llamadas a métodos, argumentos, etc.).

---

## O

### Onion Architecture
Variante de Clean Architecture donde las capas se visualizan como anillos de una cebolla, con el dominio en el centro.

---

## P

### Port (Puerto)
Interfaz que define un contrato entre el dominio y el mundo exterior. En Python moderno se implementa con `Protocol`.

```python
from typing import Protocol

class NotificationSender(Protocol):
    """Puerto para envío de notificaciones."""
    
    async def send(self, notification: Notification) -> bool:
        ...
```

### Ports & Adapters
Patrón arquitectónico que separa la lógica de negocio de los detalles de infraestructura mediante puertos (interfaces) y adaptadores (implementaciones).

### Protocol (typing.Protocol)
Clase especial de Python que define una interfaz mediante duck typing estructural. No requiere herencia explícita.

```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Cualquier clase con método render() es Renderable
class Button:
    def render(self) -> str:
        return "<button>Click</button>"
```

---

## R

### Repository Pattern
Patrón que abstrae el acceso a datos detrás de una interfaz de colección. Es un tipo común de Driven Port.

### Runtime Checkable
Decorador que permite usar `isinstance()` con Protocols en tiempo de ejecución.

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Sender(Protocol):
    async def send(self, msg: str) -> bool: ...

# Ahora se puede usar isinstance
isinstance(my_sender, Sender)  # True o False
```

---

## S

### Service Layer
Capa de aplicación que coordina casos de uso. Depende de puertos, no de implementaciones concretas.

### SOLID
Cinco principios de diseño orientado a objetos:
- **S**ingle Responsibility
- **O**pen/Closed
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion

### Spy
Tipo de test double que registra las llamadas que recibe para posterior verificación.

```python
class SpySender:
    def __init__(self):
        self.calls = []
    
    async def send(self, notification):
        self.calls.append(notification)
        return True
    
    def was_called_with(self, notification):
        return notification in self.calls
```

### Structural Subtyping
Sistema de tipos donde la compatibilidad se determina por la estructura (métodos y atributos), no por la herencia. Los Protocols implementan este concepto.

### Stub
Test double que retorna valores predefinidos sin lógica real.

---

## T

### Test Double
Término genérico para objetos que reemplazan dependencias reales en tests. Incluye: Dummy, Stub, Spy, Mock, Fake.

---

## U

### Use Case
Operación de negocio específica que la aplicación puede realizar. En Clean Architecture, los casos de uso están en la capa de aplicación.

---

## Diagrama de Referencia

```
┌─────────────────────────────────────────────────────────────────┐
│                        INFRASTRUCTURE                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   FastAPI   │  │   SQLAlchemy │  │   SMTP Client          │ │
│  │   Router    │  │   Repository │  │   Email Adapter        │ │
│  └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘ │
│         │                │                      │               │
├─────────┼────────────────┼──────────────────────┼───────────────┤
│         │     PORTS      │                      │               │
│         ▼                ▼                      ▼               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   Driving   │  │   Driven    │  │   Driven Port           │ │
│  │   Port      │  │   Port      │  │   (NotificationSender)  │ │
│  │   (API)     │  │ (Repository)│  │                         │ │
│  └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘ │
│         │                │                      │               │
├─────────┼────────────────┼──────────────────────┼───────────────┤
│         │          APPLICATION                  │               │
│         │                │                      │               │
│         └────────────────┼──────────────────────┘               │
│                          ▼                                      │
│                  ┌─────────────┐                                │
│                  │   Service   │                                │
│                  │   Layer     │                                │
│                  └──────┬──────┘                                │
│                         │                                       │
├─────────────────────────┼───────────────────────────────────────┤
│                  DOMAIN │                                       │
│                         ▼                                       │
│                  ┌─────────────┐                                │
│                  │  Entities   │                                │
│                  │  Value Obj  │                                │
│                  │  Domain Svc │                                │
│                  └─────────────┘                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔗 Referencias

- [PEP 544 - Protocols](https://peps.python.org/pep-0544/)
- [typing.Protocol Documentation](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Hexagonal Architecture - Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture - Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
