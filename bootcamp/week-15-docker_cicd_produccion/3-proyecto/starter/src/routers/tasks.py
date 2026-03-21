# ============================================
# Tasks Router - CRUD Endpoints
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para implementar
# el CRUD completo de tareas.
# ============================================

from fastapi import APIRouter, Depends, HTTPException, Query

from src.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
    TaskListResponse,
)

router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])


# ============================================
# In-memory storage (placeholder)
# Replace with real DB operations
# ============================================
fake_db: dict[int, dict] = {}
counter = 0


# ============================================
# TODO 1: Listar tareas (con paginación)
# ============================================
@router.get("", response_model=TaskListResponse)
async def list_tasks(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Items per page"),
    completed: bool | None = Query(None, description="Filter by completed status"),
) -> TaskListResponse:
    """
    List all tasks with pagination.

    - **page**: Page number (default: 1)
    - **size**: Items per page (default: 10, max: 100)
    - **completed**: Optional filter by completion status
    """
    # TODO: Implementar con DB real
    # query = db.query(Task)
    # if completed is not None:
    #     query = query.filter(Task.completed == completed)
    # total = query.count()
    # tasks = query.offset((page - 1) * size).limit(size).all()

    # Placeholder implementation
    items = list(fake_db.values())

    if completed is not None:
        items = [t for t in items if t["completed"] == completed]

    total = len(items)
    start = (page - 1) * size
    end = start + size
    paginated = items[start:end]

    return TaskListResponse(
        items=[TaskResponse(**t) for t in paginated],
        total=total,
        page=page,
        size=size,
        pages=(total + size - 1) // size,
    )


# ============================================
# TODO 2: Obtener tarea por ID
# ============================================
@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int) -> TaskResponse:
    """
    Get a task by ID.

    - **task_id**: The task's unique identifier
    """
    # TODO: Implementar con DB real
    # task = db.query(Task).filter(Task.id == task_id).first()
    # if not task:
    #     raise HTTPException(status_code=404, detail="Task not found")
    # return task

    # Placeholder implementation
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")

    return TaskResponse(**fake_db[task_id])


# ============================================
# TODO 3: Crear tarea
# ============================================
@router.post("", response_model=TaskResponse, status_code=201)
async def create_task(task_data: TaskCreate) -> TaskResponse:
    """
    Create a new task.

    - **title**: Task title (required)
    - **description**: Task description (optional)
    - **priority**: Priority level (low, medium, high)
    """
    # TODO: Implementar con DB real
    # task = Task(**task_data.model_dump())
    # db.add(task)
    # db.commit()
    # db.refresh(task)
    # return task

    # Placeholder implementation
    global counter
    from datetime import datetime, timezone

    counter += 1
    now = datetime.now(timezone.utc)

    task = {
        "id": counter,
        **task_data.model_dump(),
        "completed": False,
        "created_at": now,
        "updated_at": now,
    }
    fake_db[counter] = task

    return TaskResponse(**task)


# ============================================
# TODO 4: Actualizar tarea
# ============================================
@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_data: TaskUpdate) -> TaskResponse:
    """
    Update a task.

    All fields are optional. Only provided fields will be updated.
    """
    # TODO: Implementar con DB real
    # task = db.query(Task).filter(Task.id == task_id).first()
    # if not task:
    #     raise HTTPException(status_code=404, detail="Task not found")
    #
    # update_data = task_data.model_dump(exclude_unset=True)
    # for field, value in update_data.items():
    #     setattr(task, field, value)
    #
    # db.commit()
    # db.refresh(task)
    # return task

    # Placeholder implementation
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")

    from datetime import datetime, timezone

    task = fake_db[task_id]
    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        task[field] = value

    task["updated_at"] = datetime.now(timezone.utc)
    fake_db[task_id] = task

    return TaskResponse(**task)


# ============================================
# TODO 5: Eliminar tarea
# ============================================
@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int) -> None:
    """
    Delete a task.

    - **task_id**: The task's unique identifier
    """
    # TODO: Implementar con DB real
    # task = db.query(Task).filter(Task.id == task_id).first()
    # if not task:
    #     raise HTTPException(status_code=404, detail="Task not found")
    #
    # db.delete(task)
    # db.commit()

    # Placeholder implementation
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")

    del fake_db[task_id]
