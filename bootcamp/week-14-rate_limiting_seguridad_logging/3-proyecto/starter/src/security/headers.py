"""
Security Headers Middleware.

Este módulo implementa headers de seguridad HTTP.

TODO: Implementar middleware de headers de seguridad.
"""

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from src.config import get_settings


settings = get_settings()


# ============================================
# TODO 1: Definir Security Headers
# ============================================
# Define los headers de seguridad recomendados por OWASP

# TODO: Completar los headers de seguridad
SECURITY_HEADERS = {
    # Previene MIME sniffing
    # "X-Content-Type-Options": "nosniff",
    
    # Previene clickjacking
    # "X-Frame-Options": "DENY",
    
    # Filtro XSS del navegador
    # "X-XSS-Protection": "1; mode=block",
    
    # HSTS - fuerza HTTPS (solo en producción)
    # "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    
    # Referrer Policy
    # "Referrer-Policy": "strict-origin-when-cross-origin",
    
    # Content Security Policy básico
    # "Content-Security-Policy": "default-src 'self'; script-src 'self' 'unsafe-inline'",
    
    # Permissions Policy
    # "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
}


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Middleware que añade headers de seguridad a todas las respuestas.
    
    TODO: Implementar el middleware completo.
    """
    
    async def dispatch(self, request: Request, call_next) -> Response:
        """
        Procesa el request y añade headers de seguridad.
        
        TODO: Implementar:
        1. Llamar al siguiente middleware/endpoint
        2. Añadir todos los headers de seguridad
        3. Condicionalmente añadir HSTS solo en producción
        
        Args:
            request: Request entrante
            call_next: Siguiente handler en la cadena
            
        Returns:
            Response: Respuesta con headers de seguridad
        """
        # TODO: Implementar
        # response = await call_next(request)
        # 
        # # Añadir headers de seguridad
        # for header, value in SECURITY_HEADERS.items():
        #     response.headers[header] = value
        # 
        # # HSTS solo en producción (requiere HTTPS)
        # if settings.is_production:
        #     response.headers["Strict-Transport-Security"] = (
        #         "max-age=31536000; includeSubDomains; preload"
        #     )
        # 
        # return response
        
        # Versión básica (reemplazar con la de arriba)
        response = await call_next(request)
        return response
