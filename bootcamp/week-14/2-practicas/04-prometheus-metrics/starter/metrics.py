"""
Módulo de métricas Prometheus.

Este módulo configura el instrumentator de Prometheus y define
métricas personalizadas de negocio.
"""

from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram, Gauge


# ============================================
# PASO 1: Configurar Instrumentator
# ============================================
print("--- Paso 1: Configurar Prometheus Instrumentator ---")

# El Instrumentator añade métricas HTTP automáticas:
# - http_requests_total: contador de requests
# - http_request_duration_seconds: histograma de latencia
# - http_requests_in_progress: gauge de requests activos

# Descomenta las siguientes líneas:
# instrumentator = Instrumentator(
#     should_group_status_codes=True,      # Agrupa status codes (2xx, 3xx, etc)
#     should_ignore_untemplated=True,      # Ignora rutas no definidas
#     should_respect_env_var=True,         # Respeta ENABLE_METRICS env var
#     should_instrument_requests_inprogress=True,  # Gauge de requests activos
#     excluded_handlers=["/health/live", "/health/ready"],  # Excluir health checks
#     inprogress_name="http_requests_inprogress",
#     inprogress_labels=True,
# )

# Versión simple para que el código funcione:
instrumentator = Instrumentator()


# ============================================
# PASO 3: Métricas Personalizadas de Negocio
# ============================================
print("--- Paso 3: Métricas Personalizadas ---")

# Las métricas personalizadas miden aspectos del negocio:
# - Counter: valores que solo incrementan (órdenes, errores)
# - Histogram: distribución de valores (latencia, tamaños)
# - Gauge: valores que suben y bajan (usuarios activos)

# Descomenta las siguientes líneas:
# # Counter: Total de órdenes creadas
# ORDERS_CREATED = Counter(
#     name="orders_created_total",
#     documentation="Total number of orders created",
#     labelnames=["status"],  # Labels para filtrar
# )
#
# # Histogram: Valor de las órdenes (para analizar distribución)
# ORDER_VALUE = Histogram(
#     name="order_value_dollars",
#     documentation="Order value in dollars",
#     buckets=[10, 50, 100, 250, 500, 1000, 5000],  # Rangos de valor
# )
#
# # Gauge: Usuarios activos (valor que sube y baja)
# ACTIVE_USERS = Gauge(
#     name="active_users_total",
#     documentation="Number of currently active users",
# )
#
#
# def record_order_created(status: str = "created") -> None:
#     """Registra una orden creada."""
#     ORDERS_CREATED.labels(status=status).inc()
#
#
# def record_order_value(value: float) -> None:
#     """Registra el valor de una orden."""
#     ORDER_VALUE.observe(value)
#
#
# def set_active_users(count: int) -> None:
#     """Establece el número de usuarios activos."""
#     ACTIVE_USERS.set(count)
#
#
# def user_logged_in() -> None:
#     """Incrementa usuarios activos cuando uno inicia sesión."""
#     ACTIVE_USERS.inc()
#
#
# def user_logged_out() -> None:
#     """Decrementa usuarios activos cuando uno cierra sesión."""
#     ACTIVE_USERS.dec()


# Versiones placeholder para que el código funcione:
def record_order_created(status: str = "created") -> None:
    """Placeholder - descomenta el código real arriba."""
    pass


def record_order_value(value: float) -> None:
    """Placeholder - descomenta el código real arriba."""
    pass


def set_active_users(count: int) -> None:
    """Placeholder - descomenta el código real arriba."""
    pass


def user_logged_in() -> None:
    """Placeholder - descomenta el código real arriba."""
    pass


def user_logged_out() -> None:
    """Placeholder - descomenta el código real arriba."""
    pass
