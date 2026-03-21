"""
Notification service.

Este servicio envía notificaciones. En los tests, debe ser MOCKEADO
para evitar enviar notificaciones reales.
"""

from src.models import Task


class NotificationService:
    """Service for sending notifications."""
    
    def __init__(self, api_key: str = "default-key"):
        self.api_key = api_key
        self._sent_notifications: list[dict] = []
    
    def notify_task_completed(self, task: Task) -> bool:
        """
        Send notification when a task is completed.
        
        In production, this would send an email or push notification.
        In tests, this should be MOCKED.
        
        Args:
            task: The completed task
            
        Returns:
            True if notification was sent
        """
        # Simulate sending notification
        notification = {
            "type": "task_completed",
            "task_id": task.id,
            "task_title": task.title,
            "owner_id": task.owner_id,
        }
        
        self._sent_notifications.append(notification)
        
        # In real implementation, would call external API
        print(f"📧 Notification sent: Task '{task.title}' completed!")
        
        return True
    
    def notify_task_due_soon(self, task: Task) -> bool:
        """
        Send reminder for task due soon.
        
        Args:
            task: The task due soon
            
        Returns:
            True if notification was sent
        """
        notification = {
            "type": "task_due_soon",
            "task_id": task.id,
            "task_title": task.title,
            "due_date": str(task.due_date),
        }
        
        self._sent_notifications.append(notification)
        print(f"⏰ Reminder sent: Task '{task.title}' is due soon!")
        
        return True
    
    def get_sent_count(self) -> int:
        """Get number of notifications sent."""
        return len(self._sent_notifications)
