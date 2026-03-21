# 🎯 Domain Layer - El Corazón de la Aplicación

## 🎯 Objetivos de Aprendizaje

- Diseñar un Domain Layer rico y expresivo
- Implementar Entidades con identidad y comportamiento
- Crear Value Objects inmutables
- Definir Domain Services para lógica transversal
- Establecer Ports (interfaces) que el dominio necesita

---

## 📚 Contenido

### 1. ¿Qué es el Domain Layer?

El **Domain Layer** es el núcleo de la arquitectura hexagonal. Contiene toda la **lógica de negocio** y las **reglas del dominio**. Es la capa más estable y la que menos debe cambiar.

![Domain Layer](../0-assets/02-domain-layer.svg)

#### Características Clave

- **Sin dependencias externas**: No importa frameworks, bases de datos, ni APIs
- **Puro Python**: Solo usa la biblioteca estándar y tipado
- **Testeable en aislamiento**: No necesita infraestructura para probarse
- **Expresa el lenguaje del negocio**: Usa términos del dominio del problema

### 2. Componentes del Domain Layer

```
domain/
├── __init__.py
├── entities/           # Entidades con identidad
│   ├── __init__.py
│   ├── task.py
│   ├── project.py
│   └── user.py
├── value_objects/      # Objetos inmutables por valor
│   ├── __init__.py
│   ├── priority.py
│   ├── task_status.py
│   └── email.py
├── services/           # Lógica de dominio transversal
│   ├── __init__.py
│   └── task_assignment_service.py
├── ports/              # Interfaces/Contratos
│   ├── __init__.py
│   ├── task_repository.py
│   └── user_repository.py
├── events/             # Eventos de dominio (opcional)
│   ├── __init__.py
│   └── task_events.py
└── exceptions.py       # Excepciones de dominio
```

### 3. Entidades (Entities)

Las **Entidades** son objetos con:
- **Identidad única** que persiste en el tiempo
- **Ciclo de vida** (se crean, modifican, eliminan)
- **Comportamiento** (métodos que encapsulan reglas de negocio)

#### Ejemplo: Entidad Task

```python
# domain/entities/task.py
"""Entidad Task - Representa una tarea en el sistema."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from domain.value_objects.priority import Priority
from domain.value_objects.task_status import TaskStatus
from domain.exceptions import (
    TaskNotAssignableError,
    TaskNotStartableError,
    TaskNotCompletableError,
)


@dataclass
class Task:
    """
    Entidad Task.
    
    Una tarea tiene identidad única (id) y comportamiento
    que encapsula las reglas de negocio.
    """
    
    id: UUID
    title: str
    description: str
    status: TaskStatus = field(default=TaskStatus.TODO)
    priority: Priority = field(default=Priority.MEDIUM)
    project_id: UUID | None = field(default=None)
    assignee_id: UUID | None = field(default=None)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    
    # ========================================
    # Factory Methods
    # ========================================
    
    @classmethod
    def create(
        cls,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        project_id: UUID | None = None,
    ) -> "Task":
        """
        Factory method para crear una nueva tarea.
        
        Usar este método en lugar del constructor directamente
        para garantizar que la tarea se crea en un estado válido.
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        return cls(
            id=uuid4(),
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            project_id=project_id,
        )
    
    # ========================================
    # Behavior Methods (Reglas de Negocio)
    # ========================================
    
    def assign_to(self, user_id: UUID) -> None:
        """
        Asignar la tarea a un usuario.
        
        Regla de negocio: Solo se pueden asignar tareas
        que estén en estado TODO.
        """
        if self.status != TaskStatus.TODO:
            raise TaskNotAssignableError(
                f"Cannot assign task {self.id}: status is {self.status.value}"
            )
        
        self.assignee_id = user_id
        self._touch()
    
    def unassign(self) -> None:
        """Quitar la asignación de la tarea."""
        self.assignee_id = None
        self._touch()
    
    def start(self) -> None:
        """
        Iniciar trabajo en la tarea.
        
        Regla de negocio: Solo se pueden iniciar tareas
        que estén en estado TODO.
        """
        if self.status != TaskStatus.TODO:
            raise TaskNotStartableError(
                f"Cannot start task {self.id}: status is {self.status.value}"
            )
        
        self.status = TaskStatus.IN_PROGRESS
        self._touch()
    
    def complete(self) -> None:
        """
        Marcar la tarea como completada.
        
        Regla de negocio: No se pueden completar tareas canceladas.
        """
        if self.status == TaskStatus.CANCELLED:
            raise TaskNotCompletableError(
                f"Cannot complete task {self.id}: task is cancelled"
            )
        
        self.status = TaskStatus.DONE
        self._touch()
    
    def cancel(self) -> None:
        """
        Cancelar la tarea.
        
        Regla de negocio: No se pueden cancelar tareas ya completadas.
        """
        if self.status == TaskStatus.DONE:
            raise ValueError(
                f"Cannot cancel task {self.id}: task is already done"
            )
        
        self.status = TaskStatus.CANCELLED
        self._touch()
    
    def change_priority(self, new_priority: Priority) -> None:
        """Cambiar la prioridad de la tarea."""
        self.priority = new_priority
        self._touch()
    
    def update_details(
        self,
        title: str | None = None,
        description: str | None = None,
    ) -> None:
        """Actualizar título y/o descripción."""
        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            self.title = title.strip()
        
        if description is not None:
            self.description = description.strip()
        
        self._touch()
    
    # ========================================
    # Query Methods (No modifican estado)
    # ========================================
    
    def is_assignable(self) -> bool:
        """Verificar si la tarea puede ser asignada."""
        return self.status == TaskStatus.TODO
    
    def is_assigned(self) -> bool:
        """Verificar si la tarea tiene asignado."""
        return self.assignee_id is not None
    
    def is_overdue(self, deadline: datetime) -> bool:
        """Verificar si la tarea está vencida."""
        return (
            self.status not in (TaskStatus.DONE, TaskStatus.CANCELLED)
            and datetime.now() > deadline
        )
    
    def belongs_to_project(self, project_id: UUID) -> bool:
        """Verificar si la tarea pertenece a un proyecto."""
        return self.project_id == project_id
    
    # ========================================
    # Private Methods
    # ========================================
    
    def _touch(self) -> None:
        """Actualizar timestamp de modificación."""
        self.updated_at = datetime.now()
```

#### Ejemplo: Entidad Project

```python
# domain/entities/project.py
"""Entidad Project - Representa un proyecto que agrupa tareas."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Project:
    """
    Entidad Project.
    
    Un proyecto agrupa tareas relacionadas y tiene
    un propietario (owner).
    """
    
    id: UUID
    name: str
    description: str
    owner_id: UUID
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    is_archived: bool = field(default=False)
    
    @classmethod
    def create(
        cls,
        name: str,
        owner_id: UUID,
        description: str = "",
    ) -> "Project":
        """Factory method para crear un proyecto."""
        if not name or not name.strip():
            raise ValueError("Project name cannot be empty")
        
        return cls(
            id=uuid4(),
            name=name.strip(),
            description=description.strip(),
            owner_id=owner_id,
        )
    
    def rename(self, new_name: str) -> None:
        """Renombrar el proyecto."""
        if not new_name or not new_name.strip():
            raise ValueError("Project name cannot be empty")
        
        self.name = new_name.strip()
        self._touch()
    
    def archive(self) -> None:
        """Archivar el proyecto."""
        self.is_archived = True
        self._touch()
    
    def unarchive(self) -> None:
        """Desarchivar el proyecto."""
        self.is_archived = False
        self._touch()
    
    def transfer_ownership(self, new_owner_id: UUID) -> None:
        """Transferir propiedad del proyecto."""
        self.owner_id = new_owner_id
        self._touch()
    
    def _touch(self) -> None:
        """Actualizar timestamp de modificación."""
        self.updated_at = datetime.now()
```

### 4. Value Objects

Los **Value Objects** son objetos:
- **Inmutables**: No cambian después de crearse
- **Sin identidad**: Se comparan por sus atributos, no por ID
- **Autovalidados**: Garantizan su propia validez

#### Ejemplo: Value Objects con Enum

```python
# domain/value_objects/task_status.py
"""Value Object TaskStatus - Estados posibles de una tarea."""

from enum import Enum


class TaskStatus(Enum):
    """
    Estados posibles de una tarea.
    
    Transiciones válidas:
    - TODO -> IN_PROGRESS, CANCELLED
    - IN_PROGRESS -> DONE, CANCELLED
    - DONE -> (estado final)
    - CANCELLED -> (estado final)
    """
    
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELLED = "cancelled"
    
    def can_transition_to(self, new_status: "TaskStatus") -> bool:
        """Verificar si la transición es válida."""
        valid_transitions = {
            TaskStatus.TODO: {TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED},
            TaskStatus.IN_PROGRESS: {TaskStatus.DONE, TaskStatus.CANCELLED},
            TaskStatus.DONE: set(),  # Estado final
            TaskStatus.CANCELLED: set(),  # Estado final
        }
        return new_status in valid_transitions[self]
```

```python
# domain/value_objects/priority.py
"""Value Object Priority - Prioridad de una tarea."""

from enum import IntEnum


class Priority(IntEnum):
    """
    Prioridad de una tarea.
    
    Usa IntEnum para poder comparar prioridades numéricamente:
    Priority.CRITICAL > Priority.LOW  # True
    """
    
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
    
    @classmethod
    def from_string(cls, value: str) -> "Priority":
        """Crear Priority desde string."""
        try:
            return cls[value.upper()]
        except KeyError:
            valid = ", ".join(p.name for p in cls)
            raise ValueError(f"Invalid priority: {value}. Valid: {valid}")
```

#### Value Object Complejo: Email

```python
# domain/value_objects/email.py
"""Value Object Email - Representa un email validado."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)  # frozen=True hace inmutable
class Email:
    """
    Value Object Email.
    
    Garantiza que el email es válido al momento de creación.
    Es inmutable (frozen=True).
    """
    
    value: str
    
    def __post_init__(self) -> None:
        """Validar email después de inicialización."""
        # Patrón básico de email
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        if not re.match(pattern, self.value):
            raise ValueError(f"Invalid email format: {self.value}")
    
    @property
    def domain(self) -> str:
        """Obtener el dominio del email."""
        return self.value.split("@")[1]
    
    @property
    def local_part(self) -> str:
        """Obtener la parte local del email."""
        return self.value.split("@")[0]
    
    def __str__(self) -> str:
        """Representación string del email."""
        return self.value


# Uso
email = Email("user@example.com")
print(email.domain)  # "example.com"

# Esto lanza ValueError:
# invalid_email = Email("not-an-email")
```

### 5. Domain Services

Los **Domain Services** contienen lógica de negocio que:
- No pertenece naturalmente a una sola entidad
- Involucra múltiples entidades
- Representa un proceso o cálculo del dominio

```python
# domain/services/task_assignment_service.py
"""Domain Service para lógica de asignación de tareas."""

from uuid import UUID

from domain.entities.task import Task
from domain.entities.project import Project
from domain.exceptions import (
    TaskAssignmentError,
    UserNotInProjectError,
)


class TaskAssignmentService:
    """
    Domain Service: Lógica de asignación de tareas.
    
    Este servicio encapsula reglas de negocio que involucran
    múltiples entidades (Task, Project, User).
    """
    
    def validate_assignment(
        self,
        task: Task,
        user_id: UUID,
        project: Project | None,
        project_members: set[UUID],
    ) -> None:
        """
        Validar si una asignación es permitida.
        
        Reglas de negocio:
        1. La tarea debe ser asignable (estado TODO)
        2. Si la tarea pertenece a un proyecto, el usuario
           debe ser miembro del proyecto
        """
        # Regla 1: Tarea debe ser asignable
        if not task.is_assignable():
            raise TaskAssignmentError(
                f"Task {task.id} is not assignable"
            )
        
        # Regla 2: Usuario debe ser miembro del proyecto
        if project and user_id not in project_members:
            raise UserNotInProjectError(
                f"User {user_id} is not a member of project {project.id}"
            )
    
    def calculate_workload(
        self,
        user_tasks: list[Task],
    ) -> dict[str, int]:
        """
        Calcular carga de trabajo de un usuario.
        
        Retorna conteo de tareas por estado y prioridad.
        """
        from domain.value_objects.task_status import TaskStatus
        from domain.value_objects.priority import Priority
        
        workload = {
            "total": len(user_tasks),
            "todo": 0,
            "in_progress": 0,
            "high_priority": 0,
            "critical": 0,
        }
        
        for task in user_tasks:
            if task.status == TaskStatus.TODO:
                workload["todo"] += 1
            elif task.status == TaskStatus.IN_PROGRESS:
                workload["in_progress"] += 1
            
            if task.priority == Priority.HIGH:
                workload["high_priority"] += 1
            elif task.priority == Priority.CRITICAL:
                workload["critical"] += 1
        
        return workload
```

### 6. Ports (Interfaces)

Los **Ports** definen contratos que el dominio necesita pero **no implementa**. Usan `Protocol` para duck typing estructural.

```python
# domain/ports/task_repository.py
"""Port TaskRepository - Contrato para persistencia de tareas."""

from typing import Protocol
from uuid import UUID

from domain.entities.task import Task
from domain.value_objects.task_status import TaskStatus


class TaskRepository(Protocol):
    """
    Port: Define QUÉ necesita el dominio para persistir tareas.
    
    La implementación (CÓMO) está en Infrastructure Layer.
    """
    
    async def save(self, task: Task) -> None:
        """Guardar o actualizar una tarea."""
        ...
    
    async def get_by_id(self, task_id: UUID) -> Task | None:
        """Obtener tarea por ID."""
        ...
    
    async def get_all(self) -> list[Task]:
        """Obtener todas las tareas."""
        ...
    
    async def get_by_project(self, project_id: UUID) -> list[Task]:
        """Obtener tareas de un proyecto."""
        ...
    
    async def get_by_assignee(self, user_id: UUID) -> list[Task]:
        """Obtener tareas asignadas a un usuario."""
        ...
    
    async def get_by_status(self, status: TaskStatus) -> list[Task]:
        """Obtener tareas por estado."""
        ...
    
    async def delete(self, task_id: UUID) -> bool:
        """Eliminar una tarea. Retorna True si existía."""
        ...
    
    async def exists(self, task_id: UUID) -> bool:
        """Verificar si una tarea existe."""
        ...
```

```python
# domain/ports/project_repository.py
"""Port ProjectRepository - Contrato para persistencia de proyectos."""

from typing import Protocol
from uuid import UUID

from domain.entities.project import Project


class ProjectRepository(Protocol):
    """Port: Contrato para persistencia de proyectos."""
    
    async def save(self, project: Project) -> None:
        """Guardar o actualizar un proyecto."""
        ...
    
    async def get_by_id(self, project_id: UUID) -> Project | None:
        """Obtener proyecto por ID."""
        ...
    
    async def get_by_owner(self, owner_id: UUID) -> list[Project]:
        """Obtener proyectos de un propietario."""
        ...
    
    async def get_all(self, include_archived: bool = False) -> list[Project]:
        """Obtener todos los proyectos."""
        ...
    
    async def delete(self, project_id: UUID) -> bool:
        """Eliminar un proyecto."""
        ...
```

### 7. Domain Exceptions

Excepciones específicas del dominio que expresan errores de negocio:

```python
# domain/exceptions.py
"""Excepciones del dominio."""


class DomainError(Exception):
    """Base para errores de dominio."""
    pass


class TaskError(DomainError):
    """Base para errores relacionados con tareas."""
    pass


class TaskNotFoundError(TaskError):
    """Tarea no encontrada."""
    
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id
        super().__init__(f"Task not found: {task_id}")


class TaskNotAssignableError(TaskError):
    """Tarea no puede ser asignada."""
    pass


class TaskNotStartableError(TaskError):
    """Tarea no puede ser iniciada."""
    pass


class TaskNotCompletableError(TaskError):
    """Tarea no puede ser completada."""
    pass


class ProjectError(DomainError):
    """Base para errores relacionados con proyectos."""
    pass


class ProjectNotFoundError(ProjectError):
    """Proyecto no encontrado."""
    
    def __init__(self, project_id: str) -> None:
        self.project_id = project_id
        super().__init__(f"Project not found: {project_id}")


class TaskAssignmentError(DomainError):
    """Error en asignación de tarea."""
    pass


class UserNotInProjectError(DomainError):
    """Usuario no es miembro del proyecto."""
    pass
```

---

## 🧪 Ejercicio de Comprensión

¿Cuál es la diferencia entre estos dos diseños?

```python
# Diseño A
class Task:
    id: UUID
    title: str
    status: str
    assignee_id: UUID | None

# Diseño B
class Task:
    id: UUID
    title: str
    status: TaskStatus
    assignee_id: UUID | None
    
    def assign_to(self, user_id: UUID) -> None:
        if self.status != TaskStatus.TODO:
            raise TaskNotAssignableError()
        self.assignee_id = user_id
```

<details>
<summary>Ver respuesta</summary>

**Diseño A**: Entidad anémica
- Solo tiene datos, sin comportamiento
- Las reglas de negocio están dispersas en otros lugares
- `status` es un string sin validación

**Diseño B**: Entidad rica
- Tiene comportamiento que encapsula reglas de negocio
- `status` es un Value Object tipado
- El método `assign_to` valida y aplica la regla de negocio

El **Diseño B** es preferido en Domain-Driven Design.

</details>

---

## ✅ Checklist de Verificación

- [ ] Entidades tienen identidad (id) y comportamiento (métodos)
- [ ] Value Objects son inmutables y se validan al crear
- [ ] Domain Services contienen lógica que no pertenece a una entidad
- [ ] Ports definen contratos usando Protocol
- [ ] El dominio no tiene imports de frameworks externos
- [ ] Las excepciones expresan errores del negocio

---

_Siguiente: [03 - Application Layer](03-application-layer.md)_
