"""
Business logic services.

Este módulo contiene la lógica de negocio que debes testear
con tests unitarios.
"""

from datetime import datetime, timezone
from sqlalchemy.orm import Session

from src.models import Task
from src.schemas import TaskCreate, TaskUpdate
from src.notifications import NotificationService


class TaskService:
    """Service for task operations."""
    
    def __init__(self, db: Session, notification_service: NotificationService | None = None):
        self.db = db
        self.notification_service = notification_service or NotificationService()
    
    def create_task(self, user_id: int, task_data: TaskCreate) -> Task:
        """
        Create a new task.
        
        Args:
            user_id: ID of the task owner
            task_data: Task creation data
            
        Returns:
            Created task
        """
        task = Task(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority,
            due_date=task_data.due_date,
            owner_id=user_id,
        )
        
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        
        return task
    
    def get_task(self, task_id: int) -> Task | None:
        """
        Get a task by ID.
        
        Args:
            task_id: ID of the task
            
        Returns:
            Task if found, None otherwise
        """
        return self.db.query(Task).filter(Task.id == task_id).first()
    
    def get_tasks(
        self,
        user_id: int,
        completed: bool | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Task]:
        """
        Get tasks for a user with optional filtering.
        
        Args:
            user_id: ID of the task owner
            completed: Filter by completion status
            skip: Number of tasks to skip
            limit: Maximum number of tasks to return
            
        Returns:
            List of tasks
        """
        query = self.db.query(Task).filter(Task.owner_id == user_id)
        
        if completed is not None:
            query = query.filter(Task.completed == completed)
        
        return query.offset(skip).limit(limit).all()
    
    def update_task(self, task_id: int, task_data: TaskUpdate) -> Task | None:
        """
        Update a task.
        
        Args:
            task_id: ID of the task to update
            task_data: Update data
            
        Returns:
            Updated task if found, None otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return None
        
        update_dict = task_data.model_dump(exclude_unset=True)
        for field, value in update_dict.items():
            setattr(task, field, value)
        
        self.db.commit()
        self.db.refresh(task)
        
        return task
    
    def complete_task(self, task_id: int) -> Task | None:
        """
        Mark a task as completed.
        
        Args:
            task_id: ID of the task to complete
            
        Returns:
            Completed task if found, None otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return None
        
        task.completed = True
        task.completed_at = datetime.now(timezone.utc)
        
        self.db.commit()
        self.db.refresh(task)
        
        # Send notification
        self.notification_service.notify_task_completed(task)
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if deleted, False if not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        
        self.db.delete(task)
        self.db.commit()
        
        return True
    
    def get_pending_tasks_count(self, user_id: int) -> int:
        """
        Get count of pending (not completed) tasks.
        
        Args:
            user_id: ID of the task owner
            
        Returns:
            Number of pending tasks
        """
        return (
            self.db.query(Task)
            .filter(Task.owner_id == user_id, Task.completed == False)
            .count()
        )
    
    def get_overdue_tasks(self, user_id: int) -> list[Task]:
        """
        Get tasks that are past their due date and not completed.
        
        Args:
            user_id: ID of the task owner
            
        Returns:
            List of overdue tasks
        """
        now = datetime.now(timezone.utc)
        return (
            self.db.query(Task)
            .filter(
                Task.owner_id == user_id,
                Task.completed == False,
                Task.due_date != None,
                Task.due_date < now,
            )
            .all()
        )
