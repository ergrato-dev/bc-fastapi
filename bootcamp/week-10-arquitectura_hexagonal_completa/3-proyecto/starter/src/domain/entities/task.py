"""
Entidad: Task (Tarea).

La tarea es la entidad principal del dominio.
Tiene identidad (id) y comportamiento rico.
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid4

from domain.value_objects.task_status import TaskStatus, Priority
from domain.exceptions import TaskAlreadyCompletedError, InvalidTaskTransitionError


@dataclass
class Task:
    """
    Entidad Task - Representa una tarea del sistema.
    
    Atributos:
        id: Identificador único (UUID)
        title: Título de la tarea
        description: Descripción detallada
        status: Estado actual (Value Object)
        priority: Prioridad (Value Object)
        project_id: ID del proyecto (opcional)
        assignee_id: ID del usuario asignado (opcional)
        due_date: Fecha límite (opcional)
        created_at: Fecha de creación
        updated_at: Fecha de última actualización
    """
    
    id: UUID
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    priority: Priority = Priority.MEDIUM
    project_id: UUID | None = None
    assignee_id: UUID | None = None
    due_date: datetime | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    
    # ============================================
    # FACTORY METHOD
    # ============================================
    
    @classmethod
    def create(
        cls,
        title: str,
        description: str,
        priority: Priority = Priority.MEDIUM,
        project_id: UUID | None = None,
        due_date: datetime | None = None,
    ) -> "Task":
        """
        Factory method para crear una nueva tarea.
        
        TODO: Implementar la creación de la tarea con:
        - Generar UUID con uuid4()
        - Establecer status inicial PENDING
        - Establecer timestamps
        """
        # TODO: Implementar
        pass
    
    # ============================================
    # COMPORTAMIENTOS (BEHAVIORS)
    # ============================================
    
    def start(self) -> None:
        """
        Iniciar la tarea.
        
        TODO: Implementar:
        - Validar que la tarea esté en PENDING
        - Cambiar status a IN_PROGRESS
        - Actualizar updated_at
        - Lanzar InvalidTaskTransitionError si no es válido
        """
        # TODO: Implementar
        pass
    
    def complete(self) -> None:
        """
        Completar la tarea.
        
        TODO: Implementar:
        - Validar que la tarea esté en IN_PROGRESS
        - Cambiar status a COMPLETED
        - Actualizar updated_at
        - Lanzar TaskAlreadyCompletedError si ya está completada
        """
        # TODO: Implementar
        pass
    
    def cancel(self) -> None:
        """
        Cancelar la tarea.
        
        TODO: Implementar:
        - Validar que no esté COMPLETED
        - Cambiar status a CANCELLED
        - Actualizar updated_at
        """
        # TODO: Implementar
        pass
    
    def assign_to(self, user_id: UUID) -> None:
        """
        Asignar la tarea a un usuario.
        
        TODO: Implementar:
        - Establecer assignee_id
        - Actualizar updated_at
        """
        # TODO: Implementar
        pass
    
    def set_due_date(self, due_date: datetime) -> None:
        """
        Establecer fecha límite.
        
        TODO: Implementar:
        - Establecer due_date
        - Actualizar updated_at
        """
        # TODO: Implementar
        pass
    
    def change_priority(self, priority: Priority) -> None:
        """
        Cambiar prioridad.
        
        TODO: Implementar:
        - Establecer priority
        - Actualizar updated_at
        """
        # TODO: Implementar
        pass
    
    # ============================================
    # QUERIES (PREGUNTAS AL DOMINIO)
    # ============================================
    
    @property
    def is_completed(self) -> bool:
        """¿La tarea está completada?"""
        return self.status == TaskStatus.COMPLETED
    
    @property
    def is_overdue(self) -> bool:
        """¿La tarea está vencida?"""
        if self.due_date is None:
            return False
        return datetime.now(UTC) > self.due_date and not self.is_completed
    
    def _update_timestamp(self) -> None:
        """Actualizar timestamp de modificación."""
        self.updated_at = datetime.now(UTC)
