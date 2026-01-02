"""
Generador de Métricas
====================

Módulo para generar métricas del sistema en tiempo real.
"""

import asyncio
import random
from datetime import datetime
from typing import Any, AsyncGenerator


# ============================================
# PASO 1: Collector de métricas
# ============================================
print("--- Paso 1: MetricsCollector ---")

# Clase para recolectar métricas del sistema
# Descomenta las siguientes líneas:

# try:
#     import psutil
#     HAS_PSUTIL = True
# except ImportError:
#     HAS_PSUTIL = False
# 
# 
# class MetricsCollector:
#     """
#     Recolector de métricas del sistema.
#     
#     Usa psutil si está disponible, sino simula datos.
#     """
#     
#     def __init__(self):
#         self.connected_users = 0
#         self.total_requests = 0
#         self.errors = 0
#     
#     def get_cpu_usage(self) -> float:
#         """Retorna uso de CPU en porcentaje."""
#         if HAS_PSUTIL:
#             return psutil.cpu_percent(interval=0.1)
#         # Simular
#         return random.uniform(20, 80)
#     
#     def get_memory_usage(self) -> dict[str, float]:
#         """Retorna uso de memoria."""
#         if HAS_PSUTIL:
#             mem = psutil.virtual_memory()
#             return {
#                 "total": mem.total / (1024**3),  # GB
#                 "used": mem.used / (1024**3),
#                 "percent": mem.percent
#             }
#         # Simular
#         total = 16.0
#         used = random.uniform(4, 12)
#         return {
#             "total": total,
#             "used": used,
#             "percent": (used / total) * 100
#         }
#     
#     def get_disk_usage(self) -> dict[str, float]:
#         """Retorna uso de disco."""
#         if HAS_PSUTIL:
#             disk = psutil.disk_usage('/')
#             return {
#                 "total": disk.total / (1024**3),
#                 "used": disk.used / (1024**3),
#                 "percent": disk.percent
#             }
#         # Simular
#         return {
#             "total": 500.0,
#             "used": random.uniform(100, 300),
#             "percent": random.uniform(20, 60)
#         }
#     
#     def get_network_stats(self) -> dict[str, int]:
#         """Retorna estadísticas de red."""
#         if HAS_PSUTIL:
#             net = psutil.net_io_counters()
#             return {
#                 "bytes_sent": net.bytes_sent,
#                 "bytes_recv": net.bytes_recv,
#                 "packets_sent": net.packets_sent,
#                 "packets_recv": net.packets_recv
#             }
#         # Simular
#         return {
#             "bytes_sent": random.randint(1000000, 9000000),
#             "bytes_recv": random.randint(1000000, 9000000),
#             "packets_sent": random.randint(1000, 9000),
#             "packets_recv": random.randint(1000, 9000)
#         }
#     
#     def increment_requests(self) -> None:
#         """Incrementa contador de requests."""
#         self.total_requests += 1
#     
#     def increment_errors(self) -> None:
#         """Incrementa contador de errores."""
#         self.errors += 1
#     
#     def set_connected_users(self, count: int) -> None:
#         """Actualiza usuarios conectados."""
#         self.connected_users = count
#     
#     def get_all_metrics(self) -> dict[str, Any]:
#         """Retorna todas las métricas."""
#         return {
#             "timestamp": datetime.now().isoformat(),
#             "cpu": {
#                 "percent": self.get_cpu_usage()
#             },
#             "memory": self.get_memory_usage(),
#             "disk": self.get_disk_usage(),
#             "network": self.get_network_stats(),
#             "app": {
#                 "connected_users": self.connected_users,
#                 "total_requests": self.total_requests,
#                 "errors": self.errors,
#                 "uptime_seconds": self._get_uptime()
#             }
#         }
#     
#     def _get_uptime(self) -> float:
#         """Retorna uptime del sistema."""
#         if HAS_PSUTIL:
#             import time
#             return time.time() - psutil.boot_time()
#         return random.uniform(3600, 86400)
#     
#     async def stream_metrics(
#         self,
#         interval: float = 1.0
#     ) -> AsyncGenerator[dict[str, Any], None]:
#         """
#         Genera stream de métricas.
#         
#         Args:
#             interval: Segundos entre métricas
#             
#         Yields:
#             Dict con métricas del sistema
#         """
#         while True:
#             yield self.get_all_metrics()
#             await asyncio.sleep(interval)


# ============================================
# PASO 2: Instancia global
# ============================================
print("--- Paso 2: Instancia global ---")

# Crear instancia del collector
# Descomenta la siguiente línea:

# metrics_collector = MetricsCollector()


# ============================================
# PASO 3: Activity tracker
# ============================================
print("--- Paso 3: Activity Tracker ---")

# Clase para trackear actividad de usuarios
# Descomenta las siguientes líneas:

# from collections import deque
# 
# class ActivityTracker:
#     """Trackea actividad de usuarios."""
#     
#     def __init__(self, max_entries: int = 100):
#         self.activities: deque = deque(maxlen=max_entries)
#         self.listeners: list = []
#     
#     async def add_activity(
#         self,
#         activity_type: str,
#         user: str,
#         details: str = ""
#     ) -> None:
#         """Agrega una actividad."""
#         activity = {
#             "type": activity_type,
#             "user": user,
#             "details": details,
#             "timestamp": datetime.now().isoformat()
#         }
#         
#         self.activities.append(activity)
#         
#         # Notificar a listeners
#         for listener in self.listeners:
#             try:
#                 await listener(activity)
#             except Exception:
#                 pass
#     
#     def get_recent(self, count: int = 10) -> list[dict]:
#         """Retorna actividades recientes."""
#         return list(self.activities)[-count:]
#     
#     def add_listener(self, callback) -> None:
#         """Agrega listener de actividades."""
#         self.listeners.append(callback)
#     
#     def remove_listener(self, callback) -> None:
#         """Remueve listener."""
#         if callback in self.listeners:
#             self.listeners.remove(callback)
# 
# 
# activity_tracker = ActivityTracker()
