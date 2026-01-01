"""
Value Object Priority - Prioridad de una tarea.

Usa IntEnum para poder comparar prioridades numéricamente.
"""

from enum import IntEnum


# ============================================
# PASO 1: Definir Priority como IntEnum
# ============================================
print("--- Paso 1: Definir Priority ---")

# IntEnum permite comparaciones numéricas:
# Priority.CRITICAL > Priority.LOW  # True

# Descomenta las siguientes líneas:

# class Priority(IntEnum):
#     """
#     Prioridad de una tarea.
#     
#     Valores numéricos permiten ordenar por prioridad:
#     - LOW = 1 (menor prioridad)
#     - MEDIUM = 2
#     - HIGH = 3
#     - CRITICAL = 4 (mayor prioridad)
#     """
#     
#     LOW = 1
#     MEDIUM = 2
#     HIGH = 3
#     CRITICAL = 4
#     
#     @classmethod
#     def from_string(cls, value: str) -> "Priority":
#         """
#         Crear Priority desde string.
#         
#         Args:
#             value: Nombre de la prioridad (case-insensitive)
#             
#         Returns:
#             Priority correspondiente
#             
#         Raises:
#             ValueError: Si el valor no es válido
#         """
#         try:
#             return cls[value.upper()]
#         except KeyError:
#             valid = ", ".join(p.name for p in cls)
#             raise ValueError(f"Invalid priority: {value}. Valid: {valid}")
#     
#     def is_urgent(self) -> bool:
#         """Verificar si la prioridad es urgente (HIGH o CRITICAL)."""
#         return self >= Priority.HIGH


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Priority ---")
    
    # Descomentar para probar:
    # p1 = Priority.LOW
    # p2 = Priority.CRITICAL
    # print(f"LOW < CRITICAL: {p1 < p2}")
    # print(f"CRITICAL es urgente: {p2.is_urgent()}")
    # 
    # # Desde string
    # p3 = Priority.from_string("high")
    # print(f"Desde string 'high': {p3.name}")
    
    print("✅ Value Object Priority implementado correctamente")
