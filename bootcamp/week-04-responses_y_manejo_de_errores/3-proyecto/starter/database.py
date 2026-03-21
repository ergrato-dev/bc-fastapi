"""
Task Manager API - Simulación de Base de Datos
Semana 04 - Proyecto

Base de datos en memoria para el proyecto.
"""

from datetime import datetime
from models import TaskStatus, TaskPriority


# Simulated database (in-memory)
tasks_db: dict[int, dict] = {}
task_id_counter: int = 0


def get_next_id() -> int:
    """Generate next task ID"""
    global task_id_counter
    task_id_counter += 1
    return task_id_counter


def seed_database() -> None:
    """Seed database with sample tasks"""
    global tasks_db, task_id_counter
    
    sample_tasks = [
        {
            "title": "Learn FastAPI basics",
            "description": "Complete the first 3 weeks of bootcamp",
            "status": TaskStatus.completed,
            "priority": TaskPriority.high,
        },
        {
            "title": "Implement response models",
            "description": "Practice with Pydantic schemas",
            "status": TaskStatus.in_progress,
            "priority": TaskPriority.high,
        },
        {
            "title": "Study error handling",
            "description": None,
            "status": TaskStatus.pending,
            "priority": TaskPriority.medium,
        },
        {
            "title": "Write API documentation",
            "description": "Use OpenAPI and Swagger UI",
            "status": TaskStatus.pending,
            "priority": TaskPriority.low,
        },
    ]
    
    for task_data in sample_tasks:
        task_id = get_next_id()
        now = datetime.now()
        
        tasks_db[task_id] = {
            "id": task_id,
            "title": task_data["title"],
            "description": task_data["description"],
            "status": task_data["status"],
            "priority": task_data["priority"],
            "created_at": now,
            "updated_at": None,
            "completed_at": now if task_data["status"] == TaskStatus.completed else None,
        }


# Initialize with sample data
seed_database()
