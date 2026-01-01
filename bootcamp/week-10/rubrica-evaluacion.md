# 📊 Rúbrica de Evaluación - Semana 10

## 🏛️ Arquitectura Hexagonal Completa

---

## 📋 Información General

| Aspecto | Detalle |
|---------|---------|
| **Semana** | 10 de 16 |
| **Tema** | Arquitectura Hexagonal Completa |
| **Proyecto** | Task Management System |
| **Duración estimada** | 6 horas |
| **Puntuación máxima** | 100 puntos |
| **Puntuación mínima aprobatoria** | 70 puntos |

---

## 🎯 Objetivos Evaluados

1. Implementar Domain Layer con entidades, value objects y domain services
2. Crear Application Layer con use cases y DTOs
3. Desarrollar Infrastructure Layer con adapters intercambiables
4. Componer la aplicación correctamente (Composition Root)
5. Aplicar principios DDD táctico en FastAPI
6. Escribir tests para cada capa de forma independiente

---

## 📝 Distribución de Puntuación

### Evidencia de Conocimiento 🧠 (30 puntos)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Comprensión teórica | 10 | Entiende los principios de arquitectura hexagonal |
| Separación de capas | 10 | Identifica correctamente responsabilidades por capa |
| DDD Táctico | 10 | Comprende entidades, value objects y aggregates |

### Evidencia de Desempeño 💪 (40 puntos)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Práctica 01: Domain Modeling | 10 | Modela entidades y value objects correctamente |
| Práctica 02: Application Services | 10 | Implementa use cases con DTOs |
| Práctica 03: Infrastructure Adapters | 10 | Crea adapters que implementan ports |
| Práctica 04: Wiring & Composition | 10 | Compone la aplicación en el entry point |

### Evidencia de Producto 📦 (30 puntos)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Domain Layer completo | 8 | Entidades Task, Project con reglas de negocio |
| Application Layer funcional | 8 | Use cases CRUD + asignación funcionando |
| Infrastructure Layer | 8 | API REST + Persistencia implementados |
| Tests passing | 6 | Tests unitarios e integración pasando |

---

## 🏆 Niveles de Desempeño

### Excelente (90-100 puntos) ⭐⭐⭐

- Arquitectura hexagonal perfectamente implementada
- Domain Layer rico con validaciones de negocio
- Todos los use cases funcionando correctamente
- Tests con alta cobertura (>80%)
- Código limpio y bien documentado
- Bonus implementados (Domain Events, segundo adapter)

### Bueno (80-89 puntos) ⭐⭐

- Arquitectura hexagonal bien estructurada
- Domain Layer con entidades correctas
- Use cases principales funcionando
- Tests básicos pasando
- Código organizado y legible

### Satisfactorio (70-79 puntos) ⭐

- Estructura hexagonal básica presente
- Entidades implementadas sin value objects
- Al menos 3 use cases funcionando
- Algunos tests pasando
- Código funcional con áreas de mejora

### Insuficiente (<70 puntos) ❌

- Mezcla de responsabilidades entre capas
- Entidades anémicas (solo datos, sin comportamiento)
- Use cases incompletos o no funcionando
- Tests fallando o ausentes
- Violaciones del principio de inversión de dependencias

---

## 📋 Rúbrica Detallada del Proyecto

### Domain Layer (25 puntos)

| Aspecto | Excelente (25) | Bueno (20) | Satisfactorio (15) | Insuficiente (<15) |
|---------|---------------|------------|-------------------|-------------------|
| **Entidades** | Task, Project, User con identidad y comportamiento | Entidades con identidad pero poco comportamiento | Entidades básicas funcionales | Entidades anémicas o incorrectas |
| **Value Objects** | Priority, Status, TaskId implementados | Al menos 2 value objects | 1 value object implementado | Sin value objects |
| **Domain Services** | Lógica de dominio encapsulada | Servicios presentes pero simples | Lógica en application layer | Sin domain services |
| **Ports** | Interfaces bien definidas | Ports funcionales | Ports básicos | Ports ausentes o mal definidos |

### Application Layer (25 puntos)

| Aspecto | Excelente (25) | Bueno (20) | Satisfactorio (15) | Insuficiente (<15) |
|---------|---------------|------------|-------------------|-------------------|
| **Use Cases** | CreateTask, AssignTask, CompleteTask, GetTasks, DeleteTask | 4+ use cases | 3 use cases | <3 use cases |
| **DTOs** | Input/Output DTOs bien separados | DTOs funcionales | DTOs básicos | Uso directo de entidades |
| **Orquestación** | Services coordinan correctamente | Coordinación adecuada | Coordinación básica | Lógica mezclada |
| **Error Handling** | Excepciones de dominio manejadas | Manejo básico de errores | Algunos errores manejados | Sin manejo de errores |

### Infrastructure Layer (25 puntos)

| Aspecto | Excelente (25) | Bueno (20) | Satisfactorio (15) | Insuficiente (<15) |
|---------|---------------|------------|-------------------|-------------------|
| **Driving Adapters** | API REST completa con validaciones | API funcional | Endpoints básicos | API incompleta |
| **Driven Adapters** | Repository + servicios externos | Repository implementado | Persistencia básica | Sin adapters |
| **Implementación Ports** | Todos los ports implementados | Ports principales implementados | Algunos ports | Ports no implementados |
| **Intercambiabilidad** | Adapters fácilmente intercambiables | Adapters separados | Acoplamiento moderado | Fuerte acoplamiento |

### Testing (15 puntos)

| Aspecto | Excelente (15) | Bueno (12) | Satisfactorio (9) | Insuficiente (<9) |
|---------|---------------|------------|-------------------|-------------------|
| **Unit Tests** | Tests de domain y application | Tests de una capa | Algunos tests | Sin tests unitarios |
| **Integration Tests** | Tests de API completos | Tests básicos de API | 2-3 tests integración | Sin tests integración |
| **Test Doubles** | Fakes y Spies usados correctamente | Test doubles presentes | Algunos test doubles | Sin test doubles |

### Código y Documentación (10 puntos)

| Aspecto | Excelente (10) | Bueno (8) | Satisfactorio (6) | Insuficiente (<6) |
|---------|---------------|------------|-------------------|-------------------|
| **Clean Code** | Código ejemplar, bien nombrado | Código limpio | Código funcional | Código desorganizado |
| **Type Hints** | 100% tipado con Protocols | >80% tipado | >60% tipado | <60% tipado |
| **Documentación** | Docstrings completos | Documentación adecuada | Documentación básica | Sin documentación |

---

## 📊 Criterios de Evaluación Específicos

### ✅ Checklist Domain Layer

- [ ] Entidad `Task` con id, title, description, status, priority, project_id, assignee_id
- [ ] Entidad `Project` con id, name, description, tasks[]
- [ ] Value Object `Priority` (LOW, MEDIUM, HIGH, CRITICAL)
- [ ] Value Object `TaskStatus` (TODO, IN_PROGRESS, DONE, CANCELLED)
- [ ] Port `TaskRepository` con métodos CRUD
- [ ] Port `ProjectRepository` con métodos CRUD
- [ ] Reglas de negocio en entidades (ej: solo asignar tareas TODO)

### ✅ Checklist Application Layer

- [ ] Use Case `CreateTaskUseCase`
- [ ] Use Case `AssignTaskUseCase`
- [ ] Use Case `CompleteTaskUseCase`
- [ ] Use Case `GetTasksUseCase` (con filtros)
- [ ] DTOs de entrada separados de DTOs de salida
- [ ] Manejo de errores con excepciones de dominio

### ✅ Checklist Infrastructure Layer

- [ ] API REST con endpoints CRUD para Tasks
- [ ] API REST con endpoints CRUD para Projects
- [ ] Endpoint para asignar tarea a usuario
- [ ] Endpoint para completar tarea
- [ ] Repository in-memory implementando port
- [ ] Configuración centralizada

### ✅ Checklist Testing

- [ ] Al menos 5 tests unitarios del domain
- [ ] Al menos 5 tests unitarios de application
- [ ] Al menos 8 tests de integración de API
- [ ] Uso de Fake repositories en tests
- [ ] Todos los tests pasando

---

## 🎓 Recomendaciones para Alcanzar la Excelencia

### Domain Layer

```python
# ✅ Excelente: Entidad rica con comportamiento
class Task:
    def assign_to(self, user_id: str) -> None:
        if self.status != TaskStatus.TODO:
            raise TaskNotAssignableError(self.id)
        self._assignee_id = user_id
        
    def complete(self) -> None:
        if self.status == TaskStatus.CANCELLED:
            raise TaskAlreadyCancelledError(self.id)
        self._status = TaskStatus.DONE

# ❌ Insuficiente: Entidad anémica
class Task:
    id: str
    title: str
    assignee_id: str | None  # Se modifica directamente desde fuera
```

### Application Layer

```python
# ✅ Excelente: Use Case bien definido
class AssignTaskUseCase:
    def __init__(
        self,
        task_repo: TaskRepository,
        user_repo: UserRepository,
    ) -> None:
        self._task_repo = task_repo
        self._user_repo = user_repo
    
    async def execute(self, command: AssignTaskCommand) -> TaskDTO:
        task = await self._task_repo.get_by_id(command.task_id)
        if not task:
            raise TaskNotFoundError(command.task_id)
            
        user = await self._user_repo.get_by_id(command.user_id)
        if not user:
            raise UserNotFoundError(command.user_id)
            
        task.assign_to(command.user_id)
        await self._task_repo.save(task)
        
        return TaskDTO.from_entity(task)
```

### Testing

```python
# ✅ Excelente: Test aislado con fakes
async def test_assign_task_to_user():
    # Arrange
    fake_task_repo = FakeTaskRepository()
    fake_user_repo = FakeUserRepository()
    
    task = Task.create(title="Test Task")
    user = User.create(name="John Doe")
    
    await fake_task_repo.save(task)
    await fake_user_repo.save(user)
    
    use_case = AssignTaskUseCase(fake_task_repo, fake_user_repo)
    
    # Act
    result = await use_case.execute(
        AssignTaskCommand(task_id=task.id, user_id=user.id)
    )
    
    # Assert
    assert result.assignee_id == user.id
    
    saved_task = await fake_task_repo.get_by_id(task.id)
    assert saved_task.assignee_id == user.id
```

---

## 📅 Fechas Importantes

| Concepto | Fecha |
|----------|-------|
| Inicio de semana | Día 1 |
| Entrega de prácticas | Día 5 |
| Entrega de proyecto | Día 7 |
| Retroalimentación | Día 8-9 |

---

## 💬 Criterios de Retroalimentación

La retroalimentación se enfocará en:

1. **Arquitectura**: ¿Las capas están correctamente separadas?
2. **Domain Model**: ¿Las entidades tienen comportamiento rico?
3. **Inversión de Dependencias**: ¿El dominio no depende de infraestructura?
4. **Testing**: ¿Los tests son independientes y aislados?
5. **Clean Code**: ¿El código es legible y mantenible?

---

_Rúbrica versión 1.0 - Semana 10_
