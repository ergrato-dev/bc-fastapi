"""
Prometheus Metrics Configuration.

Este módulo configura métricas para monitoreo con Prometheus.

TODO: Implementar métricas automáticas y de negocio.
"""

from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge, Histogram

from src.config import get_settings


settings = get_settings()


# ============================================
# TODO 1: Configurar Instrumentator
# ============================================

# TODO: Configurar instrumentator avanzado
# instrumentator = Instrumentator(
#     should_group_status_codes=True,
#     should_ignore_untemplated=True,
#     should_respect_env_var=True,
#     should_instrument_requests_inprogress=True,
#     excluded_handlers=["/health/live", "/health/ready", "/metrics"],
#     inprogress_name="http_requests_inprogress",
#     inprogress_labels=True,
# )

# Versión básica
instrumentator = Instrumentator()


# ============================================
# TODO 2: Métricas de Negocio
# ============================================

# TODO: Implementar métricas de negocio para tareas
# 
# # Counter: Total de tareas creadas
# TASKS_CREATED = Counter(
#     name="tasks_created_total",
#     documentation="Total number of tasks created",
#     labelnames=["priority"],
# )
# 
# # Counter: Total de tareas completadas
# TASKS_COMPLETED = Counter(
#     name="tasks_completed_total",
#     documentation="Total number of tasks completed",
# )
# 
# # Gauge: Tareas activas (pendientes + en progreso)
# ACTIVE_TASKS = Gauge(
#     name="active_tasks_total",
#     documentation="Number of active tasks (pending + in_progress)",
# )
# 
# # Histogram: Tiempo hasta completar tarea (en horas)
# TASK_COMPLETION_TIME = Histogram(
#     name="task_completion_hours",
#     documentation="Time to complete tasks in hours",
#     buckets=[0.5, 1, 2, 4, 8, 24, 48, 72, 168],  # horas
# )


def record_task_created(priority: str = "medium") -> None:
    """
    Registra la creación de una tarea.
    
    TODO: Implementar
    
    Args:
        priority: Prioridad de la tarea
    """
    # TODO: Implementar
    # TASKS_CREATED.labels(priority=priority).inc()
    # ACTIVE_TASKS.inc()
    pass


def record_task_completed(completion_hours: float | None = None) -> None:
    """
    Registra la completación de una tarea.
    
    TODO: Implementar
    
    Args:
        completion_hours: Horas que tomó completar (opcional)
    """
    # TODO: Implementar
    # TASKS_COMPLETED.inc()
    # ACTIVE_TASKS.dec()
    # if completion_hours is not None:
    #     TASK_COMPLETION_TIME.observe(completion_hours)
    pass


def set_active_tasks(count: int) -> None:
    """
    Establece el número de tareas activas.
    
    Útil para sincronizar con la base de datos al iniciar.
    
    Args:
        count: Número de tareas activas
    """
    # TODO: Implementar
    # ACTIVE_TASKS.set(count)
    pass


# ============================================
# TODO 3: Métricas Personalizadas Adicionales
# ============================================
# Puedes añadir más métricas según necesites:
# 
# # Rate de errores por tipo
# ERROR_COUNTER = Counter(
#     name="api_errors_total",
#     documentation="Total API errors by type",
#     labelnames=["error_type", "endpoint"],
# )
# 
# # Latencia de base de datos
# DB_QUERY_DURATION = Histogram(
#     name="db_query_duration_seconds",
#     documentation="Database query duration in seconds",
#     labelnames=["operation"],
#     buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1],
# )
