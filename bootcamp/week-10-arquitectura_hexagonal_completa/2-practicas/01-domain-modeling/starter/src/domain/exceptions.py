"""
Excepciones del Dominio.

Las excepciones de dominio expresan errores del negocio
de forma clara y específica.
"""


# ============================================
# PASO 1: Definir excepciones base
# ============================================
print("--- Paso 1: Excepciones base ---")

# Descomenta las siguientes líneas:

# class DomainError(Exception):
#     """Base para todos los errores de dominio."""
#     pass


# ============================================
# PASO 2: Excepciones de Task
# ============================================
print("--- Paso 2: Excepciones de Task ---")

# Descomenta las siguientes líneas:

# class TaskError(DomainError):
#     """Base para errores relacionados con tareas."""
#     pass
# 
# 
# class TaskNotFoundError(TaskError):
#     """Tarea no encontrada."""
#     
#     def __init__(self, task_id: str) -> None:
#         self.task_id = task_id
#         super().__init__(f"Task not found: {task_id}")
# 
# 
# class TaskNotAssignableError(TaskError):
#     """Tarea no puede ser asignada (estado inválido)."""
#     pass
# 
# 
# class TaskNotStartableError(TaskError):
#     """Tarea no puede ser iniciada."""
#     pass
# 
# 
# class TaskNotCompletableError(TaskError):
#     """Tarea no puede ser completada."""
#     pass


# ============================================
# PASO 3: Excepciones de Project
# ============================================
print("--- Paso 3: Excepciones de Project ---")

# Descomenta las siguientes líneas:

# class ProjectError(DomainError):
#     """Base para errores relacionados con proyectos."""
#     pass
# 
# 
# class ProjectNotFoundError(ProjectError):
#     """Proyecto no encontrado."""
#     
#     def __init__(self, project_id: str) -> None:
#         self.project_id = project_id
#         super().__init__(f"Project not found: {project_id}")
# 
# 
# class ProjectArchivedError(ProjectError):
#     """Proyecto está archivado y no puede modificarse."""
#     pass


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de Excepciones ---")
    
    # Descomentar para probar:
    # try:
    #     raise TaskNotFoundError("123-456")
    # except TaskError as e:
    #     print(f"Capturado TaskError: {e}")
    #     print(f"Task ID: {e.task_id}")
    
    print("✅ Excepciones de dominio definidas correctamente")
