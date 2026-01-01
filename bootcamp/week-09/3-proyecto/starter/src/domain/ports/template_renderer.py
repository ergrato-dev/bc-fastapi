"""
Port: TemplateRenderer

Define el contrato para renderizar plantillas de mensajes.
"""
from typing import Protocol


class TemplateRenderer(Protocol):
    """
    Puerto para renderizado de plantillas.
    
    TODO: Implementa este Protocol con los siguientes métodos:
    
    - def render(template: str, context: dict) -> str
      Renderiza una plantilla con el contexto dado.
    
    - def validate(template: str) -> bool
      Valida que una plantilla sea sintácticamente correcta.
    """
    
    def render(self, template: str, context: dict) -> str:
        """
        Renderiza una plantilla con variables.
        
        Args:
            template: Plantilla con placeholders (ej: "Hola {name}")
            context: Variables para sustituir (ej: {"name": "Juan"})
            
        Returns:
            Texto renderizado
        """
        ...
    
    def validate(self, template: str) -> bool:
        """
        Valida una plantilla.
        
        Args:
            template: Plantilla a validar
            
        Returns:
            True si es válida, False si tiene errores
        """
        ...
