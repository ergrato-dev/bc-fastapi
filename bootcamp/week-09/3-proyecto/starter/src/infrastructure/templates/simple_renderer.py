"""
Adapter: SimpleTemplateRenderer

Implementación de TemplateRenderer usando string.format().
"""
import re
from src.domain.ports.template_renderer import TemplateRenderer


class SimpleTemplateRenderer:
    """
    Adapter que renderiza plantillas usando string.format().
    
    Implementa el Protocol TemplateRenderer.
    Usa la sintaxis de Python: {variable_name}
    
    Ejemplo:
        renderer = SimpleTemplateRenderer()
        result = renderer.render(
            "Hola {name}, tu pedido #{order_id} está listo",
            {"name": "Juan", "order_id": 123}
        )
        # Result: "Hola Juan, tu pedido #123 está listo"
    
    TODO: Implementa los métodos del Protocol.
    """
    
    def render(self, template: str, context: dict) -> str:
        """
        Renderiza una plantilla con variables.
        
        Args:
            template: Plantilla con placeholders {key}
            context: Diccionario de variables
            
        Returns:
            Texto con variables sustituidas
            
        Raises:
            KeyError: Si falta una variable requerida
            
        TODO: Implementar usando str.format() o str.format_map().
        """
        # TODO: Implementar
        pass
    
    def validate(self, template: str) -> bool:
        """
        Valida que una plantilla tenga sintaxis correcta.
        
        Args:
            template: Plantilla a validar
            
        Returns:
            True si es válida, False si tiene errores
            
        TODO: Implementar validando que los {} estén balanceados.
        """
        # TODO: Implementar
        pass
    
    def get_variables(self, template: str) -> list[str]:
        """
        Extrae los nombres de variables de una plantilla.
        
        Args:
            template: Plantilla a analizar
            
        Returns:
            Lista de nombres de variables encontradas
            
        Ejemplo:
            get_variables("Hola {name}, tu código es {code}")
            # Returns: ["name", "code"]
        """
        # Regex para encontrar {variable_name}
        pattern = r"\{(\w+)\}"
        return re.findall(pattern, template)
