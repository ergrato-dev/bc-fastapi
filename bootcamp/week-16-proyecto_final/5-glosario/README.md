# 📖 Glosario - Semana 16

## Proyecto Final y Cierre del Bootcamp

Este glosario recopila los términos clave de todo el bootcamp, con énfasis en los conceptos necesarios para el proyecto final.

---

## A

### API (Application Programming Interface)
Conjunto de definiciones y protocolos que permiten la comunicación entre aplicaciones. En este bootcamp construimos APIs RESTful con FastAPI.

### Authentication (Autenticación)
Proceso de verificar la identidad de un usuario. Responde a "¿Quién eres?". Implementamos JWT para autenticación.

### Authorization (Autorización)
Proceso de determinar qué acciones puede realizar un usuario autenticado. Responde a "¿Qué puedes hacer?".

### Async/Await
Sintaxis de Python para programación asíncrona. `async def` define una corutina, `await` espera su resultado sin bloquear.

---

## B

### Background Task
Tarea que se ejecuta después de enviar la respuesta al cliente. Útil para operaciones lentas como enviar emails.

### Bcrypt
Algoritmo de hashing diseñado para passwords. Incluye salt automático y es deliberadamente lento para dificultar ataques.

### Bearer Token
Esquema de autenticación HTTP donde el token se envía en el header `Authorization: Bearer <token>`.

---

## C

### CI/CD (Continuous Integration/Continuous Deployment)
Práctica de automatizar testing (CI) y deployment (CD) cada vez que hay cambios en el código.

### Clean Architecture
Arquitectura de software que separa el código en capas concéntricas, con las reglas de negocio en el centro, independientes de frameworks.

### CORS (Cross-Origin Resource Sharing)
Mecanismo de seguridad que controla qué dominios pueden acceder a tu API desde un navegador.

### Coverage
Métrica que indica qué porcentaje del código es ejecutado por los tests. Objetivo: >50%.

### CRUD
Acrónimo para las cuatro operaciones básicas: Create, Read, Update, Delete.

---

## D

### Dependency Injection
Patrón de diseño donde las dependencias de un objeto se pasan desde afuera en lugar de crearse internamente. FastAPI lo implementa con `Depends()`.

### Docker
Plataforma de containerización que empaqueta aplicaciones con sus dependencias para ejecutarse de forma consistente en cualquier ambiente.

### Docker Compose
Herramienta para definir y ejecutar aplicaciones Docker multi-contenedor usando un archivo YAML.

### Dockerfile
Archivo de texto con instrucciones para construir una imagen Docker.

---

## E

### Endpoint
URL específica de una API que responde a requests. Ejemplo: `GET /api/v1/users`.

### Environment Variable
Variable definida fuera del código que configura la aplicación. Ejemplo: `DATABASE_URL`.

---

## F

### FastAPI
Framework web moderno de Python para construir APIs. Características: alto rendimiento, validación automática, documentación OpenAPI.

### Fixture (pytest)
Función de pytest que proporciona datos o setup reutilizable para tests.

---

## G

### GitHub Actions
Servicio de CI/CD integrado en GitHub que ejecuta workflows automáticamente en eventos como push o PR.

---

## H

### Hash
Transformación de datos en una cadena de longitud fija. Usamos hashes para almacenar passwords de forma segura.

### Health Check
Endpoint que indica si la aplicación está funcionando correctamente. Usado por load balancers y orquestadores.

### HTTP Methods
Verbos HTTP que indican la acción a realizar: GET (leer), POST (crear), PUT (actualizar), DELETE (eliminar), PATCH (actualización parcial).

---

## J

### JWT (JSON Web Token)
Estándar para crear tokens de acceso que contienen claims (información) firmados criptográficamente.

### Joinedload
Estrategia de SQLAlchemy que carga relaciones usando JOIN en una sola query. Ideal para relaciones N:1.

---

## M

### Middleware
Código que se ejecuta antes y/o después de cada request. Usado para logging, CORS, autenticación global.

### Migration (Alembic)
Script que modifica el esquema de la base de datos de forma versionada y reversible.

### Model (SQLAlchemy)
Clase Python que representa una tabla de la base de datos. Define columnas, relaciones y constraints.

### Multi-stage Build
Técnica de Dockerfile que usa múltiples `FROM` para producir imágenes más pequeñas y seguras.

---

## N

### N+1 Problem
Anti-patrón donde se ejecutan N queries adicionales para cargar datos relacionados de N registros. Solución: eager loading.

---

## O

### ORM (Object-Relational Mapping)
Técnica que mapea objetos de programación a tablas de base de datos. SQLAlchemy es el ORM que usamos.

### OpenAPI
Especificación estándar para describir APIs REST. FastAPI genera documentación OpenAPI automáticamente.

---

## P

### Pagination
Técnica para dividir resultados grandes en páginas. Tipos: offset-based, cursor-based.

### Pydantic
Librería de Python para validación de datos usando type hints. FastAPI la usa para validar requests y responses.

### pytest
Framework de testing para Python. Características: fixtures, parametrización, plugins.

---

## R

### Rate Limiting
Técnica para limitar el número de requests que un cliente puede hacer en un período de tiempo.

### Repository Pattern
Patrón de diseño que encapsula la lógica de acceso a datos, separándola de la lógica de negocio.

### REST (Representational State Transfer)
Estilo arquitectónico para APIs web. Principios: stateless, recursos con URLs, métodos HTTP estándar.

### Refresh Token
Token de larga duración usado para obtener nuevos access tokens sin re-autenticarse.

---

## S

### Schema (Pydantic)
Clase que define la estructura y validación de datos de entrada o salida.

### Selectinload
Estrategia de SQLAlchemy que carga relaciones con una segunda query usando `IN`. Ideal para relaciones 1:N.

### Service Layer
Capa de arquitectura que contiene la lógica de negocio, orquestando repositories y aplicando reglas.

### SQLAlchemy
ORM y toolkit SQL para Python. La versión 2.x introduce estilo moderno con select() y async support.

### Swagger UI
Interfaz web interactiva para explorar y probar APIs documentadas con OpenAPI. Disponible en `/docs`.

---

## T

### Token
Cadena de caracteres que representa una sesión o autorización. JWT es un tipo de token.

### Type Hints
Anotaciones de tipos en Python que indican el tipo esperado de variables, parámetros y retornos.

---

## U

### Unit Test
Test que verifica una unidad pequeña de código (función, método) de forma aislada.

### uv
Gestor de paquetes ultra rápido para Python, alternativa moderna a pip. Usado en este bootcamp.

### Uvicorn
Servidor ASGI de alto rendimiento para aplicaciones Python async como FastAPI.

---

## V

### Validation
Proceso de verificar que los datos cumplen con reglas definidas. Pydantic maneja validación en FastAPI.

### Virtual Environment
Ambiente Python aislado con sus propias dependencias. Docker lo reemplaza en producción.

---

## W

### WebSocket
Protocolo de comunicación bidireccional persistente. Usado para funcionalidades en tiempo real.

### Workflow (GitHub Actions)
Archivo YAML que define un proceso automatizado: triggers, jobs, y steps.

---

## 🎓 Conceptos del Bootcamp Completo

| Semanas | Enfoque | Conceptos Clave |
|---------|---------|-----------------|
| 1-4 | Fundamentos | Python, Type Hints, Async, FastAPI básico |
| 5-10 | Intermedio | SQLAlchemy, CRUD, Arquitectura en capas |
| 11-14 | Avanzado | JWT, Testing, WebSockets, Seguridad |
| 15-16 | Producción | Docker, CI/CD, Deployment, Proyecto Final |

---

¡Felicidades por completar el bootcamp! 🎉
