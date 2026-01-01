"""
Port: TemplateRenderer

Define el contrato para renderizar plantillas de mensajes.
Permite usar variables dinámicas en las notificaciones.
"""
from typing import Protocol


# ============================================
# PASO 4: Definir el Protocol TemplateRenderer
# ============================================
# Este Port define cómo el dominio renderiza plantillas.
# La implementación puede ser Jinja2, string.Template, etc.

# Descomenta las siguientes líneas:

# class TemplateRenderer(Protocol):
#     """
#     Port para renderizado de plantillas.
#     
#     Permite crear mensajes dinámicos con variables.
#     
#     Ejemplo de uso:
#         template = "Hola {{name}}, tu pedido #{{order_id}} está listo"
#         context = {"name": "Juan", "order_id": "12345"}
#         result = renderer.render(template, context)
#         # result = "Hola Juan, tu pedido #12345 está listo"
#     """
#     
#     def render(self, template: str, context: dict[str, str]) -> str:
#         """
#         Renderiza una plantilla con variables.
#         
#         Args:
#             template: Plantilla con placeholders (ej: "Hola {{name}}")
#             context: Diccionario de variables a reemplazar
#             
#         Returns:
#             str: Plantilla renderizada con las variables sustituidas
#             
#         Raises:
#             TemplateError: Si la plantilla tiene errores de sintaxis
#             MissingVariableError: Si faltan variables en el context
#         """
#         ...
#     
#     def render_from_file(
#         self,
#         template_name: str,
#         context: dict[str, str]
#     ) -> str:
#         """
#         Renderiza una plantilla desde archivo.
#         
#         Args:
#             template_name: Nombre del archivo de plantilla
#             context: Variables a sustituir
#             
#         Returns:
#             str: Contenido renderizado
#             
#         Raises:
#             TemplateNotFoundError: Si el archivo no existe
#         """
#         ...
#     
#     def validate_template(self, template: str) -> list[str]:
#         """
#         Valida una plantilla y retorna las variables requeridas.
#         
#         Args:
#             template: Plantilla a validar
#             
#         Returns:
#             list[str]: Lista de nombres de variables en la plantilla
#             
#         Raises:
#             TemplateError: Si la sintaxis es inválida
#         """
#         ...


# Placeholder temporal
class TemplateRenderer(Protocol):
    """Placeholder - reemplazar con el Protocol real."""
    ...
