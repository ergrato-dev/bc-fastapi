"""
Use Case: Crear una nueva tarea.

Un Use Case representa una acción específica que el usuario
puede realizar en el sistema.
"""

from dataclasses import dataclass
from uuid import UUID

from domain.entities.task import Task
from domain.value_objects.priority import Priority
from domain.ports.task_repository import TaskRepository
from domain.ports.project_repository import ProjectRepository
from domain.exceptions import ProjectNotFoundError
from application.dtos.task_dtos import TaskDTO


# ============================================
# PASO 1: Definir el Command
# ============================================
print("--- Paso 1: Definir CreateTaskCommand ---")

# Un Command es un objeto inmutable que representa
# la intención del usuario

# Descomenta las siguientes líneas:

# @dataclass(frozen=True)
# class CreateTaskCommand:
#     """
#     Command: Datos necesarios para crear una tarea.
#     
#     frozen=True hace el objeto inmutable después de crearse.
#     Esto garantiza que el command no cambie durante el procesamiento.
#     """
#     title: str
#     description: str = ""
#     priority: str = "MEDIUM"
#     project_id: str | None = None


# ============================================
# PASO 2: Definir el Use Case
# ============================================
print("--- Paso 2: Definir CreateTaskUseCase ---")

# El Use Case orquesta la operación sin contener
# lógica de negocio (esa está en el dominio)

# Descomenta las siguientes líneas:

# class CreateTaskUseCase:
#     """
#     Use Case: Crear una nueva tarea.
#     
#     Orquesta la creación de una tarea:
#     1. Valida que el proyecto exista (si se especifica)
#     2. Crea la entidad de dominio
#     3. Persiste usando el repository
#     4. Retorna DTO
#     """
#     
#     def __init__(
#         self,
#         task_repository: TaskRepository,
#         project_repository: ProjectRepository,
#     ) -> None:
#         """
#         Inyectar dependencias.
#         
#         Nota: Los tipos son los Ports (interfaces), no implementaciones.
#         """
#         self._task_repo = task_repository
#         self._project_repo = project_repository
#     
#     async def execute(self, command: CreateTaskCommand) -> TaskDTO:
#         """
#         Ejecutar el caso de uso.
#         
#         Args:
#             command: Datos para crear la tarea
#             
#         Returns:
#             TaskDTO con los datos de la tarea creada
#             
#         Raises:
#             ProjectNotFoundError: Si el proyecto no existe
#             ValueError: Si los datos son inválidos
#         """
#         # 1. Validar proyecto si se especifica
#         project_uuid = None
#         if command.project_id:
#             project_uuid = UUID(command.project_id)
#             project = await self._project_repo.get_by_id(project_uuid)
#             if not project:
#                 raise ProjectNotFoundError(command.project_id)
#         
#         # 2. Crear entidad de dominio (la validación está en Task.create)
#         task = Task.create(
#             title=command.title,
#             description=command.description,
#             priority=Priority.from_string(command.priority),
#             project_id=project_uuid,
#         )
#         
#         # 3. Persistir usando el port
#         await self._task_repo.save(task)
#         
#         # 4. Retornar DTO
#         return TaskDTO.from_entity(task)


# ============================================
# VERIFICACIÓN
# ============================================
if __name__ == "__main__":
    print("\n--- Verificación de CreateTaskUseCase ---")
    print("✅ Use Case CreateTask definido correctamente")
