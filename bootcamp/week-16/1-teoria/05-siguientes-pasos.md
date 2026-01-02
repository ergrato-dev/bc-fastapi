# 🗺️ Siguientes Pasos: Tu Roadmap Post-Bootcamp

![Roadmap Post-Bootcamp](../0-assets/06-post-bootcamp-roadmap.svg)

## 📋 Descripción

Completar el bootcamp es solo el comienzo. Esta guía te orienta sobre qué aprender después y cómo seguir creciendo como desarrollador backend.

---

## 🎯 Objetivos

1. Identificar áreas de mejora
2. Planificar tu aprendizaje continuo
3. Conocer tecnologías complementarias
4. Establecer metas a corto y mediano plazo

---

## 📊 Tu Nivel Actual

Al completar este bootcamp, dominas:

### ✅ Dominado
- Python moderno (3.12+, type hints, async/await)
- FastAPI (routers, dependencies, middleware)
- Pydantic v2 (validación, serialización)
- SQLAlchemy 2.x (ORM, relaciones, queries)
- PostgreSQL (básico-intermedio)
- JWT Authentication
- Testing con pytest
- Docker y Docker Compose
- CI/CD con GitHub Actions
- REST API design

### 🔄 Para Profundizar
- Patrones de diseño avanzados
- Optimización de queries SQL
- Caching strategies
- Message queues
- Microservicios

### 📚 Por Aprender
- GraphQL
- gRPC
- Kubernetes
- Cloud services (AWS/GCP/Azure)
- Observability (métricas, tracing)

---

## 🛤️ Roadmap por Trimestre

### Q1: Consolidación (Meses 1-3)

**Objetivo**: Solidificar conocimientos y conseguir primer empleo

#### Semana 1-4: Proyecto Personal
```
📋 Construir un proyecto propio desde cero
   - Idea original (no tutorial)
   - Aplicar todo lo aprendido
   - Deploy público
   - Documentación completa
```

#### Semana 5-8: Profundización Técnica
```python
# 1. Patrones de diseño en Python
# Factory, Strategy, Observer, Repository

# 2. SOLID principles aplicados
# S - Single Responsibility
# O - Open/Closed
# L - Liskov Substitution  
# I - Interface Segregation
# D - Dependency Inversion

# 3. Clean Architecture profundo
# Capas: Domain → Application → Infrastructure
```

#### Semana 9-12: Búsqueda Activa
```
🔍 Aplicar a ofertas de trabajo
   - 5-10 aplicaciones por semana
   - Networking en LinkedIn
   - Entrevistas de práctica
   - Iteración en CV y portfolio
```

### Q2: Crecimiento (Meses 4-6)

**Objetivo**: Expandir habilidades técnicas

#### Caching y Performance
```python
# Redis para caching
import redis.asyncio as redis
from fastapi import FastAPI, Depends

async def get_redis():
    return redis.from_url("redis://localhost")

@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    cache: redis.Redis = Depends(get_redis),
    db: AsyncSession = Depends(get_db)
):
    # Check cache first
    cached = await cache.get(f"user:{user_id}")
    if cached:
        return json.loads(cached)
    
    # Fetch from DB
    user = await db.get(User, user_id)
    
    # Store in cache (TTL: 1 hour)
    await cache.setex(
        f"user:{user_id}",
        3600,
        user.model_dump_json()
    )
    
    return user
```

#### Message Queues
```python
# Celery para tareas asíncronas
from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def process_payment(order_id: int):
    """Procesa pago en background."""
    # Lógica de pago
    pass

# FastAPI endpoint
@router.post("/orders/{order_id}/pay")
async def pay_order(order_id: int):
    process_payment.delay(order_id)
    return {"status": "processing"}
```

#### WebSockets Avanzado
```python
# Real-time notifications
from fastapi import WebSocket, WebSocketDisconnect

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}
    
    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket
    
    async def send_notification(self, user_id: int, message: dict):
        if websocket := self.active_connections.get(user_id):
            await websocket.send_json(message)

manager = ConnectionManager()

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # Handle incoming messages
    except WebSocketDisconnect:
        del manager.active_connections[user_id]
```

### Q3: Especialización (Meses 7-9)

**Objetivo**: Elegir y profundizar en un área

#### Opción A: Cloud & DevOps
```yaml
# Kubernetes básico
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fastapi
  template:
    metadata:
      labels:
        app: fastapi
    spec:
      containers:
      - name: api
        image: myregistry/fastapi-app:latest
        ports:
        - containerPort: 8000
        resources:
          limits:
            memory: "256Mi"
            cpu: "500m"
```

Aprender:
- AWS/GCP fundamentals
- Terraform para IaC
- Kubernetes (básico)
- Monitoring (Prometheus/Grafana)

#### Opción B: Data Engineering
```python
# Apache Kafka para streaming
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

async def produce_event(topic: str, event: dict):
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
    await producer.start()
    try:
        await producer.send_and_wait(
            topic,
            json.dumps(event).encode()
        )
    finally:
        await producer.stop()

# Integración con FastAPI
@router.post("/events")
async def create_event(event: EventCreate):
    await produce_event("user-events", event.model_dump())
    return {"status": "event published"}
```

Aprender:
- Apache Kafka
- Apache Airflow
- Data pipelines
- ETL processes

#### Opción C: Microservicios
```python
# gRPC service definition
# user.proto
"""
syntax = "proto3";

service UserService {
  rpc GetUser (UserRequest) returns (UserResponse);
  rpc CreateUser (CreateUserRequest) returns (UserResponse);
}

message UserRequest {
  int32 id = 1;
}

message UserResponse {
  int32 id = 1;
  string email = 2;
  string name = 3;
}
"""

# Python gRPC implementation
import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc

class UserServicer(user_pb2_grpc.UserServiceServicer):
    async def GetUser(self, request, context):
        user = await get_user_from_db(request.id)
        return user_pb2.UserResponse(
            id=user.id,
            email=user.email,
            name=user.name
        )
```

Aprender:
- gRPC
- Service mesh (Istio)
- Event-driven architecture
- Domain-Driven Design

### Q4: Consolidación Senior (Meses 10-12)

**Objetivo**: Prepararse para nivel mid/senior

#### System Design
```
📐 Aprende a diseñar sistemas escalables:
   
1. Fundamentals
   - Load balancing
   - Database sharding
   - Caching strategies
   - CDN
   - Message queues

2. Patrones comunes
   - API Gateway
   - Circuit Breaker
   - CQRS
   - Event Sourcing
   - Saga Pattern

3. Casos de estudio
   - Diseñar Twitter
   - Diseñar URL shortener
   - Diseñar sistema de chat
```

#### Liderazgo Técnico
```
🎯 Habilidades blandas:
   
- Code reviews efectivos
- Mentoría a juniors
- Documentación técnica
- Estimación de proyectos
- Comunicación con stakeholders
```

---

## 📚 Recursos de Aprendizaje Continuo

### Cursos Recomendados

| Plataforma | Curso | Nivel |
|------------|-------|-------|
| Udemy | Python Advanced | Intermedio |
| Pluralsight | Docker Deep Dive | Intermedio |
| A Cloud Guru | AWS Solutions Architect | Avanzado |
| educative.io | System Design | Avanzado |

### Libros Esenciales

```
📖 Nivel Intermedio:
   - "Clean Code" - Robert Martin
   - "The Pragmatic Programmer" - Hunt & Thomas
   - "Designing Data-Intensive Applications" - Kleppmann

📖 Nivel Avanzado:
   - "Clean Architecture" - Robert Martin
   - "Building Microservices" - Sam Newman
   - "Site Reliability Engineering" - Google
```

### Comunidades

- **Python Discord**: Chat activo
- **FastAPI Discord**: Soporte oficial
- **Reddit**: r/Python, r/learnpython
- **Dev.to**: Artículos y tutoriales
- **Hashnode**: Blog técnico

### Práctica de Coding

```python
# LeetCode - Problemas comunes en entrevistas

# Easy: Two Sum
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Medium: Valid Parentheses
def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
```

---

## 🎯 Metas SMART

### Corto Plazo (3 meses)
```
S - Específico: Conseguir empleo como backend developer junior
M - Medible: Aplicar a 50 ofertas, 10 entrevistas
A - Alcanzable: Con mi portfolio y skills actuales
R - Relevante: Inicio de carrera en tech
T - Temporal: En los próximos 3 meses
```

### Mediano Plazo (1 año)
```
S - Específico: Alcanzar nivel mid como backend developer
M - Medible: Dominar Redis, mensajería, cloud básico
A - Alcanzable: Estudiando 5-10 horas semanales
R - Relevante: Crecimiento profesional
T - Temporal: En 12 meses
```

### Largo Plazo (3 años)
```
S - Específico: Ser senior backend / tech lead
M - Medible: Liderar proyectos, mentorear juniors
A - Alcanzable: Con experiencia y estudio continuo
R - Relevante: Meta de carrera
T - Temporal: En 3 años
```

---

## ✅ Tu Plan de Acción Semanal

### Semana Típica (10 horas de estudio)

| Día | Actividad | Tiempo |
|-----|-----------|--------|
| Lunes | Proyecto personal | 2h |
| Martes | Curso/Tutorial nuevo | 1.5h |
| Miércoles | LeetCode (2-3 problemas) | 1h |
| Jueves | Lectura técnica | 1h |
| Viernes | Open source / comunidad | 1h |
| Sábado | Proyecto personal | 2.5h |
| Domingo | Revisión + planning | 1h |

---

## 🏆 Certificaciones Útiles

| Certificación | Nivel | Valor |
|---------------|-------|-------|
| AWS Cloud Practitioner | Básico | ⭐⭐⭐ |
| AWS Solutions Architect | Intermedio | ⭐⭐⭐⭐⭐ |
| Docker Certified Associate | Intermedio | ⭐⭐⭐⭐ |
| Kubernetes CKA | Avanzado | ⭐⭐⭐⭐⭐ |
| HashiCorp Terraform | Intermedio | ⭐⭐⭐⭐ |

---

## 💡 Consejos Finales

1. **Consistencia > Intensidad**: Mejor 1 hora diaria que 10 horas un día
2. **Construye en público**: Comparte tu aprendizaje en LinkedIn/Twitter
3. **Enseña lo que aprendes**: Blog, videos, mentorías
4. **Red de contactos**: El networking abre puertas
5. **No te compares**: Cada quien tiene su ritmo
6. **Disfruta el proceso**: La tecnología evoluciona, abraza el cambio

---

## 🎓 Cierre del Bootcamp

¡Felicidades por llegar hasta aquí! 🎉

Has recorrido un largo camino desde "Hello World" hasta construir APIs profesionales listas para producción.

Recuerda:
- Tu proyecto final es tu mejor carta de presentación
- El aprendizaje nunca termina en tecnología
- La comunidad de FastAPI es increíble - participa
- Cada "no" en una entrevista te acerca al "sí"

**El mejor momento para empezar tu carrera como desarrollador fue hace años. El segundo mejor momento es ahora.**

¡Éxito en tu carrera! 🚀
